from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from item_list_app import views

urlpatterns = [
    url(r'^cardsinfo/$', views.card_list),
    url(r'^cardsinfo/(?P<pk>[0-9]+)$', views.card_detail),
    url(r'^itemsinfo/$',views.item_list),
    url(r'^itemsinfo/(?P<pk>[0-9]+)$',views.item_detail),
    url(r'^itemsinfomation/search/(?P<pk>[a-zA-Z0-9_\u4e00-\u9fa5]+)$',views.search_item)
]

urlpatterns = format_suffix_patterns(urlpatterns)