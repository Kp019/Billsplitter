from django.shortcuts import render

# Create your views here.
def HomePage(request):
    pass

def SignUp(request):
    return render(request, 'signup.html')

def LogIn(request):
    pass