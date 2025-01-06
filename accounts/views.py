from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

def signup(request):
    if request.method == 'POST':
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username, email=email, password=password1)
        user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend' 
        login(request, user)
        messages.success(request, "Account created successfully!")
        messages.success(request, "Login successful!")
        return redirect('/')

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('/')
        else:
            messages.error(request, "Invalid email/username or password!")
            return redirect('signin')

    return render(request, 'signin.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('signin')