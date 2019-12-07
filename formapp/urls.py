from django.conf.urls import url
from . import views
app_name='formapp'
urlpatterns=[
    url(r'^$',views.insert, name='insert'),
]