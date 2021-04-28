# This file Created by Devendra
from django.http import HttpResponse
from django.shortcuts import render

def index(request) :
    return render(request, 'index.html')

def about(request) :
    return render(request, 'about.html')

def contact(request) :
    return render(request, 'contact.html')

def analyze(request) :

    gettext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    newline_remove = request.POST.get('newline_remove','off')
    extraspace_remove = request.POST.get('extraspace_remove','off')
    charcount = request.POST.get('charcount','off')
    analyazed = ''
    
    if removepunc == 'on' :
        punctuations = '''!()-[]{};:'""\,<>./?@#$%^&*_~'''
        for char in gettext:
            if char not in punctuations:
                analyazed = analyazed + char

        data = { 'purpose':'Remove Punctuations', 'analyazed':analyazed }
        return render(request, 'analyaze.html', data)

    elif uppercase == 'on':
        for char in gettext:
            analyazed = analyazed + char.upper()
        data = { 'purpose':'Changed to uppercase', 'analyazed':analyazed }
        return render(request, 'analyaze.html', data)

    elif newline_remove == 'on':
        analyazed = gettext.replace('\n','')
        data = { 'purpose':'New Line Remove', 'analyazed':analyazed }
        return render(request, 'analyaze.html', data)

    elif extraspace_remove == 'on':
        for index, char in enumerate(gettext):
            if not(gettext[index] == " " and gettext[index+1] ==  " "):
                analyazed = analyazed + char
        data = { 'purpose':'Extra Spaces Remove', 'analyazed':analyazed }
        return render(request, 'analyaze.html', data)

    elif charcount == 'on':
        for char in gettext:
            analyazed = analyazed + char.upper()
        data = { 'purpose':'Changed to uppercase', 'analyazed':analyazed }
        return render(request, 'analyaze.html', data)
        
    else:
        return HttpResponse('Please Choose Options')