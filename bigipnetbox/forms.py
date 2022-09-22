
from random import choices
from sre_parse import State
from unicodedata import name
from netbox.forms import NetBoxModelForm
from .models import Clusterf5, Devicef5, Irule, Node, Partition, Pool, NodeChoices, PoolMember, VirtualAddress, VirtualServer

import re

from django import forms
from django.conf import settings
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist, ValidationError
from django.utils.translation import gettext as _

from extras.models import Tag
from tenancy.models import Tenant
from dcim.models import Device, Site
from ipam.models import IPAddress, Prefix
from ipam.formfields import IPNetworkFormField
from utilities.forms import (
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField, StaticSelect,
    APISelect, APISelectMultiple, StaticSelectMultiple, TagFilterField
)
from netbox.forms import NetBoxModelForm, NetBoxModelBulkEditForm, NetBoxModelFilterSetForm

from django.forms.widgets import TextInput


class NodeFilterForm(NetBoxModelFilterSetForm):
    model = Node
    q = forms.CharField(
        required=False,
        label='Search'
    )

class PoolFilterForm(NetBoxModelFilterSetForm):
    model = Pool
    q = forms.CharField(
        required=False,
        label='Search'
    )

class PoolMemberFilterForm(NetBoxModelFilterSetForm):
    model = PoolMember
    q = forms.CharField(
        required=False,
        label='Search'
    )

class VirtualServerFilterForm(NetBoxModelFilterSetForm):
    model = VirtualServer
    q = forms.CharField(
        required=False,
        label='Search'
    )

class VirtualAddressFilterForm(NetBoxModelFilterSetForm):
    model = VirtualAddress
    q = forms.CharField(
        required=False,
        label='Search'
    )

class ClusterFilterForm(NetBoxModelFilterSetForm):
    model = Clusterf5
    q = forms.CharField(
        required=False,
        label='Search'
    )

class PartitionFilterForm(NetBoxModelFilterSetForm):
    model = Partition
    q = forms.CharField(
        required=False,
        label='Search'
    )

class IruleFilterForm(NetBoxModelFilterSetForm):
    model = Irule
    q = forms.CharField(
        required=False,
        label='Search'
    )

class Devicef5FilterForm(NetBoxModelFilterSetForm):
    model = Devicef5
    q = forms.CharField(
        required=False,
        label='Search'
    )
    #tag = TagFilterField(model)

class NodeForm(NetBoxModelForm):
    name = forms.CharField(
        required=True,
        label='Nome do Node'
    )

    ipaddress_id = forms.ModelChoiceField(queryset = IPAddress.objects.all() ,label='Endereço IP')
    partition_id = forms.ModelChoiceField(queryset = Partition.objects.all() ,label='Partition')
    state = forms.CharField(
        required=True
    )
    class Meta:
        model = Node
        fields = [
            "name",
            "ipaddress_id",
            "description",
            "state",
            "partition_id"
        ]

class PoolForm(NetBoxModelForm):
    name = forms.CharField(
        required=True,
        label='Nome da pool'
    )
    partition_id = forms.ModelChoiceField(queryset = Partition.objects.all() ,label='Partition')
    class Meta:
        model = Pool
        fields = [
            "name",
            "allownat",
            "allowsnat",
            "description",
            "partition_id",
        ]

class VirtualServerForm(NetBoxModelForm):
    name = forms.CharField(label='Nome Virtual Server')
    class Meta:
        model = VirtualServer
        fields = [
            "name",
            "mask",
            "port",
            "virtualaddress_id",
            "partition_id"
        ]


class VirtualAddressForm(NetBoxModelForm):
    ip = forms.CharField(label='IP do endereço virtual')
    node_id = forms.ModelChoiceField(queryset = Node.objects.all() ,label='Node', required=False)
    class Meta:
        model = VirtualAddress
        fields = [
            "ip",
            "node_id",
            "ipaddress_id",
        ]

class PoolMemberForm(NetBoxModelForm):
    name = forms.CharField(label = 'Nome do Membro da Pool')
    node_id = forms.ModelChoiceField(queryset = Node.objects.all() ,label='Node', required=True)
    class Meta:
        model = PoolMember
        fields = [
            "name",
            "node_id",
            "port",
            "pool_id",
        ]

class Clusterf5Form(NetBoxModelForm):
    name = forms.CharField(label = 'Nome do cluster')
    class Meta:
        model = Clusterf5
        fields = [
            "name",
        ]

class PartitionForm(NetBoxModelForm):
    name = forms.CharField(label = 'Nome da partição')
    class Meta:
        model = Partition
        fields = [
            "name",
            "clusterf5_id"
        ]

class IruleForm(NetBoxModelForm):
    name = forms.CharField(label = 'Nome da Irule')
    class Meta:
        model = Irule
        fields = [
            "name",
            "partition_id",
            "definition",
        ]

class Devicef5Form(NetBoxModelForm):
    name = forms.CharField(label = 'Nome do device')
    class Meta:
        model = Devicef5
        fields = [
            "name",
            "device_id",
            "clusterf5_id",
        ]


""" class SettingsForm(NetBoxModelForm):
    class Meta:
        model = Settings
        fields = [
            "hostname",
            "username",
            "password",
            "version",
            "verify",
            "status",
        ]
        widgets = {
            "status": StaticSelect(
                choices=(
                    ("True", "Yes"),
                    ("False", "No"),
                )
            ),
            "verify": StaticSelect(
                choices=(
                    (True, "Yes"),
                    (False, "No"),
                )
            ),
        } """