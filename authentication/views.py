from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def index(request, *args, **kwargs):
    context = {
        'logged_in': request.user.is_authenticated
    }
    return render(request, 'authentication/index.html', context)


def register(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        plan = request.POST['plan']
    
        if User.objects.filter(username=username).exists():
            print('The username already exists!')
            return redirect('authentication:register')
        elif password1 != password2:
            print('Passwords don\'t match!')
            return redirect('authentication:register')
        else:
            new_user = User.objects.create_user(
                username=username,
                password=password1,
            )
            new_user.plan = plan
            new_user.save()
            print("User %s created" % new_user.username)

            return redirect('authentication:login')

    elif request.method == 'GET':
            context = {}
            return render(request, 'authentication/register.html', context)

def login_user(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("User '%s' logged in!" % user.username)
            return redirect('books_app:index')
        
        else:
            print("Invalid credentials!")
            return redirect('authentication:login')

    elif request.method == "GET":
        context = {}
        return render(request, 'authentication/login.html', context)

def logout_user(request, *args, **kwargs):
    logout(request)
    print('Logged out!')
    return redirect('authentication:index')

def update_details(request, *args, **kwargs):
    user = request.user

    if request.method == "POST":
        new_username = request.POST['new_username']
        new_first_name = request.POST['new_first_name']
        new_last_name = request.POST['new_last_name']
        print(new_username, new_last_name, new_first_name)

        if request.user.username == new_username:
            print('You are already using this username!')
            return redirect('authentication:update_details')
        
        elif User.objects.filter(username=new_username).exists():
            print('This username already exists!')
            return redirect('authentication:update_details')
        
        else:
            user.username = new_username
            user.first_name = new_first_name
            user.last_name = new_last_name

            user.save(update_fields=[
                'username', 'first_name', 'last_name'
            ])
            print('Details updated!')
            return redirect('authentication:index')

    elif request.method == "GET":
        context = {
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        }
        return render(request, 'authentication/update_details.html', context)