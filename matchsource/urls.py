from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='ms-home'),
    path('form/', views.form, name='ms-form'),
    path('form/mining/', views.mining, name='ms-mining'),
    path('form/email/', views.email, name='ms-email'),

]
