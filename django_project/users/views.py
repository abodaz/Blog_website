from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(requset):
    if requset.method == "POST":
        form = UserRegisterForm(requset.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(requset, f'Your Account has been created, you can log in!!')
            return redirect('login')
        else:
            print('not valid')
            messages.warning(requset,'Use a valid info!')
            return redirect('register')

    else:
        form = UserRegisterForm()
        return render(requset,'users/register.html', {'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')