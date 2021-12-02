from django.urls import path


from sistema.views import ArquivoAtualizar, ArquivoCadastrar, ArquivoHome, ArquivoRemover, DocAtualizar, DocCadastrar, DocHome, DocRemover, CaçifoAtualizar, CaçifoCadastrar, CaçifoDetail, CaçifoHome, CaçifoRemover, SecçãoDetail, SeçãoAtualizar, SeçãoCadastrar, SeçãoHome, SeçãoRemover

app_name = 'sistema'
urlpatterns = [
    #Seccoes
    path('', SeçãoHome, name='home'),
    path('registar-seção/', SeçãoCadastrar, name='registar'),
    path('atualizar-secção/<str:pk>/', SeçãoAtualizar, name='atualizar-secção'),
    path('delete-secção/<str:pk>/', SeçãoRemover, name='delete-secção'),
    path('secção/<str:pk>/', SecçãoDetail, name='secção'),


    #Caçifos
    path('home-caçifo/', CaçifoHome, name='caçifo'),
    path('registar-caçifo', CaçifoCadastrar, name='registar-caçifo'),
    path('atualizar-caçifo/<str:pk>/', CaçifoAtualizar, name='atualizar-caçifo'),
    path('delete-caçifo/<str:pk>/', CaçifoRemover, name='delete-caçifo'),
    path('caçifo/<str:pk>/', CaçifoDetail, name='caçifo-detail'),

    #Arquivos
    path('home-arquivo/', ArquivoHome, name='arquivos'),
    path('registar-arquivo', ArquivoCadastrar, name='registar-arquivo'),
    path('atualizar-arquivo/<str:pk>/', ArquivoAtualizar, name='atualizar-arquivo'),
    path('delete-arquivo/<str:pk>/', ArquivoRemover, name='delete-arquivo'),

    #Docs
    path('home-docs/<codename>/', DocHome, name='docs'),
    path('registar-doc/<str:pk>/', DocCadastrar, name='registar-doc'),
    path('atualizar-doc/<str:pk>/', DocAtualizar, name='atualizar-doc'),
    path('delete-doc/<str:pk>/', DocRemover, name='delete-doc'),
]
