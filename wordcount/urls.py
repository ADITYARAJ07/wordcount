
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('aditya/', admin.site.urls),
	path('',views.home),
	path('adi/',views.aditya),
	path('count/',views.count,name='goto'),
	path('result/',views.result,name='count'),
]
