from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'farmacia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #productos
    url(r'^', include('apps.medicamentos.urls', namespace="medicamentos_app")),

    #agregar ventas.
    url(r'^ventas/', include('apps.ventas.urls', namespace="ventas_app")),

    #login-users
    url(r'^', include('apps.users.urls',  namespace='users_app')),

    #CLientes
    url(r'^', include('apps.clientes.urls',  namespace='clientes_app')),


 #Distribuidores
    url(r'^', include('apps.distribuidor.urls',  namespace='distribuidores_app')),

        #compras
    url(r'^', include('apps.compras.urls',  namespace='compras_app')),
       #compras
    url(r'^', include('apps.laboratorio.urls',  namespace='laboratorios_app')),

     url(r'^todolist/', include('apps.inline.urls',  namespace='todolist')),

       #factura
     url(r'^', include('apps.factura.urls',  namespace='factura_app')),

)

if settings.DEBUG:
    urlpatterns += patterns("",
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,}
        ),
        )