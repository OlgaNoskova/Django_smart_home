# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)

    def post(self, request):
        post_new = Sensor.objects.create(
            name=request.data['name'],
            description=request.data['description']
        )
        return Response({'post': model_to_dict(post_new)})



class SensorDetailView(APIView):
    def patch(self, request, a):
        sensor = get_object_or_404(Sensor, pk=a)
        sensor.description = request.data['description']
        sensor.save()
        return Response({'post': model_to_dict(sensor)})

    def get(self, request, a):
        sensor = get_object_or_404(Sensor, pk=a)
        ser = SensorDetailSerializer(sensor, many=True)
        return Response({'post': model_to_dict(ser)})


class MeasurementsView(APIView):
    def post(self, request):
        sensor = get_object_or_404(Sensor, pk=request.data['sensor'])
        post_new_temp = Measurement.objects.create(
            sensor=sensor,
            temperature=request.data['temperature']
        )
        return Response({'post': model_to_dict(post_new_temp)})



