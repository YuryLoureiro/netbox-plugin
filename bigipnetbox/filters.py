
import django_filters
import netaddr
from django.db.models import Q
from netaddr.core import AddrFormatError
from extras.filters import TagFilter

from .models import Node


class NodeFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Name',
    )
    #tag = TagFilter()

    class Meta:
        model = Node
        fields = ['Node_name', 'fk_NETBOX_IpAdress', 'description', 'estado']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                Q(id__icontains=value)
                | Q(description__icontains=value)
        )
        return queryset.filter(qs_filter)
