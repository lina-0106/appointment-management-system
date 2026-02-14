from django.shortcuts import render, redirect
from .models import Appointment, Contact
from rest_framework .decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from .serailizers import AppointmentSerializer, ContactSerializer
from .forms import AppointmentForm, ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
def home(request):
    return render(request, 'myreminders/index.html')

def bookappointment(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        time=request.POST.get('time')
        status=request.POST.get('status')
        date=request.POST.get('date')
        phone=request.POST.get('phone')

        appointment=Appointment(name=name,email=email,date=date,time=time,status=status,phone=phone)
        appointment.save()
        messages.success(request, 'Your appointment has been booked successfully!')
        return redirect('bookappointment')
    form = AppointmentForm()
    return render(request, 'myreminders/bookappointment.html', {'form': form})


@login_required
def viewappointment(request):
    appointments = Appointment.objects.all()
    return render(request, 'myreminders/viewappointment.html', {
        'appointments': appointments
    })


def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,message=message)
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')          
    form=ContactForm()  
    return render(request, 'myreminders/contact.html', {'form': form})

def index(request):
    return render(request, 'myreminders/index.html')
def about(request):
    return render(request, 'myreminders/about.html')
def service(request):
    return render(request, 'myreminders/service.html')

def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return render(request,'login.html',{'error':'Invalid Credential'})
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        if password!=confirm_password:
            return render(request,"register.html",{"error":"password do not match"})
        if User.objects.filter(username=username).exists():
            return render(request,"register.html",{"error":"Username already existis"})
        user=User.objects.create_user(username=username,password=password)
        login(request,user)
        return redirect('index')
    return render(request,"register.html")


@api_view(['GET','POST'])
def appointments_api(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def contacts_api(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
