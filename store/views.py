from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonForm
from .models import Person, Courses



def content(request):
    return render(request, 'index.html')


def Register(request):
    if request.method == 'POST':
        username = request.POST[
            'username']              ###left username we can write anything there ,right username from form 'name' check
        passw = request.POST['password']
        cpass = request.POST['cpassword']
        if passw == cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")  # messageinfo shows message site in screen like printf
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=passw)
                user.save();
                return redirect('login')  # after registration page redirect to login pg
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("newpg")
        else:
            messages.info(request, "Invalid details")
            return redirect('login')
    return render(request, "login.html")


def Logout(request):
    auth.logout(request)
    return redirect('/')


def detailspg(request):
    return render(request, 'details.html')


def gform_create(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            details = form.save()
            # return redirect('add')
            messages.success(request, 'Form Submitted Successfully')
            return render(request, 'new.html', {'detail': details})
        else:
            form = PersonForm()
    return render(request, 'home.html', {'form': form})


def update_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(instance=person)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('change', pk=pk)
    return render(request, 'home.html', {'form': form})


def update_course(request):
    departments_id = request.GET.get('departments_id')
    course = Courses.objects.filter(departments_id=departments_id).all()
    return render(request, 'course_options.html', {'course': course})

    #
    # if request.method == 'POST':
    #     auth.logout(request)
    #     return redirect('/')
