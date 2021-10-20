from django.shortcuts import render
from .models import Bank
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse
from .forms import ContactForm
from .forms import BlankForm
from .forms import AnswerForm
from .forms import RemoveForm
from .forms import FindForm
import random
import os
import time
import random
import ast
import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
def post_list(request):
    return render(request, 'blog/post_list.html')

def login(request):
    return render(request, 'blog/login.html')

def add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            word = request.POST.get('word')
            var =  False
            translation = request.POST.get('translation')
            for i in Bank.objects.all():
                if i.user == request.user.get_username():
                    i.text = i.text+","+str(word)
                    i.translation = i.translation+","+translation
                    i.save()
                    var = True
                    return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")
            if var == False:
                foo_instance = Bank.objects.create(user=request.user.get_username())
                for i in Bank.objects.all():
                    if i.user == request.user.get_username():
                        i.text = str(word)
                        i.translation = translation
                        i.assessment_correct = 0
                        i.assessment_count = 0
                        i.assessment_results = "[]"
                        i.save()
                        return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")

                

    else:
        form = ContactForm()
    return render(request, 'blog/add.html', {'form':form})
def account_new(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})
def remove(request):
    if request.method == 'POST':
        form = RemoveForm(request.POST)
        if form.is_valid():
            item_number = int(request.POST.get('item_number'))
            item_number -= 1
            var = False
            for i in Bank.objects.all():
                if i.user == request.user.get_username():
                    text = i.text
                    translation = i.translation
                    temp = ""
                    text_list = []
                    translation_list = []
                    for n in range(len(text)):
                        if text[n] == ",":
                            text_list.append(temp)
                            temp = ""

                        else:
                            temp = temp+text[n]
                    text_list.append(temp)
                    temp = ""

                    for n in range(len(translation)):
                        if translation[n] == ",":
                            translation_list.append(temp)
                            temp = ""

                        else:
                            temp = temp+translation[n]
                    translation_list.append(temp)
                    temp = ""
                    p1_text_l = text_list[:int(item_number)]
                    p2_text_l = text_list[int(item_number)+1:]
                    p1_translation_l = translation_list[:int(item_number)]
                    p2_translation_l = translation_list[int(item_number)+1:]
                    text_list = p1_text_l+p2_text_l
                    translation_list = p1_translation_l+p2_translation_l
                    temp = ""
                    for n in range(len(text_list)):
                        temp = str(temp) + str(text_list[n]) + ","
                    i.text = temp[:len(temp)-1]
                    #prin()
                    temp = ""
                    for n in range(len(translation_list)):
                        temp = str(temp) + str(translation_list[n]) + ","
                    i.translation = temp[:len(temp)-1]
                    i.save()
                    var = True
                    return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")
            if var == False:
                foo_instance = Bank.objects.create(user=request.user.get_username())
                for i in Bank.objects.all():
                    if i.user == request.user.get_username():
                        i.text = str(word)
                        i.translation = translation
                        i.assessment_correct = 0
                        i.assessment_count = 0
                        i.assessment_results = "[]"
                        i.save()
                        return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")

                

    else:
        form = RemoveForm()
    return render(request, 'blog/remove.html', {'form':form})
def view(request):
    for i in Bank.objects.all():
        if i.user == request.user.get_username():
            text = i.text
            translation = i.translation
            temp = ""
            text_list = []
            translation_list = []
            for n in range(len(text)):
                if text[n] == ",":
                    text_list.append(temp)
                    temp = ""

                else:
                    temp = temp+text[n]
            text_list.append(temp)
            temp = ""

            for n in range(len(translation)):
                if translation[n] == ",":
                    translation_list.append(temp)
                    temp = ""

                else:
                    temp = temp+translation[n]
            translation_list.append(temp)
            temp = ""
            for n in range(len(text_list)):
                temp = temp+"<p id=\"main\">"+str(n+1)+". Text: "+text_list[n]+"| Translation: "+translation_list[n]+"</p><br>"
            return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a><br><h3 id=\"main\">Your words in order!</h3><br>"+temp)


