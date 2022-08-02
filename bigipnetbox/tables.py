from multiprocessing import pool
from tabnanny import verbose
import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from netbox.tables import NetBoxTable, columns
from .models import Node,Pool, VirtualAddress, VirtualServer

class NodeTable(NetBoxTable):
    pk = columns.ToggleColumn()
    node_name = tables.Column(verbose_name = "Nome Node")
    fk_Netbox_ipaddress = tables.Column(verbose_name = "Ender. IP")
    description = tables.Column(verbose_name = "descricao")
    estado = tables.Column(verbose_name = "state")

    class Meta(NetBoxTable.Meta):
        model = Node
        fields = [
            "pk",
            "node_name",
            "fk_Netbox_ipaddress",
            "description",
            "estado",
        ]

class PoolTable(NetBoxTable):
    pk = columns.ToggleColumn()
    nome_pool= tables.Column(verbose_name = "Nome pool")
    allownat = tables.Column(verbose_name = "NAT")
    allowsnat = tables.Column(verbose_name = "AllowSNat")
    description = tables.Column(verbose_name = "description")
    fk_PoolMembro_nome = tables.Column(verbose_name = "membro da pool")
    class Meta(NetBoxTable.Meta):
        model = Pool
        fields = [
            "pk",
            "nome_pool",
            "allownat",
            "allowsnat",
            "description",
            "fk_PoolMembro_nome",
        ]

class VirtualServerTable(NetBoxTable):
    pk = columns.ToggleColumn()
    virtual_server_name = tables.Column(verbose_name = "Nome Virtual Server")
    mask = tables.Column(verbose_name = "Mascara")
    porta = tables.Column(verbose_name = "Porta")
    class Meta(NetBoxTable.Meta):
        model = VirtualServer
        fields = [
            "pk",
            "virtual_server_name",
            "mask",
            "porta",
        ]

class VirtualAddressTable(NetBoxTable):
    pk = columns.ToggleColumn()
    ip_virtual_address = tables.Column(verbose_name = "Ip End. Virtual")
    partition = tables.Column(verbose_name = "partição")
    Campo = tables.Column(verbose_name = "campo")
    fk_NODE_Node_nome = tables.Column(verbose_name = "Node")

    class Meta(NetBoxTable.Meta):
        model = VirtualAddress
        fields = [
            "pk",
            "ip_virtual_address",
            "partition",
            "Campo",
            "fk_Node_node_name",
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