from django.urls import path, include
from . import views #allows us to connect to views.py through path

urlpatterns = [ #this block creates paths to the login and logout views
    path("", views.user, name="user"),
    # path ('accounts/', include('allauth.urls')),
    path("login/", views.login_view, name="login"), #login view link
    path("logout/", views.logout_view, name="logout"), #logout view link
    path('register/', views.register, name='register') #register view link
]