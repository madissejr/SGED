from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from sistema.models import Documento

@login_required
def main(request):
    docs = Documento.objects.all().__len__()
    arquivo = Documento.objects.all().__len__()
    doc = Documento.objects.all().order_by('-id')
    
    page = request.GET.get('page', 1)
    paginator = Paginator(doc, 3)
    
    try:
        docss = paginator.page(page)
    except PageNotAnInteger:
        docss = paginator.page(1)
    except EmptyPage:
        docss = paginator.page(paginator.num_pages())

    context = {'docs': docs, 'arquivos': arquivo, 'docss': docss}
    return render(request, 'home.html', context)