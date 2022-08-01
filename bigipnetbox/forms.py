
from netbox.forms import NetBoxModelForm
from .models import Node, Pool, NodeChoices, Virtual_Server

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
            "Node_name",
            "fk_NETBOX_IpAdress",
            "description",
            "estado",
        ]

class PoolForm(NetBoxModelForm):
    class Meta:
        model = Pool
        fields = [
            "Nome_pool",
            "AllowNat",
            "AllowSNat",
            "description",
        ]

class VirtualServerForm(NetBoxModelForm):
    class Meta:
        model = Virtual_Server
        fields = [
            "virtual_server_name",
            "mask",
            "porta",
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