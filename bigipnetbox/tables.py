import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from netbox.tables import NetBoxTable, columns
from .models import Settings, Node


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

class NodeTable(NetBoxTable):
    pk = columns.ToggleColumn()
    name = tables.LinkColumn(
        "plugins:bigipnetbox:settings_edit", args=[A("pk")]
    )
    password = MaskedPassword()
    ip = tables.Column()
    estado = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = Node
        fields = [
            "pk",
            "name",
            "description",
            "ip",
            "estado",
        ]