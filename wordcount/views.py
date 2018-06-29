from django.http import HttpResponse
from django.shortcuts import render
import re

def home(request):
    return render(request, 'homepage.html') 

def aditya(request):
    return HttpResponse('<h1>This is Aditya!</h1>') 

def count(request):
    return render(request, 'count.html')
	
def result(request):
	wcount=request.GET['wcount']
	wordlist=wcount.split()
	finallist={}
	for word in wordlist:
		if word in finallist:
			count+=1
		else:
			count=1
		fcount=count
		finallist.update({word:fcount})
	return render(request, 'result.html', {'wcount':wcount,'count':len(wordlist),'finallist':finallist})
	