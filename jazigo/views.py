#from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from jazigo.models import Jazigo, Sepultado, QuadraESepultura, Concessionario, TransferenciaDeOssada


class JazigoCreate(CreateView): 
    template_name = "novo_jazigo3.html"
    model = Jazigo
    fields = '__all__'
    sucess_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Jazigo Criado com Sucesso.")
        return super(JazigoCreate,self).form_valid(form)
    
class QuadraESepulturaCreate(CreateView):
    template_name = "novo_jazigo2.html"
    model = QuadraESepultura
    fields = '__all__'
    sucess_url = reverse_lazy('novo_jazigo')
    
    def get_success_url(self):
        return reverse('novo_jazigo')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Sepultura Criado com Sucesso.")
        return super(QuadraESepulturaCreate,self).form_valid(form)    
    
class ConcessionarioCreate(CreateView):
    template_name = "novo_jazigo2.html"
    model = Concessionario
    fields = '__all__'
    sucess_url = reverse_lazy('novo_jazigo')
    
    def get_success_url(self):
        return reverse('novo_jazigo')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Concessionario Criado com Sucesso.")
        return super(ConcessionarioCreate,self).form_valid(form)  
    
class SepultadoCreate(CreateView):
    template_name = "novo_jazigo2.html"
    model = Sepultado
    fields = '__all__'
    sucess_url = reverse_lazy('novo_jazigo')
    
    def get_success_url(self):
        return reverse('novo_jazigo')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Concessionario Criado com Sucesso.")
        return super(SepultadoCreate,self).form_valid(form)      

def index(request):
    jazigos = Jazigo.objects.order_by("identificacao_jazigo")
    sepultados_jazigo = Jazigo.objects.order_by("nome_sepultado")
    sepultados = list(sepultados_jazigo)
    return render(request, 'index.html', {"jazigos": jazigos, "sepultados": sepultados})
    #return HttpResponse("<h1>Página de Jazigo</h1>")

def jazigo(request, jazigo_id):
    #sepultados_jazigo = Sepultado.objects.filter(sepultado = Sepultado.nome_sepultado)
    jazigo = get_object_or_404(Jazigo, pk=jazigo_id)
    sepultados_jazigo = jazigo.nome_sepultado.all()
    return render(request, 'tumulo.html', {"jazigo": jazigo, "sepultados": sepultados_jazigo})



def novo_jazigo(request):

    if request.method == "POST":
        novo_jazigo = Jazigo(request.POST)
        
        novo_jazigo.identificacao_jazigo = QuadraESepultura.objects.get('identificacao_jazigo')
        novo_jazigo.capacidade_urnas = request.POST.get('capacidade_urnas')
        novo_jazigo.nome_concessionaro = request.POST.get('nome_concessionaro')
        novo_jazigo.jazigo_privado_publico = request.POST.get('jazigo_privado_publico')
        novo_jazigo.transferencia_ossada = request.POST.getget('transferencia_ossada')
        novo_jazigo.sepultado_local = request.POST.get('sepultado_local')
        novo_jazigo.sepultamento_externo = request.POST.get('sepultamento_externo')
        novo_jazigo.nome_sepultado = request.POST.getlist('nome_sepultado')
        novo_jazigo.observacao = request.POST.get('observacao')
        
        if novo_jazigo.is_valid():
            novo_jazigo.save()
        
    ossada = TransferenciaDeOssada.objects.all()
    concessionario = Concessionario.objects.all()
    quadra_sepultura = QuadraESepultura.objects.all()    
    sepultados_jazigo = Sepultado.objects.all()
    jazigos = Jazigo.objects.all()
    return render(request, 'novo_jazigo.html', {
        "jazigos": jazigos, 
        "sepultados": sepultados_jazigo, 
        "quadrasepulturas": quadra_sepultura, 
        "concessionarios": concessionario,
        "ossadas": ossada,
        })