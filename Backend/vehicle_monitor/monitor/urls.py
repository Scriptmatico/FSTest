from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from vehicle_monitor.monitor.views.user_view import UserRequestToken, UserView, UserAuthenticated
from vehicle_monitor.monitor.views.vehicles_view import VehicleListView,VehicleDestroyView,VehicleUpdateView,VehicleDetailsView, VehicleCreateView
from django.conf.urls import url

urlpatterns = [
    path('login', UserRequestToken.as_view()),
    path('me', UserAuthenticated.as_view()),
    path('users', UserView.as_view({'get': 'retrieve'})),
    path('vehicles', VehicleListView.as_view()),
    url(r'^vehicle', VehicleCreateView.as_view()),
    url(r'^vehicle/(?P<pk>\d+)/delete$', VehicleDestroyView.as_view()),
    url(r'^vehicle/(?P<pk>\d+)/update$', VehicleUpdateView.as_view()),
    url(r'^vehicle/(?P<pk>\d+)$', VehicleDetailsView.as_view()),
]
