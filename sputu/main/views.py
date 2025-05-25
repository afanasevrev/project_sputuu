from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Material, Homework, HomeworkSubmission, Course, Announcement, Program
from .forms import ContactForm, UserRegistrationForm, HomeworkSubmissionForm
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'main/index.html')


@login_required
def profile(request):
    return render(request, 'main/profile.html')


@login_required
def materials_list(request):
    materials = Material.objects.filter(course__students=request.user)
    return render(request, 'main/materials_list.html', {'materials': materials})


@login_required
def material_detail(request, id):
    material = get_object_or_404(Material, id=id)
    return render(request, 'main/material_detail.html', {'material': material})


@login_required
def homework_list(request):
    homeworks = Homework.objects.filter(course__students=request.user)
    return render(request, 'main/homework_list.html', {'homeworks': homeworks})


@login_required
def homework_upload(request, id):
    homework = get_object_or_404(Homework, id=id)
    if request.method == 'POST':
        form = HomeworkSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.homework = homework
            submission.student = request.user
            submission.save()
            return redirect('homework_list')
    else:
        form = HomeworkSubmissionForm()
    return render(request, 'main/homework_upload.html', {'form': form, 'homework': homework})


#def login_view(request):
#    if request.method == 'POST':
#        username = request.POST['username']
#        password = request.POST['password']
#        user = authenticate(request, username=username, password=password)
#        if user is not None:
#            login(request, user)
#            return redirect('profile')
#    return render(request, 'main/login.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Замените 'home' на нужный URL
            else:
                return render(request, 'main/login.html', {'form': form, 'error': 'Неверный логин или пароль'})
        else:
            return render(request, 'main/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contacts')
    else:
        form = ContactForm()
    return render(request, 'main/contacts.html', {'form': form})


def announcements(request):
    announcements = Announcement.objects.all()
    return render(request, 'main/announcements.html', {'announcements': announcements})


def programs(request):
    programs = Program.objects.all()
    return render(request, 'main/programs.html', {'programs': programs})