from django.shortcuts import render, redirect
from .models import FakultetData
from .forms import FakultetDataForm

# Create your views here.


def index(request):
    data = FakultetData.objects.all()
    if request.method == 'POST':
        form = FakultetDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FakultetDataForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)