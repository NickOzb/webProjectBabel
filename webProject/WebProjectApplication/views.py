from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from .forms import *
from rest_framework import generics
from .serializers import TovarSerializer, RoomSerializer
from .models import Tovar, Room

# Create your views here.
def index(request):
    return render(request, 'WebProjectApplication/index.html')

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class TovarView(generics.ListAPIView):
    queryset = Tovar.objects.all()
    serializer_class = TovarSerializer

def createbanks(request):
    newBanks = Bank.objects.all()
    if request.method == "POST":
        newBank = Bank()
        newBank.id = request.POST.get("id")
        newBank.namebanka = request.POST.get("namebanka")
        newBank.save()
        return HttpResponseRedirect("/createbanks")
    return render(request, 'WebProjectApplication/createbanks.html', {'newBanks':newBanks})

def editbanks(request, id):
    try:
        newBank = Bank.objects.get(id=id)
        if request.method == "POST":
            newBank.namebanka = request.POST.get('namebanka')
            newBank.save()
            return HttpResponseRedirect("/createbanks")
        else:
            return render(request, 'WebProjectApplication/editbanks.html', {'newBank': newBank})
    except Bank.DoesNotExist:
        return HttpResponseNotFound("<h2>Bank not found</h2>")

def deletebanks(request, id):
    try:
        newBank = Bank.objects.get(id=id)
        newBank.delete()
        return HttpResponseRedirect("/createbanks")
    except Bank.DoesNotExist:
        return HttpResponseNotFound("<h2>Bank not found</h2>")

def createtovar(request):
    Tovars = Tovar.objects.all()
    if request.method == 'GET':
        form = TovarForm()
    elif request.method == 'POST':
        form = TovarForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createtovar')

    return render(request, 'WebProjectApplication/createtovar.html', {'form': form, 'Tovars': Tovars})

def edittovar(request, id):
    try:
        Tovars = Tovar.objects.all()
        newTovars = Tovar.objects.get(id=id)
        if request.method == 'GET':
            form = TovarForm(instance=newTovars)
            return render(request, 'WebProjectApplication/createtovar.html', {'form': form, 'newTovars': newTovars, 'Tovars':Tovars})
        elif request.method == 'POST':
            form = TovarForm(request.POST, instance=newTovars)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/createtovar')
    except Tovar.DoesNotExist:
        return render(request, 'WebProjectApplication/createtovar.html', {'form': form, 'newTovars': newTovars, 'Tovars':Tovars})

def deletetovar(request, id):
    try:
        newTovars = Tovar.objects.get(id=id)
        newTovars.delete()
        return HttpResponseRedirect('/createtovar')
    except Tovar.DoesNotExist:
         return HttpResponseNotFound('<h2> Товар не найден </h2> ')

def createkategory(request):
    Kategorys = Kategoriitovara.objects.all()
    if request.method == 'GET':
        form = KategoryForm()
    elif request.method == 'POST':
        form = KategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createkategory')

    return render(request, 'WebProjectApplication/createkategory.html', {'form': form, 'Kategorys': Kategorys})

def editkategory(request, id):
    try:
        Kategorys = Kategoriitovara.objects.all()
        newKategorys = Kategoriitovara.objects.get(id=id)
        if request.method == 'GET':
            form = KategoryForm(instance=newKategorys)
            return render(request, 'WebProjectApplication/createkategory.html', {'form': form, 'newKategorys': newKategorys, 'Kategorys':Kategorys})
        elif request.method == 'POST':
            form = KategoryForm(request.POST, instance=newKategorys)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/createkategory')
    except Tovar.DoesNotExist:
        return render(request, 'WebProjectApplication/createkategory.html', {'form': form, 'newTovars': newKategorys, 'Kategorys':Kategorys})

def deletekategory(request, id):
    try:
        newKategorys = Kategoriitovara.objects.get(id=id)
        newKategorys.delete()
        return HttpResponseRedirect('/createkategory')
    except Kategoriitovara.DoesNotExist:
         return HttpResponseNotFound('<h2> Категория не найдена </h2> ')

def createnalog(request):
    Nalogs = Nalogi.objects.all()
    if request.method == 'GET':
        form = NalogiForm()
    elif request.method == 'POST':
        form = NalogiForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createnalog')

    return render(request, 'WebProjectApplication/createnalog.html', {'form': form, 'Nalogs': Nalogs})

