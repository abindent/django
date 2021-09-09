from django.http import HttpResponse
from django.shortcuts import render
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class command(BaseCommand):
     def handle(self, *args, **options):
        User.objects.create_user(username="sinchan", email="maitrababai2007@gmail.com", password="SinchanSuperAdmin45", is_staff=True, is_active=True, is_superuser=True,) 
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
  
