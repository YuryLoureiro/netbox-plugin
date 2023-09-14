import platform
from django.conf import settings
from django.http import Http404, HttpResponseServerError, JsonResponse
from django.views.defaults import ERROR_500_TEMPLATE_NAME
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from netbox.views import generic

from .models import *
from .forms import  *
from .tables import *
from .filters import *
from .forms import *

#Node
class NodeListView(generic.ObjectListView):
    queryset = Node.objects.all()
    table = NodeTable
    filterset = NodeFilterSet
    filterset_form = NodeFilterForm
    action_buttons = ('add',)

class NodeView(generic.ObjectView):
    queryset = Node.objects.all()
    table = NodeTable
    def get_extra_context(self, request, instance):
        pool_table = PoolMemberTable(instance.pools.all())

        data = {
                "pool_table" : pool_table,
            }
        return data

class NodeEdit(generic.ObjectEditView):
    queryset = Node.objects.all()
    form = NodeForm


class NodeDelete(generic.ObjectDeleteView):
    queryset = Node.objects.all()


class NodeBulkDelete(generic.BulkDeleteView):
    queryset = Node.objects.all()
    table = NodeTable


class NodeBulkEditView(generic.BulkEditView):
    queryset = Node.objects.all()
    filterset = NodeFilterSet
    table = NodeTable
    form = NodeBulkEditForm

#POOL
class PoolListView(generic.ObjectListView):
    queryset = Pool.objects.all()
    table = PoolTable
    filterset = PoolFilterSet
    filterset_form = PoolFilterForm

class PoolView(generic.ObjectView):
    queryset = Pool.objects.all()
    table = PoolTable
    def get_extra_context(self, request, instance):
        pool_table = PoolMemberTable(instance.members.all())

        data = {
                "pool_table" : pool_table,
            }
        return data

class PoolEdit(generic.ObjectEditView):
    queryset = Pool.objects.all()
    form = PoolForm


class PoolDelete(generic.ObjectDeleteView):
    queryset = Pool.objects.all()


class PoolBulkDelete(generic.BulkDeleteView):
    queryset = Pool.objects.all()
    table = PoolTable

class PoolBulkEditView(generic.BulkEditView):
    queryset = Pool.objects.all()
    filterset = PoolFilterSet
    table = PoolTable
    form = PoolBulkEditForm

#Virtual Server
class VirtualServerListView(generic.ObjectListView):
    queryset = VirtualServer.objects.all()
    table = VirtualServerTable
    filterset = VirtualServerFilterSet
    filterset_form = VirtualServerFilterForm

class VirtualServerView(generic.ObjectView):
    queryset = VirtualServer.objects.all()
    table = VirtualServerTable


class VirtualServerEdit(generic.ObjectEditView):
    queryset = VirtualServer.objects.all()
    form = VirtualServerForm


class VirtualServerDelete(generic.ObjectDeleteView):
    queryset = VirtualServer.objects.all()


class VirtualServerBulkDelete(generic.BulkDeleteView):
    queryset = VirtualServer.objects.all()
    table = VirtualServerTable

class VirtualServerBulkEditView(generic.BulkEditView):
    queryset = VirtualServer.objects.all()
    filterset = VirtualServerFilterSet
    table = VirtualServerTable
    form = VirtualServerBulkEditForm

#Virtual Adress
class VirtualAddressListView(generic.ObjectListView):
    queryset = VirtualAddress.objects.all()
    table = VirtualAddressTable
    filterset = VirtualAddressFilterSet
    filterset_form = VirtualAddressFilterForm

class VirtualAddressBulkEditView(generic.BulkEditView):
    queryset = VirtualAddress.objects.all()
    filterset = VirtualAddressFilterSet
    table = VirtualAddressTable
    form = VirtualAddressBulkEditForm

class VirtualAddressView(generic.ObjectView):
    queryset = VirtualAddress.objects.all()
    table = VirtualAddressTable


class VirtualAddressEdit(generic.ObjectEditView):
    queryset = VirtualAddress.objects.all()
    form = VirtualAddressForm


class VirtualAddressDelete(generic.ObjectDeleteView):
    queryset = VirtualAddress.objects.all()


class VirtualAddressBulkDelete(generic.BulkDeleteView):
    queryset = VirtualAddress.objects.all()
    table = VirtualAddressTable


#Pool Member
class PoolMemberListView(generic.ObjectListView):
    queryset = PoolMember.objects.all()
    table = PoolMemberTable
    filterset = PoolMemberFilterSet
    filterset_form = PoolMemberFilterForm

