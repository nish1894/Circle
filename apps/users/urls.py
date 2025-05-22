from django.urls import path, include
from .views import *
urlpatterns = [
    path('profile/', profile_view, name ="profile"),
    path('profile/edit/', profile_edit_view, name="profile-edit"),
    path('onboarding/', profile_edit_view, name="profile-onboarding"),
    path('profile/settings/',profile_settings_view,name= "profile-settings"),
    path('profile/email_change/', profile_email_change, name="profile-email-change"),
    path('email_verify/', profile_email_verify, name="profile-email-verify"),
    path('profile/delete/', profile_delete_view, name ="profile-delete"),

    #keep this at the very end because it will catch other generic urls
    path('<str:username>/', profile_view, name="profile-view"),

]