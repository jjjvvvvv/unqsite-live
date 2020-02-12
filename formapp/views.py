from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm

def contact(request):

    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            #print(name, email, phone, message)
            form.save()

    form = ContactForm()
    return render(request, 'form.html', {'form': form})

def snippet_detail(request):

    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()


    form = SnippetForm()
    return render(request, 'form.html', {'form': form})