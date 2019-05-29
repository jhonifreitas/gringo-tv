from django.urls import reverse_lazy

from gringo_tv.core import views
from gringo_tv.custom_profile import models, forms


class ProfileListView(views.BaseListView):

    model = models.Profile
    template_name = 'profile/list.html'


class ProfileCreateView(views.BaseCreateView):

    model = models.Profile
    form_class = forms.ProfileForm
    template_name = 'profile/form.html'
    success_url = reverse_lazy('profile:list')
    success_message = 'Usuário cadastrado!'


class ProfileUpdateView(views.BaseUpdateView):

    model = models.Profile
    form_class = forms.ProfileForm
    template_name = 'profile/form.html'
    success_url = reverse_lazy('profile:list')
    success_message = 'Usuário salvo!'

    def get_form(self):
        form = super().get_form()
        form.fields['password'].required = False
        form.fields['password1'].required = False
        form.fields['first_name'].initial = form.instance.user.first_name
        form.fields['last_name'].initial = form.instance.user.last_name
        form.fields['username'].initial = form.instance.user.username
        return form


class ProfileDeleteView(views.BaseDeleteView):

    model = models.Profile
    template_name = 'profile/list.html'
    success_url = reverse_lazy('profile:list')
    success_message = 'Usuário deletado!'


# #####################################################################################################################
# INDICATION
# #####################################################################################################################
class IndicationListView(views.BaseListView):

    model = models.Indication
    template_name = 'indication/list.html'


class IndicationCreateView(views.BaseCreateView):

    model = models.Indication
    form_class = forms.IndicationForm
    template_name = 'indication/form.html'
    success_url = reverse_lazy('indication:list')
    success_message = 'Usuário cadastrado!'

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class IndicationUpdateView(views.BaseUpdateView):

    model = models.Indication
    form_class = forms.IndicationForm
    template_name = 'indication/form.html'
    success_url = reverse_lazy('indication:list')
    success_message = 'Usuário salvo!'


class IndicationDeleteView(views.BaseDeleteView):

    model = models.Indication
    success_url = reverse_lazy('indication:list')
    success_message = 'Usuário deletado!'
