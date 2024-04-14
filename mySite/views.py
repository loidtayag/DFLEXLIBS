from celery.result import AsyncResult
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import Upload
from rdflib import Graph
from .DFLEXLIBS.validation.buildingMOTIF_interface import results
import json
from .DFLEXLIBS import controls as API_PATH
from . import API
import zipfile
import os
import io
from celery import shared_task
import secrets
import string
from django.core.cache import cache
import time
import yaml

@shared_task
def myTask(uploaded):
     return results(uploaded)

def base(request):
     return render(request, "base.html", {})

def search(request):
     filter = request.GET.get('order')
     data = list(API.getControls().keys())

     if filter is None or filter == 'ascending':
          data = sorted(data)
     elif filter == 'descending':
          data = sorted(data, reverse=True)

     temp = {
          "validation_table": [],
          "suitable_controlApps": [], 
          "non_suitable_controlApps": []
     }
     temp["validation_table"] = [[item, True] for item in data]
     temp["suitable_controlApps"] = data
     data = temp

     res = render(request, "results.html", {'data': data, 'order': filter})
     res.set_cookie('data', json.dumps(data))
     
     return res

def navigate(req):
     archetype = req.GET.get("archetype")
     target = req.GET.get("target")
     options = None
     prompt_upper = 'Archetype'
     prompt_lower = 'archetype'

     if archetype == None and target == None:
          options = API.getFilters().keys()
     elif archetype != None and target == None:
          prompt_upper = 'Target level'
          prompt_lower = 'target level'
          options = API.getFilters()[archetype].keys()
     elif archetype != None and target != None:
          prompt_upper = 'Strategy'
          prompt_lower = 'application'
          options = API.getFilters()[archetype][target]
     
     return render(req, "navigate.html", {'options': options, 'prompt_upper': prompt_upper, 'prompt_lower': prompt_lower})

# celery -A myApp worker --pool=solo -l info
def checkValidate(req): 
     try:
          id = req.GET.get('id')
          token = req.GET.get('token')
          task = AsyncResult(id)
          tokens = list(cache.get('tokens'))

          if tokens[0] == token:
               cache.set('lastCheck', time.time())
               cache.delete('alreadyDeleted')

               if task.ready():
                    res = JsonResponse(task.get(), safe = False)
                    res.set_cookie('data', task.get())
                    tokens.pop(0)
                    cache.set('tokens', tokens)
                    return res
               else:
                    return JsonResponse({"validation_table": "Task is still running..."})
          elif token in tokens:
               lastCheck = cache.get('lastCheck') 
               alreadDeleted = cache.get('alreadyDeleted')
               if alreadDeleted == None and time.time() - float(lastCheck) > 5:
                    tokens.pop(0)
                    cache.set('tokens', tokens)
                    cache.set('alreadyDeleted', '')

               return JsonResponse({"validation_table": "In queue...", "place": tokens.index(token)})
     except Exception as _:
          return JsonResponse({"validation_table": "Error..."})

def validate(req):
     data = "Upload graph first" 
     uploaded = "Upload graph first" 

     def generateToken(len = 20):
          symbols = string.ascii_letters + string.digits
          return ''.join(secrets.choice(symbols) for _ in range(len))
          
     if req.method == "POST":
          form = Upload(req.POST, req.FILES)
          res = None
          if form.is_valid():
               uploaded = form.cleaned_data['file'].read().decode()
               graph = Graph()
               graph.parse(data=uploaded)
               uploaded = graph.serialize()
               
               try:
                    data = results(uploaded)
               except Exception as e:
                    data = 'Error'

               res = HttpResponse(data, content_type='text')
               res.set_cookie('data', data)
               # This is for celery but doesn't work on deployment
               # id = myTask.delay(uploaded).id
               # data = str(id)
               # token = generateToken()
               # data += '&' + token
               
               # tokens = cache.get('tokens') 
               # if tokens == None:
               #      tokens = []
               # else:
               #      tokens = list(tokens)

               # tokens.append(token)
               # cache.set('tokens', tokens)
               
               # if tokens[0] == token:
               #      cache.set('lastCheck', time.time())
          else:
               data = 'File data is invalid'
               res = HttpResponse(data, content_type='text')
          return res

     return render(req, "validate.html", {"form": Upload()})

def resultss(req):
     filter = req.GET.get('order')
     data = json.loads(req.COOKIES.get('data'))

     temp = {
          "validation_table": [],
          "suitable_controlApps": [], 
          "non_suitable_controlApps": []
     }

     if filter == 'ascending':
          temp["validation_table"] = sorted(data["validation_table"], key=lambda item: item[0])
     elif filter == 'descending':
          temp["validation_table"] = sorted(data["validation_table"], key=lambda item: item[0], reverse = True)
     elif filter == None:
          temp["validation_table"] = data["validation_table"]

     temp["suitable_controlApps"] = data['suitable_controlApps']
     temp["non_suitable_controlApps"] = data['non_suitable_controlApps']
     data = temp

     res = render(req, "results.html", {'data': data})
     res.set_cookie('data', json.dumps(data))
     
     return res

