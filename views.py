from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django. contrib import messages
from.forms import LoginForm
from.models import*

# Create your views here.
def index(request):
    data=Appointment.objects.all()
    return render(request,'index.html',{data:'data'})

def userdata(request):
    if request.method =="POST":
        name=request.POST['name']
        age=request.POST['age']
        phonenumber=request.POST['phonenumber']
        address=request.POST['address']
        issues=request.POST['issues']
        gender=request.POST['gender']
        print(name,age,phonenumber,issues,gender,'test')
        Appointment(name=name,age=age,phonenumber=phonenumber,address=address, issues=issues,gender=gender).save()
        messages.success(request,"Appointment successfully......!")
    return redirect('/')


def Patient(request):
    data=Appointment.objects.all()
    return render(request,"patient.html",{'data':data})

   

def Register(request):
    if request.method == 'POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        myuser=User.objects.create_user(username=username,email=email,password=password)
        myuser.is_staff=True
        myuser.first_name=name
        myuser.save()
        return redirect('login')
    
    else:
        form=UserCreationForm()
        return render(request,'registration/register.html',{})

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        myuser=authenticate(request,username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            return redirect('manage')
        else:
            messages.error(request, "somthing erroe...!")
            return redirect('login')
    else:    
        return render(request,'registration/login.html',{})
    
def logout_user(request):
    return redirect('index')

def Home(request):
    return redirect('index')

    
def Manage(request):
    return render(request,'manage.html')

def data_user(request):
    if request.method == 'POST':
        id=request.POST['id']
        name=request.POST['name']
        specialist=request.POST['specialist']
        number=request.POST['number']
        print(id,name,specialist,number,'test')
        docters(id=id,name=name,specialist=specialist,number=number).save()
        messages.success(request,"successfully......!")
        return redirect('/')
    else:
        messages.success(request,"somthing error......!")
        return render(request,'manage.html')


def Docter(request):
    data=docters.objects.all()
    return render(request,"docter.html",{'data':data})

def Appointed(request):
    data=Appointed.objects.all()
    return render(request,"Appointed.html",{'data':data})

   
  



      