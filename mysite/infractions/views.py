from django.shortcuts import render

# Create your views here.
import json


from django.http import HttpResponse

from .models import Infraction


def index(request):
    json_data = open('/Users/nicolas/Desktop/Django-exam/mysite/infractions.json')   
    data1 = json.load(json_data) 
    values = json.dumps(data1)
    json_data.close()
    
    #all_data_list = Infractions.objects.order_by('-infraction_speed')
    #context = {'all_data_list': all_data_list}
    #return render(request, 'infractions/index.html', context)
    return HttpResponse("you're viewing infractions index")


