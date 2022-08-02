
from netbox.forms import NetBoxModelForm
from .models import Node, Pool, NodeChoices, VirtualAddress, VirtualServer

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
    Node_name = forms.CharField(
        required=False,
        label='Name'
    )
    estado = forms.MultipleChoiceField(
        choices=NodeChoices,
        required=False,
        widget=StaticSelectMultiple()
    )

    #tag = TagFilterField(model)

class NodeForm(NetBoxModelForm):
    class Meta:
        model = Node
        fields = [
            "node_name",
            "fk_Netbox_ipaddress",
            "description",
            "estado",
        ]

class PoolForm(NetBoxModelForm):
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
    class Meta:
        model = VirtualServer
        fields = [
            "virtual_server_name",
            "mask",
            "porta",
        ]


class VirtualAddressForm(NetBoxModelForm):
    class Meta:
        model = VirtualAddress
        fields = [
            "ip_virtual_address",
            "partition",
            "campo",
            "fk_Node_node_nome",
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