from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PatientRegisterForm, TechnicianRegisterForm, DoctorRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from .models import Profile



def register(request):
    return render(request, 'users/register.html', {'title': 'Register'})

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            print("test before save")
            form.save()
            print("test after save")

            messages.success(request, f'Your patient account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = PatientRegisterForm()
    return render(request, 'users/register_patient.html', {'form': form})

def register_technician(request):
    if request.method == 'POST':
        form = TechnicianRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your technician account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = TechnicianRegisterForm()
    return render(request, 'users/register_technician.html', {'form': form})

def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your doctor account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = DoctorRegisterForm()
    return render(request, 'users/register_doctor.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)