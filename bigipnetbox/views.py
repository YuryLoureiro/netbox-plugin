import platform
from django.conf import settings
from django.http import Http404, HttpResponseServerError, JsonResponse
from django.views.defaults import ERROR_500_TEMPLATE_NAME
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from netbox.views import generic

from .models import Node,Pool,PoolMembro, VirtualServer,VirtualAddress
from .forms import  NodeForm, PoolForm, VirtualServerForm, VirtualAddressForm
from .tables import NodeTable, PoolTable, VirtualServerTable, VirtualAddressTable
from .filters import NodeFilterSet
from .forms import NodeFilterForm

#Node
class NodeListView(generic.ObjectListView):
    queryset = Node.objects.all()
    table = NodeTable
    filterset = NodeFilterSet
    filterset_form = NodeFilterForm

class NodeView(generic.ObjectView):
    queryset = Node.objects.all()
    table = NodeTable


class NodeEdit(generic.ObjectEditView):
    queryset = Node.objects.all()
    form = NodeForm


class NodeDelete(generic.ObjectDeleteView):
    queryset = Node.objects.all()


class NodeDeleteBulk(generic.BulkDeleteView):
    queryset = Node.objects.all()
    table = NodeTable

#POOL
class PoolListView(generic.ObjectListView):
    queryset = Pool.objects.all()
    table = PoolTable

class PoolView(generic.ObjectView):
    queryset = Pool.objects.all()
    table = PoolTable


class PoolEdit(generic.ObjectEditView):
    queryset = Pool.objects.all()
    form = PoolForm


class PoolDelete(generic.ObjectDeleteView):
    queryset = Pool.objects.all()


class PoolDeleteBulk(generic.BulkDeleteView):
    queryset = Pool.objects.all()
    table = PoolTable

#Virtual Server
class VirtualServerListView(generic.ObjectListView):
    queryset = VirtualServer.objects.all()
    table = VirtualServerTable

class VirtualServerView(generic.ObjectView):
    queryset = VirtualServer.objects.all()
    table = VirtualServerTable


class VirtualServerEdit(generic.ObjectEditView):
    queryset = VirtualServer.objects.all()
    form = VirtualServerForm


class VirtualServerDelete(generic.ObjectDeleteView):
    queryset = VirtualServer.objects.all()


class VirtualServerDeleteBulk(generic.BulkDeleteView):
    queryset = VirtualServer.objects.all()
    table = VirtualServerTable

#Virtual Adress
class VirtualAddressListView(generic.ObjectListView):
    queryset = VirtualAddress.objects.all()
    table = VirtualAddressTable

class VirtualAddressView(generic.ObjectView):
    queryset = VirtualAddress.objects.all()
    table = VirtualAddressTable


class VirtualAddressEdit(generic.ObjectEditView):
    queryset = VirtualAddress.objects.all()
    form = VirtualAddressForm


class VirtualAddressDelete(generic.ObjectDeleteView):
    queryset = VirtualAddress.objects.all()


class VirtualAddressDeleteBulk(generic.BulkDeleteView):
    queryset = VirtualAddress.objects.all()
    table = VirtualAddressTable





#exemplos

""" class SettingsView(generic.ObjectListView):
    queryset = Settings.objects.all()
    table = SettingsTable
    template_name = "bigipnetbox/settings.html"


class SettingsEdit(generic.ObjectEditView):
    queryset = Settings.objects.all()
    form = SettingsForm
    template_name = "bigipnetbox/settings_edit.html"


class SettingsDelete(generic.ObjectDeleteView):
    queryset = Settings.objects.all()


class SettingsDeleteBulk(generic.BulkDeleteView):
    queryset = Settings.objects.all()
    table = SettingsTable """