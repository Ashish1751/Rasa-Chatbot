# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
# from rasa_sdk import FormAction
from googleapiclient.discovery import build
import requests, logging, mysql.connector
from datetime import datetime, timedelta

logger = logging.getLogger("PyEdamam")

class ActionAge(Action):

    def name(self) -> Text:
        return "action_age"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            particular_date = datetime(2022, 10, 1)
            new_date = datetime.today() - particular_date
            print (new_date.days)
            dispatcher.utter_message(text="My current age is: {} days".format(new_date.days))

            return []

class ActionItemVideo(Action):

    def name(self) -> Text:
        return "action_item_video"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food = tracker.get_slot("food_name")
        if food == None:
            logger.error("Food attribute is empty")
        print(food)
        api_key = "AIzaSyAfhUaXx6IC0Yif1jwkbYosbsN2tNQmjUg"
        youtube = build('youtube', 'v3', developerKey=api_key)
        req = youtube.search().list(q="How to make "+ food, part='snippet', type='video', maxResults=5, pageToken=None)
        res = req.execute()
        video = []
        for i in res["items"]:
            print(i)
            video.append(i["id"]["videoId"])
            print(video[-1])

        video_str = ""
        for i in video:
            video_str += "www.youtube.com/watch?v=" + i + "\n" 

        print(video_str)

        dispatcher.utter_message(text="Good Choice!\n"+str(video_str))

        return []

class ActionItem1(Action):
    def name(self):
        return "action_get_image"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        food = tracker.get_slot("food_name")
        print(food)
        if food == None:
            logger.error("Food attribute is empty")
        # return []
        url = 'https://api.edamam.com/search?q=' + food + '&app_id=817470ee&app_key=e329ec5077c9bf6736410b49b64c41a2&from=0&to=3' 
        res = requests.get(url)
        if res.status_code == 401:
            logger.error("invalid recipe api key")
        res = res.json()
        # print(res)

        for d in res['hits']:
                recipe = d['recipe']
                recipeName = recipe.get('label')
                ingredients = recipe.get('ingredientLines')
                recipeUrl = recipe.get('url')
                imageUrl = recipe.get('image')
                cautions = recipe.get('cautions')
                cuisine = recipe.get('cuisineType')
                meal = recipe.get('mealType')
                dish = recipe.get('dishType')

                dispatcher.utter_message(image=imageUrl)
                dispatcher.utter_message(text="Recipe: {}".format(recipeName))
                dispatcher.utter_message(text="Main ingredients: {}".format(ingredients[:3]))
                dispatcher.utter_message(text="Cautions: {}".format(cautions))
                dispatcher.utter_message(text="Cuisine Type: {}".format(cuisine))
                dispatcher.utter_message(text="Meal Type: {}".format(meal))
                dispatcher.utter_message(text="Dish Type: {}".format(dish))
                dispatcher.utter_message(text="More informations here: {}".format(recipeUrl))

                print("Recipe name: ",recipeName)
                # print("Image Url:", imageUrl)
                print("Recipe ingredients: " , ingredients[:3])
        return []

