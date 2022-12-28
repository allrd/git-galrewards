from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from Product.models import category,product,cart
from django.template import loader
from django.urls import reverse

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
        data={}
        unq_cat_list = []
        catList = []
        if request.method == "POST":
            str = request.POST.get("serach")
            prd = product.objects.filter(ProductName__contains=str)
            print(prd)   
        else:
            prd = product.objects.all()
        
        cat = category.objects.all()
        prd1 = product.objects.all()
        for pr in prd1:
            if pr.Category.id not in unq_cat_list:
                unq_cat_list.append(pr.Category.id)
                    # print(unq_cat_list)
        for ct in cat:
            if ct.id in unq_cat_list:
                catList.append(ct)
        
        user_id = request.user.id        
        all_cart_rec = cart.objects.filter(user_id=user_id)
        count = 0
        for nn in all_cart_rec:
            count += 1
        data={
            'cat' : catList,
            'prd' : prd,
            'cnt': count
        }
        print(prd)
        return render(request,'home.html',data)
    except:
        pass    
        
def logouts(request):
    logout(request)
    messages.success(request,'Logged out Sucessfully')
    return redirect('/')

def carts(request):
    try:
        if request.method == "POST":
            ids = request.POST.get('action')
            idCheck = ids[0:3]
            print(idCheck)
            if idCheck == "pls":
                idss = ids.lstrip(idCheck)
                cart_rec = cart.objects.get(id=idss)
                cart_rec.qty += 1
                cart_rec.save()
            elif idCheck == "neg":
                idss = ids.lstrip(idCheck)
                cart_rec = cart.objects.get(id=idss)
                cart_rec.qty -= 1
                cart_rec.save()
    
    except:
        pass    
    data={}
    unq_cat_list = []
    catList = []
    cat = category.objects.all()
    prd = product.objects.all()
    user_id = request.user.id
    user_rec = User.objects.get(id=user_id)
    mycart = cart.objects.filter(user_id=user_rec)
    for pr in prd:
        if pr.Category.id not in unq_cat_list:
            unq_cat_list.append(pr.Category.id)
            # print(unq_cat_list)
    for ct in cat:
        if ct.id in unq_cat_list:
            catList.append(ct)
            
    count = mycart.count()
    subtotal = 0
    for n in mycart:
        subtotal += n.Product_id.points
    
    total = 0
    for tot in mycart:
        total += (tot.Product_id.points)*tot.qty
    
    data={
        'cat' : catList,
        'prd' : prd,
        'myCart':mycart,
        'cnt': count,
        'total': total,
    }
    return render(request, 'cart.html',data)

def checkout(request):
    try:
        if request.method == "POST":
            pass
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

def addToCart(request,prdId):
    prd_details = product.objects.get(id=prdId)
    prd_name = prd_details.ProductName
    #print(prd_name)
    username = None
    username = request.user.id
    user_rec = User.objects.get(id=username)
    
    insert_rec = cart(Product_id=prd_details,user_id=user_rec,qty=1)
    insert_rec.save()
    
    all_cart_rec = cart.objects.filter(user_id=user_rec)
    count = 0
    for n in all_cart_rec:
        count += 1
    produc = product.objects.all()
    
    
    
    data={
        'myCart': all_cart_rec,
        'prd': produc,
        'cnt': count,
    }
    return HttpResponseRedirect(reverse('home'),data)
   
def deleteCartRec(request,prddId):
    rec = cart.objects.get(id=prddId)
    # print(rec)
    rec.delete()
    print(rec)
    
    return HttpResponseRedirect(reverse('cart'))

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
    username = request.user.id
    user_rec = User.objects.get(id=username)
    all_cart_rec = cart.objects.filter(user_id=user_rec)
    count = all_cart_rec.count()
    
    for pr in prd:
        if pr.Category.id not in unq_cat_list:
            unq_cat_list.append(pr.Category.id)
            # print(unq_cat_list)
    for ct in cat:
        if ct.id in unq_cat_list:
            catList.append(ct)
    data={
        'cat' : catList,
        'prd' : prd1,
        'cnt': count
    }
    return render(request,'home.html',data)