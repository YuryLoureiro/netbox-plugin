from django.db import models
from django.urls import reverse
from utilities.querysets import RestrictedQuerySet
from netbox.models.features import ChangeLoggingMixin

from utilities.choices import ChoiceSet


class Settings(ChangeLoggingMixin, models.Model):
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

class Pool_membro(models.Model):
    nome_membro = models.CharField(
        max_length=200
    )
    fk_NODE_node_membro = models.ForeignKey(to='Pool', on_delete = models.SET_NULL, null=True, blank = True)