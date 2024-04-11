from django.shortcuts import render
from django.db.models import Avg
from .models import Comment

def avis(request):
    # Récupérer les commentaires positifs et négatifs
    avis_positifs = Comment.objects.filter(label=True)[:5]
    avis_negatifs = Comment.objects.filter(label=False)[:5]

    # Calculer la moyenne des étoiles obtenues pour les avis positifs
    moyenne_etoiles = Comment.objects.filter(label=True).exclude(note__isnull=True).aggregate(moyenne=Avg('note'))

    # Calculer le pourcentage de commentaires positifs
    total_avis = Comment.objects.count()
    total_avis_positifs = Comment.objects.filter(label=True).count()
    pourcentage_positif = (total_avis_positifs / total_avis) * 100 if total_avis > 0 else 0

    context = {
        'avis_positifs': avis_positifs,
        'avis_negatifs': avis_negatifs,
        'moyenne_etoiles': moyenne_etoiles['moyenne'],
        'pourcentage_positif': pourcentage_positif,
    }
    return render(request, 'comments/avis.html', context)

def avis_positifs(request):
    avis_positifs = Comment.objects.filter(label=True)
    context = {
        'avis_positifs': avis_positifs,
    }
    return render(request, 'comments/avis_positifs.html', context)

def avis_negatifs(request):
    avis_negatifs = Comment.objects.filter(label=False)
    context = {
        'avis_negatifs': avis_negatifs,
    }
    return render(request, 'comments/avis_negatifs.html', context)


