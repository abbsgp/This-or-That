from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
import treeBasedDB
  
db = treeBasedDB.dataBase()

def index(request):
    if request.method == 'POST':
        word1 = request.POST['word1']
        word2 = request.POST['word2']
        chosen = request.POST['chosen']
        score = int(request.POST['score'])

        mostpopular, scores = db.getMostPopular([word1,word2])
        if chosen == mostpopular:
            correct = "You Are Correct"
            score += 1;
        else:
            correct = "You Are Incorrect"
            score = 0

        print(correct)
        words = db.getWords()

        data = {'word1':words[0],
           'word2':words[1],
        'mostpopular':mostpopular,
        'correct':correct,
        'score':score}
    else:
        words = db.getWords()
        data ={'word1':words[0],
                'word2':words[1],
                'score':'0'}
    return render(request, "main/index.html",data)

