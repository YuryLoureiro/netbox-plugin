from multiprocessing import pool
from sre_parse import State
from tabnanny import verbose
import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from netbox.tables import NetBoxTable, columns
from .models import *

class NodeTable(NetBoxTable):
    pk = columns.ToggleColumn()
    name = tables.Column(verbose_name = "Nome Node")
    ipaddress_id = tables.LinkColumn(
        "ipam:ipaddress", args=[A("ipaddress_id.pk")], verbose_name = "IP"
    )
    description = tables.Column(verbose_name = "descricao")
    state = tables.Column(verbose_name = "estado")
    partition_id = tables.LinkColumn(
        "plugins:bigipnetbox:partition_list", verbose_name = "Partição"
    )
    class Meta(NetBoxTable.Meta):
        model = Node
        fields = [
            "pk",
            "name",
            "ipaddress_id",
            "description",
            "state",
            "partition_id"
        ]

class PoolTable(NetBoxTable):
    pk = columns.ToggleColumn()
    name= tables.Column(verbose_name = "Nome pool")
    allownat = tables.Column(verbose_name = "NAT")
    allowsnat = tables.Column(verbose_name = "AllowSNat")
    description = tables.Column(verbose_name = "description")
    partition_id  = tables.LinkColumn(
        "plugins:bigipnetbox:partition_list", verbose_name = "Membro da pool"
    )
    class Meta(NetBoxTable.Meta):
        model = Pool
        fields = [
            "pk",
            "name",
            "allownat",
            "allowsnat",
            "description",
            "partition_id",
        ]

class VirtualServerTable(NetBoxTable):
    pk = columns.ToggleColumn()
    name = tables.Column(verbose_name = "Nome Virtual Server")
    mask = tables.Column(verbose_name = "Mascara")
    port = tables.Column(verbose_name = "Porta")
    class Meta(NetBoxTable.Meta):
        model = VirtualServer
        fields = [
            "pk",
            "name",
            "mask",
            "port",
            "pool_id",
            "virtualaddress_id",
            "partition_id"
        ]

class VirtualAddressTable(NetBoxTable):
    pk = columns.ToggleColumn()
    ip = tables.Column(verbose_name = "Ip End. Virtual")
    node_id = tables.LinkColumn(
        "plugins:bigipnetbox:node_list", verbose_name = "Node"
    )

    class Meta(NetBoxTable.Meta):
        model = VirtualAddress
        fields = [
            "pk",
            "ip",
            "node_id",
            "ipaddress_id",
        ]

class PoolMemberTable(NetBoxTable):
    pk = columns.ToggleColumn()
    name = tables.Column(verbose_name = "Nome do Membro")
    node_id = tables.LinkColumn(
        "plugins:bigipnetbox:node_list", verbose_name = "Node"
    )

    class Meta(NetBoxTable.Meta):
        model = PoolMember
        fields = [
            "pk",
            "name",
            "node_id",
            "port",
            "pool_id"
        ]

class Clusterf5Table(NetBoxTable):
    pk = columns.ToggleColumn()
    name = tables.Column(verbose_name = "Nome do cluster")
    class Meta(NetBoxTable.Meta):
        model = Clusterf5
        fields = [
            "pk",
            "name",
        ]


class PartitionTable(NetBoxTable):
    pk = columns.ToggleColumn()
    name = tables.Column(verbose_name = "Nome do Membro")
    cluster_id = tables.LinkColumn(
        "plugins:bigipnetbox:cluster_list", verbose_name = "Cluster"
    )

    class Meta(NetBoxTable.Meta):
        model = Partition
        fields = [
            "pk",
            "name",
            "cluster_id",
        ]

class IruleTable(NetBoxTable):
    pk = columns.ToggleColumn()
    name = tables.Column(verbose_name = "Nome do Membro")
    partition_id = tables.LinkColumn(
        "plugins:bigipnetbox:partition_list", verbose_name = "Cluster"
    )

    class Meta(NetBoxTable.Meta):
        model = Irule
        fields = [
            "pk",
            "name",
            "partition_id",
            "definition"
        ]

class Devicef5Table(NetBoxTable):
    pk = columns.ToggleColumn()
    name = tables.Column(verbose_name = "Nome do Membro")
    device_id = tables.LinkColumn(
        "plugins:bigipnetbox:devicef5_list", verbose_name = "Cluster"
    )

    class Meta(NetBoxTable.Meta):
        model = Devicef5
        fields = [
            "pk",
            "name",
            "cluster_id",
            "device_id"
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