from django.urls import path
from authentication.views import index, register, login_user, logout_user, update_details

app_name = 'authentication'
urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('update-details', update_details, name='update_details'),
]