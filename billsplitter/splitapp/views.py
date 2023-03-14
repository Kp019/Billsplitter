from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login
from .models import Bill, create_grp, add_parti

# Create your views here.
def login(request):
    return render(request, 'login.html')    


def signup(request):
    return render(request, 'signup.html')    


def bill(request):
    if request.method == 'POST': 
        Bill.b_name = request.POST.get('b_name')
        item_name = request.POST.get('b_item')
        item_qty = request.POST.get('b_qty')
        item_price = request.POST.get('b_price')
        Bill.add_item(item_name,item_qty,item_price)

    return render(request, 'create_bill.html')


def create_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        create_grp.grp_name = group_name
    return render(request, 'creategroup.html')



def add_parti(request):
    if request.method == 'POST':
        participant = User.objects.all()
        p_name = request.POST.get('name')
        if p_name in participant:
            add_parti.parti_name = p_name

    return render(request, 'addparti.html')


def bill_details(request):
    if request.method == 'POST':
        final_amt = Bill.bill
    return render(final_amt, 'bulldetails.html')