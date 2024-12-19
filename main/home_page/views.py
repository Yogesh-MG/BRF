from django.shortcuts import render, redirect
from .forms import FillForm, NewsletterForm
from django.contrib import messages
# Create your views here.

def base(request):
    if request.method == "POST":
        if request.POST.get('form_type') == 'form1':
            form = FillForm(request.POST)
            print(form)
            if form.is_valid():
                form.save()
                messages.success(request, "You have submitted sucessfull")
                return redirect('home')
            else:
                messages.error(request, 'failed')
                
                
        elif request.POST.get('form_type') == 'form2':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                messages.error(request, 'failed')
            
    return render(request, 'home.html')

def about(request):
    return render(request, 'about_page/about.html')