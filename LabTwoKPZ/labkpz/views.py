from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from db import DBWork
from myforms import AddPerson, AddApplication, AddBurn, AddMarig, AddDie, AddChang

from models import Person, Application, Marriage, Burn, ChangeName, Die

def hello(request):
    s1 = Person.objects.all()
    s2 = Application.objects.all()
    s3 = Marriage.objects.all()
    s4 = Burn.objects.all()
    s5 = Die.objects.all()
    s6 = ChangeName.objects.all()
    res = {"username": 'World', "f1": s1, "f2": s2, "f3": s3, "f4": s4, "f5": s5, "f6": s6}
    return render(request, "index.html", res)

def addper(request):
    if request.method == 'POST':
        form = AddPerson(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        form = AddPerson()
        return render(request, "add.html", {"form": form})

def addapp(request):
    if request.method == 'POST':
        form = AddApplication(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        form = AddApplication()
        return render(request, "add.html", {"form": form})

def addburn(request):
    if request.method == 'POST':
        form = AddBurn(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        form = AddBurn()
        return render(request, "add.html", {"form": form})

def addmarig(request):
    if request.method == 'POST':
        form = AddMarig(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        form = AddMarig()
        return render(request, "add.html", {"form": form})

def adddie(request):
    if request.method == 'POST':
        form = AddDie(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        form = AddDie()
        return render(request, "add.html", {"form": form})

def addchang(request):
    if request.method == 'POST':
        form = AddChang(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        form = AddChang()
        return render(request, "add.html", {"form": form})

def removeper(request, id):
    per = Person.objects.get(pk=id)
    per.delete()
    return HttpResponseRedirect(reverse('main'))

def removeapp(request, id):
    app = Application.objects.get(pk=id)
    app.delete()
    return HttpResponseRedirect(reverse('main'))

def removemar(request, id):
    mar = Marriage.objects.get(pk=id)
    mar.delete()
    return HttpResponseRedirect(reverse('main'))

def removeburn(request, id):
    bur = Burn.objects.get(pk=id)
    bur.delete()
    return HttpResponseRedirect(reverse('main'))

def removedie(request, id):
    die = Die.objects.get(pk=id)
    die.delete()
    return HttpResponseRedirect(reverse('main'))

def removechang(request, id):
    cha = ChangeName.objects.get(pk=id)
    cha.delete()
    return HttpResponseRedirect(reverse('main'))

def editper(request, id):
    if request.method == 'POST':
        app = Person.objects.get(pk=id)
        form = AddPerson(request.POST, instance=app)
        form.save()
        return HttpResponseRedirect(reverse('main'))
    else:
        app = Person.objects.get(pk=id)
        form = AddPerson(instance=app)
        return render(request, "add.html", {"form": form})

def editapp(request, id):
    if request.method == 'POST':
        app = Application.objects.get(pk=id)
        form = AddApplication(request.POST, instance=app)
        form.save()
        return HttpResponseRedirect(reverse('main'))
    else:
        app = Application.objects.get(pk=id)
        form = AddApplication(instance=app)
        return render(request, "add.html", {"form": form})

def editmar(request, id):
    if request.method == 'POST':
        app = Marriage.objects.get(pk=id)
        form = AddMarig(request.POST, instance=app)
        form.save()
        return HttpResponseRedirect(reverse('main'))
    else:
        app = Marriage.objects.get(pk=id)
        form = AddMarig(instance=app)
        return render(request, "add.html", {"form": form})

def editchang(request, id):
    if request.method == 'POST':
        app = ChangeName.objects.get(pk=id)
        form = AddChang(request.POST, instance=app)
        form.save()
        return HttpResponseRedirect(reverse('main'))
    else:
        app = ChangeName.objects.get(pk=id)
        form = AddChang(instance=app)
        return render(request, "add.html", {"form": form})

def editdie(request, id):
    if request.method == 'POST':
        app = Die.objects.get(pk=id)
        form = AddDie(request.POST, instance=app)
        form.save()
        return HttpResponseRedirect(reverse('main'))
    else:
        app = Die.objects.get(pk=id)
        form = AddDie(instance=app)
        return render(request, "add.html", {"form": form})

def editburn(request, id):
    if request.method == 'POST':
        app = Burn.objects.get(pk=id)
        form = AddBurn(request.POST, instance=app)
        form.save()
        return HttpResponseRedirect(reverse('main'))
    else:
        app = Burn.objects.get(pk=id)
        form = AddBurn(instance=app)
        return render(request, "add.html", {"form": form})

def action(request):
    db_obj = DBWork()
    if 'load' in request.GET:
        db_obj.read_json()
        return HttpResponseRedirect(reverse('main'))
    if 'addPer' in request.GET:
        return HttpResponseRedirect(reverse('addPer'))
    if 'addApp' in request.GET:
        return HttpResponseRedirect(reverse('addApp'))
    if 'addBurn' in request.GET:
        return HttpResponseRedirect(reverse('addBurn'))
    if 'addMarig' in request.GET:
        return HttpResponseRedirect(reverse('addMarig'))
    if 'addDie' in request.GET:
        return HttpResponseRedirect(reverse('addDie'))
    if 'addChang' in request.GET:
        return HttpResponseRedirect(reverse('addChang'))

