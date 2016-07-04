from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Perso, Profile, BasicWay, Race, RaceTrait

class IndexView(generic.ListView):
    template_name = 'cof/index.html'
    context_object_name = 'perso_list'

    def get_queryset(self):
        """
        Return perso's list in database
        """
        return Perso.objects.order_by('first_name')

class RacesView(generic.ListView):
    template_name = 'cof/races.html'
    context_object_name = 'races_list'

    def get_queryset(self):
        return Race.objects.order_by('race_name')

class RaceView(generic.DetailView):
    model = Race
    template_name = 'cof/race.html'

class ProfilesView(generic.ListView):
    template_name = 'cof/profiles.html'
    context_object_name = 'profiles_list'

    def get_queryset(self):
        return Profile.objects.order_by('profile_name')

class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'cof/profile.html'

class PersoView(generic.DetailView):
    model = Perso
    template_name = 'cof/perso.html'
