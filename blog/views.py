from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def hello_world(request):

    return HttpResponse(f"<h1>Hi  {datetime.now()}</h1>")
