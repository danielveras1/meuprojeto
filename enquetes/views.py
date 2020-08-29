from django.shortcuts import render
from enquetes.models import Enquete

def bemvindo(request):
    return render(request, 'bemvindo.html')

def enquete(request, enquete_id):
    enquete = Enquete()
    if enquete_id == 1:
        enquete = Enquete("","Qual o seu nome?", '2020-08-29')
    elif enquete_id == 2:
        enquete = Enquete("","Qual a sua cidade?", '2020-08-29')
    elif enquete_id == 3:
        enquete = Enquete("","Data de nascimento: ", '2020-08-29')
    return render(request, 'enquete.html', { "enquete" : enquete})
