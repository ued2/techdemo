from django.urls import path
from .import views

urlpatterns = [
	path('', views.home, name='ms-home'),
    path('create_account/', views.create_account, name='ms-create'),
    path('create_account/questionnaire',
         views.questionnaire, name='ms-ca-questionnaire'),
    path('create_account/login/questionnaire',
         views.questionnaire, name='ms-cal-questionnaire'),
    path('login/', views.login, name='ms-login'),
    path('logout/', views.logout, name='ms-logout'),
    path('questionnaire/', views.questionnaire, name='ms-questionnaire'),
    path('questionnaire/email/', views.email, name='ms-email'),
    path('questionnaire/profile_mining',
         views.profile_mining, name='ms-q-profile_mining'),
    path('profile_mining/', views.profile_mining, name='ms-profile_mining'),
    path('matches/', views.matches, name='ms-matches'),


]