def test_c(request):
    for i in Bank.objects.all():
        if i.user == request.user.get_username():
            i.assessment_count = int(i.assessment_count) + 1
            i.save()
            text = i.text
            translation = i.translation
            temp = ""
            text_list = []
            translation_list = []
            for n in range(len(text)):
                if text[n] == ",":
                    text_list.append(temp)
                    temp = ""

                else:
                    temp = temp+text[n]
            text_list.append(temp)
            temp = ""

            for n in range(len(translation)):
                if translation[n] == ",":
                    translation_list.append(temp)
                    temp = ""

                else:
                    temp = temp+translation[n]
            translation_list.append(temp)
            temp = ""
            assessmentlist = []
            for n in range(len(i.assessment_counter)):
                if i.assessment_counter[n] == ",":
                    assessmentlist.append(int(temp))
                    temp = ""

                else:
                    temp = temp+i.assessment_counter[n]
            #prn()
            acceptable = []
            for n in range(len(text_list)):
                if not n in assessmentlist:
                    acceptable.append(n)
            previousresults = ast.literal_eval(i.assessment_results)
            
            if len(assessmentlist)==len(text_list):
                assessment_correct = i.assessment_correct
                i.assessment_correct = 0
                i.assessment_counter = ""
                #prin()
                previousresults.append(len(text_list))
                previousresults.append(int(assessment_correct))
                previousresults.append(str(datetime.datetime.now()))
                i.assessment_count = 0
                i.assessment_results = str(previousresults)
                i.save()
            
                return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><p id=\"main\">You got "+str(assessment_correct)+" out of "+str(len(text_list))+"!</p><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")

            ra = random.randint(0,len(acceptable)-1)
            ra1 = acceptable[ra]
            #prin()
            i.assessment_counter = i.assessment_counter+str(ra1)+","
            i.save()

            temp = ""
    
            i.save()
            #prin()
            assessmentlist = []
            for n in range(len(i.assessment_counter)):
                if i.assessment_counter[n] == ",":
                    assessmentlist.append(int(temp))
                    temp = ""

                else:
                    temp = temp+i.assessment_counter[n]
            if len(assessmentlist)>len(text_list):
                assessment_correct = i.assessment_correct
                i.assessment_correct = 0
                i.assessment_counter = ""
                #prin()
                i.assessment_count = 0
                i.save()
            
                return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><p id=\"main\">You got "+str(assessment_correct)+" out of "+str(len(text_list))+"!</p><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")

            ran = random.randint(1,2)    
    
            counter = i.assessment_counter
            #prin()
            if ran == 1:
                i.assessment_temp = text_list[ra1]
            else:
                i.assessment_temp = translation_list[ra1]
    
            i.assessment_type = ran
            #prin()
            i.save()
            response = redirect('/test')
            return response
            return render(request, 'blog/testsubmit.html')

def test(request):
    a_id = []
    for i in Bank.objects.all():
        if i.user == request.user.get_username():
            a_id.append(i.id)
    bank = Bank.objects.filter(id__in=a_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            for i in Bank.objects.all():
                if i.user == request.user.get_username():
                    answer = request.POST.get('answer')
                    if i.assessment_type == "1":
                        text = i.text
                        translation = i.translation
                        temp = ""
                        text_list = []
                        translation_list = []
                        for n in range(len(text)):
                            if text[n] == ",":
                                text_list.append(temp)
                                temp = ""

                            else:
                                temp = temp+text[n]
                        text_list.append(temp)
                        temp = ""

                        for n in range(len(translation)):
                            if translation[n] == ",":
                                translation_list.append(temp)
                                temp = ""

                            else:
                                temp = temp+translation[n]
                        translation_list.append(temp)
                        temp = ""
                        assessment_list = []
                        for n in range(len(i.assessment_counter)):
                            if i.assessment_counter[n] == ",":
                                assessment_list.append(temp)
                                temp = ""

                            else:
                                temp = temp+i.assessment_counter[n]
                        assessment_list.append(temp)
                        temp = ""
                        a_counter_list = []
                        for n in range(len(i.assessment_counter)):
                            if i.assessment_counter[n] == ",":
                                a_counter_list.append(temp)
                                temp = ""
                            else:
                                temp = str(temp)+str(i.assessment_counter[n])
                        last = int(a_counter_list[len(a_counter_list)-1])
                        translation__ = translation_list[last].upper()
                        
                        if answer.upper() == translation_list[last].upper():
                            i.assessment_correct =int(i.assessment_correct)+ 1
                            i.save()
                            if len(a_counter_list)>len(text_list):
                                assessment_correct = i.assessment_correct
                                i.assessment_correct = 0
                                i.assessment_counter = ""
                                i.assessment_count = 0
                                i.save()
                                return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><p id=\"main\">You got "+str(assessment_correct)+" out of "+str(len(text_list))+"!</p><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")
                                
                            else:
                                response = redirect('/testsubmit')
                                return response
                        else:
                            if len(a_counter_list)>len(text_list):
                                assessment_correct = i.assessment_correct
                                i.assessment_correct = 0
                                i.assessment_counter = ""
                                i.assessment_count = 0
                                i.save()
                                return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><p id=\"main\">You got "+str(assessment_correct)+" out of "+str(len(text_list))+"!</p><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")
                                
                            else:
                                response = redirect('/testsubmit')
                                return response
                    else:
                        text = i.text
                        translation = i.translation
                        temp = ""
                        text_list = []
                        translation_list = []
                        for n in range(len(text)):
                            if text[n] == ",":
                                text_list.append(temp)
                                temp = ""

                            else:
                                temp = temp+text[n]
                        text_list.append(temp)
                        temp = ""

                        for n in range(len(translation)):
                            if translation[n] == ",":
                                translation_list.append(temp)
                                temp = ""

                            else:
                                temp = temp+translation[n]
                        translation_list.append(temp)
                        temp = ""
                        assessment_list = []
                        for n in range(len(i.assessment_counter)):
                            if i.assessment_counter[n] == ",":
                                assessment_list.append(temp)
                                temp = ""

                            else:
                                temp = temp+i.assessment_counter[n]
                        assessment_list.append(temp)
                        temp = ""
                        a_counter_list = []
                        for n in range(len(i.assessment_counter)):
                            if i.assessment_counter[n] == ",":
                                a_counter_list.append(temp)
                                temp = ""
                            else:
                                temp = str(temp)+str(i.assessment_counter[n])
                        answerUpper = answer.upper()
                        translation_l = translation_list[len(translation_list)-1].upper()
                        last = int(a_counter_list[len(a_counter_list)-1])
                        if answer.upper() == text_list[last].upper():
                            i.assessment_correct =int(i.assessment_correct)+ 1
                            i.save()
                            if len(a_counter_list)>len(text_list):
                                assessment_correct = i.assessment_correct
                                i.assessment_correct = 0
                                i.assessment_counter = ""
                                i.assessment_count = 0
                                i.save()
                                return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><p id=\"main\">You got "+str(assessment_correct)+" out of "+str(len(text_list))+"!</p><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")
                                
                            else:
                                response = redirect('/testsubmit')
                                return response
                        else:
                            if len(a_counter_list)>len(text_list):
                                assessment_correct = i.assessment_correct
                                i.assessment_correct = 0
                                i.assessment_counter = ""
                                i.assessment_count = 0
                                i.save()
                                return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><p id=\"main\">You got "+str(assessment_correct)+" out of "+str(len(text_list))+"!</p><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")
                                
                            else:
                                response = redirect('/testsubmit')
                                return response
    else:
        form = AnswerForm()

    return render(request, 'blog/assessment.html', {
        'form':form,
        'bank':bank,
    })
