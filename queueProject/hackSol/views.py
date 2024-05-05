from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    print("entered")
    return render(request, 'hackSol/mainPage.html')
