from django.shortcuts import render
from django.http import HttpResponse
from .forms import Upload
from rdflib import Graph
from validation.buildingMOTIF_interface import results
import json
import controls as API_PATH
from controls.demo import API
import base64
import zipfile
import os

# Create your views here.

def index(request):
     return render(request, "main/base.html", {})

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

               return HttpResponse(data, content_type='text')
          else:
               data = 'File data is invalidd'

     return render(req, "main/upload.html", {"form": Upload()})

def filter(req):
     zone = req.GET.get("zone")
     target = req.GET.get("target")
     toShow = None
     title_upper = 'Archetype'
     title_lower = 'archetype'

     if zone == None and target == None:
          toShow = API.getFilters().keys()
     elif zone != None and target == None:
          title_upper = 'Target level'
          title_lower = 'target level'
          toShow = API.getFilters()[zone].keys()
     elif zone != None and target != None:
          title_upper = 'Strategy'
          title_lower = 'application'
          toShow = API.getFilters()[zone][target]
     
     return render(req, "main/filter.html", {'toShow': toShow, 'title_upper': title_upper, 'title_lower': title_lower})

def resultss(req):
     data = ''
     filter = req.GET.get('order')

     with open("data.txt", "r") as file:
          data = json.loads(file.read())
          if filter is None or filter == 'ascending':
               data['validation_table'] = sorted(data['validation_table'], key=lambda item: item[0])
          elif filter == 'descending':
               data['validation_table'] = sorted(data['validation_table'], key=lambda item: item[0], reverse=True)

     with open("data.txt", "w") as file:
          json.dump(data, file)

     return render(req, "main/results.html", {'data': data, 'order': filter})

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
               print(item)
               data = item
               break
     
     reasons = data[1:]     
     reasons_text = [s.split("http")[0] for s in reasons]
     reasons_link = ["http" + s.split("http")[1] for s in reasons]
     reasons = list(zip(reasons_text, reasons_link))
     return render(req, "main/results/report.html", {'name': data[0], 'reasons': reasons})
    
def info(req):
     data = ''
     index = req.GET.get('index', '')
     name = req.GET.get('name', '')

     if index:
          index = int(index)

          with open("data.txt", "r") as file:
               data = json.loads(file.read())["validation_table"][index]
     elif name:
          data = [name]

     desc = API.getInformation(data[0])['description']
     requirements = API.getInformation(data[0])['requirements']

     flow_package_path = API.getInformation(data[0])['flow_chart']
     perf_package_path = API.getInformation(data[0])['performance']
     flow_path = os.path.join(os.path.dirname(API_PATH.__file__), flow_package_path)
     perf_path = os.path.join(os.path.dirname(API_PATH.__file__), perf_package_path)
     
     # with open(flow_path, 'rb') as file1:
     #      with open("main/static/" + os.path.basename(flow_path), 'wb') as file2:
     #           file2.write(file1.read())

     # with open(perf_path, 'rb') as file1:
     #      with open("main/static/" + os.path.basename(perf_path), 'wb') as file2:
     #           file2.write(file1.read())

     return render(req, "main/results/info.html", {'name': data[0], 'desc': desc, 'flow': os.path.basename(flow_path), 'perf': os.path.basename(perf_path), 'req': requirements})


def description(req):
     data = ''
     index = req.GET.get('index')
     name = req.GET.get('name')

     if index:
          index = int(index)
          data = ''

          with open("data.txt", "r") as file:
               data = json.loads(file.read())["validation_table"][index]
          
          description = API.getInformation(data[0])['description']

          return render(req, "main/results/desc.html", {'name': data[0], 'desc': description})
     elif name:
          description = API.getInformation(name)['description']
     
          return render(req, "main/results/desc.html", {'name': name, 'desc': description})

