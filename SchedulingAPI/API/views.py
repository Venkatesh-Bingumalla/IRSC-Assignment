from django.shortcuts import render
from rest_framework.response import Response
from datetime import datetime
import json
import requests

def Schedule1(request,Date="Mention the Date",url="Mention the Url"):
    values=Date#get the user entered date 
    da_obj = datetime.strptime(values, '%Y-%m-%d %H:%M:%S')

    link=url
    today=datetime.now()#get the current date
    if today==da_obj:
        response = requests.get('link') 
        res=response.status_code
    else:
        res="Date-Time not amtched"
    return render(request,'API/home.html',{'val':da_obj,'link':link,'dt':today,'r':res})
def ping(request):
    if request.method=='GET':
        x = '{ "Status":"OK" }'
        y = json.loads(x)
        return render(request,'API/ping.html',{"res":y})
        

