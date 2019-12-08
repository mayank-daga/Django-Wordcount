from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def wordcounter(request):

    fulltext = request.GET['fulltext']
    wordlists = fulltext.split()
    worddictionary = {}
    for word in wordlists:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sorteddict_= sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'wordcounter.html', {'fulltext': fulltext, 'count': len(wordlists),
                                                'sorteddict_': sorteddict_})

def about(request):
    return render(request, 'about.html')