# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http.response import JsonResponse
from django.views.generic import View
from django.views.generic import TemplateView, DetailView
from django.views.generic import CreateView, UpdateView

from insitu import documents
from insitu import forms
from insitu import models
from insitu.utils import get_choices, ALL_OPTIONS_LABEL
from insitu.views.base import ESDatatableView
from picklists import models as pickmodels


class ProductList(TemplateView):
    template_name = 'product/list.html'

    def get_context_data(self):
        context = super(ProductList, self).get_context_data()
        services = get_choices('name', model_cls=models.CopernicusService)
        groups = get_choices('name', model_cls=pickmodels.ProductGroup)
        statuses = get_choices('name', model_cls=pickmodels.ProductStatus)
        coverages = get_choices('name', model_cls=pickmodels.Coverage)
        components = get_choices('name', model_cls=models.Component)
        entities = get_choices('acronym', model_cls=models.EntrustedEntity)
        context.update({
            'services': services,
            'groups': groups,
            'statuses': statuses,
            'coverages': coverages,
            'components': components,
            'entities': entities,
        })
        return context


class ProductListJson(ESDatatableView):
    columns = ['acronym', 'name', 'group', 'service', 'component', 'entity',
               'status', 'coverage']
    order_columns = columns
    filters = ['service', 'group', 'status', 'coverage', 'component', 'entity']
    document = documents.ProductDoc


class ComponentsFilter(View):
    def get(self, request, *args, **kwargs):
        service = request.GET.get('service', '')
        entity = request.GET.get('entity', '')

        components = models.Component.objects.all()
        if service and service != ALL_OPTIONS_LABEL:
            components = components.filter(service__name=service)
        if entity and entity != ALL_OPTIONS_LABEL:
            components = components.filter(entrusted_entity__acronym=entity)
        data = {'components': get_choices('name', objects=components)}
        return JsonResponse(data)


class ProductAdd(CreateView):
    template_name = 'product/add.html'
    form_class = forms.ProductForm

    def get_success_url(self):
        return reverse('product:list')


class ProductEdit(UpdateView):
    template_name = 'product/edit.html'
    form_class = forms.ProductForm
    model = models.Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product:list')


class ProductDetail(DetailView):
    template_name = 'product/detail.html'
    model = models.Product
    context_object_name = 'product'
