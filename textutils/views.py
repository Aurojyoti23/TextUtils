from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    getxt = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == "on":
        panctuations = '''!~`.,<>/?'":;\|[]{}()*@$%^&-_'''
        analyzed = ""
        for char in getxt:
            if char not in panctuations:
                analyzed = analyzed+char
        params = {'purpose':'Removed Panctuations', 'analyzed_text':analyzed}
        getxt = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in getxt:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        getxt = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in getxt:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char.upper()

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        getxt = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(getxt):
            if not(getxt[index] == " " and getxt[index + 1] == " "):
                analyzed = analyzed + char

            params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