class ActionItem(Action):
    def name(self):
        return "action_item"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        food = tracker.get_slot("food_name")
        print(food)
        if food == None:
            logger.error("Food attribute is empty")
        # return []
        food = food.replace(" ", "%20")
        url = "https://api.edamam.com/api/nutrition-data?app_id=2ae12d8e&app_key=1c41fde6eeefe0f9f39d1100d3eed619&ingr=1%20" + food 
        # url = "https://api.edamam.com/api/food-database/parser?app_id=f430e3c8&app_key=aa5699aac4713d645ab16452abe894c8&ingr=1%20" + food
        res = requests.get(url)
        if res.status_code == 401:
            logger.error("invalid recipe api key")
        res = res.json()
        # print(res)
        # return []
        if int(res.get('calories')) == 0:
            dispatcher.utter_message(text="We could not find what you were searching for but maybe some of this suggestions will do the job?")
            url = "https://api.edamam.com/api/food-database/parser?app_id=f430e3c8&app_key=aa5699aac4713d645ab16452abe894c8&ingr=1%20" + food

            res = requests.get(url)
            if res.status_code == 401:
                logger.error("invalid recipe api key")
            res = res.json()
            # print(res)

            for d in res['hints'][:5]:
                recipe = d['food']
                recipeName = recipe.get('label')
                nutrients = recipe.get('nutrients')
                # ingredients = recipe.get('foodContentsLabel')
                cal = nutrients.get('ENERC_KCAL')
                
                dispatcher.utter_message(text="Recipe: {}".format(recipeName))
                # dispatcher.utter_message(text="Main ingredients: {}".format(ingredients))
                dispatcher.utter_message(text="Your meal is about: {} kcal".format(cal))

                print("Recipe name: ",recipeName)
                # print("Recipe ingredients: " , ingredients)
                print("Nutrients: ",nutrients)

            return []
        
        cal = res.get('calories')
        weight = res.get('totalWeight')
        dl = res.get('dietLabels')
        hl = res.get('healthLabels')

        dispatcher.utter_message(text="Your meal is about: {} kcal for a weight of {}g".format(cal,weight))
        dispatcher.utter_message(text="It's diet labels are: {}".format(dl))
        dispatcher.utter_message(text="It's health labels are: {}".format(hl))
        return []

class ActionEmailCheck(Action):

    def name(self) -> Text:
        return "action_email_check"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("action_confirm_user_email")
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="",
                                       database="testDB")  # # auth_plugin='mysql_native_password'
        userEmail = tracker.latest_message.get('text')
        userEmail = userEmail.split("|")[-1][:-1]
        print(userEmail)
        query = "select fname from users where email = '{}';".format(userEmail)
        cursor = mydb.cursor()
        print(query)

        try:
            x = cursor.execute(query)
            if x == 0:
                print("Sorry, could not find you in the DB")
                dispatcher.utter_message("Sorry I could not find you by your email! :( ")
            else:
                result = cursor.fetchone()
                
                dispatcher.utter_message("Welcome back, {} !".format(str(result[0])))
                dispatcher.utter_message("How can I help you?")
        except:
            dispatcher.utter_message("Sorry I could not find you by your email! :( ")
        return [SlotSet("user_email", userEmail)]

class ActionUserSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            email = tracker.get_slot("user_email")
            email = email.split("|")[-1][:-1]
            SlotSet("user_email", email)
            fname = tracker.get_slot("first_name")
            lname = tracker.get_slot("last_name")

            mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="testDB")

            query = "insert into users(fname, lname, email) values ('{}','{}','{}');".format(fname, lname, email)
            print(query)
            cursor = mydb.cursor()

            try:
                result = cursor.execute(query)
                mydb.commit()
                dispatcher.utter_message(response="utter_slots_values", first_name=tracker.get_slot('first_name'),
                                         last_name=tracker.get_slot('last_name'))
            except mysql.connector.Error as err:
                dispatcher.utter_message("Error!")
                print(err)
    
            return [SlotSet("user_email", email)]

class ActionGetImage(Action):

    def name(self) -> Text:
        return "action_get_image1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        food = tracker.get_slot("food_name")
        print(food)
        if food == None:
            logger.error("Food attribute is empty")
        # return []
        food = food.replace(" ", "+")
        url = "https://pixabay.com/api/?key=31483378-7da7104ebaf3528c0ba33ce71&image_type=photo&per_page=5&q=" + food
        res = requests.get(url)
        if res.status_code == 401:
            logger.error("invalid recipe api key")
        res = res.json()
        # print(res)

        for d in res['hits']:
            recipeName = d['tags'].split(",")[0]
            recipeUrl = d['webformatURL']

            dispatcher.utter_message(text="Showing images related to: {}".format(recipeName))
            dispatcher.utter_message(text="More informations here: {}".format(recipeUrl))
            
            print("Tags: ",recipeName)

        return []
        
