from measurement.serializers import DetailedSerializer, MeasurementSerializer, UpdateSerializer, SensorSerializer
from .models import Sensor, Measurements
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class MeasurementsCreateViewSet(ListCreateAPIView):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()


class SensorListCreateViewSet(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        serializer = DetailedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()


class SensorDetailedViewSet(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    def get_serializer_class(self):
        if self.request.method =='PATCH':
            return UpdateSerializer
        return DetailedSerializer
    
