from django.shortcuts import render
from .models import Bank
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse
from .forms import ContactForm
from .forms import BlankForm
from .forms import AnswerForm
from .forms import RemoveForm
import random
import os
import time
import random
from django.shortcuts import redirect
def post_list(request):
    if request.method == 'POST':
        form = BlankForm(request.POST)
        if form.is_valid():
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
                    
                    

    else:
        form = BlankForm()
    return render(request, 'blog/post_list.html', {'form':form})

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
                        i.save()
                        return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")

                

    else:
        form = ContactForm()
    return render(request, 'blog/add.html', {'form':form})
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
                        i.save()
                        return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>Lan Bank</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">Lan Bank</h1></a></center></div><center><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")

                

    else:
        form = RemoveForm()
    return render(request, 'blog/remove.html', {'form':form})
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
                    assessmentlist.append(temp)
                    temp = ""

                else:
                    temp = temp+i.assessment_counter[n]
    
            found = True
            while found == True:
                if len(assessmentlist) == 0:
                    ra1 = random.randint(0,len(text_list)-1)
                    #prin()
                    found = False
                    i.assessment_counter = str(ra1)+","
                    i.save()
                else:
                    ra1 = random.randint(0,len(text_list)-1)
                    assessment_counter = i.assessment_counter+str(ra1)+","
                    temp = ""
                    assessmentlist = []
                    for n in range(len(assessment_counter)):
                        if assessment_counter[n] == ",":
                            assessmentlist.append(temp)
                            temp = ""

                        else:
                            temp = temp+assessment_counter[n]
                    if not ra1 in assessmentlist:
                        found = False
                        i.assessment_counter = i.assessment_counter+str(ra1)+","
                        i.save()

                    

                    #prin()

            temp = ""
    
            i.save()
            #prin()
            assessmentlist = []
            for n in range(len(i.assessment_counter)):
                if i.assessment_counter[n] == ",":
                    assessmentlist.append(temp)
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


