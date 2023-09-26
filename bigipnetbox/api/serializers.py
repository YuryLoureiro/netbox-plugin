import ipaddress
from rest_framework import serializers
#from bigipnetbox.models import bigipnetbox
from ..models import *
from netbox.api.fields import ChoiceField, ContentTypeField
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ipam.api.nested_serializers import NestedIPAddressSerializer
from dcim.api.nested_serializers import NestedDeviceSerializer


class NestedPartitionSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:bigipnetbox-api:partition-detail'
    )
    
    class Meta:
        model = Partition
        fields = [
            'id', 'url', 'display', 'name', 'clusterf5_id',
        ]

class NestedNodeSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:bigipnetbox-api:node-detail'
    )
    
    class Meta:
        model = Node
        fields = [
            'id', 'url', 'display', 'name', 'ipaddress_id', 'description', 'state', 'partition_id',
        ]

class NestedPoolSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:bigipnetbox-api:pool-detail'
    )
    
    class Meta:
        model = Pool
        fields = [
            'id', 'url', 'display', 'name', 'allownat', 'allowsnat', 'description', 'partition_id',
        ]

class NestedVirtualAddressSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:bigipnetbox-api:virtualaddress-detail'
    )

    class Meta:
        model = VirtualAddress
        fields = [
            'id', 'url', 'display', 'ip', 'node_id', 'ipaddress_id',
        ]

class NestedClusterf5Serializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:bigipnetbox-api:clusterf5-detail'
    )

    class Meta:
        model = Clusterf5
        fields = [
            'id', 'url', 'display', 'name',
        ]

class NodeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:bigipnetbox-api:node-detail'
    )
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    ipaddress_id = NestedIPAddressSerializer(many=False,required=False, allow_null=True)
    description = serializers.CharField()
    state = ChoiceField(choices=NodeStatusChoices, required=False)
    partition_id = NestedPartitionSerializer(required=True)

    def get_display(self, obj):
        return f"{obj}"
    
    class Meta:
        model = Node
        fields = [
            'id', 'url', 'display', 'name', 'ipaddress_id', 'description', 'state', 'partition_id',
        ]
    
    def create(self, validated_data):
        return Node.objects.create(**validated_data)

class PoolSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:bigipnetbox-api:pool-detail'
    )
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    allownat = serializers.CharField()
    allowsnat = serializers.CharField()
    description = serializers.CharField()
    partition_id = NestedPartitionSerializer(required=False)

    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = Pool
        fields = [
            'id', 'url', 'display', 'name', 'allownat', 'allowsnat', 'description', 'partition_id',
        ]
    def create(self, validated_data):
        return Pool.objects.create(**validated_data)

class PoolMemberSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:bigipnetbox-api:poolmember-detail'
    )
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    port = serializers.IntegerField()
    node_id = NestedNodeSerializer(required=False)
    pool_id = NestedPoolSerializer(required=True)

    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = PoolMember
        fields = [
            'id', 'url', 'display', 'name', 'node_id', 'port', 'pool_id',
        ]
    def create(self, validated_data):
        return PoolMember.objects.create(**validated_data)

class VirtualServerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:bigipnetbox-api:virtualserver-detail'
    )
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    mask = serializers.IntegerField()
    port = serializers.IntegerField()
    pool_id = NestedPoolSerializer(required=False)
    virtualaddress_id = NestedVirtualAddressSerializer(required=True)
    partition_id = NestedPartitionSerializer(required=False)

    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = VirtualServer
        fields = [
            'id', 'url', 'display', 'name', 'mask', 'port', 'pool_id', 'virtualaddress_id', 'partition_id'
        ]
    def create(self, validated_data):
        return VirtualServer.objects.create(**validated_data)

class VirtualAddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:bigipnetbox-api:virtualaddress-detail'
    )
    ip = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    node_id = NestedNodeSerializer(required=False)
    ipaddress_id = NestedIPAddressSerializer(many=False,required=True, allow_null=False)

    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = VirtualAddress
        fields = [
            'id', 'url', 'display', 'ip', 'node_id', 'ipaddress_id',
        ]
    
    def create(self, validated_data):
        return VirtualAddress.objects.create(**validated_data)

class Clusterf5Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:bigipnetbox-api:clusterf5-detail'
    )
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')

    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = Clusterf5
        fields = [
            'id', 'url', 'display', 'name',
        ]
    
    def create(self, validated_data):
        return Clusterf5.objects.create(**validated_data)

class PartitionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:bigipnetbox-api:partition-detail'
    )
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    clusterf5_id = NestedClusterf5Serializer(required=False)
   
    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = Partition
        fields = [
            'id', 'url', 'display', 'name', 'clusterf5_id',
        ]
    
    def create(self, validated_data):
        return Partition.objects.create(**validated_data)

class IruleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:bigipnetbox-api:irule-detail'
    )
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    partition_id = NestedPartitionSerializer(required=True)
    definition = serializers.CharField()
   
    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = Irule
        fields = [
            'id', 'url', 'display', 'name', 'partition_id', 'definition',
        ]
    
    def create(self, validated_data):
        return Irule.objects.create(**validated_data)

class Devicef5Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:bigipnetbox-api:devicef5-detail'
    )
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    device_id = NestedDeviceSerializer(many=True, required=True, allow_null=False)
    clusterf5_id = NestedClusterf5Serializer(required=False)
   
    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = Devicef5
        fields = [
            'id', 'url', 'display', 'name', 'device_id', 'clusterf5_id',
        ]
    
    def create(self, validated_data):
        return Devicef5.objects.create(**validated_data)