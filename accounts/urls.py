from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from accounts.views import MyPasswordChangeView, MyPasswordResetDoneView

app_name = 'accounts'

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('change-password/',MyPasswordChangeView.as_view(),name='password-change-view'),
    path('change-password/done/',MyPasswordResetDoneView.as_view(),name="password-change-done-view"),
    path('<int:pk>/delete/',views.UserDeleteView.as_view(template_name="accounts/delete_account.html"),name='delete-account'),
]
