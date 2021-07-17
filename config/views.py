from django.shortcuts import render
from django.http import HttpResponse
import sys

import wolframalpha

# work done by Travis Smith
def wolfram_query(question):
    # # Taking input from user
    # question = input('Question: ')

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
    return answer

# work found in here

# David Strelyuk

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def search(request):
    if request.method == "POST":
        question = request.POST['searched']
        answer = wolfram_query(question)
        context = {
            'question': question,
            'answer': answer
        }
        return render(request, "search.html", context)
    else:
        return render(request, "search.html", {})