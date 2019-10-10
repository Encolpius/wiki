from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('update/', views.profile_update, name="profile-update"),
    path('<username>/', views.show_user_profile, name="profile-detail"),
]
