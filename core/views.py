
#from django import views
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request,'core/home.html')
class singup(View):
    def get(self,request):
        fm=SignUpForm()
        return render(request,'core/signup.html',{'form':fm})
    def post(self,request):
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"sign up success !")
            return redirect('/signup')
        else:
             return render(request,'core/signup.html',{'form':fm})

class mylogin(View):
    def get(self,request):
        fm=myloginform()
        return render(request,'core/login.html',{'form':fm}) 
    def post(self,request):
        fm=myloginform(request,data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('/')
                
    
            else:
        # Return an 'invalid login' error message.
                return render(request,'core/login.html',{'form':fm})
        else:
            return render(request,'core/login.html',{'form':fm})         






#def signup(request):
#    return render(request,'core/signup.html')
def about(request):
    return render(request,'core/about.html')
def contact(request):
    return render(request,'core/contact.html')
#def login(request):
 #   return render(request,'core/login.html')
