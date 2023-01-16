from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from Product.models import category,product,cart,subCategory,brand,currency
from django.template import loader
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

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

def prdDelete(request,prdId):
    rec = product.objects.get(id=prdId)
    rec.delete()
    return HttpResponseRedirect(reverse('adminHome'))

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

def adminHome(request):
    all_product=product.objects.all()
    data={
         'allProduct':all_product,
    }
    return render(request,'adminPanel/adminHome.html',data)

def adminBrand(request):
    allBrand = brand.objects.all()
    data={
        'allBrand': allBrand,
    }
    return render(request,'adminPanel/adminBrand.html',data)
def adminCategory(request):
    allcat = category.objects.all()
    data={
        'allcat': allcat,
    }
    return render(request,'adminPanel/adminCategory.html',data)
def adminSubCategory(request):
    allSubcat = subCategory.objects.all()
    data={
        'allSubCat': allSubcat,
    }
    return render(request,'adminPanel/adminSubCategory.html',data)

def adminCurrency(request):
    allCurrency = currency.objects.all()
    data={
        'allcat': allCurrency,
    }
    return render(request,'adminPanel/adminCurrency.html',data)

def addProdcut(request):
    try:
        if request.method == "POST":
            catogery = category.objects.get(id=request.POST.get("catDetails"))
            subCategorys =  subCategory.objects.get(id= request.POST.get("SubCatogery"))
            brands = brand.objects.get(id= request.POST.get("brand"))
            prdName = request.POST.get("prdDetails")
            currs = currency.objects.get(id=request.POST.get("Curren111"))
            curr = currs.currency
            purAmount = request.POST.get("purchaseAmount111")
            rates1 =request.POST.get("ratetake")
            costUSD =request.POST.get("costInUsd111")
            pnt =request.POST.get("PointMain")
            print(pnt)
            specific =request.POST.get("specification111")
            fills = request.FILES.get("file111")
            #fill = request.FILES['file111']
            # form = UploadFileForm(request.POST, request.FILES)
            print("Rohit")
            crr = product.objects.create(
                productImage=fills,
                Category = catogery,
                subCategory = subCategorys,
                Brand = brands,
                ProductName=prdName,
                purchaseCurrency=curr.lower(),
                usdConversionRate = rates1,
                costInUsd = costUSD,
                points = pnt,
                purchaseAmount = purAmount,
                specifications = specific,
            )
            print(crr)
    except:
        pass
    
    cat = category.objects.all()
    sub_cat = subCategory.objects.all()
    brnd = brand.objects.all()
    curr = currency.objects.all()
    data = {
        'Cat':cat,
        'Sub_Cat':sub_cat,
        'Brnd':brnd,
        'Cur':curr,
    }
    return render(request,'adminPanel/addProduct.html',data)

def addBrand(request):
    try:
        if request.method == 'POST':
            print('Rohir')
            brd = request.POST.get("brdd")
            print(brd)
            brr = brand.objects.create(
                Brand=brd,
            )
            print(brr)
            allBrand = brand.objects.all()
            data={
                'allBrand': allBrand,
                }
            return render(request,'adminPanel/adminBrand.html',data)

    
    except:
        pass
    
    return render(request,'adminPanel/addBrand.html')

def addCategory(request):
    try:
        if request.method == "POST":
            cat = request.POST.get("catt")
            crr = category.objects.create(
                category = cat,
            )
            print(crr)
            allCat = category.objects.all()
            data={
                'allcat':allCat,
            }
            return render(request,'adminPanel/adminCategory.html',data)
    except:
        pass
    
    return render(request,'adminPanel/addCategory.html')
 
def addSubCategory(request):
    try:
        if request.method == "POST":
            Subcat = request.POST.get("Subcatt")
            catogery = category.objects.get(id=request.POST.get("catDetails"))
            Subcrr = subCategory.objects.create(
                subCategory = Subcat,
                categoryL = catogery,
            )
            print(Subcrr)
            allSubcat = subCategory.objects.all()
            data={
                'allSubCat': allSubcat,
            }
            return render(request,'adminPanel/adminSubCategory.html',data)
    except:
        pass
    
    cat = category.objects.all()
    sub_cat = subCategory.objects.all()
    brnd = brand.objects.all()
    curr = currency.objects.all()
    data = {
        'Cat':cat,
        'Sub_Cat':sub_cat,
        'Brnd':brnd,
        'Cur':curr,
    }
    
    return render(request,'adminPanel/addSubCategory.html',data)
 
def addCurrency(request):
    try:
        if request.method == 'POST':
            curr = request.POST.get('currencyMain')
            addCrr = currency.objects.create(
                currency = curr,
            )
            print('addCrr')
            allCurrency = currency.objects.all()
            data={
                'allcat': allCurrency,
            }
            return render(request,'adminPanel/adminCurrency.html',data)
    except:
        pass
    
    return render(request,'adminPanel/addCurrency.html')  
    
def adminLogin(request):
    data={}
    if request.method == "POST":
        userN = request.POST.get('userName')
        pas= request.POST.get('password')
        print(userN)
        print(pas)
        check = authenticate(username=userN, password=pas)
        chh = User.objects.get(username=userN)
        all_product = product.objects.all()
        if chh.is_superuser:
            print("admin")
            if check != None:
                login(request, check)
                data={
                    'userName' : check.first_name,
                    'allProduct':all_product,
                }
                messages.success(request, "Login Secessfully")
                return redirect('adminHome')
            else:
                messages.error(request, "Wrong Details")
        else:
            messages.error(request,"Not a Admin User details")

    return render(request,'adminPanel/adminLogin.html')