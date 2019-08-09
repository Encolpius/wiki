from django.shortcuts import render

articles = [
    {
        'author': 'Noara',
        'title': 'Arrival in Saltmarsh',
        'date_posted': 'August 3, 2019',
        'content': 'We arrived in Saltmarsh. The people here are so friendly!'
    },
    {
        'author': 'Noara',
        'title': 'The Tower of Zenopus',
        'date_posted': 'August 4, 2019',
        'content': 'Crazy weird doors in the basement!!'
    }
]

def home(request):
    context = {
        'articles': articles
    }
    return render(request, "saltmarsh/home.html", context)

def about(request):
    return render(request, "saltmarsh/about.html")