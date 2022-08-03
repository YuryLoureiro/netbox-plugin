
import django_filters
import netaddr
from django.db.models import Q
from netaddr.core import AddrFormatError
from extras.filters import TagFilter

from .models import Node, Pool, PoolMembro, ClusterBig, VirtualServer, VirtualAddress


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
                #Q(id__icontains=value)
                Q(node_name__icontains=value)
        )
        return queryset.filter(qs_filter)

class PoolFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    #tag = TagFilter()

    class Meta:
        model = Pool
        fields = ['nome_pool', 'allownat', 'allowsnat', 'description', 'fk_PoolMembro_nome']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                #Q(id__icontains=value)
                Q(nome_pool__icontains=value)
        )
        return queryset.filter(qs_filter)

class PoolMembroFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    #tag = TagFilter()

    class Meta:
        model = PoolMembro
        fields = ['nome_membro', 'fk_Node_node_nome']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                #Q(id__icontains=value)
                Q(nome_membro__icontains=value)
        )
        return queryset.filter(qs_filter)

class VirtualServerFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    #tag = TagFilter()

    class Meta:
        model = VirtualServer
        fields = ['virtual_server_name', 'mask', 'porta', 'fk_Pool_nome_pool', 'fk_VirtualAddress_ip_virtual_address']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                #Q(id__icontains=value)
                Q(virtual_server_name__icontains=value)
        )
        return queryset.filter(qs_filter)

class VirtualAddressFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    #tag = TagFilter()

    class Meta:
        model = VirtualAddress
        fields = ['ip_virtual_address', 'partition', 'campo', 'fk_Node_node_nome']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                #Q(id__icontains=value)
                Q(ip_virtual_address__icontains=value)
        )
        return queryset.filter(qs_filter)

class ClusterBigFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    #tag = TagFilter()

    class Meta:
        model = ClusterBig
        fields = ['Nome_cluster', 'fk_Netbox_device', 'fk_Node_node_nome', 'fk_VirtualServer_virtual']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                #Q(id__icontains=value)
                Q(Nome_cluster__icontains=value)
        )
        return queryset.filter(qs_filter)
