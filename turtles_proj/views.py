

from django.shortcuts import render 
from django.http import JsonResponse
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
    try:
        user = auth.sign_in_with_email_and_password(email,password)
    except:
        errorMessage = "Email/Password is incorrect"
        return render(request,"Login.html",{"errorMessage":errorMessage})


    return render(request,"Home.html",{"day":day,"idn":idn,"projectname":projectname })
#go back to home page without pass/email error
def home_loggedin(request):
    day = database.child('Data').child('day').get().val() 
    idn = database.child('Data').child('idn').get().val() 
    projectname = database.child('Data').child('projectname').get().val()

    return render(request,"Home.html",{"day":day,"idn":idn,"projectname":projectname })
#take to login page
def login (request):
    return render(request,"Login.html")

def charts(request):
        return render(request, "pHchart.html")

#grab database data put in labels, values. return as a jsonresponse for charts
def LineChart(request):

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

    labels = [day1, day2, day3, day4, day5, day6, day7]
    values = [value1, value2, value3, value4, value5, value6, value7]

    return JsonResponse(data={
        'labels': labels,
        'values': values,
    })
