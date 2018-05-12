from django.conf.urls import url,include
from django.contrib import admin
from .import views
admin.autodiscover()

urlpatterns = (
    url(r'^index/$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^regist/$',views.regist,name='regist'),
    url(r'^admin/', admin.site.urls),
)