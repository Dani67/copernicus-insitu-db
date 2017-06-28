from django.conf.urls import url, include

from insitu import views


product_requirement_patterns = [
    url(r'^add/$',
        views.ProductRequirementAdd.as_view(),
        name='add'),

    url(r'^(?P<pk>[0-9]+)/$',
        views.ProductRequirementEdit.as_view(),
        name='edit'),

    url(r'^(?P<pk>[0-9]+)/delete$',
        views.ProductRequirementDelete.as_view(),
        name='delete'),
]

product_patterns = [
    url(r'^list/$',
        views.ProductList.as_view(),
        name='list'),

    url(r'^filter/components/$',
        views.ComponentsFilter.as_view(),
        name='filter_components'),

    url(r'^data/$',
        views.ProductListJson.as_view(),
        name='json'),

    url(r'^add/$',
        views.ProductAdd.as_view(),
        name='add'),

    url(r'^(?P<pk>[0-9]+)/$',
        views.ProductDetail.as_view(),
        name='detail'),

    url(r'^(?P<pk>[0-9]+)/edit/$',
        views.ProductEdit.as_view(),
        name='edit'),

    url(r'^(?P<product_pk>[0-9]+)/requirement/',
        include(product_requirement_patterns,
                namespace='requirement')),
]

requirement_product_requirement_patterns = [
    url(r'^add/$',
        views.RequirementProductRequirementAdd.as_view(),
        name='add'),

    url(r'^(?P<pk>[0-9]+)/edit$',
        views.ProductRequirementEdit.as_view(),
        name='edit'),

    url(r'^(?P<pk>[0-9]+)/delete$',
        views.ProductRequirementDelete.as_view(),
        name='delete'),
]


requirement_patterns = [
    url(r'^(?P<pk>[0-9]+)/$',
        views.RequirementDetail.as_view(),
        name='detail'),

    url(r'^(?P<requirement_pk>[0-9]+)/product/',
        include(requirement_product_requirement_patterns,
                namespace='product')),
]

urlpatterns = [
    url(r'^$',
        views.HomeView.as_view(),
        name='home'),

    url(r'^product/',
        include(product_patterns,
                namespace='product')),
    url(r'^requirement/',
        include(requirement_patterns,
                namespace='requirement')),
]
