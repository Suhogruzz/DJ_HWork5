from django.urls import path

from measurement.views import MeasurementsCreateViewSet, SensorDetailedViewSet, SensorListCreateViewSet


urlpatterns = [
    path('sensors/', SensorListCreateViewSet.as_view()),
    path('sensors/<pk>/', SensorDetailedViewSet.as_view()),
    path('measurements/', MeasurementsCreateViewSet.as_view()),
]
