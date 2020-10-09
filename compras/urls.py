from django.urls import path
from compras.views import CursosAPIView, CursoAPIView

urlpatterns = [
    path('produtos/', CursosAPIView.as_view(), name='produtos'),
    path('produto/<int:pk>/', CursoAPIView.as_view(), name='produto'),
 ]
