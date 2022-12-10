# Rasa-Chatbot

Rasa version: 3.1

Python version: 3.8

It is recommended to run the chatbot with the aforementioned Python and Rasa versions. Conda can be used to create a Python environment of the specified version. If this is your first time running the bot, train the model first. Just to ensure that the bot is up to date.

This chatbot is equipped with 2 step fallback. So, it provides a smooth experience in handling new information or the bot faces understanding the sentence.

Command to create the python environment and install the dependencies: 
- conda create -n `<env_name>` python=3.8 
- pip3 install -r requirements.txt

## Conversational Flows:

### Multi Conversation-1
User: How many calories are present in croissant?  
Zoos:   
Your meal is about: 113 kcal for a weight of 28.0g  
It's diet labels are: ['LOW_SODIUM']  
It's health labels are: ['LOW_FAT_ABS', 'LOW_POTASSIUM', 'KIDNEY_FRIENDLY', 'KETO_FRIENDLY', 'VEGETARIAN', 'PESCATARIAN', 'MEDITERRANEAN', 'PEANUT_FREE', 'TREE_NUT_FREE', 'SOY_FREE', 'FISH_FREE', 'SHELLFISH_FREE', 'PORK_FREE', 'RED_MEAT_FREE', 'CRUSTACEAN_FREE', 'CELERY_FREE', 'MUSTARD_FREE', 'SESAME_FREE', 'LUPINE_FREE', 'MOLLUSK_FREE', 'ALCOHOL_FREE', 'SULPHITE_FREE', 'KOSHER']  
User: Videos?  
Zoos:  
Good Choice!  
www.youtube.com/watch?v=K689erbK3XI  
www.youtube.com/watch?v=hJxaVD6eAtc  
www.youtube.com/watch?v=djnNkLi_K6E  
www.youtube.com/watch?v=vpwY3nmLLaA  
www.youtube.com/watch?v=bOQfTGfNLjM  

### Multi Conversation-2
User: How many calories are present in croissant?  
Zoos: 
Your meal is about: 113 kcal for a weight of 28.0g  
It's diet labels are: ['LOW_SODIUM']  
It's health labels are: ['LOW_FAT_ABS', 'LOW_POTASSIUM', 'KIDNEY_FRIENDLY', 'KETO_FRIENDLY', 'VEGETARIAN', 'PESCATARIAN', 'MEDITERRANEAN', 'PEANUT_FREE', 'TREE_NUT_FREE', 'SOY_FREE', 'FISH_FREE', 'SHELLFISH_FREE', 'PORK_FREE', 'RED_MEAT_FREE', 'CRUSTACEAN_FREE', 'CELERY_FREE', 'MUSTARD_FREE', 'SESAME_FREE', 'LUPINE_FREE', 'MOLLUSK_FREE', 'ALCOHOL_FREE', 'SULPHITE_FREE', 'KOSHER']  
User: Images?  
Zoos:  
[Image]  
Recipe: Croissant Loaf recipes  
Main ingredients: ['2 pounds croissant dough', '1/2 cup sugar', '2 teaspoons or so, freshly grated cinnamon']  
Cautions: []  
Cuisine Type: ['british']  
Meal Type: ['breakfast']  
Dish Type: ['bread']  
More informations here: http://notwithoutsalt.com/croissant-loaf-giveaway/  
[Image]   
Recipe: Hot Ham-and-Cheese Croissant  
Main ingredients: ['1 croissant', '1 teaspoon mayonnaise', '1 teaspoon Dijon mustard']  
Cautions: ['Sulfites']  
Cuisine Type: ['british']  
Meal Type: ['breakfast']  
Dish Type: ['bread']  
More informations here: https://www.marthastewart.com/1537958/hot-ham-and-cheese-croissant  
[Image]  
Recipe: Croissant Breakfast Sandwich  
Main ingredients: ['2 croissants', '2 eggs', '2 oz smoked salmon']  
Cautions: []  
Cuisine Type: ['nordic']  
Meal Type: ['lunch/dinner']  
Dish Type: ['sandwiches']  
More informations here: http://norecipes.com/blog/2010/09/05/croissant-breakfast-sandwich/  

### Other conversations:
User: What cuisine is fish?  
Zoos:   
[Image]  
Recipe: Burnt-Scallion Fish  
Main ingredients: ['2 bunches scallions', '8 tbsp. butter', '2 8-oz. fish filets']  
Cautions: []  
Cuisine Type: ['chinese']  
Meal Type: ['lunch/dinner']  
Dish Type: ['main course']  
More informations here: http://www.saveur.com/article/Recipes/Burnt-Scallion-Fish  
[Image]  
Recipe: Fish Head Curry  
Main ingredients: ['1/2 to 2 fish heads, depending on size, about 5 pounds total', '2 tablespoons vegetable oil', '1/4 cup red or green thai curry paste']  
Cautions: ['Tree-Nuts', 'Shellfish', 'Sulfites', 'FODMAP']  
Cuisine Type: ['south east asian']  
Meal Type: ['lunch/dinner']  
Dish Type: ['main course']  
More informations here: http://www.seriouseats.com/recipes/2011/04/fish-head-curry-recipe.html  
[Image]  
Recipe: Fish And Chips  
Main ingredients: ['4 medium potatoes I used a mix of yukon gold and russet', '4 medium fish fillets cod, haddock and albacore work well', '1/2 cup + 2 tablespoons flour']  
Cautions: ['Gluten', 'Wheat']  
Cuisine Type: ['british']  
Meal Type: ['lunch/dinner']  
Dish Type: ['main course']  
More informations here: http://norecipes.com/blog/fish-and-chips-recipe/  


User: What is your age?  
Zoos: My current age is 61 days.  


User: What is your name?  
Zoos: My name is Zoos  


User: Who created you?  
Zoos: I was created by Ashish Mernedi  


User: Help  
Zoos: This is a chatbot that helps you with find number of calories in a food, diet labels, health labels etc.. Not only that it helps you in making of that food items with help of videos. Even you can know what type of cuisine/meal is a dish and many more. Get started by asking cal in food name, cuisine of hakka noodle, images of hakka noodles etc... Ex:cal in chicken?  


User: Describe yourself  
Zoos: Myself Zoos. I help you find number of calories a food contains, diet labels, health labels, cuisine type, dish type and many more... Not only that I can help you in prepare those items with some YouTube videos and articles online.  


User: Hi  
Zoos: Hey! How are you?  
User: Fine  
Zoos: Have we spoke before?  
User: Yes  
Zoos: What is your email?  
User: test@gmail.com  
Zoos: Welcome back, test! How can I help you?  

These are some of the conversations, similarly you can ask about dish type, meal type...  
If you are visiting first time, you can register yourself with email, so bot could you recognise you next time. It even shows some images if you are sad.

Below are some of the food items which you can try:  
Chicken, Egg fried rice, sausage, manchuria, Chicken sausage, hakka noodles, veg noodles, coffee, croissant, garlic, onions, turmeric, ginger, bread, omelette, Idli, Dosa, Pancake, Chocolate Cake, Vada, Puri, Chocolate, pizza, chicken wings, cheese, egg, fish, Pongal, Salmon.

The above list contains a mix of food items, where the bot uses different apis to fetch.   
Note: The above list is tested before adding 2 step fallback. 