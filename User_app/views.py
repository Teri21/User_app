from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    context = {
        "All_the_Users": User.objects.all()
        # variable/key: accesses the value
    }
    return render(request, "index.html", context)


# want the info. that's supplied inside of our form,so use request.POST is the form data
    # then need key to get access to the first_name,last_name,etc, which is the name="" in html
# added redirect on line 1 & return redirect to our root route where we'll be pulling
  # all the Users from database inside our index.html template


def create_user(request):
    if request.method == "POST":
        User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'],
                            email_address=request.POST['email'], age=request.POST['age'])
    return redirect('/')
