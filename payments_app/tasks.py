from celery import shared_task

import requests

url = "https://api.africastalking.com/version1/messaging"

headers = {'ApiKey': '5e5de5e73e0332922cc6065b42fb5bf79d464b7a52b5d3dde0abd0861c8b0ec1', 
           'Content-Type': 'application/x-www-form-urlencoded',
           'Accept': 'application/json'}

data = {'username': 'NdutaRed',        
        'message': "Hello world !",
        'to': '+254712227589'}

# create a task

@shared_task
def make_post_request():  
    response = requests.post( url = url, headers = headers, data = data )
    return response

# from time import sleep

# #create a task

# @shared_task
# def sleeptime(total_time):

#     sleep(total_time)

#     return "yea"