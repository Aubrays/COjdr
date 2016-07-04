from django.conf.urls import url

from . import views

app_name = 'cof'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name ='index'),
    url(r'^perso/(?P<slug>[\w-]+)', views.PersoView.as_view(), name = 'perso'),
    url(r'^races/$', views.RacesView.as_view(), name ='races'),
    url(r'^races/(?P<slug>[\w-]+)', views.RaceView.as_view(), name = 'race'),
    url(r'^profiles/$', views.ProfilesView.as_view(), name ='profiles'),
    url(r'^profiles/(?P<slug>[\w-]+)', views.ProfileView.as_view(), name = 'profile'),
]
