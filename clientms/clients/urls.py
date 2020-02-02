from django.urls import path

from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    ClientAddCommentView,
)

urlpatterns = [

    path('<int:pk>/edit/', ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('new/', ClientCreateView.as_view(), name='client_new'),

    path('<int:pk>/add_comment/', ClientAddCommentView.as_view(), name='client_add_comment'),

    path('', ClientListView.as_view(), name='client_list'),

]
