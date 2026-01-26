from django.contrib import admin
from django.urls import path,include
from accounts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.RegesterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),



    path('profile/', views.profile_view, name='profile'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/', views.reset_password, name='reset_password'),
]