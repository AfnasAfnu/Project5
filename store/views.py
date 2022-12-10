
# Create your views here.


from django.contrib import messages
from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonForm
from .models import Person, Courses




# Create your views here.
def content(request):
    return render(request,'index.html')





def gform_create(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            details=form.save()
            # return redirect('add')
            messages.info(request,'Order Confirmed')

            return render(request,'new.html',{'detail':details})
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


# AJAX
def update_course(request):
    departments_id = request.GET.get('departments_id')
    course = Courses.objects.filter(departments_id=departments_id).all()
    return render(request, 'course_options.html', {'course': course})