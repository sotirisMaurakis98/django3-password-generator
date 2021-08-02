from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
	return render(request,'generator/home.html')

def password(request):

	thepassword = '' 

	characters = list('abcdefghijklmnopqrstuvwxyz')

	length = int(request.GET.get('length',12))

	numbers = request.GET.get('numbers')

	special = request.GET.get('special')

	uppercase = request.GET.get('uppercase')

	if numbers:
		characters.extend(list('123456789'))

	if special:
		characters.extend(list('!@#$%^&*}{)(+=/'))
		
	if uppercase:
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	

	for x in range(length):
		thepassword += random.choice(characters)

	return render(request, 'generator/password.html',
		{'password':thepassword})






