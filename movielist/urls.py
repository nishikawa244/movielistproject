from django.urls import path
from . import views

urlpatterns = [
    path('movielist/',views.RecordListView.as_view(),name='movielist'),
    path('detail/<int:pk>/',views.RecordDetailView.as_view(),name='detail'),
    path('create/',views.RecordCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.RecordUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.RecordDeleteView.as_view(),name='delete'),
]