from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import CustomUserForm
from epoll.forms import VoterForm
from django.contrib.auth import login, logout
from .email_backend import EmailBackend
# Create your views here.

def account_login(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return redirect(reverse("administrator:adminDashboard"))
        else:
            return redirect(reverse("epoll:voterDashboard"))

    context = {}
    if request.method == 'POST':
        user = EmailBackend.authenticate(request, username=request.POST.get(
            'email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            if user.user_type == '1':
                return redirect(reverse("administrator:adminDashboard"))  
            else:
                return redirect(reverse("epoll:voterDashboard"))
        else:
            messages.error(request, "Invalid details")
            return redirect("accounts:accounts_login")

    return render(request, "login.html")


def account_register(request):
    userForm = CustomUserForm(request.POST or None)
    voterForm = VoterForm(request.POST or None)
    context = {
        'form1': userForm,
        'form2': voterForm
    }
    if request.method == 'POST':
        if userForm.is_valid() and voterForm.is_valid():
            user = userForm.save(commit=False)
            voter = voterForm.save(commit=False)
            voter.admin = user
            user.save()
            voter.admin.save()
            messages.success(request, "Account created. You can login now!")
            return redirect(reverse('accounts:accounts_login'))
        else:
            messages.error(request, "Provided data failed validation")
            return account_login(request)
    return render(request, "register.html", context)


def account_logout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        messages.success(request, "Thank you for visiting us!")
    else:
        messages.error(
            request, "You need to be logged in to perform this action")

    return render(request, "landing_page.html")
        
