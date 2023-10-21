from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm
from main.models import Test, CheckTest

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponse("Siz allaqachon tizimga kirib bolgansiz!")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return HttpResponse("Username yoki parol noto`g`ri")

    return render(request, "users/login.html")

def logout_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            logout(request)
            return redirect("index")
        return render(request, "users/logout.html")
    else:
        return HttpResponse("Siz allaqachon tizimdan chiqib ketib bolgansiz!")
    
def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        has_error = False
        if User.objects.filter(email=email):
            messages.error(request, "Ushbu email bilan foydalanuvchi mavjud.")
            has_error = True
        if User.objects.filter(username=username):
            messages.error(request, "Bu username bilan foydalanuvchi mavjud.")
            has_error = True
        if password1 != password2:
            messages.error(request, "Parollar o`aro bir xil emas.")
            has_error = True
        if len(password1) < 8:
            messages.error(request, "parol kamida 8 ta belgidan iborat bo`lishi kerak ")
            has_error = True
        
        if not has_error:
            user = User.objects.create(email=email, username=username, first_name=first_name)
            user.set_password(password1)
            user.save()
            return redirect('login')
        else:
            pass
    return render(request, "users/signup.html") 

@login_required(login_url="login")
def update_user(request):
    user = request.user
    form = UserForm(instance=user)
    profileForm = ProfileForm(instance=user.profile)
    if request.method == "POST":
        profileForm = ProfileForm(instance=user.profile, data=request.POST, files=request.FILES)
        form = UserForm(instance=user, data=request.POST)
        if form.is_valid() and profileForm.is_valid():
            form.save()
            profileForm.save()
            return redirect("profile", user.id)
        else:
            return render(request, "users/update_user.html", {"fofrm":form, "profileForm":profileForm})
    return render(request, "users/update_user.html", {"form":form, "profileForm":profileForm})


def profile(request, user_id):
    # user = User.objects.get(id=user_id)
    user = get_object_or_404(User, id=user_id)
    if user.profile.close_acc == False or user == request.user:
        number_of_test = Test.objects.filter(author=user).count()
        check_tests = CheckTest.objects.filter(student=user)
        number_of_checktests = check_tests.count()
        tests = []
        for checktest in check_tests:
            if not checktest.test in tests:
                tests.append(checktest.test)
        context = {
            "user":user,
            "number_of_test":number_of_test,
            "number_of_checktests":number_of_checktests,
            "check_tests":check_tests,
            "tests":tests
        }
        return render(request, "users/profile.html", context)
    else:
        raise Http404("This is a private account")