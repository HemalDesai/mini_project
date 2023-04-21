from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog_food
from accounts.models import Accounts
from .forms import *
from datetime import datetime

def LNMfood_home(request):
    if not request.session.has_key('uid'):
        return redirect('login')
    blogs = Blog_food.objects.filter(date__lt=datetime.now().date())
    blogs.delete()
    blogs = Blog_food.objects.filter(date=datetime.now().date(), time__lt=datetime.now().time())
    blogs.delete()
    blogs = Blog_food.objects.all().order_by('date')
    context ={'username': request.session['uid']}
    if blogs.count():
        context = {'blogs': blogs, 'username': request.session['uid']}
    return render(request, 'LNMfood/LNMfood_home.html', context)


def view_blog_food(request):

    blogs = Blog_food.objects.filter(username_id= request.session['uid']).order_by('date')
    context = {'user_blogs': blogs, 'username': request.session['uid']}
    return render(request, 'LNMfood/view_blog_food.html', context)


def insert_blog_food(request):

    if request.method == 'POST':
        username = request.session['uid']
        blog = Blog_food()
        blog.pickup = request.POST['pickup']
        blog.drop = request.POST['drop']
        blog.username = Accounts(user_name= username)
        blog.space = request.POST['space']
        blog.contact_num = request.POST['contact_num']
        blog.fare = request.POST['fare']
        blog.date = request.POST['date']
        blog.time = request.POST['time']
        blog.color = Blog_food.get_random_colour()
        blog.save()
        return redirect('LNMfood_home')
    account = Accounts.objects.get(user_name=request.session[('uid')])
    context = {'username': request.session['uid'], 'account': account}
    return render(request, 'LNMfood/insert_blog_food.html', context)


def delete_blog(request, id):
    blog = Blog_food.objects.filter(id=id)
    blog.delete()
    return view_blog_food(request)