from django.shortcuts import render, get_object_or_404, redirect
from .models import Animaux, ZoneCoeur
from .forms import AnimauxForm, ZoneForm


def animaux_liste(request):
    animal=Animaux.objects.all()
    return render(request, 'AnimauxZone/Animaux_liste.html', {'animaux': animal})


def animaux_detail(request, pk):
    animal = get_object_or_404(Animaux, pk=pk)
    return render(request, 'AnimauxZone/Animaux_detail.html', {"animal": animal})


def zone_coeur_liste(request):
    zone_coeur=ZoneCoeur.objects.all()
    return render(request, 'AnimauxZone/ZoneCoeur_liste.html', {'ZoneCoeur': zone_coeur})


def zone_coeur_detail(request, pk):
    zonecoeur= get_object_or_404(ZoneCoeur, pk=pk)
    return render(request, 'AnimauxZone/ZoneCoeur_liste.html', {"ZoneCoeur": zonecoeur})


def home_view(request):
    return render(request, 'AnimauxZone/home.html')


def nouveau_animaux(request):
    form=AnimauxForm(request.POST or None)
    if form.is_valid():
        form.save()
        message="l'animal est enregistré avec succées!"
        form = AnimauxForm()
    else:
        form = AnimauxForm()
        message = ""
    return render(request, 'AnimauxZone/Animaux_new.html', {'form':form, 'messages':message},)


def zone_nouveau(request):
    form=ZoneForm(request.POST or None)
    if form.is_valid():
        form.save()
        message="Zone coeur est enregistré avec succées!"
        form = ZoneForm()
    else:
        form = ZoneForm()
        message = ""
    return render(request, 'AnimauxZone/zone_new.html', {'form':form, 'messages':message},)


def enregistrement_view(request):
    return render(request,'AnimauxZone/enregistrement.html',)


def delete_animal(request, pk):
    animal=Animaux.objects.get(pk=pk)
    animal.delete()
    return redirect("/")


def edit_animal(request, pk):
    animal = Animaux.objects.get(pk=pk)
    form = AnimauxForm(request.POST,instance=animal)
    if form.is_valid():
        form.save()
        message = "l'animal est enregistré avec succées!"
        return redirect("/")
    else:
        form = AnimauxForm(instance=animal)
        message = ""
    return render(request, 'AnimauxZone/Animaux_new.html', {'form': form, 'messages': message}, )


def delete_zone(request, pk):
    zone=ZoneCoeur.objects.get(pk=pk)
    zone.delete()
    return redirect("/Zonecoeur/")


def edit_zone(request, pk):
    zone = ZoneCoeur.objects.get(pk=pk)
    form = ZoneForm(request.POST, instance=zone)
    if form.is_valid():
        form.save()
        message = "Zone coeur est enregistré avec succées!"
        form = ZoneForm(instance=zone)
        return redirect("/Zonecoeur/")
    else:
        form = ZoneForm(instance=zone)
        message = ""
    return render(request, 'AnimauxZone/zone_new.html', {'form': form, 'messages': message}, )