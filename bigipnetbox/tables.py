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
    name = tables.LinkColumn("plugins:bigipnetbox:node", args=[A("pk")], verbose_name = "Nome")
    ipaddress_id = tables.LinkColumn(
        "ipam:ipaddress", args=[A("ipaddress_id.pk")], verbose_name = "IP"
    )
    description = tables.Column(verbose_name = "Descrição")
    state = tables.Column(verbose_name = "Estado")
    partition_id = tables.LinkColumn(
        "plugins:bigipnetbox:partition", args=[A("partition_id.pk")], verbose_name = "Partição"
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
    name = tables.LinkColumn("plugins:bigipnetbox:pool", args=[A("pk")], verbose_name = "Nome pool")
    allownat = tables.Column(verbose_name = "Allow NAT")
    allowsnat = tables.Column(verbose_name = "Allow SNat")
    description = tables.Column(verbose_name = "Descrição")
    partition_id  = tables.LinkColumn(
        "plugins:bigipnetbox:partition", args=[A("partition_id.pk")], verbose_name = "Partição"
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
    name = tables.LinkColumn("plugins:bigipnetbox:virtualserver", args=[A("pk")],verbose_name = "Nome")
    mask = tables.Column(verbose_name = "Mascara")
    port = tables.Column(verbose_name = "Porta")
    class Meta(NetBoxTable.Meta):
        model = VirtualServer
        fields = [
            "pk",
            "name",
            "mask",
            "port"
        ]

class VirtualAddressTable(NetBoxTable):
    pk = columns.ToggleColumn()
    ip = tables.LinkColumn("plugins:bigipnetbox:virtualaddress", args=[A("pk")],verbose_name = "Ip End. Virtual")
    node_id = tables.LinkColumn("plugins:bigipnetbox:node", args=[A("node_id.pk")], verbose_name = "Node")

    class Meta(NetBoxTable.Meta):
        model = VirtualAddress
        fields = [
            "pk",
            "ip",
            "node_id"
        ]

class PoolMemberTable(NetBoxTable):
    pk = columns.ToggleColumn()
    name = tables.LinkColumn("plugins:bigipnetbox:poolmember", args=[A("pk")],verbose_name = "Nome")
    node_id = tables.LinkColumn("plugins:bigipnetbox:node", args=[A("node_id.pk")], verbose_name = "Node")
    pool_id = tables.LinkColumn("plugins:bigipnetbox:pool", args=[A("pool_id.pk")], verbose_name = "Pool")
    class Meta(NetBoxTable.Meta):
        model = PoolMember
        fields = [
            "pk",
            "name",
            "node_id",
            "port",
            "pool_id",
        ]

class Clusterf5Table(NetBoxTable):
    pk = columns.ToggleColumn()
    name = tables.LinkColumn("plugins:bigipnetbox:clusterf5", args=[A("pk")],verbose_name = "Nome")
    class Meta(NetBoxTable.Meta):
        model = Clusterf5
        fields = [
            "pk",
            "name",
        ]


class PartitionTable(NetBoxTable):
    pk = columns.ToggleColumn()
    name = tables.LinkColumn("plugins:bigipnetbox:partition", args=[A("pk")],verbose_name = "Nome")
    clusterf5_id = tables.LinkColumn(
        "plugins:bigipnetbox:clusterf5", args=[A("clusterf5_id.pk")],verbose_name = "Cluster"
    )

    class Meta(NetBoxTable.Meta):
        model = Partition
        fields = [
            "pk",
            "name",
            "clusterf5_id",
        ]

class IruleTable(NetBoxTable):
    pk = columns.ToggleColumn()
    name = tables.LinkColumn("plugins:bigipnetbox:irule", args=[A("pk")],verbose_name = "Nome")
    partition_id = tables.LinkColumn(
        "plugins:bigipnetbox:partition",args=[A("partition_id.pk")], verbose_name = "Partição"
    )
    definition = tables.Column(verbose_name = "Definição")
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
    name = tables.LinkColumn("plugins:bigipnetbox:devicef5", args=[A("pk")],verbose_name = "Nome")
    device_id = tables.LinkColumn(
        "plugins:bigipnetbox:devicef5_list", verbose_name = "Device netbox"
    )
    clusterf5_id = tables.LinkColumn(
        "plugins:bigipnetbox:clusterf5", args=[A("clusterf5_id.pk")],verbose_name = "Cluster"
    )
    class Meta(NetBoxTable.Meta):
        model = Devicef5
        fields = [
            "pk",
            "name",
            "clusterf5_id",
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