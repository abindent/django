from django.http import HttpResponse
from django.shortcuts import render
 
def index(request):
     return render(request, 'index.html')

def aboutus(request):
    return render(request, 'about.html')
def banappeal(request):
  return render(request, 'ban-appeal.html') 
def stats(request):
      return render(request, 'stats.html') 
def support(request):
     return render(request, 'support.html')
def applications(request):
     return render(request, 'apply.html')
