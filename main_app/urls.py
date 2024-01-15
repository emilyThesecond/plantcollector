from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
    path('plants/<int:plant_id>/add_watering/', views.add_watering, name='add_watering'),
    path('watering/<int:pk>/delete/', views.WateringDelete.as_view(), name='watering_delete'),
    path('soils/', views.SoilList.as_view(), name='soils_index'),
    path('soils/<int:pk>/', views.SoilDetail.as_view(), name='soils_detail'),
    path('soils/create/', views.SoilCreate.as_view(), name='soils_create'),
    path('soils/<int:pk>/update/', views.SoilUpdate.as_view(), name='soils_update'),
    path('soils/<int:pk>/delete/', views.SoilDelete.as_view(), name='soils_delete'),
    path('cats/<int:plant_id>/assoc_soil/<int:soil_id>/', views.assoc_soil, name='assoc_soil'),
    path('cats/<int:plant_id>/remove_soil/<int:soil_id>/', views.remove_soil, name='remove_soil'),
]