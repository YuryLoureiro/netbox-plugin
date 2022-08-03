
from netbox.forms import NetBoxModelForm
from .models import ClusterBig, Node, Pool, NodeChoices, PoolMembro, VirtualAddress, VirtualServer

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
    estado = forms.MultipleChoiceField(
        choices=NodeChoices,
        required=False,
        widget=StaticSelectMultiple()
    )

    #tag = TagFilterField(model)

class NodeForm(NetBoxModelForm):
    node_name = forms.CharField(
        required=True,
        label='Nome do Node'
    )

    fk_Netbox_ipaddress = forms.ModelChoiceField(queryset = IPAddress.objects.all() ,label='Endereço IP')
    class Meta:
        model = Node
        fields = [
            "node_name",
            "fk_Netbox_ipaddress",
            "description",
            "estado",
        ]

class PoolForm(NetBoxModelForm):
    fk_PoolMembro_nome = forms.ModelChoiceField(queryset = PoolMembro.objects.all() ,label='Membro Pool')
    class Meta:
        model = Pool
        fields = [
            "nome_pool",
            "allownat",
            "allowsnat",
            "description",
            "fk_PoolMembro_nome",
        ]

class VirtualServerForm(NetBoxModelForm):
    virtual_server_name = forms.CharField(label='Nome Virtual Server')
    class Meta:
        model = VirtualServer
        fields = [
            "virtual_server_name",
            "mask",
            "porta",
        ]


class VirtualAddressForm(NetBoxModelForm):
    ip_virtual_address = forms.CharField(label='IP virtual')
    fk_Node_node_nome = forms.ModelChoiceField(queryset = Node.objects.all() ,label='Node', required=False)
    class Meta:
        model = VirtualAddress
        fields = [
            "ip_virtual_address",
            "partition",
            "campo",
            "fk_Node_node_nome",
        ]

class PoolMembroForm(NetBoxModelForm):
    nome_membro = forms.CharField(label = 'Nome do Membro da Pool')
    fk_Node_node_nome = forms.ModelChoiceField(queryset = Node.objects.all() ,label='Node', required=True)
    class Meta:
        model = PoolMembro
        fields = [
            "nome_membro",
            "fk_Node_node_nome",
        ]

class ClusterBigForm(NetBoxModelForm):

    fk_Netbox_device = forms.ModelChoiceField(queryset = Device.objects.all() ,label='Device Big Ip', required=False)
    fk_Node_node_nome = forms.ModelChoiceField(queryset = Node.objects.all() ,label='Node', required=False)
    fk_VirtualServer_virtual = forms.ModelChoiceField(queryset = VirtualServer.objects.all() ,label='Virtual Server', required= False)
    class Meta:
        model = ClusterBig
        fields = [
            "Nome_cluster",
            "fk_Netbox_device",
            "fk_Node_node_nome",
            "fk_VirtualServer_virtual",
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