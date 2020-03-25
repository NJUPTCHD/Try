from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.template import loader

from retailer.models import Users


def check_user( request ):
    username = request.GET.get("username")
    users = Users.objects.filter(user_name = username)
    data = {
        "status":200,     #状态码200代表用户名可用
        "msg":'username can be used'
    }
    if users.exists():
        data["status"] = 901    #状态码901代表用户名已经存在
        data["msg"] = 'username already exist'
    if len(username)>8:
        data["status"] = 902    #状态码902代表用户名长度不正确
        data["msg"] = 'username length wrong'
    return JsonResponse(data = data)

def check_phone( request ):
    phone = request.GET.get("phone")
    users = Users.objects.filter(user_phone = phone)
    data = {
        "status":200,     #状态码200代表号码可用
        "msg":'phone can be used'
    }
    if users.exists():
        data["status"] = 901    #状态码901代表号码已经存在
        data["msg"] = 'phone already exist'
    if len(phone)!=11:
        data["status"] = 902    #状态码902代表号码格式错误
        data["msg"] = 'phone format wrong'
    return JsonResponse(data = data)




def send_email(request):
    subject = 'Activate'
    message = '<h1>Hello</h1>'
    from_email = 'wodeyouxiang@163.com'
    recipient_list = [
        'wodeyouxiang@163.com',
    ]
    data = {
        'username':'xfy',
        'activate':'http://www.shangbang.com/active/?u_token=YYYY'
        # u_token缓存中作为key,value->username
    }
    html_message = loader.get_template('user/activate.html').render(data)

    send_mail(subject = subject,message = message,html_message = html_message,from_email = from_email,recipient_list = recipient_list)
    return  HttpResponse("发送成功！SUCCESS")