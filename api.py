import os
import openai
import config # with api key

openai.api_key = config.OPENAI_API_KEY

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}]
)

print(completion.choices[0].messages)
