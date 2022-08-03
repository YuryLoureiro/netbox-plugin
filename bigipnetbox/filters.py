
import django_filters
import netaddr
from django.db.models import Q
from netaddr.core import AddrFormatError
from extras.filters import TagFilter

from .models import Node


class NodeFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    #tag = TagFilter()

    class Meta:
        model = Node
        fields = ['node_name', 'fk_Netbox_ipaddress', 'description', 'estado']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                Q(id__icontains=value)
                | Q(node_name__icontains=value)
        )
        return queryset.filter(qs_filter)
