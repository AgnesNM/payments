# import africastalking

# class SMS:
    
#     def __init__(self):
#         self.username = "NdutaRed"
#         self.api_key = "5e5de5e73e0332922cc6065b42fb5bf79d464b7a52b5d3dde0abd0861c8b0ec1"
        

#     def send(self, ):

#       recipients = ["+254712227589"]
#       message = "Hello, this is Abby"
      

#       try:
#          #initialize the SDK
#          africastalking.initialize(self.username, self.api_key)

#          #get the SMS service
#          sms = africastalking.SMS

#          response = sms.send(message, recipients)

#          print(response)

#       except:
#          print("oops, the message was not sent")      
     

# if __name__ == '__main__':
#     SMS().send()

# # **********************

# # import requests

# # url = "https://api.africastalking.com/version1/messaging"

# # headers = {'ApiKey': '5e5de5e73e0332922cc6065b42fb5bf79d464b7a52b5d3dde0abd0861c8b0ec1', 
# #            'Content-Type': 'application/x-www-form-urlencoded',
# #            'Accept': 'application/json'}

# # data = {'username': 'NdutaRed',        
# #         'message': "Hello world !",
# #         'to': '+254712227589'}


# # def make_post_request():  
# #     response = requests.post( url = url, headers = headers, data = data )
# #     return response


# # print( make_post_request().json() )

