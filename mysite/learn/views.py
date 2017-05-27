#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	data = map(str,range(100))
	return render(request,'home.html',{'data':data})