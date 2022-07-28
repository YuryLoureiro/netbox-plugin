from tkinter import NE
from utilities.forms import StaticSelect
from netbox.forms import NetBoxModelForm
from .models import Settings,Node

class SettingsForm(NetBoxModelForm):
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
        }

class NodeForm(NetBoxModelForm):
    class Meta:
        model = Node
        fields = [
            "node_name",
            "fk_NETBOX_IpAdress",
            "description",
            "estado",
        ]