from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from Product.models import category,product

def logins(request):
    data={}
    if request.method == "POST":
        userN = request.POST.get('userName')
        pas= request.POST.get('password')
        print(userN)
        print(pas)
        check = authenticate(username=userN, password=pas)
        if check != None:
            login(request, check)
            data={
                'userName' : check.first_name,
            }
            messages.success(request, "Login Secessfully")
            return redirect("home/",data)
        else:
            messages.error(request, "Wrong Details")
        
    return render(request,'index.html')

def register(request):
    try:
        if request.method == "POST":
            fname = request.POST['fname']
            lname = request.POST['lname']
            userName = request.POST['userName']
            email = request.POST['email']
            pass1 = request.POST['password']
            pass2 = request.POST['passwordR']
            create = User.objects.create_user(userName,email,pass1)
            create.first_name = fname
            create.last_name = lname
            create.save()
            messages.success(request,"You have register Secessfully")
            return redirect('login')
            
            
    
    except:
        pass
    return render(request,'register.html')

def home(request):
    try:
        if request.method == "POST":
            messages.success(request, "Hello Then")
    
    except:
        pass    
    data={}
    unq_cat_list = []
    catList = []
    cat = category.objects.all()
    prd = product.objects.all()
    for pr in prd:
        if pr.Category.id not in unq_cat_list:
            unq_cat_list.append(pr.Category.id)
            # print(unq_cat_list)
    for ct in cat:
        if ct.id in unq_cat_list:
            catList.append(ct)
    data={
        'cat' : catList,
        'prd' : prd
    }
    return render(request,'home.html',data)

def logouts(request):
    logout(request)
    messages.success(request,'Logged out Sucessfully')
    return redirect('/')

def cart(request):
    try:
        if request.method == "POST":
            messages.success(request, "Hello Then")
    
    except:
        pass    
    data={}
    unq_cat_list = []
    catList = []
    cat = category.objects.all()
    prd = product.objects.all()
    for pr in prd:
        if pr.Category.id not in unq_cat_list:
            unq_cat_list.append(pr.Category.id)
            # print(unq_cat_list)
    for ct in cat:
        if ct.id in unq_cat_list:
            catList.append(ct)
    data={
        'cat' : catList,
        'prd' : prd
    }
    return render(request, 'cart.html',data)


def checkout(request):
    try:
        if request.method == "POST":
            messages.success(request, "Hello Then")
    
    except:
        pass    
    data={}
    unq_cat_list = []
    catList = []
    cat = category.objects.all()
    prd = product.objects.all()
    for pr in prd:
        if pr.Category.id not in unq_cat_list:
            unq_cat_list.append(pr.Category.id)
            # print(unq_cat_list)
    for ct in cat:
        if ct.id in unq_cat_list:
            catList.append(ct)
    data={
        'cat' : catList,
        'prd' : prd
    }
    return render(request, 'checkout.html',data)



def fetchproduct(request,ids):
    data={}
    unq_cat_list = []
    catList = []
    
    cat1 = category.objects.filter(id=ids)
    for n in cat1:
        catt = n.category
    cat = category.objects.all()
    prd = product.objects.all()
    prd1 = product.objects.filter(Category=catt)
    
    
    for pr in prd:
        if pr.Category.id not in unq_cat_list:
            unq_cat_list.append(pr.Category.id)
            # print(unq_cat_list)
    for ct in cat:
        if ct.id in unq_cat_list:
            catList.append(ct)
    data={
        'cat' : catList,
        'prd' : prd1
    }
    return render(request,'home.html',data)