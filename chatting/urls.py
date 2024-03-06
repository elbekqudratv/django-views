from django.urls import path
from views import chatting


urlpatterns = [
    path('',chatting,name = 'home'),

]