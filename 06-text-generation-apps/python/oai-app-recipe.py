from openai import OpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# configure Azure OpenAI service client 
client = OpenAI()

#deployment=os.environ['OPENAI_DEPLOYMENT']
deployment="gpt-3.5-turbo"

no_recipes = input("No of recipes (for example, 5: ")

ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots: ")

filter = input("Filter (for example, vegetarian, vegan, or gluten-free: ")

# interpolate the number of recipes into the prompt an ingredients
prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}: "
messages = [{"role": "user", "content": prompt}]

completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=600, temperature = 0.1)


# print response
print("Recipes:")
print(completion.choices[0].message.content)

old_prompt_result = completion.choices[0].message.content
prompt_shopping = "Produce a shopping list, and please don't include ingredients that I already have at home: "

new_prompt = f"Given ingredients at home {ingredients} and these generated recipes: {old_prompt_result}, {prompt_shopping}"
messages = [{"role": "user", "content": new_prompt}]
completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=600, temperature=0)

# print response
print("\n=====Shopping list ======= \n")
print(completion.choices[0].message.content)

# User:
# No of recipes (for example, 5: 1
# List of ingredients (for example, chicken, potatoes, and carrots: pork, brussel sprouts, onions 
# Filter (for example, vegetarian, vegan, or gluten-free: 
# None 

# Output:
# Recipes:
# Pork and Brussels Sprouts Stir Fry:

# Ingredients:
# - 1 lb pork tenderloin, thinly sliced
# - 1 lb Brussels sprouts, trimmed and halved
# - 1 onion, thinly sliced
# - 3 cloves garlic, minced
# - 2 tbsp soy sauce
# - 1 tbsp oyster sauce
# - 1 tbsp sesame oil
# - 1 tsp ginger, minced
# - Salt and pepper to taste
# - Cooking oil

# Instructions:
# 1. Heat some cooking oil in a large skillet or wok over medium-high heat.
# 2. Add the sliced pork and cook until browned and cooked through. Remove from skillet and set aside.
# 3. In the same skillet, add a bit more oil if needed and sauté the onions until translucent.
# 4. Add the Brussels sprouts and cook until slightly tender.
# 5. Add the garlic, ginger, soy sauce, oyster sauce, and sesame oil. Stir well to combine.
# 6. Return the cooked pork to the skillet and mix everything together.
# 7. Cook for another 2-3 minutes, or until the Brussels sprouts are cooked to your liking.
# 8. Season with salt and pepper to taste.
# 9. Serve hot and enjoy!

# =====Shopping list ======= 

# - Pork tenderloin
# - Cooking oil