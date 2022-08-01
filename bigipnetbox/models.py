from django.db import models
from django.urls import reverse
from utilities.querysets import RestrictedQuerySet
from netbox.models.features import ChangeLoggingMixin
from utilities.choices import ChoiceSet

class NodeChoices(ChoiceSet):

    STATUS_ACTIVE = 'active'
    STATUS_RESERVED = 'reserved'
    STATUS_DEPRECATED = 'deprecated'

    CHOICES = (
        (STATUS_ACTIVE, 'Active', 'blue'),
        (STATUS_RESERVED, 'Reserved', 'cyan'),
        (STATUS_DEPRECATED, 'Deprecated', 'red'),
    )

class Node(models.Model):
    Node_name = models.CharField(
        max_length=200
    )
    fk_NETBOX_IpAdress = models.OneToOneField(
                                            to = 'ipam.IPAddress',
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            blank=True
    )
    description = models.CharField(
        max_length=200,
        blank=True
    )
    estado = models.CharField(
        max_length=200,
        choices=NodeChoices,
        default=NodeChoices.STATUS_ACTIVE
    )
    objects = RestrictedQuerySet.as_manager()

class Pool(models.Model):
    Nome_pool = models.CharField(
        max_length=200
    )
    AllowNat = models.CharField(
        max_length=200
    )
    AllowSNat = models.CharField(
        max_length=200
    )
    description = models.CharField(
        max_length=200,
        blank=True
    )
    fk_POOL_MEMBRO_Nome = models.ForeignKey(to='Pool_membro', on_delete = models.SET_NULL, null=True, blank = True)
    objects = RestrictedQuerySet.as_manager()

    class Meta:
        app_label = "bigipnetbox"
        ordering = ["Nome_pool"]

    def __str__(self):
        return self.Nome_pool

    def get_absolute_url(self):
        return reverse("plugins:bigipnetbox:Pool")


class Pool_membro(models.Model):
    nome_membro = models.CharField(
        max_length=200
    )
    fk_NODE_Node_nome = models.ForeignKey(to='Node', on_delete = models.SET_NULL, null=True, blank = True)

    class Meta:
        app_label = "bigipnetbox"
        ordering = ["nome_membro"]

    def __str__(self):
        return self.nome_membro

    def get_absolute_url(self):
        return reverse("plugins:bigipnetbox:Pool_membro")

class Virtual_Server(models.Model):
    virtual_server_name = models.CharField(
        max_length=200
    )
    mask = models.CharField(
        max_length=200
    )
    porta = models.CharField(
        max_length=200
    )
    fk_Nome_pool = models.ForeignKey(to='Pool', on_delete = models.SET_NULL, null=True, blank = True)
    fk_virtual_address = models.ForeignKey(to='Virtual_Address', on_delete = models.SET_NULL, null=True, blank = True)
    objects = RestrictedQuerySet.as_manager()

class Virtual_Address(models.Model):
    pk_virtual_addess = models.CharField(
        max_length=200
    )
    ip_virtual_address = models.CharField(
        max_length=200
    )
    partition = models.CharField(
        max_length=200
    )
    Campo = models.CharField(
        max_length=200
    )
    fk_NODE_Node_nome = models.ForeignKey(to='Node', on_delete = models.SET_NULL, null=True, blank = True)

class Cluster_Big(models.Model):
    Nome_cluster = models.CharField(
        max_length=200
    )
    fk_NETBOX_Device = models.ForeignKey(to='dcim.Device', on_delete = models.SET_NULL, null=True, blank = True)
    fk_NODE_Node_nome = models.ForeignKey(to='Node', on_delete = models.SET_NULL, null=True, blank = True)
    fk_VIRTUAL_SERVER_virtual = models.ForeignKey(to='Virtual_Server', on_delete = models.SET_NULL, null=True, blank = True)









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