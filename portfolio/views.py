from django.shortcuts import render
from .forms import ContactForm


def index(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            context = {'form': form}
    else:
        context = {'form': form}
    return render(request, 'portfolio/index.html', context)