def task_submit(request, id):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            for i in Task.objects.all():
                if i.id == id:
                    expectedoutput = i.output
                    endinput = i.input
                    keywords = i.keyterms

            bad_chars="[]',"
            endinput_list = []
            ichars = []
            for i in range(len(endinput)-2):
                if not endinput[i+2] == ",":
                    ichars.append(endinput[i+2])
                else:
                    ichars.append("END")
            iword = ""
            for i in range(len(ichars)):
                if ichars[i] != "END":
                    iword = str(iword)+str(ichars[i])
                else:
                    endinput_list.append(iword)
                    iword = ""
            keywords_list =[]
            kword = ""
            for i in range(len(keywords)-2):
                if not keywords[i+2] == ",":
                    kword = str(kword)+str(keywords[i+2])
                else:
                    keywords_list.append(kword)
                    kword = ""

            code = request.POST.get('code')
            submit = []
            a_submit = []
            stat_input = 0
            submitappend = ""
            for x in range(len(code)):
                if code[x] == ";":
                    submit.append(submitappend)
                    submitappend = ""
                else:
                    submitappend = str(submitappend)+str(code[x])

            a_submit = []
            output = 0
            received_input=0
            stat_input = 0
            outputvar1 = random.randint(1000,10000)
            outputvar = "a"+str(outputvar1)
            keywords_received = 0
            for i in range(len(submit)):
                if submit[i].find("print(") != -1:
                    code = submit[i]
                    find = submit[i].find("print(")
                    value = code[find+6:-1]
                    if output > 0:
                        a_submit.append(code[:find]+str(outputvar)+".append("+str(value)+")")
                        if keywords_received < len(keywords_list):
                            if submit[i].find(keywords_list[keywords_received]) != -1:
                                keywords_received += 1

                    else:
                        a_submit.append(code[:find]+str(outputvar)+" = ["+str(value)+"]")
                        output+=1
                        if keywords_received < len(keywords_list):
                            if submit[i].find(keywords_list[keywords_received]) != -1:
                                keywords_received += 1
                elif submit[i].find("input(") != -1:
                    code = submit[i]
                    find = submit[i].find("input(")
                    value = code[:find-1]
                    a_submit.append(value+str(endinput_list[stat_input]))
                    stat_input += 1
                    received_input += 1
                    if keywords_received < len(keywords_list):
                        if submit[i].find(keywords_list[keywords_received]) != -1:
                            keywords_received += 1
                else:
                    a_submit.append(submit[i])
                    if keywords_received < len(keywords_list):
                        if submit[i].find(keywords_list[keywords_received]) != -1:
                            keywords_received += 1
            if a_submit != []:
                with open("mark.py", "w") as file:
                    file.write(a_submit[0])

                for i in range(len(a_submit)-1):
                    with open("mark.py", "a") as file:
                        file.write('\n'+a_submit[i+1])

                with open("mark.py", "a") as file1:
                    file1.write('\n'+"with open(\"output.txt\", \"w\") as f:")
                with open("mark.py", "a") as file2:
                    file2.write('\n'+"  "+"f.write(str("+str(outputvar)+"))")
                print("Test program created!")
                try:
                    exec(open("mark.py").read())
                except:
                    return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>MARKER</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">MARKER</h1></a></center></div><center><p id=\"main\">An error was found in your code please retry this task!</p><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")
                print("Attempting to gather output data...")
            
                r = open("output.txt")
                print("Gathered successfully!")
                char = []
                char1 = []
                insertend = False
                insertend1 = False
                words = []
                words1 = []
                word = ""
                word1 = ""
                for i in range(len(r.read())):
                    r = open("output.txt")
                    if bad_chars.find(r.read()[i]) == -1:
                        r = open("output.txt")
                        char.append(r.read()[i])
                        r = open("output.txt")
                        insertend = True
                    elif insertend == True:
                        insertend = False
                        char.append("END")
                for i in range(len(char)):
                    if char[i] != "END":
                        word = word+char[i]
                    else:
                        words.append(word)
                        word = ""


                for i in range(len(expectedoutput)-2):
                    if not expectedoutput[i+2] == ",":
                        char1.append(expectedoutput[i+2])
                    elif expectedoutput[i+2] == ",":
                        char1.append("END")
                for i in range(len(char1)):
                    if char1[i] != "END":
                        word1 = word1+char1[i]
                    else:
                        words1.append(word1)
                        word1 = ""
                mark = 0
                total_marks = (len(words1))+len(endinput_list)+len(keywords_list)
                try:
                    for i in range(len(words1)):
                        if words1[i].upper() == words[i].upper():
                            mark+=1
                        elif words[i].upper().find(words1[i].upper()) != -1:
                            mark+=1
                except IndexError:
                    print("Hi")
                if received_input == len(endinput_list):
                    mark+=received_input
                mark += keywords_received
                r.close()
                os.remove("mark.py")
                os.remove("output.txt")
                username= request.user.get_username()
                for i in Task.objects.all():
                    if i.id == id:
                        if i.students.find(request.user.get_username()) == -1:
                            i.students = str(i.students)+str(request.user.get_username())+","
                            i.marks = str(i.marks)+str(mark)+","
                            i.save()
                        else:
                            comma_counter = 0
                            counter = 0
                            find0 = i.students.find(request.user.get_username())
                            old_marks = ""
                            marks_comma_counter = 0
                            Loop = True
                            for o in range(find0):
                                if i.students[o] == ",":
                                    comma_counter += 1
                            while Loop == True:
                                if marks_comma_counter == comma_counter+1:
                                    Loop = False
                                elif i.marks[counter] == ",":
                                    marks_comma_counter +=1
                                elif marks_comma_counter == comma_counter:
                                    old_marks = old_marks+str(i.marks[counter])
                                counter += 1
                            i.marks = i.marks[:comma_counter+1]+str(mark)+i.marks[comma_counter+1+len(old_marks):]
                            i.save()
                            
                return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>MARKER</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">MARKER</h1></a></center></div><center><p id=\"main\">Your mark is "+str(mark)+" out of "+str(total_marks)+"</p><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")

            else:
                return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>MARKER</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">MARKER</h1></a></center></div><center><p id=\"main\">Unfortunately no code was found. Please make sure you include a ; after every line of code!</p><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")
    else:
        form = ContactForm()
    return render(request, 'blog/task_submit.html', {'form':form})
