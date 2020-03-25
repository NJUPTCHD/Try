from django.db import models

class Users(models.Model):
    user_name = models.CharField(max_length=16,unique = True)
    user_password = models.CharField(max_length = 256)
    user_phone = models.CharField(max_length = 15, unique = True)
    is_certify = models.BooleanField(default = False)
    is_delete = models.BooleanField(default = False)

    class Meta:
        db_table = 'users'

class Retailers(models.Model):
    retailer_user_name = models.CharField(max_length=16,unique = True)
    retailer_user_phone = models.CharField(max_length = 15, unique = True)

    retailer_name = models.CharField(max_length = 16,unique = True)
    retailer_address = models.CharField(max_length = 32,unique = True)
    retailer_keeper = models.CharField(max_length = 8)
    retailer_capital = models.FloatField()

    class Meta:
        db_table = 'retailer'


class ProductType(models.Model):
    pruduct_type_keeper = models.CharField(max_length=16,unique = True)

    pruduct_type_no = models.IntegerField()
    pruduct_type_name = models.CharField(max_length=16,unique = True)
    class Meta:
        db_table = 'productType'

class Products(models.Model):
    pruduct_keeper = models.CharField(max_length=16,unique = True)


    pruduct_name = models.CharField(max_length = 32)
    product_image = models.ImageField(upload_to='image/productimage')
    pruduct_description = models.CharField(max_length = 50)
    pruduct_type= models.IntegerField(default = 0)
    pruduct_price = models.FloatField()

    prodect_sales = models.IntegerField()
    prodect_date = models.DateField()
    prodect_isdelete = models.BooleanField()
    prodect_discount = models.FloatField()
    class Meta:
        db_table = 'products'

class sumAmount(models.Model):
    sdate = models.DateField()
    samount = models.FloatField()
    class Meta:
        db_table = "sumAmount"