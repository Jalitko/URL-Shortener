from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Short
import json

def log(*args, **kwargs):
    WARNING = f'\033[94m\033[1m{args[0]}'
    ENDC = '\033[0m'
    
    args = list(args)
    args.pop(0)
    args = tuple(args)
    args = (WARNING, *args, ENDC)

    print(*args, **kwargs)
# Create your views here.



def index(request, short = None):
    
    if request.method == 'POST':
        
        if "title" in request.POST:
            title = request.POST.get('title')
            url = request.POST.get("url")
            short = request.POST.get("short")
            
            short_obj = Short.objects.create(
                            title = title,
                            short = short,
                            url = url 
                        )
            
            
            response = [str(short_obj.id), title, url, short]
            response = json.dumps(response)
            
            return HttpResponse(response, content_type='application/json')
            
        
        elif "delete" in request.POST:
            id = request.POST.get('id')
            Short.objects.get(id=id).delete()
            return HttpResponse('kool')
            
    
    
    if short is None:
        
        shorts = Short.objects.all()
        context= {
            'shorts' : shorts,
        }
        return render(request, "index.html", context)
        
    
    
    try : 
        url = Short.objects.get(short=short)
        link = url.url
        if "http" not in link:
            link = "http://" + link
            log(link)
        return redirect(link)
    except: 
        return render(request, "error.html")









#python manage.py runserver 192.168.101.46:5000