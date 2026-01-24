from django.contrib import admin
from django.urls import path,include
from billing import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', views.payment, name='payment'),
    path('invoice/', views.invoice, name='invoice'),
]