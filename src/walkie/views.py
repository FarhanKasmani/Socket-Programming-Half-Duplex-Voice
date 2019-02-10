from django.shortcuts import render, redirect, reverse
from .client import send, recieve

def voice(request):
        return render(request,"start.html", {})

def sendV(request):
        print("Hi")
        send()
        return render(request, 'start.html', {})

def recieveV(request):
        print("Hi")
        recieve()
        return render(request, 'start.html', {})


