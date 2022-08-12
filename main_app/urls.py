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
    path('readings/<int:reading_id>/add_bookmark', views.add_bookmark, name='add_bookmark'),
    path('readings/<int:reading_id>/assoc_badge/<int:badge_id>/', views.assoc_badge, name='assoc_badge'),
    path('readings/<int:reading_id>/unassoc_badge/<int:badge_id>/', views.unassoc_badge, name='unassoc_badge'),
    path('badges/', views.BadgeList.as_view(), name='badges_index'),
    path('badges/<int:pk>/', views.BadgeDetail.as_view(), name='badges_detail'),
    path('badges/create/', views.BadgeCreate.as_view(), name='badges_create'),
    path('badges/<int:pk>/update/', views.BadgeUpdate.as_view(), name='badges_update'),
    path('badges/<int:pk>/delete/', views.BadgeDelete.as_view(), name='badges_delete'),


]
