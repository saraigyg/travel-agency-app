
from django.shortcuts import get_object_or_404, render, redirect
from .models import Booking, Tour
from django.http import HttpResponse
from datetime import datetime


def book_tour(request):
    if request.method == 'POST':
        try:
            # Fetch data from POST request
            tour_id = request.POST['tour'] 
            first_name = request.POST['firstName'] 
            last_name = request.POST['lastName']  
            email = request.POST['email'].strip().lower()  
            phone = request.POST['phone']  
            num_people = int(request.POST['num_people']) 
            start_date = request.POST['startDate']  
            end_date = request.POST['endDate']  
            special_requests = request.POST['specialRequests']  

            # Parse start and end dates
            start_date_str = request.POST['startDate']
            end_date_str = request.POST['endDate']

            # Convert the strings to date objects
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()  # convert to date format
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()  # convert to date format

            # Fetch the selected tour
            selected_tour = Tour.objects.get(pk=tour_id)

            # Calculate the total cost
            total_cost = num_people * selected_tour.price

            # Save the booking
            booking = Booking.objects.create(
                customer_name=f"{first_name} {last_name}",
                email=email,
                phone=phone,
                tour=selected_tour,
                date=start_date,
                num_people=num_people,
                total_cost=total_cost,
                special_requests=special_requests 
            )

            # Redirect to the confirmation page, passing the booking details
            return redirect('booking_confirmation', booking_id=booking.id)

        except KeyError as e:
            return HttpResponse(f"Missing key in POST data: {e}", status=400)
        except Tour.DoesNotExist:
            return HttpResponse("Selected tour does not exist.", status=404)
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}", status=500)

    # If GET, render the booking form
    tours = Tour.objects.all()
    return render(request, 'tours/booking.html', {'tours': tours})

def booking_confirmation(request, booking_id):
    # Get the booking details using the booking_id
    booking = get_object_or_404(Booking, pk=booking_id)
    
    # Pass the booking details to the template
    return render(request, 'tours/confirmation.html', {'booking': booking})


def tour_list(request):
    return render(request, 'tours/tour_list.html')

def index(request):
    return render(request, 'tours/index.html')

def beach_destinations(request):
    return render(request, 'tours/beach.html')

def city_destinations(request):
    return render(request, 'tours/city.html')

def adventure_destinations(request):
    return render(request, 'tours/adventure.html')

# This view just renders the booking form page
def book_now(request):
    tours = Tour.objects.all()  # Fetch all tours from the database
    return render(request, 'tours/booking.html', {'tours': tours})

def family_package(request):
    return render(request, 'tours/family.html')

def couples_package(request):
    return render(request, 'tours/couples.html')

def group_package(request):
    return render(request, 'tours/group.html')

