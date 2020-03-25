from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from retailer.models import Users, Products,sumAmount
from django.utils import timezone
import datetime
import random
import string


def login( request ):
    data={
        "title":"登录",
    }
    if request.method == "GET":
        return render(request,"login.html",context = data)
    elif request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')
        users = Users.objects.filter(user_name=name)
        if users.exists():
            user = users.first()# 获取用户名相同的model的信息
            if check_password(password,user.user_password):# 哈希解密验证密码
                request.session['user_id'] = user.id  # 在session里边存储了当前登录用户的唯一标识id  其实这段的session我还没搞透彻  今晚再搞
                return redirect(reverse('retailer:mine'))
    #登陆失败的提示我还没做  目前是点击登录不跳转的retailer:mine即为登陆失败
    return  redirect(reverse('retailer:login'))


def register( request ):
    data = {
        "title":"注册",
    }
    if request.method == "GET":
        return render(request,'register.html',context = data)
    elif request.method == "POST":

        name = request.POST.get('username')
        password=request.POST.get('pwd1')
        phone= request.POST.get('phone')

        user = Users()
        user.user_password=make_password(password)
        user.user_name=name
        user.user_phone=phone
        user.save()
        data={
            "title":"登录",
        }
        # 这里我没做注册成功后的跳转页面   目前是注册成功直接跳转到登录界面了
        return render(request,"login.html",context = data)
    # return render(request,'register.html',context = data)


def forget( request ):
    return HttpResponse("你已进入\"忘记密码\"界面")


def index( request ):
    # data = {
    #     "title":"首页",
    #     # "status":"登录状态",
    # }
    # return render(request,"index.html",context = data)
    prodectList = Products.objects.all()
    pruduct_name = list(Products.objects.values_list("pruduct_name",flat=True))
    # Pname = list(Products.objects.filter().values_list())
    prodect_sales = list(Products.objects.values_list("prodect_sales",flat=True))

    amountList = sumAmount.objects
    Amount = list(amountList.values_list('samount', flat=True))
    Dates = list(amountList.values_list('sdate', flat=True))
    Dates7 = [Dates[-7], Dates[-6], Dates[-5], Dates[-4], Dates[-3], Dates[-2], Dates[-1]]
    Amount7 = [Amount[-7], Amount[-6], Amount[-5], Amount[-4], Amount[-3], Amount[-2], Amount[-1]]
    datestr_list = []
    for date in Dates7:
        this_date = datetime.date.strftime(date, '%m-%d')
        datestr_list.append(this_date)
    return render(request, 'index.html',{"title":"首页", "prodects": prodectList, "pname": pruduct_name, "psales": prodect_sales,"dates":datestr_list,"amount":Amount7,})



def capital( request ):
    data = {
        "title":"资金管理",
    }
    return render(request,"capital.html")


def order( request ):
    data = {
        "title":"订单详情",
    }
    return render(request,"order.html")


def product( request ):
    data = {
        "title":"产品中心",
    }
    if request.method == "GET":
        return render(request,"product.html")
    if request.method == "POST":
        productname = request.POST.get('productname')
        producttype = request.POST.get('producttype')
        productprice = request.POST.get('productprice')
        productdescription = request.POST.get('productdescription')
        productimage=request.FILES.get('productimage')
        # print(productname + '-----' +producttype + '-----'+productdescription)
        productprice = float(productprice)
        product = Products()
        #product.pruduct_keeper = '获取到当前登录账户的用户名'
        #当我给product模型添加字段后，通过表单插入上架商品的数据的字段不能为空，暂且默认为常数值，以方便实现功能
        product.pruduct_name = productname
        product.product_image = productimage
        product.product_description = productdescription
        product.pruduct_price = productprice
        product.prodect_sales = 0 #新上架商品销量为0
        product.prodect_date = timezone.now() #获取上架时间
        product.prodect_isdelete = 0 #下架为布尔值为0
        product.prodect_discount =0 #默认不打折
        #生成字符串，暂时性解决主键问题
        seed = "abcdefghijklmnopqrstuvwxyz"
        sa = []
        for i in range(8):
            sa.append(random.choice(seed))
            product.pruduct_keeper = ''.join(sa)
            product.save()
            return HttpResponse("上传成功！SUCCESS!!!")


def delete(request):
    if request.method == "GET":
        return render(request,"product.html")
    if request.method == "POST":
        productdelete = request.POST.get("delete")
        deletename = Products.objects.get(pruduct_name=productdelete)
        print(deletename.pruduct_price)
        deletename.prodect_isdelete = 1
        deletename.save()
        return HttpResponse("下架成功！SUCCESS!!!")

# def search(request):
#     if request.method == "GET":
#         return render(request,"product.html")
#     if request.method == "POST":
#         search = request.POST.get("result")
#         result = Products.objects.get(pruduct_name=search)
#         print(result.pruduct_name)
#         resultId = result.id
#         resultName = result.pruduct_name
#         resultImg = result.product_image
#         resultDiscription = result.pruduct_description
#         resultPrice = result.pruduct_price
#         nowName = result.pruduct_name
#         nowPrice = result.pruduct_price
#         # newName = request.POST.get("newname")
#         # newPrice = request.POST.get("newprice")
#         # result.pruduct_name = newName
#         # result.pruduct_price = newPrice
#         # result.save()
#         return render(request,'product.html',{'resultId':resultId,'resultName':resultName,'resultImg':resultImg,'resultDiscription':resultDiscription,'resultPrice':resultPrice,'newName':nowName,'newPrice':nowPrice,})

# def change(request):
#     if request.method == "GET":
#         return render(request,"product.html")
#     if request.method == "POST":
#         search = request.POST.get("result")
#         result = Products.objects.get(pruduct_name=search)
#         nowName = result.pruduct_name
#         nowPrice = result.pruduct_price
#         newName = request.POST.get("newname")
#         newPrice = request.POST.get("newprice")
#         result.pruduct_name = newName
#         result.pruduct_price = newPrice
#         result.save()
#         return HttpResponse("修改成功")
#

def mine( request ):

    data = {
        "title":"个人账户",
    }

    return render(request,"mine.html")
