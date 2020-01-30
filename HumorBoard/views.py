from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render
from HumorBoard.models import *
from datetime import datetime

# Create your views here.
# def index(request):
#     return HttpResponse("<h1>Hello, World!</h1>")
def index(request):
    msg = 'My Message'
    return render(request, 'HumorBoard/index.html', {'message': msg})


# Feedback 객체 생성
userInfo = UserInfo(name='Kim', email='kim@test.com', comment='Hi', createDate=datetime.now())

# 새 객체 INSERT
userInfo.save()

def error(request):
    #return HttpResponseNotFound('<h1>not found</h1>')
    raise Http404("Not Found")