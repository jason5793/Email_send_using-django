from django.core.mail import send_mail 
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import Contact

def index(request):
    if request.method =='POST':
        form=Contact(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            date=form.cleaned_data['date']
            html=render_to_string('contact/emails/contactform.html',{
                'name':name,
                'email':email,
                'dob':date
            })
            print('the form is valid')
            send_mail(' the conatct form subject','this is the message','pyrbotgaming@gmail.com',['jasonvlog81@gmail.com'],html_message=html)
            return redirect('index')
    else: 
        form=Contact
    return render(request,'contact/index.html',{
        'form':form
    })   