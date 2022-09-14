from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from . models import Song
from . models import backsong
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
def home(request):
    #return HttpResponse("<center><b><h1>Welocome friends at Adbhut Sur</h1></b></center>")
    return render(request, 'main.html')


def index(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)

def rec(request):
    page_obj= backsong.objects.all()
    context={"page_obj":page_obj}
    return render(request,"record.html",context)

def sing(request):
    page_ob= backsong.objects.all()
    context={"page_ob":page_ob}
    return render(request,"sing/index.html",context)

def nam(request):
    if request.method == 'POST':
        # no need to do this
        # request_csrf_token = request.POST.get('csrfmiddlewaretoken', '')
        ms=request.POST['send']
      #  vansh = request.POST.get('result_data') 
       # request_getdata ={"vansh":vansh}
      #  page_obj= backsong.objects.all()
        a=backsong.objects.filter(title=ms)
        context={"page_obj":a}
 #       cont={"msg":msg}
    return render(request,"record.html",context) 

