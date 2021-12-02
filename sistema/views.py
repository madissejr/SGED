from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from sistema.forms import ArquivoForm, DocumentoForm, CaçifoForm, SecçãoForm

from sistema.models import Arquivo, Documento, Caçifo, Secção

from sged.decorators import usuariosAutorizados

# Create your views here.
@login_required
@usuariosAutorizados(allowed_roles=['gestor', 'admin'])
def SeçãoHome(request):
    secção = Secção.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(secção, 3)
    
    try:
        secções = paginator.page(page)
    except PageNotAnInteger:
        secções = paginator.page(1)
    except EmptyPage:
        secções = paginator.page(paginator.num_pages())

    context = {'secções': secções}
    return render(request, 'seccao/home.html', context)

@login_required
@usuariosAutorizados(allowed_roles=['gestor', 'admin'])
def SeçãoCadastrar(request):
    form = SecçãoForm()
    if request.method == 'POST':
        form = SecçãoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            return redirect('sistema:home')
    context = {'form': form}
    return render(request, 'seccao/registar.html', context)

@login_required
@usuariosAutorizados(allowed_roles=['gestor', 'admin'])
def SeçãoAtualizar(request, pk):
    secção = Secção.objects.get(id=pk)

    context = {}
    form = SecçãoForm(instance=secção)
    if request.method == 'POST':
        form = SecçãoForm(request.POST, instance=secção)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.modificador = request.user.username
            obj.save()

            return redirect('sistema:home')
    
    context['form'] = form

    return render(request, 'seccao/registar.html', context)

@login_required
@usuariosAutorizados(allowed_roles=['gestor', 'admin'])
def SeçãoRemover(request, pk):
    secção = Secção.objects.get(id=pk)

    if request.method == 'POST':
        secção.delete()
        return redirect('sistema:home')
    
    context = {'secção': secção}
    return render(request, 'seccao/delete.html', context)

@login_required
@usuariosAutorizados(allowed_roles=['gestor', 'admin'])
def SecçãoDetail(request, pk):
    secção = Secção.objects.get(id=pk)
    caçifo = Caçifo.objects.filter(secção = secção)

    page = request.GET.get('page', 1)
    paginator = Paginator(caçifo, 4)
    
    try:
        caçifos = paginator.page(page)
    except PageNotAnInteger:
        caçifos = paginator.page(1)
    except EmptyPage:
        caçifos = paginator.page(paginator.num_pages())

    context = {
        'secção':secção,
        'caçifos':caçifos
    }

    return render(request, 'seccao/seccao-details.html', context)

# Caçifo views
@login_required
@usuariosAutorizados(allowed_roles=['gestor', 'admin'])
def CaçifoHome(request):
    caçifo = Caçifo.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(caçifo, 5)
    
    try:
        caçifos = paginator.page(page)
    except PageNotAnInteger:
        caçifos = paginator.page(1)
    except EmptyPage:
        caçifos = paginator.page(paginator.num_pages())

    context = {'caçifos': caçifos}
    return render(request, 'caçifo/home.html', context)

@login_required
@usuariosAutorizados(allowed_roles=['gestor', 'admin'])
def CaçifoCadastrar(request):
    form = CaçifoForm()
    
    if request.method == 'POST':
        form = CaçifoForm(request.POST)
        secção = Secção.objects.get(id=int(form.data['secção']))
        caçifo = Caçifo.objects.all().filter(secção = secção).__len__()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            if not Caçifo.objects.filter(secção = secção).exists():
                obj.codename = f'{secção.codename}{caçifo + 1}'
            else:
                obj.codename = f'{secção.codename}{Caçifo.objects.filter(secção=secção).last().__getattribute__("id")}'
            obj.save()
            return redirect('sistema:caçifo')
    context = {'form': form}
    return render(request, 'caçifo/registar.html', context)

@login_required
@usuariosAutorizados(allowed_roles=['gestor', 'admin'])
def CaçifoAtualizar(request, pk):
    caçifo = Caçifo.objects.get(id=pk)

    context = {}
    form = CaçifoForm(instance=caçifo)
    if request.method == 'POST':
        form = CaçifoForm(request.POST, instance=caçifo)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.modificador = request.user.username
            obj.save()
            return redirect('sistema:caçifo')
    
    context['form'] = form

    return render(request, 'caçifo/registar.html', context)

@login_required
@usuariosAutorizados(allowed_roles=['gestor', 'admin'])
def CaçifoRemover(request, pk):
    caçifo = Caçifo.objects.get(id=pk)

    if request.method == 'POST':
        caçifo.delete()
        return redirect('sistema:caçifo')
    
    context = {'caçifo': caçifo}
    return render(request, 'caçifo/delete.html', context)

