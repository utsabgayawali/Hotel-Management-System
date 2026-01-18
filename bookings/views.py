from django.shortcuts import render

# Create your views here.



def room_list(request):
    return render(request,'bookings/room_list.html')

def booking_form(request):
    return render(request,'bookings/booking_form.html')

def booking_detail(request):
    return render(request,'bookings/booking_detail.html')