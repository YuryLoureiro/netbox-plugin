from multiprocessing import pool
import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from netbox.tables import NetBoxTable, columns
from .models import Node,Pool

class NodeTable(NetBoxTable):
    pk = columns.ToggleColumn()
    Node_name = tables.Column(verbose_name = "Nome Node")
    fk_NETBOX_IpAdress = tables.Column(verbose_name = "Ender. IP")
    description = tables.Column(verbose_name = "descricao")
    estado = tables.Column(verbose_name = "state")

    class Meta(NetBoxTable.Meta):
        model = Node
        fields = [
            "pk",
            "Node_name",
            "fk_NETBOX_IpAdress",
            "description",
            "estado",
        ]

class PoolTable(NetBoxTable):
    pk = columns.ToggleColumn()
    Nome_pool= tables.Column(verbose_name = "Nome pool")
    AllowNat = tables.Column(verbose_name = "NAT")
    AllowSNat = tables.Column(verbose_name = "AllowSNat")
    description = tables.Column(verbose_name = "description")

    class Meta(NetBoxTable.Meta):
        model = Pool
        fields = [
            "pk",
            "Nome_pool",
            "AllowNat",
            "AllowSNat",
            "description",
        ]






""" 
class MaskedPassword(tables.Column):
    def render(self, value):
        value = "*****"
        return mark_safe(value)


class SettingsTable(NetBoxTable):
    pk = columns.ToggleColumn()
    hostname = tables.LinkColumn(
        "plugins:bigipnetbox:settings_edit", args=[A("pk")]
    )
    username = tables.Column()
    password = MaskedPassword()
    version = tables.Column()
    verify = columns.BooleanColumn()
    status = columns.BooleanColumn()

    class Meta(NetBoxTable.Meta):
        model = Settings
        fields = [
            "pk",
            "hostname",
            "username",
            "password",
            "version",
            "verify",
            "status",
        ] 
 """