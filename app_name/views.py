from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from .forms import BleepModelForm
from .models import Bleep


class BleepCreateView(CreateView):
    form_class = BleepModelForm
    template_name = 'bleep_create_view.html'
    success_url = '/bleeps/create'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.user = self.request.user
        return super(BleepCreateView, self).form_valid(form)


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