def flow(req):
     data = ''
     index = req.GET.get('index')
     name = req.GET.get('name')

     if index:
          index = int(index)
          with open("data.txt", "r") as file:
               data = json.loads(file.read())["validation_table"][index]
          
          package_path = API.getInformation(data[0])['flow_chart']
          path = os.path.join(os.path.dirname(API_PATH.__file__), package_path)

          return render(req, "main/results/flow.html", {'name': data[0], 'path': os.path.basename(path)})
     elif name:
          package_path = API.getInformation(name)['flow_chart']
          path = os.path.join(os.path.dirname(API_PATH.__file__), package_path)

          return render(req, "main/results/flow.html", {'name': name, 'path': os.path.basename(path)})

def performance(req):
     data = ''
     index = req.GET.get('index')
     name = req.GET.get('name')

     if index:
          index = int(index)
          with open("data.txt", "r") as file:
               data = json.loads(file.read())["validation_table"][index]
          
          package_path = API.getInformation(data[0])['performance']
          path = os.path.join(os.path.dirname(API_PATH.__file__), package_path)

          return render(req, "main/results/performance.html", {'name': data[0], 'path': os.path.basename(path)})
     elif name:
          package_path = API.getInformation(name)['performance']
          path = os.path.join(os.path.dirname(API_PATH.__file__), package_path)
     
          return render(req, "main/results/performance.html", {'name': name, 'path': os.path.basename(path)})

def requirements(req):
     data = ''
     index = req.GET.get('index')
     name = req.GET.get('name')

     if index:
          index = int(index)
          data = ''

          with open("data.txt", "r") as file:
               data = json.loads(file.read())["validation_table"][index]
          
          requirements = API.getInformation(data[0])['requirements']

          return render(req, "main/results/requirements.html", {'name': data[0], 'requirements': requirements})
     elif name:
          requirements = API.getInformation(name)['requirements']
     
          return render(req, "main/results/requirements.html", {'name': name, 'requirements': requirements})

def configuration(req):
     data = ''
     index = req.GET.get('index')
     name = req.GET.get('name')

     if index:
          index = int(index)
          data = ''

          with open("data.txt", "r") as file:
               data = json.loads(file.read())["validation_table"][index]
          
          configuration = API.getInformation(data[0])['configuration']

          return render(req, "main/results/configuration.html", {'name': data[0], 'configuration': configuration})
     elif name:
          configuration = API.getInformation(name)['configuration']

          return render(req, "main/results/configuration.html", {'name': name, 'configuration': configuration})

def downloadCon(req):
     data = ''
     index = req.GET.get('index')
     name = req.GET.get('name')
     configs = req.GET.get('configs')

     if index:
          index = int(index)

          with open("data.txt", "r") as file:
               data = json.loads(file.read())["validation_table"][index]
     
          paths = API.getConfigurationFiles(data[0], configs)
     elif name:     
          configs = json.loads(configs)
          paths = API.getConfigurationFiles(name, configs)

     with zipfile.ZipFile('main/static/controls.zip', 'w') as zip:
          for path in paths:
               path = os.path.join(os.path.dirname(API_PATH.__file__), path)
               
               with open(path, 'r') as file:
                    zip.writestr(os.path.basename(path), file.read())

     response = None

     with open('main/static/controls.zip', 'rb') as zip_response:
          response = HttpResponse(zip_response.read(), content_type='application/zip')
          response['Content-Disposition'] = f'attachment; filename=controls.zip'

     return response

def download(req):
     data = ''
     index = req.GET.get('index')
     name = req.GET.get('name')
     paths = []

     if index:
          index = int(index)

          with open("data.txt", "r") as file:
               data = json.loads(file.read())["validation_table"][index]
     
          paths = API.getInformation(data[0])['download']
          print("OOOOOOOOOOOOOOOOOOOOOO")
          print(paths)
     elif name:     
          paths = API.getInformation(name)['download']

     with zipfile.ZipFile('main/static/controls.zip', 'w') as zip:
          for path in paths:
               path = os.path.join(os.path.dirname(API_PATH.__file__), path)
               
               with open(path, 'r') as file:
                    zip.writestr(os.path.basename(path), file.read())

     response = None

     with open('main/static/controls.zip', 'rb') as zip_response:
          response = HttpResponse(zip_response.read(), content_type='application/zip')
          response['Content-Disposition'] = f'attachment; filename=controls.zip'

     return response
