from netbox.api.viewsets import NetBoxModelViewSet

from ..models import *
from ..filters import *
from .serializers import *

class NodeViewSet(NetBoxModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    filterset_class = NodeFilterSet

class PoolViewSet(NetBoxModelViewSet):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer
    filterset_class = PoolFilterSet

class PoolMemberViewSet(NetBoxModelViewSet):
    queryset = PoolMember.objects.all()
    serializer_class = PoolMemberSerializer
    filterset_class = PoolMemberFilterSet

class VirtualServerViewSet(NetBoxModelViewSet):
    queryset = VirtualServer.objects.all()
    serializer_class = VirtualServerSerializer
    filterset_class = VirtualServerFilterSet

class VirtualAddressViewSet(NetBoxModelViewSet):
    queryset = VirtualAddress.objects.all()
    serializer_class = VirtualAddressSerializer
    filterset_class = VirtualAddressFilterSet

class Clusterf5ViewSet(NetBoxModelViewSet):
    queryset = Clusterf5.objects.all()
    serializer_class = Clusterf5Serializer
    filterset_class = Clusterf5FilterSet

class PartitionViewSet(NetBoxModelViewSet):
    queryset = Partition.objects.all()
    serializer_class = PartitionSerializer
    filterset_class = PartitionFilterSet

class IruleViewSet(NetBoxModelViewSet):
    queryset = Irule.objects.all()
    serializer_class = IruleSerializer
    filterset_class = IruleFilterSet

class Devicef5ViewSet(NetBoxModelViewSet):
    queryset = Devicef5.objects.all()
    serializer_class = Devicef5Serializer
    filterset_class = Devicef5FilterSet
