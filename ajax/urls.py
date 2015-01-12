from django.conf.urls import patterns, url
from ajax import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^configJunosInterfaces/$', views.configJunosInterfaces, name='configJunosInterfaces'),
    url(r'^preconfigJunosDomain/$', views.preconfigJunosDomain, name='preconfigJunosDomain'),
    url(r'^preconfigFirefly/$', views.preconfigFirefly, name='preconfigFirefly'),
    url(r'^getJunosConfig/$', views.getJunosConfig, name='getJunosConfig'),
    url(r'^getJunosStartupState/$', views.getJunosStartupState, name='getJunosStartupState'),
    url(r'^syncLinkData/$', views.syncLinkData, name='syncLinkData'),
    url(r'^refreshDeploymentStatus/$', views.refreshDeploymentStatus, name='refreshDeploymentStatus'),
    url(r'^refreshHypervisorStatus/$', views.refreshHypervisorStatus, name='refreshHypervisorStatus'),
    url(r'^deployTopology/$', views.deployTopology, name='deployTopology'),
    url(r'^manageDomain/$', views.manageDomain, name='manageDomain'),
    url(r'^manageNetwork/$', views.manageNetwork, name='manageNetwork'),
    url(r'^manageHypervisor/$', views.manageHypervisor, name='manageHypervisor'),
    url(r'^executeCli/$', views.executeCli, name='executeCli'),
    url(r'^pushConfigSet/$', views.pushConfigSet, name='pushConfigSet'),
    url(r'^deleteConfigSet/$', views.deleteConfigSet, name='deleteConfigSet'),
    url(r'^viewNetwork/(?P<network_name>[^/]+)$', views.viewNetwork, name='viewNetwork'),
    url(r'^viewDomain/(?P<domain_id>[^/]+)$', views.viewDomain, name='viewDomain'),
)