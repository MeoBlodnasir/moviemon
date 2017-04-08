from django.shortcuts import render, HttpResponse
from . import forms

# Create your views here.

def titlescreen(request):
    if (request.method == 'POST'):
        form = forms.MyForm(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data['submit'])
        else:
            return HttpResponse("OULQLQ")

    else:
        form = forms.MyForm()
    return render(request, "game/controls.html")

