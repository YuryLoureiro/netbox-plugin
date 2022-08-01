import platform
from django.conf import settings
from django.http import Http404, HttpResponseServerError, JsonResponse
from django.views.defaults import ERROR_500_TEMPLATE_NAME
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from netbox.views import generic
from .models import Node,Pool,Pool_membro, Virtual_Server
from .forms import  NodeForm, PoolForm, VirtualServerForm
from .tables import NodeTable, PoolTable, VirtualServerTable
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

class VirtualServerListView(generic.ObjectListView):
    queryset = Virtual_Server.objects.all()
    table = VirtualServerTable

class VirtualServerView(generic.ObjectView):
    queryset = Virtual_Server.objects.all()
    table = VirtualServerTable


class VirtualServerEdit(generic.ObjectEditView):
    queryset = Virtual_Server.objects.all()
    form = VirtualServerForm


class VirtualServerDelete(generic.ObjectDeleteView):
    queryset = Virtual_Server.objects.all()


class VirtualServerDeleteBulk(generic.BulkDeleteView):
    queryset = Virtual_Server.objects.all()
    table = VirtualServerTable








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