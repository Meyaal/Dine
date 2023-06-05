from django.shortcuts import render, redirect, get_object_or_404
from .forms import Bookingform
from .models import Booking
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def booking_page(request):
    if request.method == 'POST':
        form = Bookingform(data=request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            messages.success(request, "booking confirmed")
            return redirect('mybookings_page')
        else: 
            messages.error(request, "information missed or invalid or dubble booking")
    form = Bookingform()
    context = {
        "form" : form
    }
    return render(request, "booking.html", context)
            

def mybookings_page(request):
    if request.user.is_authenticated: 
        bookings = Booking.objects.filter(user=request.user)
        context = {
            "bookings" : bookings
        }
        return render(request, "mybookings.html", context)
    else:
        return render("../accounts/login")

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user != booking.user:
        return redirect('mybookings_page')
    if request.method == 'POST':
        form = Bookingform(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "booking uppdated")
            return redirect('mybookings_page')
    form = Bookingform(instance=booking)
    context = {
        "form" : form
    }
    return render(request, 'edit_booking.html', context)

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user != booking.user:
        return redirect('mybookings_page')
    booking.delete()
    messages.success(request, "booking deleted")
    return redirect('mybookings_page')


