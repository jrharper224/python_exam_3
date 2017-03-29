from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import *


# Create your views here.
def index(request):

    return render(request, 'wish/index.html')


def user_wishes(request):
    return dedirect('/wish')

def item(request, id):
    context = {
    'id': id,
    'item': Wish_list.objects.get(id = id),
    'wishers': Wish_list.objects.get(id = id)
    }
    return render(request, 'wish/item.html', context)

def wish(request):
    context = {
        'user_items': Wish_list.objects.filter(added_by = request.session['name'])|Wish_list.objects.filter(wishers = request.session['id']),
        'other_items': Wish_list.objects.all().exclude(added_by = request.session['name']),
        # 'other_items':Wish_list.objects.exclude(wishers = request.session['id'], added_by = request.session['name']),
        # When I do the above query that should be excluding both wishers and added_by for the logged in user, the query filters nothing out. I am unsure why.


        }

    return render(request, 'wish/success.html', context)
def delete_item(request, id):
    item = Wish_list.objects.get(id = id)
    item.delete()
    return HttpResponseRedirect('/wish')

def list_add(request, id):
    item = Wish_list.objects.get(id = id)
    user = request.session['id']
    item.wishers.add(user)
    return redirect('/wish')


def login_user(request):
    login = User.objects.login_user(request.POST)
    if login[0]:
        request.session['id'] = login[1].id
        request.session['name'] = login[1].name
        return redirect('/wish')
    else:
        message.error(request, "Invalid Login")
    return redirect('/')


def create_user(request):
    #used to validate and create a new user
    if User.objects.validate_user(request.POST):
        user = User.objects.create(
            name = request.POST.get('name'),
            username = request.POST.get('username'),
            password = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt()),
            date_hired = request.POST.get('date_hired'),
        )
        request.session['user_id'] = user.id
        request.session['name'] = user.name
        request.session['id'] = request.session['user_id']
        return redirect('/wish')
    return redirect('/')



def add_item(request):
    return render(request, 'wish/create.html')

def create_item(request):
    if Wish_list.objects.validate_item(request.POST):
        item = Wish_list.objects.create(
            item = request.POST.get('item'),
            added_by = request.session['name'],
        )
        return redirect('/wish')
    return redirect('/add_item')


def logout(request):
    request.session.clear()
    return redirect('/')
