from django.shortcuts import render
from .models import Employes
# Create your views here.

def Dashboard(request):

    total_participantes = Employes.objects.filter(status='AC').count()
    participantes_con_votacion = Employes.objects.filter(votacion=True).count()
    promedio_votacion = participantes_con_votacion / total_participantes *100 if total_participantes > 0 else 0
    total_jubilados = Employes.objects.filter(status='JUB').count()
    participantes_jub_con_votacion = Employes.objects.filter(status='JUB', votacion=True).count()
    promedio_votacion_jubilados = participantes_jub_con_votacion / total_jubilados * 100 if  total_jubilados > 0 else 0

    total_hp = Employes.objects.filter(status='HP').count()
    participantes_HP_con_votacion = Employes.objects.filter(status='HP', votacion=True).count()
    promedio_votacion_hp = participantes_HP_con_votacion / total_hp * 100 if  total_hp> 0 else 0


    total_noparticipando = Employes.objects.filter(votacion=False).count()
    content = {
        'total_hp':total_hp,
        'total_participantes': total_participantes,
        'total_jubilados':total_jubilados,
        'participantes_con_votacion': participantes_con_votacion,
        'promedio_votacion_jubilados': promedio_votacion_jubilados,
        'promedio_votacion': promedio_votacion,
        'promedio_votacion_hp':promedio_votacion_hp,
        'total_noparticipando':total_noparticipando,
    }


    return render(request, 'dashboard.html', content)
