from django.shortcuts import render





def payment(request):
    return render(request,'billing/payment.html')
def invoice(request):
    return render(request,'billing/invoice.html')