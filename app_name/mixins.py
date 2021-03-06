from django import forms
from django.forms.utils import ErrorList


class FormUserNeededMixin(object):
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User must be logged in.'])
            return self.form_invalid(form)


class UserOwnerMixin(FormUserNeededMixin, object):
    def form_valid(self, form):
        # Form is only valid if it's for the same user
        if form.instance.user == self.request.user:
            return super(UserOwnerMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['Not allowed.'])
            return self.form_invalid(form)