def editnalog(request, id):
    try:
        Nalogs = Nalogi.objects.all()
        newNalogs = Nalogi.objects.get(id=id)
        if request.method == 'GET':
            form = NalogiForm(instance=newNalogs)
            return render(request, 'WebProjectApplication/createnalog.html', {'form': form, 'newNalogs': newNalogs, 'Nalogs':Nalogs})
        elif request.method == 'POST':
            form = NalogiForm(request.POST, instance=newNalogs)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/createnalog')
    except Tovar.DoesNotExist:
        return render(request, 'WebProjectApplication/createnalog.html', {'form': form, 'newNalogs': newNalogs, 'Nalogs':Nalogs})

def deletenalog(request, id):
    try:
        newNalogs = Nalogi.objects.get(id=id)
        newNalogs.delete()
        return HttpResponseRedirect('/createnalog')
    except Kategoriitovara.DoesNotExist:
         return HttpResponseNotFound('<h2> Налог не найден </h2> ')

def createdvizhenie(request):
    Dvizhenies = Dvizhenie.objects.all()
    if request.method == 'GET':
        form = DvizhenieForm()
    elif request.method == 'POST':
        form = DvizhenieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createdvizhenie')

    return render(request, 'WebProjectApplication/createdvizhenie.html', {'form': form, 'Dvizhenies': Dvizhenies})

def editdvizhenie(request, id):
    try:
        Dvizhenies = Dvizhenie.objects.all()
        newDvizhenies = Dvizhenie.objects.get(id=id)
        if request.method == 'GET':
            form = DvizhenieForm(instance=newDvizhenies)
            return render(request, 'WebProjectApplication/createdvizhenie.html', {'form': form, 'newDvizhenies': newDvizhenies, 'Dvizhenies':Dvizhenies})
        elif request.method == 'POST':
            form = DvizhenieForm(request.POST, instance=newDvizhenies)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/createdvizhenie')
    except Tovar.DoesNotExist:
        return render(request, 'WebProjectApplication/createdvizhenie.html', {'form': form, 'newDvizhenies': newDvizhenies, 'Dvizhenies':Dvizhenies})

def deletedvizhenie(request, id):
    try:
        newDvizhenies = Dvizhenie.objects.get(id=id)
        newDvizhenies.delete()
        return HttpResponseRedirect('/createdvizhenie')
    except Dvizhenie.DoesNotExist:
         return HttpResponseNotFound('<h2> Товар не найден </h2> ')

def createorg(request):
    Orgs = Organizatsiya.objects.all()
    if request.method == 'GET':
        form = OrgForm()
    elif request.method == 'POST':
        form = OrgForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createorg')

    return render(request, 'WebProjectApplication/createorg.html', {'form': form, 'Orgs': Orgs})

def editorg(request, id):
    try:
        Orgs = Organizatsiya.objects.all()
        newOrgs = Organizatsiya.objects.get(id=id)
        if request.method == 'GET':
            form = OrgForm(instance=newOrgs)
            return render(request, 'WebProjectApplication/createorg.html', {'form': form, 'newOrgs': newOrgs, 'Orgs':Orgs})
        elif request.method == 'POST':
            form = OrgForm(request.POST, instance=newOrgs)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/createorg')
    except Organizatsiya.DoesNotExist:
        return render(request, 'WebProjectApplication/createorg.html', {'form': form, 'newOrgs': newOrgs, 'Orgs':Orgs})

def deleteorg(request, id):
    try:
        newOrgs = Organizatsiya.objects.get(id=id)
        newOrgs.delete()
        return HttpResponseRedirect('/createorg')
    except Organizatsiya.DoesNotExist:
         return HttpResponseNotFound('<h2> Организация не найдена </h2> ')

def createnakladnie(request):
    Nakladnies = Nakladnie.objects.all()
    if request.method == 'GET':
        form = NakladnieForm()
    elif request.method == 'POST':
        form = NakladnieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createnakladnie')

    return render(request, 'WebProjectApplication/createnakladnie.html', {'form': form, 'Nakladnies': Nakladnies})

def editnakladnie(request, id):
    try:
        Nakladnies = Nakladnie.objects.all()
        newNakladnies = Nakladnie.objects.get(id=id)
        if request.method == 'GET':
            form = NakladnieForm(instance=newNakladnies)
            return render(request, 'WebProjectApplication/createnakladnie.html', {'form': form, 'newNakladnies': newNakladnies, 'Nakladnies':Nakladnies})
        elif request.method == 'POST':
            form = NakladnieForm(request.POST, instance=newNakladnies)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/createnakladnie')
    except Nakladnie.DoesNotExist:
        return render(request, 'WebProjectApplication/createnakladnie.html', {'form': form, 'newNakladnies': newNakladnies, 'Nakladnies':Nakladnies})

