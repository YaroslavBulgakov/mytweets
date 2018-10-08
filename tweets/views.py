from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
'''
Итак создадим классовое представление в них есть свои плюсы,для начала простое
а потом уже перейдем к немного более сложным
'''
class Index(View):
    def get(self,request):
        params={}
        params['name']='Django'
        return render(request,'base.html',params)
    def post(self,request):
        return HttpResponse('Запрос опубликован')

