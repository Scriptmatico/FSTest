from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from vehicle_monitor.monitor.models import Vehicle
from vehicle_monitor.monitor.serializers.vehicleserializer import VehicleSerializer
from vehicle_monitor.monitor.serializers.responseserializer import JSONResponse
from rest_framework.generics import DestroyAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView

# get vehicles
class VehicleListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        vehicles = Vehicle.objects.filter(user=request.user)
        serializer= VehicleSerializer(data=vehicles, many = True)
        serializer.is_valid()
        #return Response(serializer.data)
        return JSONResponse(serializer.data)

class VehicleDestroyView(DestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the vehicles
        for the currently authenticated user.
        """
        user = self.request.user
        return Vehicle.objects.filter(user=user)

class VehicleUpdateView(UpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the vehicles
        for the currently authenticated user.
        """
        user = self.request.user
        return Vehicle.objects.filter(user=user)

class VehicleDetailsView(RetrieveAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the vehicles
        for the currently authenticated user.
        """
        user = self.request.user
        return Vehicle.objects.filter(user=user)

class VehicleCreateView(CreateAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)