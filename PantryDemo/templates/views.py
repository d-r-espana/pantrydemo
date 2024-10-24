from django.shortcuts import render

def welcome(request):
    """View function for the welcome page."""
    return render(request, 'welcome/welcome.html')

def about(request):
    """View function for the about page."""
    return render(request, 'about.html')

def dashboard(request):
    """View function for the dashboard page (restricted access)."""
    # Add logic to check if the user is authenticated before rendering
    # the dashboard. If not authenticated, redirect to login page.
    return render(request, 'dashboard.html')

def login(request):
    """View function for the login page."""
    # Add logic to handle login form submission and user authentication
    return render(request, 'login.html')

def signup(request):
    """View function for the signup page."""
    # Add logic to handle signup form submission and user creation
    return render(request, 'signup.html')