from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('readings/', views.readings_index, name='index'),
    path('readings/<int:reading_id>/', views.readings_detail, name='detail' ),
    path('readings/create/', views.ReadingCreate.as_view(), name='readings_create'), 
    path('readings/<int:pk>/update/', views.ReadingUpdate.as_view(), name='readings_update'),
    path('readings/<int:pk>/delete/', views.ReadingDelete.as_view(), name='readings_delete'),

]
