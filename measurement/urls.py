from django.urls import path

from measurement.views import SensorView, MeasurementsView, SensorDetailView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:a>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]
