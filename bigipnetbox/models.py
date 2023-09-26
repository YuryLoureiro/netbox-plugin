from unicodedata import name
from django.db import models
from django.urls import reverse
from utilities.querysets import RestrictedQuerySet
from netbox.models.features import ChangeLoggingMixin

from .choices import NodeStatusChoices, PoolAllowChoices

class Node(models.Model):
    name = models.CharField(
        max_length=200
    )
    ipaddress_id = models.OneToOneField(
                                            to = 'ipam.IPAddress',
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            blank=True
    )
    description = models.CharField(
        max_length=200,
        blank=True
    )
    state = models.CharField(
        max_length=200,
        choices=NodeStatusChoices,
        default=NodeStatusChoices.STATUS_ACTIVE
    )
    partition_id = models.ForeignKey(to='Partition', on_delete = models.SET_NULL, null=True, blank = True)
    objects = RestrictedQuerySet.as_manager()

    class Meta:
        app_label = "bigipnetbox"
        ordering = ["name"]
        verbose_name = 'Node'
        verbose_name_plural = 'Nodes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:bigipnetbox:node_list")

###POOL###

class Pool(models.Model):
    name = models.CharField(
        max_length=200
    )
    allownat = models.CharField(
        max_length=200,
        choices=PoolAllowChoices,
        default=PoolAllowChoices.CHOICE_YES,
        blank=True
    )
    allowsnat = models.CharField(
        max_length=200,
        choices=PoolAllowChoices,
        default=PoolAllowChoices.CHOICE_YES,
        blank=True
    )
    description = models.CharField(
        max_length=200,
        blank=True
    )
    partition_id = models.ForeignKey(to='Partition', on_delete = models.SET_NULL, null=True, blank = True)

    objects = RestrictedQuerySet.as_manager()
    class Meta:
        app_label = "bigipnetbox"
        ordering = ["name"]
        verbose_name = 'Pool'
        verbose_name_plural = 'Pools'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:bigipnetbox:pool_list")



class PoolMember(models.Model):
    name = models.CharField(
        max_length=200
    )
    node_id = models.ForeignKey(to='Node', on_delete = models.SET_NULL, null=True, blank = True, related_name = "pools")
    port = models.IntegerField()
    pool_id = models.ForeignKey(to='Pool', on_delete = models.SET_NULL, null=True, blank = True, related_name = "members")

    objects = RestrictedQuerySet.as_manager()
    class Meta:
        app_label = "bigipnetbox"
        ordering = ["name"]
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:bigipnetbox:poolmember_list")

##VIRTUAL SERVER###

class VirtualServer(models.Model):
    name = models.CharField(
        max_length=200
    )
    mask = models.IntegerField(default=0)
    port = models.IntegerField(default=0)
    pool_id = models.ForeignKey(to='Pool', on_delete = models.SET_NULL, null=True, blank = True)
    virtualaddress_id = models.ForeignKey(to='VirtualAddress', on_delete = models.SET_NULL, null=True, blank = True)
    partition_id = models.ForeignKey(to='Partition', on_delete = models.SET_NULL, null=True, blank = True)

    objects = RestrictedQuerySet.as_manager()
    class Meta:
        app_label = "bigipnetbox"
        ordering = ["name"]
        verbose_name = 'Virtual Server'
        verbose_name_plural = 'Virtual Servers'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:bigipnetbox:virtualserver_list")



class VirtualAddress(models.Model):
    ip = models.CharField(
        max_length=200
    )
    node_id = models.ForeignKey(to='Node', on_delete = models.SET_NULL, null=True, blank = True)
    ipaddress_id = models.ForeignKey(to = 'ipam.IPAddress', on_delete=models.SET_NULL, null=True, blank=True)
    objects = RestrictedQuerySet.as_manager()
    class Meta:
        app_label = "bigipnetbox"
        ordering = ["ip"]
        verbose_name = 'Virtual Address'
        verbose_name_plural = 'Virtual Addresses'
    def __str__(self):
        return self.ip
    
    def get_absolute_url(self):
        return reverse("plugins:bigipnetbox:virtualaddress_list")
    


class Clusterf5(models.Model):
    name = models.CharField(
        max_length=200
    )

    objects = RestrictedQuerySet.as_manager()

    class Meta:
        app_label = "bigipnetbox"
        ordering = ["name"]
        verbose_name = 'Cluster'
        verbose_name_plural = 'Clusters'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:bigipnetbox:clusterf5_list")


class Partition(models.Model):
    name = models.CharField(
        max_length=200
    )
    clusterf5_id = models.ForeignKey(to = 'Clusterf5', on_delete=models.SET_NULL, null=True, blank=True)

    objects = RestrictedQuerySet.as_manager()
    class Meta:
        app_label = "bigipnetbox"
        ordering = ["name"]
        verbose_name = 'Partition'
        verbose_name_plural = 'Partitions'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:bigipnetbox:partition_list")

class Irule(models.Model):
    name = models.CharField(
        max_length=200
    )
    partition_id = models.ForeignKey(to='Partition', on_delete = models.SET_NULL, null=True, blank = True)
    definition = models.TextField(blank=False,)

    objects = RestrictedQuerySet.as_manager()
    class Meta:
        app_label = "bigipnetbox"
        ordering = ["name"]
        verbose_name = 'Irule'
        verbose_name_plural = 'Irules'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:bigipnetbox:irule_list")

class Devicef5(models.Model):
    name = models.CharField(
        max_length=200
    ) 
    device_id = models.ForeignKey(to = 'dcim.Device', on_delete=models.SET_NULL, null=True, blank=True)
    clusterf5_id = models.ForeignKey(to = 'Clusterf5', on_delete=models.SET_NULL, null=True, blank=True)

    objects = RestrictedQuerySet.as_manager()
    class Meta:
        app_label = "bigipnetbox"
        ordering = ["name"]
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
    
""" class Settings(ChangeLoggingMixin, models.Model):
    created = models.DateTimeField(
            auto_now_add=True,
            blank=True,
            null=True
        )
    last_updated = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )
    hostname = models.CharField(max_length=2000, unique=True, blank=True, null=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    version = models.CharField(max_length=10)
    verify = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    objects = RestrictedQuerySet.as_manager()
    class Meta:
        app_label = "bigipnetbox"
        ordering = ["hostname"]
    def __str__(self):
        return self.hostname
    def get_absolute_url(self):
        return reverse("plugins:bigipnetbox:settings")
 """