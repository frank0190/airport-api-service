from django.urls import path, include
from rest_framework import routers
from airport.views import AirplaneTypeViewSet, AirplaneViewSet, CrewViewSet, CountryViewSet

router = routers.DefaultRouter()

router.register("airplane_types", AirplaneTypeViewSet)
router.register("airplanes", AirplaneViewSet)
router.register("crews", CrewViewSet)
router.register("countries", CountryViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "airport"
