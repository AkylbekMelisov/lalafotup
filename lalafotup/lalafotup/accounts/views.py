from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect('home')
    context = {"form": form}
    return render(request, 'my_accs/register.html', context)


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        try:
            login(request, user)
            return redirect('home')
        except:
            return HttpResponse("У Вас не достаточно прав!!! Активируйте свой аккаунт!")
    return render(request, 'my_accs/login.html')


def logout_page(request):
    logout(request)
    return redirect('home')
