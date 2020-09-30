from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('suns/<title>', views.suns),
    path('timestables/<brand>/<name>/<date>/<title>', views.get_times_tables),
]