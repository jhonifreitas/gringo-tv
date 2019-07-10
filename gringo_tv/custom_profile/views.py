from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from gringo_tv.core import views
from gringo_tv.custom_profile import models, forms


class ProfileListView(views.BaseListView):

    paginate_by = 10
    model = models.Profile
    template_name = 'profile/list.html'
    permission_required = ['custom_profile.list_profile']

    def get_queryset(self):
        object_list = super().get_queryset()
        text_filter = self.request.GET.get('q')
        if hasattr(self.request.user, 'dealer'):
            object_list = object_list.filter(dealer=self.request.user.dealer)
        if text_filter:
            object_list = object_list.filter(
                Q(user__username__icontains=text_filter) |
                Q(user__first_name__icontains=text_filter) |
                Q(user__last_name__icontains=text_filter))
        return object_list


class ProfileCreateView(views.BaseCreateView):

    model = models.Profile
    form_class = forms.ProfileForm
    template_name = 'profile/form.html'
    success_url = reverse_lazy('profile:list')
    success_message = 'Usuário cadastrado!'
    permission_required = ['custom_profile.add_profile']

    def form_valid(self, form):
        if hasattr(self.request.user, 'dealer'):
            form.instance.dealer = self.request.user.dealer
        return super().form_valid(form)


class ProfileUpdateView(views.BaseUpdateView):

    model = models.Profile
    form_class = forms.ProfileForm
    template_name = 'profile/form.html'
    success_url = reverse_lazy('profile:list')
    success_message = 'Usuário salvo!'
    permission_required = ['custom_profile.update_profile']

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
    permission_required = ['custom_profile.delete_profile']


class ProfilePointsView(views.BaseView):

    def post(self, request, pk):
        profile = get_object_or_404(models.Profile.objects.all(), pk=pk)
        if request.GET.get('plus'):
            profile.points += 1
        elif request.GET.get('minus'):
            profile.points -= 1
        profile.save()
        messages.success(request, 'Pontos do usuário registrados com sucesso!')
        return redirect(reverse_lazy('profile:list'))


# #####################################################################################################################
# INDICATION
# #####################################################################################################################
class IndicationListView(views.BaseListView):

    paginate_by = 10
    model = models.Indication
    template_name = 'indication/list.html'

    def get_queryset(self):
        object_list = super().get_queryset()
        if self.request.GET.get('profile'):
            object_list = object_list.filter(profile__uuid=self.request.GET.get('profile'))
        else:
            if hasattr(self.request.user, 'profile'):
                object_list = object_list.filter(profile=self.request.user.profile)
            elif hasattr(self.request.user, 'dealer'):
                object_list = object_list.filter(profile__dealer=self.request.user.dealer)
        return object_list


class IndicationCreateView(views.BaseCreateView):

    model = models.Indication
    form_class = forms.IndicationForm
    template_name = 'indication/form.html'
    success_url = reverse_lazy('indication:list')
    success_message = 'Indicação cadastrada!'

    def form_valid(self, form):
        if hasattr(self.request.user, 'profile'):
            form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class IndicationUpdateView(views.BaseUpdateView):

    model = models.Indication
    form_class = forms.IndicationForm
    template_name = 'indication/form.html'
    success_url = reverse_lazy('indication:list')
    success_message = 'Indicação salva!'


class IndicationStatusView(views.BaseView):

    model = models.Indication
    success_url = reverse_lazy('indication:list')
    success_message = 'Status alterado!'

    def post(self, request, pk):
        obj = get_object_or_404(self.model.objects.all(), pk=pk)
        obj.status = request.GET.get('status')
        obj.save()
        messages.success(request, self.success_message)
        return redirect(self.success_url)


class IndicationDeleteView(views.BaseDeleteView):

    model = models.Indication
    success_url = reverse_lazy('indication:list')
    success_message = 'Indicação deletada!'
