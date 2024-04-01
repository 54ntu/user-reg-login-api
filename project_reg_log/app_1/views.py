from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from app_1.serializers import UserModelSerializer
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
def register(request):

    # this one is for simple method or for templates

    # if request.method =="POST":
    #     username = request.POST.get('username')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     existingUser = User.objects.filter(username=username)
    #     if existingUser.exists():
    #         return HttpResponse('user already exists')
    #     else:
    #         user = User.objects.create_user(username,email,password)
    #         user.save()
    #         return redirect('login')
    # return render(request, "register.html")


    #### here we will write code for apis
    if request.method =="POST":
        obj1 = JSONParser().parse(request)
        print(obj1)
        username = obj1.get('username')
        print(username)
        existingUser = User.objects.filter(username=username)
        if existingUser.exists():
            return JsonResponse({'message':"user with same username already exists"})
        serializer = UserModelSerializer(data=obj1)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'data saved successfully'})
        return JsonResponse(serializer.errors,status=400)
    

        # serializer= UserModelSerializer(data=obj1)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse({'message':'data saved successfully'})
        # return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def user_login(request):

    # if request.method == "POST":
    #     username= request.POST.get('username')
    #     pass1 = request.POST.get('password')
    #     print(username,pass1)
        
    #     user = authenticate(request, username=username, password=pass1)
    #     if user is not None:
    #         login(request,user)
    #         return HttpResponse('user logged in')
    #     return HttpResponse('failed user login')

    # return render(request, "login.html")


    ####code for apis
    if request.method  =="POST":
        obj1 = JSONParser().parse(request)
        print("obj1: ",obj1)
        username = obj1.get('username')
        pass1 = obj1.get('password')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            serializer= UserModelSerializer(user)
            return JsonResponse({"message":"user logged in "}, status=200) 
        else:
            return JsonResponse({'message':"something went wrong"},status=400)       