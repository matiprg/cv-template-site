from django.urls import path
from blog.views import *
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static

app_name='blog'
urlpatterns=[
    path('',index_view,name='post'),
    
    
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)