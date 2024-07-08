from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        # request.POST here is the data flowing from UI to this function
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_name = form.save()  # Save the form data to the database
            # Log User In
            login(request, user_name)
            return redirect('blogs:blogs_list')  # appname: named url value
    else:  # Get Method Called
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    # GET request if user hits login.html
    # POST request if user submits the login form
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Login User
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blogs:blogs_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blogs:blogs_list')