def report(req):
     data = json.loads(req.COOKIES.get('data'))
     index = int(req.GET.get('index', ''))
     want =  data["validation_table"][index]
     data = data['non_suitable_controlApps']

     for item in data:
          if item[0] == want[0]:
               data = item
               break
     
     reasons = data[1:]     
     reasons_text = [s.split("http")[0] for s in reasons]
     reasons_link = ["http" + s.split("http")[1] for s in reasons]
     reasons = list(zip(reasons_text, reasons_link))
     return render(req, "results/report.html", {'name': data[0], 'reasons': reasons})
    
def info(req):
     index = req.GET.get('index', '')
     name = req.GET.get('name', '')

     if index:
          data = json.loads(req.COOKIES.get('data'))
          index = int(index)
          data = data["validation_table"][index]
     elif name:
          data = [name]

     desc = API.getInformation(data[0])['description']
     requirements = API.getInformation(data[0])['requirements']
     flow_path = API.getInformation(data[0])['flow_chart']
     perf_path = API.getInformation(data[0])['performance']

     return render(req, "results/info.html", {'name': data[0], 'desc': desc, 'flow': flow_path, 'perf': perf_path, 'req': requirements})

def description(req):
     index = req.GET.get('index')
     name = req.GET.get('name')

     if index:
          data = json.loads(req.COOKIES.get('data'))
          index = int(index)
          data = data["validation_table"][index]
          
          description = API.getInformation(data[0])['description']

          return render(req, "results/desc.html", {'name': data[0], 'desc': description})
     elif name:
          description = API.getInformation(name)['description']
     
          return render(req, "results/desc.html", {'name': name, 'desc': description})

def flow(req):
     index = req.GET.get('index')
     name = req.GET.get('name')

     if index:
          data = json.loads(req.COOKIES.get('data'))
          index = int(index)
          data = data["validation_table"][index]
          
          path = API.getInformation(data[0])['flow_chart']

          return render(req, "results/flow.html", {'name': data[0], 'path': path})
     elif name:
          path = API.getInformation(name)['flow_chart']

          return render(req, "results/flow.html", {'name': name, 'path': path})

def performance(req):
     index = req.GET.get('index')
     name = req.GET.get('name')

     if index:
          data = json.loads(req.COOKIES.get('data'))
          index = int(index)
          data = data["validation_table"][index]
          
          path = API.getInformation(data[0])['performance']

          return render(req, "results/performance.html", {'name': data[0], 'path': path})
     elif name:
          path = API.getInformation(name)['performance']
     
          return render(req, "results/performance.html", {'name': name, 'path': path})

def requirements(req):
     index = req.GET.get('index')
     name = req.GET.get('name')

     if index:
          data = json.loads(req.COOKIES.get('data'))
          index = int(index)
          data = data["validation_table"][index]
          
          requirements = API.getInformation(data[0])['requirements']

          return render(req, "results/requirements.html", {'name': data[0], 'requirements': requirements})
     elif name:
          requirements = API.getInformation(name)['requirements']
     
          return render(req, "results/requirements.html", {'name': name, 'requirements': requirements})

def configuration(req):
     index = req.GET.get('index')
     name = req.GET.get('name')

     if index:
          data = json.loads(req.COOKIES.get('data'))
          index = int(index)
          data = data["validation_table"][index]
          name = data[0]
          configuration = API.getInformation(data[0])['configuration']

          return render(req, "results/configuration.html", {'name': data[0], 'configuration': configuration, 'name': name})
     elif name:
          configuration = API.getInformation(name)['configuration']

          return render(req, "results/configuration.html", {'name': name, 'configuration': configuration, 'name': name})

def downloadCon(req):
    name = ''
    configs = {}

    for key, value in req.GET.items():
        if key == 'control':
            name = value
        else:
            configs[key] = value

    configuration_data = API.getConfigurationFiles(name, configs)
    yaml_data = yaml.dump(configuration_data, default_flow_style=False)

    myZip = io.BytesIO()
    with zipfile.ZipFile(myZip, 'w') as zip:
        zip.writestr('configuration.yaml', yaml_data.encode('utf-8'))

    myZip.seek(0)
    response = HttpResponse(myZip.read(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=configuration.zip'

    return response

def download(req):
     index = req.GET.get('index')
     name = req.GET.get('name')
     paths = []

     if index != None:
          data = json.loads(req.COOKIES.get('data'))
          index = int(index)

          data = data["validation_table"][index]
          paths = API.getInformation(data[0])['download']
     elif name != None:     
          paths = API.getInformation(name)['download']

     myZip = io.BytesIO()

     def getImages(srcDir):
          for path in os.listdir(srcDir):
               path = os.path.join(srcDir, path)

               if os.path.isdir(path):
                    getImages(path)
               else:
                    if path.lower().endswith('.py'): 
                         with open(path, 'r') as file:
                              zip.writestr(os.path.basename(path), file.read())

     with zipfile.ZipFile(myZip, 'w') as zip:
          for path in paths:
               path = os.path.join(os.path.dirname(os.path.dirname(API_PATH.__file__)), path)
               if os.path.isdir(path):
                    getImages(path)
               else:
                    with open(path, 'r') as file:
                         zip.writestr(os.path.basename(path), file.read())

     myZip.seek(0)
     response = HttpResponse(myZip.read(), content_type='application/zip')
     response['Content-Disposition'] = f'attachment; filename=controls.zip'

     return response
