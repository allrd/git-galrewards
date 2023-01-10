from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

COUNTRY_CHOOSE = (
    ('ghana','GHANA'),
    ('uae', 'UAE'),
    ('ivory cost','IVORY COST'),
    ('senegal','SENEGAL'),
    ('turkey','TURKEY'),
)

CURRNECY_CHOOSE =(('ghs','GHS'),('usd','USD'))

class category(models.Model):
    category = models.CharField(max_length=30, unique=True)
    status = models.BooleanField(default=True)
    country = models.CharField(max_length=15,choices=COUNTRY_CHOOSE,default='ghana')
    def __str__(self):
        return self.category
    
class subCategory(models.Model):
    subCategory = models.CharField(max_length=30, unique=True)
    categoryL = models.ForeignKey('category', on_delete=models.CASCADE, to_field='category')
    def __str__(self):
        return self.subCategory
    
class brand(models.Model):
    Brand = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.Brand

    
class product(models.Model):
    Category= models.ForeignKey('category', on_delete=models.CASCADE,to_field='category')
    subCategory=models.ForeignKey('subCategory', on_delete=models.CASCADE,to_field='subCategory')
    Brand = models.ForeignKey('brand',on_delete=models.CASCADE,to_field='Brand')
    ProductName = models.CharField(max_length=50, unique=True)
    purchaseCurrency = models.CharField(max_length=3,choices=CURRNECY_CHOOSE, default='ghs')
    purchaseAmount = models.CharField(max_length=25)
    usdConversionRate= models.DecimalField(max_digits=10,decimal_places=2)
    costInUsd = models.IntegerField()
    perPointCost=models.DecimalField(max_digits=5,decimal_places=4,default=0.018)
    points=models.IntegerField()
    specifications= HTMLField()
    status = models.BooleanField(default=True)
    productImage = models.ImageField(upload_to="product/",max_length=250,null=True,default=None)
    def __str__(self):
        return self.ProductName
    
class cart(models.Model):
    Product_id = models.ForeignKey('product',on_delete=models.CASCADE, to_field='ProductName')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    qty = models.IntegerField()

class currency(models.Model):
    currency = models.CharField( max_length=3, unique=True)

# Create your models here.
