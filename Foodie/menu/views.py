from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'index.html')

def booking_page(request):
    if request.method == 'POST':
        return redirect("mybookings_page")
    return render(request, 'booking.html')

def mybookings_page(request):
    return render(request, 'mybookings.html')

def edit_booking(request):
    return render(request, 'edit_booking.html')

def delete_booking(request):
    return redirect('mybookings_page')