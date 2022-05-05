from django.shortcuts import render
import json

def index_page(request):
    return render(request, 'index.html')


# def login(request): # User login
#     if request.method == 'GET':
#         return render(request, 'login.html')


