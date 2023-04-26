from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from accounts.models import Accounts
from .forms import *
# Create your views here.

categories = {
    'All': 'All',
    'Electronics': 'Electronics',
    'Furniture': 'Furniture',
    'Fashion': 'Fashion',
    'Books': 'Books',
    'Sports': 'Sports',
    'Services': 'Services',
    'Vehicles': 'Vehicles',
    'Food': 'Food'
}


def LNMlnf_home(request):
    if not request.session.has_key('uid'):
        return redirect('login')
    products = LNFProducts.objects.all()
    context = {'categories': categories, 'products': products,
               'username': request.session['uid'], 'type': 'All'}
    if request.method == 'POST' and request.POST['category'] != 'All':
        products = LNFProducts.objects.filter(category=request.POST['category'])
        context['products'] = products
        context['type'] = request.POST['category']
    return render(request, 'LNMlnf/LNMlnf_home.html', context)


def lnfview_product(request):
    if not request.session.has_key('uid'):
        return redirect('login')

    username = request.session['uid']
    user_products = LNFProducts.objects.filter(username_id=username)
    context = {'products': user_products, 'categories': categories,
               'username': request.session['uid']}
    return render(request, 'LNMlnf/view_product.html', context)


def lnfinsert_product(request):
    if not request.session.has_key('uid'):
        return redirect('login')
    if request.method == 'POST':
        product = LNFProducts()
        product.name = request.POST['name']
        product.description = request.POST['description']
        # product.price = request.POST['price']
        product.photo = request.FILES['photo']
        product.category = request.POST['category']
        product.contact_num = request.POST['contact_num']
        product.color = product.get_random_colour()
        product.username = Accounts(user_name=request.session['uid'])
        product.save()
        return redirect('LNMshop_home')
    account = Accounts.objects.get(user_name=request.session[('uid')])
    context = {'form': LNFProductForm(), 'categories': categories,
               'username': request.session['uid'], 'account': account}
    return render(request, 'LNMlnf/insert_product.html', context)


def lnfdelete_product(request, id):
    product = LNFProducts.objects.filter(id=id)
    product.delete()
    username = request.session['uid']
    user_products = LNFProducts.objects.filter(username_id=username)
    context = {'products': user_products, 'username': request.session['uid']}
    return render(request, 'LNMlnf/view_product.html', context)






def lnfupdate_product(request):

    if request.method == 'POST':
        product = LNFProducts.objects.get(id=request.POST['id'])
        product_form = LNFProductForm(
            request.POST, request.FILES, instance=product)
        print(product_form)
        if product_form.is_valid():
            product_form.save()

    return redirect('view_product')
