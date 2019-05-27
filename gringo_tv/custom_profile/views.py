from gringo_tv.core import views

from gringo_tv.custom_profile import models, forms


class ProfileListView(views.BaseListView):

    model = models.Profile
    template_name = 'profile/list.html'


class ProfileCreateView(views.BaseCreateView):

    model = models.Profile
    form_class = forms.ProfileForm
    template_name = 'profile/list.html'


class ProfileUpdateView(views.BaseUpdateView):

    model = models.Profile
    template_name = 'profile/list.html'


class ProfileDeleteView(views.BaseDeleteView):

    model = models.Profile
    template_name = 'profile/list.html'
