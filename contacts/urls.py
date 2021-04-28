from django.urls import path
from . import views
app_name = 'contacts'
urlpatterns = [
    path('', views.ContactList.as_view(), name='list'),
    path('<int:pk>/', views.ContactDetail.as_view(), name='detail'),
    path('create', views.ContactCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.ContactUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.ContactDelete.as_view(), name='delete'),
]