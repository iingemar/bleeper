from django.shortcuts import render, get_object_or_404

from .models import Bleep


def index_view(request):
    bleeps = Bleep.objects.all()
    context = {
        'bleeps': bleeps
    }
    return render(request, 'index_view.html', context)


def bleep_detail_view(request, bleep_id):
    print(bleep_id)
    bleep = get_object_or_404(Bleep, id=bleep_id)
    print(bleep)
    context = {
        'bleep': bleep
    }
    return render(request, 'bleep_detail_view.html', context)