def deletenakladnie(request, id):
    try:
        newNakladnies = Nakladnie.objects.get(id=id)
        newNakladnies.delete()
        return HttpResponseRedirect('/createnakladnie')
    except Nakladnie.DoesNotExist:
         return HttpResponseNotFound('<h2> Накладная не найдена </h2> ')

def createpodr(request):
    Podrs = Podrazdeleniya.objects.all()
    if request.method == 'GET':
        form = PodrForm()
    elif request.method == 'POST':
        form = PodrForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createpodr')

    return render(request, 'WebProjectApplication/createpodr.html', {'form': form, 'Podrs': Podrs})

def editpodr(request, id):
    try:
        Podrs = Podrazdeleniya.objects.all()
        newPodrs = Podrazdeleniya.objects.get(id=id)
        if request.method == 'GET':
            form = PodrForm(instance=newPodrs)
            return render(request, 'WebProjectApplication/createpodr.html', {'form': form, 'newPodrs': newPodrs, 'Podrs':Podrs})
        elif request.method == 'POST':
            form = OrgForm(request.POST, instance=newPodrs)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/createpodr')
    except Podrazdeleniya.DoesNotExist:
        return render(request, 'WebProjectApplication/createpodr.html', {'form': form, 'newPodrs': newPodrs, 'Podrs':Podrs})

def deletepodr(request, id):
    try:
        newPodrs = Podrazdeleniya.objects.get(id=id)
        newPodrs.delete()
        return HttpResponseRedirect('/createpodr')
    except Podrazdeleniya.DoesNotExist:
         return HttpResponseNotFound('<h2> Подразделение не найдено </h2> ')

def createtaks(request):
    Takss = Taksirovka.objects.all()
    if request.method == 'GET':
        form = TaksForm()
    elif request.method == 'POST':
        form = TaksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createtaks')

    return render(request, 'WebProjectApplication/createtaks.html', {'form': form, 'Takss': Takss})

def edittaks(request, id):
    try:
        Takss = Taksirovka.objects.all()
        newTakss = Taksirovka.objects.get(id=id)
        if request.method == 'GET':
            form = TaksForm(instance=newTakss)
            return render(request, 'WebProjectApplication/createtaks.html', {'form': form, 'newTakss': newTakss, 'Takss':Takss})
        elif request.method == 'POST':
            form = TaksForm(request.POST, instance=newTakss)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/createtaks')
    except Taksirovka.DoesNotExist:
        return render(request, 'WebProjectApplication/createtaks.html', {'form': form, 'newTakss': newTakss, 'Takss':Takss})

def deletetaks(request, id):
    try:
        newTakss = Taksirovka.objects.get(id=id)
        newTakss.delete()
        return HttpResponseRedirect('/createtaks')
    except Taksirovka.DoesNotExist:
         return HttpResponseNotFound('<h2> Таксировка не найдена </h2> ')

def createost(request):
    Osts = Ostatki.objects.all()
    if request.method == 'GET':
        form = OstForm()
    elif request.method == 'POST':
        form = OstForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createost')

    return render(request, 'WebProjectApplication/createost.html', {'form': form, 'Osts': Osts})

def editost(request, id):
    try:
        Osts = Ostatki.objects.all()
        newOsts = Ostatki.objects.get(id=id)
        if request.method == 'GET':
            form = OstForm(instance=newOsts)
            return render(request, 'WebProjectApplication/createost.html', {'form': form, 'newOsts': newOsts, 'Takss':Osts})
        elif request.method == 'POST':
            form = TaksForm(request.POST, instance=newOsts)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/createost')
    except Ostatki.DoesNotExist:
        return render(request, 'WebProjectApplication/createost.html', {'form': form, 'newOsts': newOsts, 'Osts':Osts})

def deleteost(request, id):
    try:
        newOsts = Taksirovka.objects.get(id=id)
        newOsts.delete()
        return HttpResponseRedirect('/createost')
    except Ostatki.DoesNotExist:
         return HttpResponseNotFound('<h2> Товар не найден </h2> ')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('Аккаунт не активен')
            else:
                return HttpResponse('Неправильный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'webProjectApplication/login.html', {'form': form})