class PoolMemberView(generic.ObjectView):
    queryset = PoolMember.objects.all()
    table = PoolMemberTable


class PoolMemberEdit(generic.ObjectEditView):
    queryset = PoolMember.objects.all()
    form = PoolMemberForm


class PoolMemberDelete(generic.ObjectDeleteView):
    queryset = PoolMember.objects.all()


class PoolMemberBulkDelete(generic.BulkDeleteView):
    queryset = PoolMember.objects.all()
    table = PoolMemberTable

class PoolMemberBulkEditView(generic.BulkEditView):
    queryset = PoolMember.objects.all()
    filterset = PoolMemberFilterSet
    table = PoolMemberTable
    form = PoolMemberBulkEditForm


#CLUSTER
class Clusterf5ListView(generic.ObjectListView):
    queryset = Clusterf5.objects.all()
    table = Clusterf5Table
    filterset = Clusterf5FilterSet
    filterset_form = Clusterf5FilterForm

class Clusterf5View(generic.ObjectView):
    queryset = Clusterf5.objects.all()
    table = Clusterf5Table


class Clusterf5Edit(generic.ObjectEditView):
    queryset = Clusterf5.objects.all()
    form = Clusterf5Form


class Clusterf5Delete(generic.ObjectDeleteView):
    queryset = Clusterf5.objects.all()


class Clusterf5BulkDelete(generic.BulkDeleteView):
    queryset = Clusterf5.objects.all()
    table = Clusterf5Table

class Clusterf5BulkEditView(generic.BulkEditView):
    queryset = Clusterf5.objects.all()
    filterset = Clusterf5FilterSet
    table = Clusterf5Table
    form = Clusterf5BulkEditForm


#PARTITION
class PartitionListView(generic.ObjectListView):
    queryset = Partition.objects.all()
    table = PartitionTable
    filterset = PartitionFilterSet
    filterset_form = PartitionFilterForm

class PartitionView(generic.ObjectView):
    queryset = Partition.objects.all()
    table = PartitionTable


class PartitionEdit(generic.ObjectEditView):
    queryset = Partition.objects.all()
    form = PartitionForm


class PartitionDelete(generic.ObjectDeleteView):
    queryset = Partition.objects.all()


class PartitionBulkDelete(generic.BulkDeleteView):
    queryset = Partition.objects.all()
    table = PartitionTable

class PartitionBulkEditView(generic.BulkEditView):
    queryset = Partition.objects.all()
    filterset = PartitionFilterSet
    table = PartitionTable
    form = PartitionBulkEditForm

#Devicef5
class Devicef5ListView(generic.ObjectListView):
    queryset = Devicef5.objects.all()
    table = Devicef5Table
    filterset = Devicef5FilterSet
    filterset_form = Devicef5FilterForm

class Devicef5View(generic.ObjectView):
    queryset = Devicef5.objects.all()
    table = Devicef5Table


class Devicef5Edit(generic.ObjectEditView):
    queryset = Devicef5.objects.all()
    form = Devicef5Form


class Devicef5Delete(generic.ObjectDeleteView):
    queryset = Devicef5.objects.all()


class Devicef5BulkDelete(generic.BulkDeleteView):
    queryset = Devicef5.objects.all()
    table = Devicef5Table

class Devicef5BulkEditView(generic.BulkEditView):
    queryset = Devicef5.objects.all()
    filterset = Devicef5FilterSet
    table = Devicef5Table
    form = Devicef5BulkEditForm

#Irule
class IruleListView(generic.ObjectListView):
    queryset = Irule.objects.all()
    table = IruleTable
    filterset = IruleFilterSet
    filterset_form = IruleFilterForm

class IruleView(generic.ObjectView):
    queryset = Irule.objects.all()
    table = IruleTable


class IruleEdit(generic.ObjectEditView):
    queryset = Irule.objects.all()
    form = IruleForm


class IruleDelete(generic.ObjectDeleteView):
    queryset = Irule.objects.all()


class IruleBulkDelete(generic.BulkDeleteView):
    queryset = Irule.objects.all()
    table = IruleTable

class IruleBulkEditView(generic.BulkEditView):
    queryset = Irule.objects.all()
    filterset = IruleFilterSet
    table = IruleTable
    form = IruleBulkEditForm
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


class SettingsBulkDelete(generic.BulkDeleteView):
    queryset = Settings.objects.all()
    table = SettingsTable """