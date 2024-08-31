from django import forms

USER_TYPE=[
        ('admin', 'admin'),
        ('user', 'user'),
    ]

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})) 
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})) 
    usertype = forms.ChoiceField(choices=USER_TYPE, widget=forms.Select(attrs={'class': 'form-select form-select-lg mb-3', 'placeholder': 'Choose user type'}))

class LoginForm(forms.Form): 
    email = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email'})) 
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

Cities = [
    ('Chennai', 'Chennai'),
    ('Bangalore', 'Bangalore'),
    ('Hyderabad', 'Hyderabad'),
    ('Mumbai', 'Mumbai'),
    ('Indore', 'Indore'),
    ('Delhi', 'Delhi'),
    ('Pune', 'Pune'),
    ('Trivendrum', 'Trivendrum'),
    ('Bhopal', 'Bhopal'),
    ('Kolkata', 'Kolkata'),
    ('varanasi', 'varanasi'),
    ('Jaipur', 'Jaipur'),
]


class flightSearchForm(forms.Form):
    originCity = forms.ChoiceField(choices=Cities, widget=forms.Select(attrs={'class': 'form-select form-select-lg mb-3', 'placeholder': 'Choose user type'}))
    destinationCity = forms.ChoiceField(choices=Cities, widget=forms.Select(attrs={'class': 'form-select form-select-lg mb-3', 'placeholder': 'Choose user type'}))
    journeyDate = forms.DateField( widget=forms.DateInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'type':"date"}))


class NewflightForm(forms.Form):
    flightNumber = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    flightName = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    originCity = forms.ChoiceField(choices=Cities, widget=forms.Select(attrs={'class': 'form-select form-select-lg', 'placeholder': 'Choose user type'}))
    destinationCity = forms.ChoiceField(choices=Cities, widget=forms.Select(attrs={'class': 'form-select form-select-lg', 'placeholder': 'Choose user type'}))
    totalSeats = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    basePrice = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    departureTime = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'time'}))
    arrivalTime = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'time'}))

seats = [
    ('Economy', 'Economy'),
    ('Premium Economy', 'Premium Economy'),
    ('Business Class', 'Business Class'),
    ('First class', 'First class'),
]

class BookflightForm(forms.Form):
    email = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})) 
    mobile = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})) 
    passengersCount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    journeyDate = forms.DateField( widget=forms.DateInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'type':"date"}))
    seatType = forms.ChoiceField(choices=seats, widget=forms.Select(attrs={'class': 'form-select form-select-lg mb-3', 'placeholder': 'Choose user type'}))


