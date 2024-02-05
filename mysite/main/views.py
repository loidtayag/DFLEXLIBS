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

               with open("data.txt", "w") as file:
                    file.write(data)

               return render(req, "main/upload.html", {"form": Upload(), "uploaded": uploaded, 'suitable_controlApps': json.loads(data)["suitable_controlApps"], 'non_suitable_controlApps': json.loads(data)["non_suitable_controlApps"], "data": data, 'uploaded': True})
          else:
               data = 'File data is invalidd'

     return render(req, "main/upload.html", {"form": Upload(), "uploaded": uploaded, 'suitable_controlApps': '', 'non_suitable_controlApps': '', "data": data, 'uploaded': False})
     
def resultss(req):
     data = ''

     with open("data.txt", "r") as file:
          data = file.read()

     return render(req, "main/results.html", {'data': json.loads(data)})

def report(req):
     data = ''
     index = int(req.GET.get('index', ''))
     want = ''

     with open("data.txt", "r") as file:
          data = json.loads(file.read())
          want = data["validation_table"][index]
          data = data['non_suitable_controlApps']

     for item in data:
          if item[0] == want[0]:
               data = item
               break

     reasons = data[1:]     
     reasons_text = [s.split("http")[0] for s in reasons]
     reasons_link = ["http" + s.split("http")[1] for s in reasons]
     reasons = list(zip(reasons_text, reasons_link))
     return render(req, "main/results/report.html", {'name': data[0], 'reasons': reasons})
    
def info(req):
     data = ''
     index = int(req.GET.get('index', ''))

     with open("data.txt", "r") as file:
          data = json.loads(file.read())["validation_table"][index]

     return render(req, "main/results/info.html", {'name': data[0]})
