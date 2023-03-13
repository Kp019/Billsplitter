from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

def SignUp(request):
    return render(request, 'signup.html')

def LogIn(request):
    return render(request, 'login.html')