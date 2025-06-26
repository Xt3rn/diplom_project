from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Diplom


def index(request):
    return HttpResponse('Диплом ПОКАЖИ!!!!!')


def diploma_list(request):
    diploms = Diplom.objects.all()
    return render(request, 'diplom_detail.html', {'diploms': diploms})


def diploma_edit(request, pk):
    diplom = get_object_or_404(Diplom, pk=pk)
    if request.method == 'POST':
        diplom.student_name = request.POST.get('student_name')
        diplom.title = request.POST.get('title')
        diplom.supervisor = request.POST.get('supervisor')
        diplom.year = int(request.POST.get('year'))
        diplom.description = request.POST.get('description')
        diplom.save()
        return redirect('diploma_list')
    return render(request, 'diplom_edit.html', {'diplom': diplom})
