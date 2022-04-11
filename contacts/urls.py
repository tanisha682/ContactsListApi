from django.urls import path
from .views import ContactList, ContactDetailView


urlpatterns = [
    path('list/', ContactList.as_view()),
    path('detail/<int:id>', ContactDetailView.as_view()),
]