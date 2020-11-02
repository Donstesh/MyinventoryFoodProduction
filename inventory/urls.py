from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    # url(r'^(?P<product_id>[0-9]+)$', detail, name="detail"),
    url(r'^(?P<pk>\d+)$', detail, name="detail"),
    url(r'^edit/(?P<pk>\d+)$', edit, name="edit"),
    url(r'^addnew$', addnew, name="addnew"),

    url(r'^addsupllier$', addsupllier, name='addsupllier'),
    url(r'^addsale$', addsale, name='addsale'),
    url(r'^addexp$', addexp, name='addexp'),
    url(r'^addemployee$', addemployee, name='addemployee'),



]
