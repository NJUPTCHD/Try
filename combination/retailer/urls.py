from django.conf.urls import url

from retailer import views, view_helper
app_name = 'retailer'
urlpatterns = [
    url(r'^login/',views.login,name = 'login'),
    url(r'^register/',views.register,name = 'register'),
    url(r'^forget/',views.forget,name = 'forget'),

    url(r'^checkuser/',view_helper.check_user,name = 'check_user'),
    url(r'^checkphone/',view_helper.check_phone,name = 'check_phone'),


    url(r'^index/',views.index,name='index'),
    url(r'^capital/',views.capital,name='capital'),
    url(r'^order/',views.order,name='order'),
    url(r'^product/',views.product,name='product'),
    # url(r'^prodect/',views.change,name='change'),
    # url(r'^prodect/',views.search,name='change'),
    url(r'^prodect/',views.delete,name="delete"),
    url(r'^mine/',views.mine,name='mine'),
]