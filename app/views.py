from django.shortcuts import render,HttpResponse

# Create your views here.
def test_page(request):
    return HttpResponse ("test ok")


def accueil(request):
    context = {
        'titre': 'Bienvenue sur mon site',
        'utilisateur': 'Abd',
        'technos': ['Django', 'Linux', 'Nextcloud']
    }
    return render(request, 'index.html', context)