from multiprocessing import pool
from tabnanny import verbose
import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from netbox.tables import NetBoxTable, columns
from .models import ClusterBig, Node,Pool, PoolMembro, VirtualAddress, VirtualServer

class NodeTable(NetBoxTable):
    pk = columns.ToggleColumn()
    node_name = tables.Column(verbose_name = "Nome Node")
    fk_Netbox_ipaddress = tables.LinkColumn(
        "ipam:ipaddress", args=[A("fk_Netbox_ipaddress.pk")], verbose_name = "IP"
    )
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
    fk_PoolMembro_nome = tables.LinkColumn(
        "plugins:bigipnetbox:poolmembro_list", verbose_name = "Membro da pool"
    )
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
    fk_Node_node_nome = tables.LinkColumn(
        "plugins:bigipnetbox:node_list", verbose_name = "Node"
    )

    class Meta(NetBoxTable.Meta):
        model = VirtualAddress
        fields = [
            "pk",
            "ip_virtual_address",
            "partition",
            "Campo",
            "fk_Node_node_nome",
        ]

class PoolMembroTable(NetBoxTable):
    pk = columns.ToggleColumn()
    nome_membro = tables.Column(verbose_name = "Nome do Membro")
    fk_Node_node_nome = tables.LinkColumn(
        "plugins:bigipnetbox:node_list", verbose_name = "Node"
    )

    class Meta(NetBoxTable.Meta):
        model = PoolMembro
        fields = [
            "pk",
            "nome_membro",
            "fk_Node_node_nome",
        ]

class ClusterBigTable(NetBoxTable):
    pk = columns.ToggleColumn()
    Nome_cluster = tables.Column(verbose_name = "Nome do cluster")
    fk_Netbox_device = tables.LinkColumn(
        "dcim:device", args=[A("fk_Netbox_device.pk")], verbose_name = "Device"
    )
    fk_Node_node_nome = tables.LinkColumn(
        "plugins:bigipnetbox:node_list", verbose_name = "Node"
    )
    fk_VirtualServer_virtual = tables.LinkColumn(
        "plugins:bigipnetbox:virtualserver_list", verbose_name = "Virtual Server"
    )

    class Meta(NetBoxTable.Meta):
        model = ClusterBig
        fields = [
            "pk",
            "Nome_cluster",
            "fk_Netbox_device",
            "fk_Node_node_nome",
            "fk_VirtualServer_virtual",
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