from rest_framework import generics
from .models import Produto
from .serializers import ProdutoSerializer


################################# API VERSAO 1 ###########################################################################
##########################################################################################################################

class CursosAPIView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
   # queryset = Curso.objects.raw('SELECT * FROM cursos_Curso')
    serializer_class = ProdutoSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
   # queryset = Curso.objects.raw('SELECT * FROM cursos_Curso')
    serializer_class = ProdutoSerializer
