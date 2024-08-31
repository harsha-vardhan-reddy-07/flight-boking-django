from django.shortcuts import render
from .models import users_collection, flight_collection, booking_collection
from .forms import LoginForm, RegisterForm, flightSearchForm, NewflightForm, BookflightForm
import bson

def landing(request):
    error = ""
    flights = []
    flightSearch = False
    flightLen = 0
    if request.method == 'POST':
        form = flightSearchForm(request.POST)
        if form.is_valid():
            originCity = form.cleaned_data['originCity']
            destinationCity = form.cleaned_data['destinationCity']
            journeyDate = form.cleaned_data['journeyDate']

            flights = [t for t in flight_collection.find({"originCity": originCity, "destinationCity": destinationCity})]
            for t in flights:
                t['id'] = str(t['_id'])
            flightLen = len(flights)
            flightSearch = True
            
        else:
            form = flightSearchForm()
            error = 'Invalid form data. Please try again.'
    else:
        form = flightSearchForm()
    return render(request, 'landing.html', {"form": form, "flights": flights, "flightLen": flightLen, "flightSearch": flightSearch, "error": error})

def login(request):
    error=''
    data = {}
    isLogged = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                data = users_collection.find_one({'email': email})
                if data.get('password') == password:
                    data['userId'] = str(data['_id'])
                    isLogged = True
                
                else:
                    form = LoginForm()
                    error = 'Wrong credientials. Please try again.'
                    
            except:
                form = LoginForm()
                error = 'User not found!! Please try again.'
        else:
            form = LoginForm()
            error = 'Wrong credientials. Please try again.'
    else:
        form = LoginForm()
    
    context = {'form': form, 'isLogged': isLogged, 'data': data, 'error': error}
    return render(request, 'login.html', context)



def register(request):
    error=''
    data = {}
    isLogged = False
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            usertype = form.cleaned_data['usertype']

            user = {"username": username, "email": email, "password": password, "usertype": usertype}
            result = users_collection.insert_one(user)
            isLogged = True
            data = {
            'userId': str(result.inserted_id),
            'username': username,
            'email': email,
            'password': password,
            'usertype': usertype
            }
            
        else:
            form = RegisterForm()
            error = 'Invalid form data. Please try again.'
    else:
        form = RegisterForm()
    
    context = {'form': form, 'isLogged': isLogged, 'data': data, 'error': error}
    return render(request, 'register.html', context)



def loadBookflight(request, flightId):
    return render(request, 'user/loadBookflight.html', {"flightId": flightId})

def bookflight(request, flightId, userId):
    success = False
    error = ''
    print(userId)
    flight = flight_collection.find_one({"_id": bson.ObjectId(flightId)})
    if request.method == 'POST':
        form = BookflightForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            passengersCount = form.cleaned_data['passengersCount']
            journeyDate = str(form.cleaned_data['journeyDate'])
            seatType = form.cleaned_data['seatType']

            seatPrices = {
                'First class': 4,
                'Business Class': 3,
                'Premium Economy': 2,
                'Economy': 1
            }

            totalPrice = 0

            flight = flightId,

            flightData = flight_collection.find_one({"_id": bson.ObjectId(flightId)})
            
            totalPrice = int(seatPrices[seatType]) * int(passengersCount) * flightData['basePrice']


            flightName = flightData['flightName']
            flightNumber = flightData['flightNumber']
            StartCity = flightData['originCity']
            destinationCity = flightData['destinationCity']
            bookingStatus = "confirmed"

            booking = {"email": email, "mobile": mobile, "passengersCount": passengersCount, "journeyDate": journeyDate, "seatType": seatType,
                       "totalPrice": totalPrice, "userId": userId, "flightName":flightName, "flightNumber": flightNumber, "StartCity": StartCity,
                       "destinationCity": destinationCity, "bookingStatus": bookingStatus}
            result = booking_collection.insert_one(booking)
            success = True
            
        else:
            form = BookflightForm()
            error = 'Invalid form data. Please try again.'
    else:
        form = BookflightForm()
    return render(request, 'user/bookflight.html', {"flight": flight, "form": form, "success": success, "error": error})

def loadBookings(request):
    return render(request, 'user/loadBookings.html')

def bookings(request, id):
    bookings = [b for b in booking_collection.find({"userId": id})]
    print(bookings)
    for b in bookings:
        b['id'] = str(b['_id'])
    return render(request, 'user/bookings.html', {"bookings":bookings})

