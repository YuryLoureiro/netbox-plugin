
from utilities.forms import StaticSelect
from netbox.forms import NetBoxModelForm
from .models import Node, Pool

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