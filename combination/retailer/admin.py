from django.contrib import admin

# Register your models here.
from .models import Users,Retailers,ProductType,Products,sumAmount

admin.site.site_header = "后台管理系统"
admin.site.index_title = '后台系统'

class UserAdmin(admin.ModelAdmin):
    # 修改列表页属性
    list_display = ['pk','user_name','user_password','user_phone','is_certify','is_delete']
    # list_filter = [] #过滤字段
    search_fields = [] #搜索字段
    list_per_page = 5 #每页显示
    # 添加修改页属性
    fields = []#规定属性先后顺序
    fieldsets = []#给属性分组，不能同时使用

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['pk','pruduct_keeper','pruduct_name','product_image','pruduct_description','pruduct_type','pruduct_price','prodect_sales','prodect_date','prodect_isdelete','prodect_discount']
    fields = []
    list_per_page = 5

class sumAmountAdmin(admin.ModelAdmin):
    list_display = ['sdate','samount']
    fields = []
    list_per_page = 7
admin.site.register(Users,UserAdmin)
admin.site.register(Retailers)
admin.site.register(ProductType)
admin.site.register(Products,ProductsAdmin)
admin.site.register(sumAmount,sumAmountAdmin)



