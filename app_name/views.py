from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import BleepModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Bleep


class BleepUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    form_class = BleepModelForm
    success_url = '/bleeps/'
    queryset = Bleep.objects.all()
    template_name = 'bleep/bleep_update_view.html'


class BleepCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = BleepModelForm
    template_name = 'bleep/bleep_create_view.html'
    success_url = '/bleeps/create/'
    # Needed for LoginRequiredMixin. Otherwise defaults to /accounts/login
    login_url = '/admin/'


class BleepDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Bleep.objects.all()
    success_url = reverse_lazy('home')
    template_name = 'bleep/bleep_confirm_delete.html'


def bleep_create_view(request):
    # Populate form
    form = BleepModelForm(request.POST or None)

    if form.is_valid():
        # Create a database object from the data bound to the form
        instance = form.save(commit=False)
        # Set the user from the request
        instance.user = request.user
        # Then save.
        instance.save()

    context = {
        'form': form
    }

    return render(request, 'bleep/bleep_create_view.html', context)


def index_view(request):
    bleeps = Bleep.objects.all()
    context = {
        'bleeps': bleeps
    }
    return render(request, 'bleep/index_view.html', context)


def bleep_detail_view(request, bleep_id):
    print(bleep_id)
    bleep = get_object_or_404(Bleep, id=bleep_id)
    print(bleep)
    context = {
        'bleep': bleep
    }
    return render(request, 'bleep/bleep_detail_view.html', context)
