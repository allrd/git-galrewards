"""my URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.logins,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('logout/',views.logouts,name='logout'),
    path('home/<int:ids>/',views.fetchproduct,name='fetchproduct'),
    path('carts/',views.carts,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('addToCart/<int:prdId>',views.addToCart,name='addToCart'),
    path('deleteCartRec/<int:prddId>',views.deleteCartRec,name='deleteCartRec'),
    path('adminHome/',views.adminHome,name='adminHome'),
    path('adminBrand/',views.adminBrand,name="adminBrand"),
    path('adminCategory/',views.adminCategory,name="adminCategory"),
    path('adminSubCategory/',views.adminSubCategory,name="adminSubCategory"),
    path('adminCurrency/',views.adminCurrency,name="adminCurrency"),
    path('adminLogin/', views.adminLogin,name='adminLogin'),
    path('addProduct/',views.addProdcut,name='addProduct'),
    path('addBrand/',views.addBrand,name='addBrand'),
    path('addCategory/',views.addCategory,name='addCategory'),
    path('addSubCategory/',views.addSubCategory,name='addSubCategory'),
    path('addCurrency/',views.addCurrency,name='addCurrency'),
    path('prdDelete/<int:prdId>',views.prdDelete,name="prdDelete"),
    path('brdDelete/<int:brdId>',views.brdDelete,name="brdDelete"),
    path('catDelete/<int:catId>',views.catDelete,name="catDelete"),
    path('subDelete/<int:subId>',views.subDelete,name="subDelete"),
    path('curDelete/<int:curId>',views.curDelete,name="curDelete"),
    path('curEdit/<int:curId>',views.curEdit,name="curEdit"),
    path('prdEdit/<int:prdId>',views.prdEdit,name="prdEdit"),
    path('contact/',views.contact,name="contact"),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)