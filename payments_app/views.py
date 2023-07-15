from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {"message":"Set reminders for recurring payments"}
    return render(request, "payments_app/index.html", context = my_dict)

