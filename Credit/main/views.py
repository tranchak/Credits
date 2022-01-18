from django.shortcuts import render


# Create your views here.
from .models import Bank


def get_home(request):
    banks=Bank.objects.all()
    contex={'banks':banks}

    return render(request, 'main/home.html',contex)


def get_bank(request):
    banks = Bank.objects.all()
    contex = {'banks': banks}
    return render(request, 'main/banks.html',contex)