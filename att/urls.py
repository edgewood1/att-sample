from django.conf.urls import include, url
from django.contrib import admin

from firstapp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'att.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 
    url (r'^$', views.index, name="index"),
    url (r'^projectone/', views.projectone, name="projectone"),
    # uses id = digists  item/1, item will be passed as an id parameter to the item_detail view
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
