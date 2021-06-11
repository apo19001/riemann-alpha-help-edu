# CSE310 Applied Programming
#Seal Team 1 Project
#Goal is to make a web app that will utilize WolframAlphas API for an educational app

import wolframalpha

# Taking input from user
question = input('Question: ')

# App id obtained by apllying for one on the official website
app_id = 'HT2JL8-V2WHEWTT7G'

# Instance of wolf ram alpha
# client class
client = wolframalpha.Client(app_id)

# Stores the response from
# wolf ram alpha
res = client.query(question)

# Includes only text from the response
answer = next(res.results).text

print(answer)
