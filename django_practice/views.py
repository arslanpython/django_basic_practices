import json
import string

from django.http import HttpResponse
from django.shortcuts import render

from .repository import data


def home(request):
    params = {'question': 'How are you?', 'ans': 'Yes! Fine'}
    return render(request, 'index.html', params)
    # return HttpResponse(<h1>Welcome In Django<h1>)


def analyzed(request):
    text = request.GET.get('text', default='default value')
    print('---> ', text)

    remove_punctuation = request.GET.get('remove_punctuation', 'off')
    print('---> ', remove_punctuation)
    analyzed_text = ''

    if remove_punctuation == 'on':
        for char in text:
            if char not in string.punctuation:
                analyzed_text += char

        params = {'purpose': 'Removed Punctuations!', 'analyzed': analyzed_text}

        return render(request, 'analyzed.html', params)
    else:
        return HttpResponse(text)


def questionnaire(request):
    count = request.GET.get('count')
    if count:
        count = int(count) + 1
    else:
        count = 0
    questions = data['questions']
    if count < len(questions):
        question = questions[count]['question']
        ans = questions[count]['choices']
        params = {'question': question, 'ans': ans, 'count': count}
        return render(request, 'questionnaire.html', params)
    else:
        return HttpResponse("No more questions left")

def about(request):
    return HttpResponse("About Arslan")
