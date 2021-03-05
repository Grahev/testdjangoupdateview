from django.shortcuts import render, redirect
from .forms import mainForm
from .models import myModel

# Create your views here.
def mainView(request):
    items = myModel.objects.all()
    context = {
        'items': items
    }
    return render(request,'testapp/main.html', context)


def update(request, pk):
    item = myModel.objects.get(id=pk)
    form = mainForm(instance=item)
    if request.method == 'POST':
        form = mainForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('main')
    context = {
        'form': form
    }
    return render(request,'testapp/update.html', context)