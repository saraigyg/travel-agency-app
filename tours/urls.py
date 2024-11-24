from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('tours/', views.tour_list, name='tour_list'),
    path('', views.index, name='home'),
    path('beach/', views.beach_destinations, name='beach_destinations'),
    path('city/', views.city_destinations, name='city_destinations'),
    path('adventure/', views.adventure_destinations, name='adventure_destinations'),
    path('family/', views.family_package, name='family_package'),
    path('couples/', views.couples_package, name='couples_package'),
    path('group/', views.group_package, name='group_package'),
    path('login/', TemplateView.as_view(template_name='user/login.html'), name='login'),
     # Display the booking form
    path('book/', views.book_now, name='book_now'),  
    # Handle form submission
    path('book/submit/', views.book_tour, name='book_tour_submit'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]


