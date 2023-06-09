from django.shortcuts import render, redirect, get_object_or_404
from .forms import Bookingform
from .models import Booking
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')  
    """The view for the start page. Renders the index.html
    page which also extends the base.html
    """

def booking_page(request):
    """
    The booking page view handles rendering based on user authentication status. 
    If the user is logged in, it renders the booking.html page; otherwise, 
    it directs the user to the login or signup page. After the user makes a booking, 
    they are redirected to the mybooking overview page. 
    The view captures input from the form and stores it in the Booking model.
    """
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
    """The view that renders the mybookings.html which shows all
    current booking by the user. Checks if user is logged in
    otherwise it redirects to the signup page.
    """
    if request.user.is_authenticated: 
        bookings = Booking.objects.filter(user=request.user)
        context = {
            "bookings" : bookings
        }
        return render(request, "mybookings.html", context)
    else:
        return render("../accounts/login")

def edit_booking(request, booking_id):
    """
    The edit_booking view renders the edit_booking page, 
    allowing the user to update an existing booking. 
    It verifies if the current user matches the user who made the booking; 
    otherwise, it redirects them to the mybookings_page. 
    The view uses the form data provided by the user to update the corresponding booking in the database.
    """
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
    """The view that performs the deletion of a booking.
    Checks if current user matches the user that made the booking,
    otherwise it redirects to the mybookings_page.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user != booking.user:
        return redirect('mybookings_page')
    booking.delete()
    messages.success(request, "booking deleted")
    return redirect('mybookings_page')


