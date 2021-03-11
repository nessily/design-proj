

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
auth = firebase.auth() 
database=firebase.database() 

#Using data from firebase, return values to html file displayed on web page  
def home (request): 
    day = database.child('Data').child('day').get().val() 
    idn = database.child('Data').child('idn').get().val() 
    projectname = database.child('Data').child('projectname').get().val()

    email = request.POST.get('email')
    password = request.POST.get('password')
    user = auth.sign_in_with_email_and_password(email,password)

    return render(request,"Home.html",{"day":day,"idn":idn,"projectname":projectname })
def login (request):
    return render(request,"Login.html")
def pH (request):
    day1 = database.child('ph/1').child('day').get().val()
    value1 = database.child('ph/1').child('value').get().val()
    day2 = database.child('ph/2').child('day').get().val()
    value2 = database.child('ph/2').child('value').get().val()
    day3 = database.child('ph/3').child('day').get().val()
    value3 = database.child('ph/3').child('value').get().val()
    day4 = database.child('ph/4').child('day').get().val()
    value4 = database.child('ph/4').child('value').get().val()
    day5 = database.child('ph/5').child('day').get().val()
    value5 = database.child('ph/5').child('value').get().val()
    day6 = database.child('ph/6').child('day').get().val()
    value6 = database.child('ph/6').child('value').get().val()
    day7 = database.child('ph/7').child('day').get().val()
    value7 = database.child('ph/7').child('value').get().val()
    return render(request,"pHchart.html",{"day1":day1,"value1":value1,"day2":day2,
    "value2":value2,"day3":day3,"value3":value3,"day4":day4,"value4":value4,
    "day5":day5,"value5":value5,"day6":day6,"value6":value6,"day7":day7,"value7":value7})

