from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing),
    path("login/", views.login),
    path("register/", views.register),

    path("load-bookflight/<str:flightId>", views.loadBookflight),
    path("bookflight/<str:flightId>/<str:userId>", views.bookflight),
    
    path("load-bookings/", views.loadBookings),
    path("bookings/<str:id>", views.bookings),

    path("cancel-user-booking/<str:id>", views.cancelUserTicket),
    path("cancel-booking/<str:id>", views.cancelTicket),

    path("admin/", views.admin),
    path("allBookings/", views.allBookings),
    path("allUsers/", views.allUsers),
    path("allflights/", views.allflights),
    path("newflight/", views.newflight),
    path("editflight/<str:id>", views.editflight),

]