def cancelUserTicket(request, id):
    success = False
    booking = booking_collection.update_one({"_id": bson.ObjectId(id)}, {"$set": {"bookingStatus": "Cancelled"}})
    success = True
    return render(request, 'user/cancel-booking.html', {"success":success})


def cancelTicket(request, id):
    success = False
    booking_collection.update_one({"_id": bson.ObjectId(id)}, {"$set": {"bookingStatus": "Cancelled"}})
    success = True
    return render(request, 'admin/cancel-booking.html', {"success":success})

def admin(request):

    users = [u for u in users_collection.find()]
    usersCount = len(users)

    flights = [t for t in flight_collection.find()]
    flightsCount = len(flights)

    bookings = [b for b in booking_collection.find()]
    bookingsCount = len(bookings)

    return render(request, 'admin/admin.html', {"usersCount": usersCount, "flightsCount": flightsCount, "bookingsCount":bookingsCount})


def allBookings(request):
    bookings = [b for b in booking_collection.find()]
    for b in bookings:
        b['id'] = str(b['_id'])
    return render(request, 'admin/allBookings.html', {"bookings":bookings})

def allUsers(request):
    users = [u for u in users_collection.find()]
    for u in users:
        u['id'] = str(u['_id'])
    return render(request, 'admin/allUsers.html', {"users": users})

def allflights(request):
    flights = [t for t in flight_collection.find()]
    for t in flights:
        t['id'] = str(t['_id'])
    return render(request, 'admin/allflights.html', {"flights": flights})

def newflight(request):
    success = False
    if request.method == 'POST':
        form = NewflightForm(request.POST)
        if form.is_valid():
            flightNumber = form.cleaned_data['flightNumber']
            flightName = form.cleaned_data['flightName']
            originCity = form.cleaned_data['originCity']
            destinationCity = form.cleaned_data['destinationCity']
            totalSeats = form.cleaned_data['totalSeats']
            basePrice = form.cleaned_data['basePrice']
            departureTime = str(form.cleaned_data['departureTime'])
            arrivalTime = str(form.cleaned_data['arrivalTime'])

            flight = {"flightNumber": flightNumber, "flightName": flightName, "originCity": originCity, "destinationCity": destinationCity, 
                    "totalSeats": totalSeats, "basePrice": basePrice, "departureTime": departureTime, "arrivalTime": arrivalTime}
            result = flight_collection.insert_one(flight)
   
            success = True
            
        else:
            form = NewflightForm()
            error = 'Invalid form data. Please try again.'
    else:
        form = NewflightForm()
    return render(request, 'admin/newflight.html', {"form":form, "success": success})

def editflight(request, id):
    success = False
    error = ''
    flight = flight_collection.find_one({"_id": bson.ObjectId(id)})
    if request.method == 'POST':
        form = NewflightForm(request.POST)
        if form.is_valid():
            object_id = bson.ObjectId(id)

            flightNumber = form.cleaned_data['flightNumber']
            flightName = form.cleaned_data['flightName']
            originCity = form.cleaned_data['originCity']
            destinationCity = form.cleaned_data['destinationCity']
            totalSeats = form.cleaned_data['totalSeats']
            basePrice = form.cleaned_data['basePrice']
            departureTime = str(form.cleaned_data['departureTime'])
            arrivalTime = str(form.cleaned_data['arrivalTime'])

            flight_collection.update_one({"_id": object_id}, {"$set": {"flightNumber": flightNumber, "flightName": flightName, "originCity": originCity, "destinationCity": destinationCity, 
                    "totalSeats": totalSeats, "basePrice": basePrice, "departureTime": departureTime, "arrivalTime": arrivalTime}})
            success = True
  
            
        else:
            form = NewflightForm()
            print("erroruu")
            success = False
            error = 'Invalid form data. Please try again.'
    else:
        object_id = bson.ObjectId(id)
        flight = flight_collection.find_one({'_id': object_id})
        if flight is None:
            error = "Error in fetching flight!!"
            form = NewflightForm()
        else:
            form = NewflightForm(initial={
                            "flightNumber": flight['flightNumber'], 
                            "flightName": flight['flightName'], 
                            "originCity": flight['originCity'], 
                            "destinationCity": flight['destinationCity'], 
                            "totalSeats": flight['totalSeats'],
                            "basePrice": flight['basePrice'], 
                            "departureTime": flight['departureTime'], 
                            "arrivalTime": flight['arrivalTime']
                        })
    
    context = {'form': form, 'success': success, 'error': error}
    return render(request, 'admin/editflight.html', context)