def find(request):
    if request.method == 'POST':
        form = FindForm(request.POST)
        if form.is_valid():
            for i in Bank.objects.all():
                if i.user == request.user.get_username():
                    find = request.POST.get('find')
                    text = i.text
                    translation = i.translation
                    temp = ""
                    text_list = []
                    translation_list = []
                    find_list = []
                    opp_list = []
                    for n in range(len(text)):
                        if text[n] == ",":
                            text_list.append(temp)
                            temp = ""

                        else:
                            temp = temp+text[n]
                    text_list.append(temp)
                    temp = ""
                    for n in range(len(translation)):
                        if translation[n] == ",":
                            translation_list.append(temp)
                            temp = ""

                        else:
                            temp = temp+translation[n]
                    translation_list.append(temp)
                    temp = ""
                    for n in range(len(text_list)):
                        if text_list[n].upper().find(find.upper()) != -1:
                            find_list.append(text_list[n])
                            opp_list.append(translation_list[n])
                        elif translation_list[n].upper().find(find.upper()) != -1:
                            find_list.append(translation_list[n])
                            opp_list.append(text_list[n])
                    for n in range(len(find_list)):
                        temp = temp+"<p id=\"main\">"+str(n+1)+". Found: "+find_list[n]+"| Translation: "+opp_list[n]+"</p><br>"
                    if len(find_list) == 1:
                        res = "1 result found!"
                    else:
                        res = str(len(find_list))+" results found!"
                    return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a><br><h3 id=\"main\">"+res+"</h3><br>"+temp)

                        
    else:
        form = FindForm()
    return render(request, 'blog/find.html', {'form':form})

def results(request):
    for i in Bank.objects.all():
        if i.user == request.user.get_username():
            results = ast.literal_eval(i.assessment_results)
            temp = ""
            averagetotal = 0
            if len(results) != 0 and results != 0:
                for n in range(int(len(results)/3)):
                    r = (n*3)
                    percentage = round(results[r+1]/results[r],3)*100
                    averagetotal += percentage
                    temp = temp+"<p id=\"main\">"+str(n+1)+") "+str(results[r+1])+" out of "+str(results[r])+" | "+str(percentage)+"% correct! | Completed at "+str(results[r+2])+"</p><br>"
                average = round(averagetotal/(n+1),3)
                return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><p id=\"main\">Your average score is "+str(average)+"%</p><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a><br><hr><br><u><h2 id=\"main\">Scores:</h2></u><br>"+temp)
            else:
                return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><h3 id = \"main\">Oops...</h3><br><p id =\"main\">Unfortunately there are no results that we can see. This might be caused by the fact you haven't done any assessments; you can complete an assessment by clicking the button below:<br><a href=\"testsubmit\" id=\"button\">Click here to complete an assessment!</a><br><h3 id=\"main\">Or</h3><br><a href=\"/\" id=\"button\">You can click here to return back to the home page</a><br>")
