from django.contrib import admin
from django.urls import path,include
from bookings import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('room_list/', views.room_list, name='room_list'),
    path('booking_form/', views.booking_form, name='booking_form'),
    path('booking_detail/', views.booking_detail, name='booking_detail'),
    
]