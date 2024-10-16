from django.urls import path, include

from .views import SignUpView, CustomLoginView, Custom404View, HomeView, LogoutView

urlpatterns = [
    path("", HomeView.as_view(), name="home"), # Home view

    path("signup/", SignUpView.as_view(), name="signup"), 
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),  
    path("", include("django.contrib.auth.urls")),  

    path('<path:invalid_path>/', Custom404View.as_view(), name='custom_404'),  # For error catching


]