@login_required
@usuariosAutorizados(allowed_roles=['gestor', 'admin'])
def CaçifoDetail(request, pk):
    caçifo = Caçifo.objects.get(id=pk)
    arquivo = Arquivo.objects.filter(caçifo = caçifo)

    page = request.GET.get('page', 1)
    paginator = Paginator(arquivo, 4)
    
    try:
        arquivos = paginator.page(page)
    except PageNotAnInteger:
        arquivos = paginator.page(1)
    except EmptyPage:
        arquivos = paginator.page(paginator.num_pages())

    context = {
        'caçifo':caçifo,
        'arquivos':arquivos
    }

    return render(request, 'caçifo/caçifo-detail.html', context)

# Arquivo Views
@login_required
def ArquivoHome(request):
    arquivo = Arquivo.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(arquivo, 5)
    
    try:
        arquivos = paginator.page(page)
    except PageNotAnInteger:
        arquivos = paginator.page(1)
    except EmptyPage:
        arquivos = paginator.page(paginator.num_pages())

    context = {'arquivos': arquivos}
    return render(request, 'arquivo/home.html', context)

@login_required
def ArquivoCadastrar(request):
    form = ArquivoForm()
    if request.method == 'POST':
        form = ArquivoForm(request.POST)
        caçifo = Caçifo.objects.get(id=int(form.data['caçifo']))
        arquivo = Arquivo.objects.all().filter(caçifo = caçifo).__len__()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            if not Arquivo.objects.filter(caçifo = caçifo).exists():
                obj.codename = f'{caçifo.codename}-{arquivo + 1}'
            else:
                arquivo = Arquivo.objects.filter(caçifo = caçifo).last().__getattribute__('id')
                obj.codename = f'{caçifo.codename}-{arquivo + 1}'
            obj.save()
            return redirect('sistema:arquivos')
    context = {'form': form}
    return render(request, 'arquivo/registar.html', context)

@login_required
def ArquivoAtualizar(request, pk):
    arquivo = Arquivo.objects.get(id=pk)

    context = {}
    form = ArquivoForm(instance=arquivo)
    if request.method == 'POST':
        form = ArquivoForm(request.POST, instance=arquivo)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.modificador = request.user.username
            obj.save()
            return redirect('sistema:arquivos')
        
    context['form'] = form

    return render(request, 'arquivo/registar.html', context)

@login_required
def ArquivoRemover(request, pk):
    arquivo = Arquivo.objects.get(id=pk)

    if request.method == 'POST':
        arquivo.delete()
        return redirect('sistema:arquivos')
    context = {'arquivo': arquivo}
    return render(request, 'arquivo/delete.html', context)

# Doc views
@login_required
def DocHome(request, codename):
    ar = Arquivo.objects.get(codename=codename)
    doc = Documento.objects.all().filter(arquivo = ar)
    
    page = request.GET.get('page', 1)
    paginator = Paginator(doc, 5)
    
    try:
        docs = paginator.page(page)
    except PageNotAnInteger:
        docs = paginator.page(1)
    except EmptyPage:
        docs = paginator.page(paginator.num_pages())

    context = {'docs': docs, 'arquivo': ar}
    return render(request, 'doc/home.html', context)

@login_required
def DocCadastrar(request, pk):
    arquivo = Arquivo.objects.get(id=pk)
    if request.method == 'GET':
        form = DocumentoForm(request.GET or None)
       
        data = {
            'arquivo': arquivo
        }
        form = DocumentoForm(initial=data)
    elif request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            return redirect('sistema:docs', arquivo.codename)
    else:
        form = DocumentoForm()
    context = {'form': form}
    return render(request, 'doc/registar.html', context)

@login_required
def DocAtualizar(request, pk):
    doc = Documento.objects.get(id=pk)

    context = {}
    form = DocumentoForm(instance=doc)
    if request.method == 'POST':
        form = DocumentoForm(request.POST, instance=doc)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.modificador = request.user.username
            obj.save()
            return redirect('sistema:docs', doc.arquivo.codename)
        
    context['form'] = form

    return render(request, 'arquivo/registar.html', context)

@login_required
def DocRemover(request, pk):
    documento = Documento.objects.get(id=pk)

    if request.method == 'POST':
        documento.delete()
        return redirect('sistema:docs', documento.arquivo.codename)
    context = {'documento': documento}
    return render(request, 'doc/delete.html', context)