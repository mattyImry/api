from django.urls import path
from .views import AddressViews


urlpatterns = [
    path('address/', AddressViews.as_view()),
    path('address/<int:id>', AddressViews.as_view())
]
