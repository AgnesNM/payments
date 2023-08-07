from django.shortcuts import render
from django.http import HttpResponse

# from . tasks import sleeptime

from . tasks import make_post_request

# Create your views here.

def index(request):
    my_dict = {"message":"Set reminders for recurring payments"}
    return render(request, "payments_app/index.html", context = my_dict)

def celery_view(request):

    sms_data = make_post_request().json()

    celery_dict = {"sms": sms_data}

    return render(request, "payments_app/sms.html", context = celery_dict)

def validation(request): 

    validation_dict = {"validation":"Hey this is the validation page"}

    return render(request, "payments_app/validation.html", context = validation_dict)

def confirmation(request): 

    confirmation_dict = {"confirmation":"Hey this is the confirmation page"}

    return render(request, "payments_app/confirmation.html", context = confirmation_dict)

    


    # #invoke celery to run the task
    # sleeptime.delay(15)

    # return HttpResponse("Hey, it's almost nap time")