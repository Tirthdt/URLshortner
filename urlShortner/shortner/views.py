from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Links
import uuid
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def create(request):
    if request.method == 'POST':
        print("hello")
        link = json.loads(request.body)['link']
        link_id = str(uuid.uuid4())[:5]
        new_url = Links(link=link, uuid=link_id)
        new_url.save()
        return JsonResponse({"UID": link_id})

def go(request, pk):
    url_details = Links.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)
