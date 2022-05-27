import imp

from django.shortcuts import render, redirect
from .forms import CreateUserForm , UserUpdateForm , ProfileUpdateForm
from django.views.generic import ListView 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required(login_url='login')
def home(request):
    p_form = ProfileUpdateForm(instance=request.user.foydalanuvchi)
    context = {
       'p_form':p_form         
    }
    return render(request, 'bulim/home.html',context)



@login_required(login_url='login')
def Profile(request):
    if request.method == 'POST':
        
         u_form = UserUpdateForm(request.POST,instance=request.user)
         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.foydalanuvchi)
         
         if u_form.is_valid() and p_form.is_valid():
             u_form.save()
             p_form.save() 
             
             messages.success(request, 'Qoyil yangi malumotlar profilni yangiladi')
             return redirect('profile') 
    else:
           u_form = UserUpdateForm(instance=request.user)
           p_form = ProfileUpdateForm(instance=request.user.foydalanuvchi)
    
    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    
    return render(request, 'bulim/profile.html', context)

def RegisterPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm(request.POST)
        if request.method == 'POST':
            
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data.get('username')
                form.save()      
                messages.success(request, 'Siz register buldingiz ' + user)    
                return redirect('login')
            
            else:
                messages.info(request, 'Parol yoki email xato , Parol misol : Twist2004?')  
        return render(request,'bulim/index.html',{'form':form})

def LoginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
              login(request, user)
              return redirect('home')
        else:
            messages.error(request, 'Parol yoki username xato')
            return redirect('login')
    return render(request,'bulim/login.html')   


def logoutUser(request):
    logout(request)
    return redirect('login')     






class PostListView(ListView):
    model = Product 
    template_name = 'bulim/home.html'
    context_object_name = 'product'

    
    