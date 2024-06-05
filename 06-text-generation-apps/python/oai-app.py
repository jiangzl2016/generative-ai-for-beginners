from openai import OpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# configure OpenAI service client 
client = OpenAI()

#deployment=os.environ['OPENAI_DEPLOYMENT']
deployment="gpt-3.5-turbo"

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.

# brave knight who roamed the countryside in search of adventure. He was known far and wide for his gallantry and skill with a sword, and many peasants spoke of his brave deeds in hushed tones. One day, as he rode through the dense forest, he came across a distressed maiden in need of help. And so began a tale of daring rescue, fierce battles, and ultimately, a love that would defy all odds.
