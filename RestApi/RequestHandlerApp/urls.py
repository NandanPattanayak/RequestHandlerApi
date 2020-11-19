from django.urls import path
from .import views
from rest_framework_jwt.views import obtain_jwt_token ,refresh_jwt_token
urlpatterns = [

      path('',views.HomeView),
      path('aimaps_data/',views.AimapsView),
      path('data/',views.FetchDataView),
]