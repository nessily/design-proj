

from django.shortcuts import render 
import pyrebase 

#connection from firebase to project  
config={ 
    "apiKey": "AIzaSyDCjOYgDFdk1wgbSZgajOJrjeVtaNDkvrQ", 
    "authDomain": "turtles-ee1ed.firebaseapp.com", 
    "databaseURL": "https://turtles-ee1ed-default-rtdb.firebaseio.com", 
    "projectId": "turtles-ee1ed", 
    "storageBucket": "turtles-ee1ed.appspot.com", 
    "messagingSenderId": "89823642890", 
    "appId": "1:89823642890:web:ad29a5798dc2b90e7d66f3",
    "measurementId": "G-K5JR3QVYWB"
} 
firebase=pyrebase.initialize_app(config) 
authe = firebase.auth() 
database=firebase.database() 

#Using data from firebase, return values to html file displayed on web page  
def home (request): 
    day = database.child('Data').child('day').get().val() 
    idn = database.child('Data').child('idn').get().val() 
    projectname = database.child('Data').child('projectname').get().val() 
    return render(request,"Home.html",{"day":day,"idn":idn,"projectname":projectname })
def login (request):
    username = database.child('User').child('username').get().val()
    password = database.child('User').child('password').get().val()
    return render(request,"Login.html",{"username":username,"password":password })