from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from.views import appointments_api, contacts_api

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('viewappointment/',views.viewappointment,name='viewappointment'),
    path('bookappointment/',views.bookappointment,name='bookappointment'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    path('accounts/profile',views.index,name='profile'),
    path('appointments/', views.appointments_api, name='appointments_api'),
    path('contacts/', views.contacts_api, name='contacts_api'),
    path('regisster/',views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]