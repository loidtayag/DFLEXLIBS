from django.shortcuts import render
from django.http import HttpResponse
from .forms import Upload
from rdflib import Graph
from validation.buildingMOTIF_interface import results
import json

# Create your views here.

def index(req):
     return render(req, "main/base.html", {})

def upload(req):
     data = "Upload graph first" 
     uploaded = "Upload graph first" 
          
     if req.method == "POST":
          form = Upload(req.POST, req.FILES)
          if form.is_valid():
               uploaded = form.cleaned_data['file'].read().decode()
               graph = Graph()
               graph.parse(data=uploaded)
               uploaded = graph.serialize()
               data = results(uploaded)          
               return render(req, "main/upload.html", {"form": Upload(), "uploaded": uploaded, 'suitable_controlApps': json.loads(data)["suitable_controlApps"], 'non_suitable_controlApps': json.loads(data)["non_suitable_controlApps"], "data": data})
          else:
               data = 'File data is invalidd'
          
     return render(req, "main/upload.html", {"form": Upload(), "uploaded": uploaded, 'suitable_controlApps': '', 'non_suitable_controlApps': '', "data": data})
     