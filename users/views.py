from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST);
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f"{username} is created successfully")
            return redirect('login')
        else :
            return render(request, "users/register.html", {
                "form": form
            })
    form=UserRegisterForm();
    return render(request,"users/register.html",{
        "form":form
    })


def home(request):
    return render(request,"users/home.html")