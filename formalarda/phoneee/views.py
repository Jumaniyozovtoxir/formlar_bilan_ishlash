from django.shortcuts import render
from .models import Telefon
from .forms import TelefonForm

# Create your views here.
def index(requests):
    if requests.GET:
        qidirtop= requests.GET.get('search')
        tel = Telefon.objects.all().filter(nomi=qidirtop)

    elif requests.POST:
        fomms = TelefonForm(requests.POST)
        fomms.save()
        tel = Telefon.objects.all()

    else:
        tel = Telefon.objects.all()

    ctx ={
        'tel':tel
    }

    return render(requests, 'index.html',ctx)

def add_phone(requests):
    ozgaruvchi=TelefonForm()
    if requests.POST:
        fomms=TelefonForm(requests.POST)
        fomms.save()
    ctx = {
        'ozgaruvchi':ozgaruvchi
    }

    return render(requests, 'add_phone.html', ctx)
