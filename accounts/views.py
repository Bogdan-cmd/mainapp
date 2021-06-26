from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .import forms
from django.views.generic import CreateView, DeleteView
#from django.views.generic.edit import DeleteView
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
import chromelogger as console

User = get_user_model()

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password-change.html'
    success_url = reverse_lazy('accounts:password-change-done-view')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password-reset-done.html'


@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "PROFIUL TĂU A FOST UPDATAT CU SUCCES!")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)



    context = {
    'user_form':user_form,
    'profile_form':profile_form
    }

    return render(request, 'accounts/profile.html',context)


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accounts:signup')


@login_required
def delete_user(request):
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.info(request, 'CONTUL TĂU A FOST ȘTERS.')
        return redirect('index')
    else:
        delete_form = UserDeleteForm(instance=request.user)

    context = {
        'delete_form': delete_form
    }

    return render(request, 'accounts/delete_account.html', context)
