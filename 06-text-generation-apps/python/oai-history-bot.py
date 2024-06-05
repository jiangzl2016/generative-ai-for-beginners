from openai import OpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# configure Azure OpenAI service client 
client = OpenAI()
deployment="gpt-3.5-turbo"

# add your completion code
persona = input("Tell me the historical character I want to be: ")
question = input("Ask your question about the historical character: ")
prompt = f"""
You are going to play as a historical character {persona}. 

Whenever certain questions are asked, you need to remember facts about the timelines and incidents and respond the accurate answer only. Don't create content yourself. If you don't know something, tell that you don't remember.

Provide answer for the question: {question}
"""
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0)

# print response
print(completion.choices[0].message.content)

# Tell me the historical character I want to be: Winston Churchill
# Ask your question about the historical character: Tell me about a story that happened to Britain during WWII. Limit your answer to 150 words.                    
# One significant event that happened to Britain during WWII was the Battle of Britain in 1940. It was a pivotal air battle between the Royal Air Force (RAF) and the German Luftwaffe, where Britain successfully defended against German air attacks, preventing a potential invasion. This victory boosted British morale and marked a turning point in the war. Winston Churchill famously praised the RAF pilots, saying, "Never in the field of human conflict was so much owed by so many to so few." The Battle of Britain demonstrated Britain's resilience and determination in the face of adversity.