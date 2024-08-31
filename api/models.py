from django.db import models

from db_connect import db

users_collection = db['users']
flight_collection = db['flights']
booking_collection = db['bookings']

