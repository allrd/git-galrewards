from django.contrib import admin
from Product.models import category,subCategory,brand,product,cart

class categoryAdmin(admin.ModelAdmin):
    list_display =('id','category','status','country')
admin.site.register(category,categoryAdmin)

class subCatogeryAdmin(admin.ModelAdmin):
    list_display=('id','subCategory','categoryL_id','categoryL')
admin.site.register(subCategory,subCatogeryAdmin)

class brandAdmin(admin.ModelAdmin):
    list_display=('id','Brand')
admin.site.register(brand,brandAdmin)

class productAdmin(admin.ModelAdmin):
    list_display=('id','Category_id','subCategory_id','Brand_id','ProductName','productImage')
admin.site.register(product,productAdmin)

class cartAdmin(admin.ModelAdmin):
    list_display=('id','Product_id','user_id')
admin.site.register(cart,cartAdmin)

# Register your models here.
