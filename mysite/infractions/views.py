from django.shortcuts import render

# Create your views here.
import json


from django.http import HttpResponse


def index(request):
    #json_data = open('/Users/nicolas/Desktop/Django-exam/mysite/infractions.json')   
    #data1 = json.load(json_data) # deserialises it
    #data2 = json.dumps(data1) # json formatted string
    #json_data.close()
    return HttpResponse("Hello, world. You're at the infraction index.")