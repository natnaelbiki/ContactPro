from django.shortcuts import render
from django.db.models import Q
from .models import Branch, Manager
from rest_framework import generics

def index(request):
    manager = Manager.objects.all()
    branch = Branch.objects.all()
    context = {
        'managers': manager,
        'branches': branch,
        }

    return render(request, 'home.html', context=context)


def ManagerView(request):
    manager = Manager.objects.all()

    context = {
        'managers': manager,
        }

    return render(request, 'manager.html', context=context)

def BranchView(request):
    branch = Branch.objects.all()

    context = {
        'branches': branch,
        }

    return render(request, 'branch.html', context=context)

def SearchView(request):
    query = request.GET.get('search')
    print(query)
    return render(request, 'search.html', context=result)    
