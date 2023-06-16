from django.urls import path
from jazigo.views import JazigoCreate, index, jazigo, novo_jazigo, QuadraESepulturaCreate, ConcessionarioCreate, SepultadoCreate
from . import views

urlpatterns = [
    path('', index, name="home"),
    path('jazigo/<int:jazigo_id>', jazigo, name='jazigo'),
    path('novojazigo/', views.JazigoCreate.as_view(), name="novo_jazigo"),
    path('novasepultura/', views.QuadraESepulturaCreate.as_view(), name="nova_sepultura"),
    path('novoconcessionario/', views.ConcessionarioCreate.as_view(), name="novo_concessionario"),
    path('novosepultado/', views.SepultadoCreate.as_view(), name="novo_sepultado"),
    #path('novojazigo', novo_jazigo, name="novo_jazigo")
    
    #path('jazigo/<int:jazigo_id>', JazigoDetailView.as_view()),
]