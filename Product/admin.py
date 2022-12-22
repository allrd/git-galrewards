from django.contrib import admin
from Product.models import category,subCategory,brand,product

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


# Register your models here.
