from rest_framework.test import APITestCase,APIRequestFactory
from django.contrib.auth.models import User
from faker import Faker
from faker.providers import geo
from vehicle_monitor.monitor.models import Vehicle
from rest_framework.test import force_authenticate
from vehicle_monitor.monitor.views.vehicles_view import VehicleListView, VehicleDetailsView, VehicleDestroyView
from vehicle_monitor.monitor.views.vehicles_view import VehicleCreateView, VehicleUpdateView
from vehicle_monitor.monitor.serializers.vehicleserializer import VehicleSerializer

import json

# Create your tests here.
class LoginAuthTests(APITestCase):
    def test_i_can_not_login(self):
        # try login without data
        response = self.client.post(f'/api/login')
        self.assertEqual(response.status_code, 400)

        # prepare some dummy data and try login
        data = {'username':'ismael','password':'123456'}
        response = self.client.post(f'/api/login', data=data)
        self.assertEqual(response.status_code, 400)

    def test_user_can_login(self):
        #create user before test
        user = User.objects.create_user(username='ismael',password='123456', email="exodo999@gmail.com")
        data = {'username':'ismael','password':'123456'}
        
        #Response is success
        response = self.client.post(f'/api/login', data=data)
        self.assertEqual(response.status_code, 200)
        
        #User id matchs
        self.assertEqual(user.id, response.data['user_id'])


class VehicleObjectCRUDTest(APITestCase):
    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(geo)
        self.user = User.objects.create_user(username='myuser',password='123456', email="me@gmail.com")
        self.factory = factory = APIRequestFactory()

    def test_vehicle_object_creation(self):
        local_geo = self.fake.local_latlng()
        vehicle = Vehicle.objects.create(name="Vehicle 1", long=local_geo[0], lat=local_geo[1], user = self.user)
        
        self.assertIsNotNone(vehicle)
        self.assertEqual(self.user, vehicle.user)

    def test_error_get_auth_vehicles(self):
        response = self.client.post(f'/api/vehicle')
        self.assertEqual(response.status_code, 401)

    def test_get_vehicles_with_auth_user(self):
        view = VehicleListView.as_view()
        
        ##
        fake = Faker()
        fake.add_provider(geo)
        for i in range(5):
            local_geo = self.fake.local_latlng()
            Vehicle.objects.create(name="Vehicle "+str(i), long=local_geo[0], lat=local_geo[1], user = self.user)
        # Make an authenticated request to the view...
        request = self.factory.get('/api/vehicles')
        force_authenticate(request, user=self.user)
        response = view(request)
        
        self.assertEqual(len(json.loads(response.content)), 5)


    def test_can_get_vehicle_details(self):
        view = VehicleDetailsView.as_view()
        vehicle = Vehicle.objects.create(name='My awesome vehicle', lat=1, long=1, user=self.user)
        request = self.factory.get(f'/api/vehicle/{vehicle.id}')
        force_authenticate(request, user=self.user)
        response = view(request, pk=vehicle.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, VehicleSerializer(instance=vehicle).data)


    def test_can_delete_vehicle(self):
        view = VehicleDestroyView.as_view()
        vehicle = Vehicle.objects.create(name='My awesome vehicle', lat=1, long=1, user=self.user)
        request = self.factory.delete(f'/api/vehicle/{vehicle.id}/delete')
        force_authenticate(request, user=self.user)
        response = view(request, pk=vehicle.id)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Vehicle.objects.count(), 0)

    def test_can_update_vehicle(self):
        view = VehicleUpdateView.as_view()
        vehicle = Vehicle.objects.create(name='My awesome vehicle', lat=1, long=1, user=self.user)
        request = self.factory.patch(f'/api/vehicle/{vehicle.id}/update', data={'name': 'My other vehicle'})
        force_authenticate(request, user=self.user)
        response = view(request, pk=vehicle.id)

        vehicle.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(vehicle.name, 'My other vehicle')

    
    def test_can_create_vehicle(self):
        view = VehicleCreateView.as_view()
        data = {'name':'My New Vehicle', 'lat':'1.000000', 'long':'1.000000'}
        request = self.factory.post(f'/api/vehicle',data=data)
        force_authenticate(request,user=self.user)
        response = view(request)
        
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['lat'], data['lat'])
        self.assertEqual(response.data['long'], data['long'])