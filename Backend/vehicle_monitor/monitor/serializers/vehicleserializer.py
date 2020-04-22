from rest_framework import serializers
from vehicle_monitor.monitor.models import Vehicle

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['name','long', 'lat','created_at','updated_at']