def students(request):
    allowed_tasks = []
    for i in Task.objects.all():
        if request.user.get_short_name() == i.school:
            allowed_tasks.append(i.id)

    tasks = Task.objects.filter(id__in=allowed_tasks)
    return render(request, 'blog/students_data.html', {'tasks':tasks})
def students_list(request, id):
    students_list = []
    student_name = ""
    for i in Task.objects.all():
        if i.id == id:
            for o in range(len(i.students)-2):
                if i.students[o+2] == ",":
                    students_list.append(student_name)
                    student_name = ""
                else:
                    student_name=str(student_name)+i.students[o+2]
            with open("id.txt", "w") as t:
                t.write(str(id))
            
            return render(request, 'blog/students_list.html', {'students_list':students_list})

def student_mark(request, student):
    with open("id.txt") as t:
        id = t.read()
    comma_counter = 0
    counter = 0
    old_marks = ""
    marks_comma_counter = 0
    Loop = True
    for i in Task.objects.all():
        if i.id == int(id):
            find0 = i.students.find(student)
            for o in range(find0):
                if i.students[o] == ",":
                    comma_counter += 1
            while Loop == True:
                if marks_comma_counter == comma_counter+1:
                    Loop = False
                elif i.marks[counter] == ",":
                    marks_comma_counter +=1
                elif marks_comma_counter == comma_counter:
                    old_marks = old_marks+str(i.marks[counter])
                counter += 1
            expectedoutput = i.output
            endinput = i.input
            keywords = i.keyterms
            endinput_list = []
            ichars = []
            for n in range(len(endinput)-2):
                if not endinput[n+2] == ",":
                    ichars.append(endinput[n+2])
                else:
                    ichars.append("END")
            iword = ""
            for n in range(len(ichars)):
                if ichars[n] != "END":
                    iword = str(iword)+str(ichars[n])
                else:
                    endinput_list.append(iword)
                    iword = ""
            keywords_list =[]
            kword = ""
            for n in range(len(keywords)-2):
                if not keywords[n+2] == ",":
                    kword = str(kword)+str(keywords[n+2])
                else:
                    keywords_list.append(kword)
                    kword = ""
            char1 = []
            word1 = ""
            words1 =[]

            for n in range(len(expectedoutput)-2):
                if not expectedoutput[n+2] == ",":
                    char1.append(expectedoutput[n+2])
                elif expectedoutput[n+2] == ",":
                    char1.append("END")
            for n in range(len(char1)):
                if char1[n] != "END":
                    word1 = word1+char1[n]
                else:
                    words1.append(word1)
                    word1 = ""
            total_marks = (len(words1))+len(endinput_list)+len(keywords_list)
            return HttpResponse("<html><head><style>#header /*Styles for Header*/{padding: 15px;color: #ffffff;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;background-color: #00ddff;}#main {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 18px;}#button {background-color: white;color: black;border: 2px #e7e7e7;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button:hover {background-color: #e7e7e7; color: black;font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#button1 {background-color: white;color: black;border: 2px solid #e7e7e7;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;border-radius: 5px;}#button1:hover {background-color: #e7e7e7; color: black;width=\"50%\"font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 20px;}#title {font-family: \"Trebuchet MS\", Helvetica, sans-serif;font-size: 24px;}</style><title>MARKER</title></head><body><div><center><a href=\"/\"><h1 id=\"header\">MARKER</h1></a></center></div><center><p id=\"main\">The student "+str(student)+" has got "+str(old_marks)+" out of "+str(total_marks)+" on "+str(i.title)+"</p><br><a href=\"/\" id=\"button\">Click here to return back to the home page</a>")

