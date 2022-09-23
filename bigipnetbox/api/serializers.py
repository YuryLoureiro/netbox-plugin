from rest_framework import serializers
#from bigipnetbox.models import bigipnetbox
from ..models import *
from netbox.api import ChoiceField, ContentTypeField, WritableNestedSerializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer

class NodeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    ipaddress_id = serializers.IntegerField(source='ipaddress_id.id', required=True, allow_null=False)
    description = serializers.CharField()
    state = ChoiceField(choices=NodeChoices, required=False)
    partiton_id = serializers.IntegerField(source='partition_id.id', required=True)

    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = Node
        fields = [
            'id', 'url', 'display', 'name', 'ipaddress_id', 'description', 'state', 'partition_id',
        ]

class PoolSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    allownat = serializers.CharField()
    allowsnat = serializers.CharField()
    description = serializers.CharField()
    partiton_id = serializers.IntegerField(source='partition_id.id', required=False)

    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = Pool
        fields = [
            'id', 'url', 'display', 'name', 'allownat', 'allowsnat', 'description', 'partition_id',
        ]

class PoolMemberSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    port = serializers.IntegerField()
    node_id = serializers.IntegerField(source='node_id.id', required=False)
    pool_id = serializers.IntegerField(source='pool_id.id', required=True)

    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = PoolMember
        fields = [
            'id', 'url', 'display', 'name', 'node_id', 'port', 'pool_id',
        ]

class VirtualServerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    mask = serializers.IntegerField()
    port = serializers.IntegerField()
    pool_id = serializers.IntegerField(source='pool_id.id', required=False)
    virtualaddress_id = serializers.IntegerField(source='virtualaddress_id.id', required=True)
    partition_id = serializers.IntegerField(source='partition_id.id', required=False)

    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = VirtualServer
        fields = [
            'id', 'url', 'display', 'name', 'mask', 'port', 'pool_id', 'virtualaddress_id', 'partition_id'
        ]

class VirtualAddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ip = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    node_id = serializers.IntegerField(source='node_id.id', required=False)
    ipaddress_id = serializers.IntegerField(source='ipaddress_id.id', required=True, allow_null=False)

    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = VirtualAddress
        fields = [
            'id', 'url', 'display', 'name', 'ip', 'node_id', 'pool_id', 'ipaddress_id',
        ]

class Clusterf5Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')

    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = VirtualAddress
        fields = [
            'id', 'url', 'display', 'name',
        ]

class PartitionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    clusterf5_id = serializers.IntegerField(source='clusterf5_id.id', required=False)
   
    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = VirtualAddress
        fields = [
            'id', 'url', 'display', 'name', 'clusterf5_id',
        ]

class IruleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    partition_id = serializers.IntegerField(source='partition_id.id', required=True)
    definition = serializers.CharField()
   
    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = VirtualAddress
        fields = [
            'id', 'url', 'display', 'name', 'partition_id', 'definition',
        ]

class Devicef5Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    display = serializers.SerializerMethodField('get_display')
    device_id = serializers.IntegerField(source='device_id.id', required=True, allow_null=False)
    clusterf5_id = serializers.IntegerField(source='clusterf5_id.id', required=False)
   
    def get_display(self, obj):
        return f"{obj}"

    class Meta:
        model = VirtualAddress
        fields = [
            'id', 'url', 'display', 'name', 'device_id', 'clusterf5_id',
        ]