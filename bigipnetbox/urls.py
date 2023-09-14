from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import views
from .models import *

app_name = "bigipnetbox"

urlpatterns = (
    path("node/", views.NodeListView.as_view(), name="node_list"),
    path("node/add/", views.NodeEdit.as_view(), name="node_add"),
    path("node/edit/", views.NodeBulkEditView.as_view(), name="node_bulk_edit"),
    path("node/delete/", views.NodeBulkDelete.as_view(), name="node_bulk_delete"),
    path("node/<int:pk>/", views.NodeView.as_view(), name="node"),
    path("node/<int:pk>/edit/", views.NodeEdit.as_view(), name="node_edit"),
    path("node/<int:pk>/delete/", views.NodeDelete.as_view(), name="node_delete"),
    path("node/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="node_changelog", kwargs={"model": Node}),

    path("pool/", views.PoolListView.as_view(), name="pool_list"),
    path("pool/add/", views.PoolEdit.as_view(), name="pool_add"),
    path("pool/edit/", views.PoolBulkEditView.as_view(), name="pool_bulk_edit"),
    path("pool/delete/", views.PoolBulkDelete.as_view(), name="pool_bulk_delete"),
    path("Pool/<int:pk>/", views.PoolView.as_view(), name="pool"),
    path("pool/<int:pk>/edit/", views.PoolEdit.as_view(), name="pool_edit"),
    path("pool/<int:pk>/delete/", views.PoolDelete.as_view(), name="pool_delete"),
    path("pool/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="pool_changelog", kwargs={"model": Pool}),

    path("virtualserver/", views.VirtualServerListView.as_view(), name="virtualserver_list"),
    path("virtualserver/add/", views.VirtualServerEdit.as_view(), name="virtualserver_add"),
    path("virtualserver/edit/", views.VirtualServerBulkEditView.as_view(), name="virtualserver_bulk_edit"),
    path("virtualserver/delete/", views.VirtualServerBulkDelete.as_view(), name="virtualserver_bulk_delete"),
    path("virtualserver/<int:pk>/", views.VirtualServerView.as_view(), name="virtualserver"),
    path("virtualserver/<int:pk>/edit/", views.VirtualServerEdit.as_view(), name="virtualserver_edit"),
    path("virtualserver/<int:pk>/delete/", views.VirtualServerDelete.as_view(), name="virtualserver_delete"),
    path("virtualserver/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="virtualserver_changelog", kwargs={"model": VirtualServer}),

    path("virtualaddress/", views.VirtualAddressListView.as_view(), name="virtualaddress_list"),
    path("virtualaddress/add/", views.VirtualAddressEdit.as_view(), name="virtualaddress_add"),
    path("virtualaddress/edit/", views.VirtualAddressBulkEditView.as_view(), name="virtualaddress_bulk_edit"),
    path("virtualaddress/delete/", views.VirtualAddressBulkDelete.as_view(), name="virtualaddress_bulk_delete"),
    path("virtualaddress/<int:pk>/", views.VirtualAddressView.as_view(), name="virtualaddress"),
    path("virtualaddress/<int:pk>/edit/", views.VirtualAddressEdit.as_view(), name="virtualaddress_edit"),
    path("virtualaddress/<int:pk>/delete/", views.VirtualAddressDelete.as_view(), name="virtualaddress_delete"),
    path("virtualaddress/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="virtualaddress_changelog", kwargs={"model": VirtualAddress}),

    path("poolmember/", views.PoolMemberListView.as_view(), name="poolmember_list"),
    path("poolmember/add/", views.PoolMemberEdit.as_view(), name="poolmember_add"),
    path("poolmember/edit/", views.PoolMemberBulkEditView.as_view(), name="poolmember_bulk_edit"),
    path("poolmember/delete/", views.PoolMemberBulkDelete.as_view(), name="poolmember_bulk_delete"),
    path("poolmember/<int:pk>/", views.PoolMemberView.as_view(), name="poolmember"),
    path("poolmember/<int:pk>/edit/", views.PoolMemberEdit.as_view(), name="poolmember_edit"),
    path("poolmember/<int:pk>/delete/", views.PoolMemberDelete.as_view(), name="poolmember_delete"),
    path("poolmember/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="poolmember_changelog", kwargs={"model": PoolMember}),

    path("clusterf5/", views.Clusterf5ListView.as_view(), name="clusterf5_list"),
    path("clusterf5/add/", views.Clusterf5Edit.as_view(), name="clusterf5_add"),
    path("clusterf5/edit/", views.Clusterf5BulkEditView.as_view(), name="clusterf5_bulk_edit"),
    path("clusterf5/delete/", views.Clusterf5BulkDelete.as_view(), name="clusterf5_bulk_delete"),
    path("clusterf5/<int:pk>/", views.Clusterf5View.as_view(), name="clusterf5"),
    path("clusterf5/<int:pk>/edit/", views.Clusterf5Edit.as_view(), name="clusterf5_edit"),
    path("clusterf5/<int:pk>/delete/", views.Clusterf5Delete.as_view(), name="clusterf5_delete"),
    path("clusterf5/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="clusterf5_changelog", kwargs={"model": Clusterf5}),

    path("partition/", views.PartitionListView.as_view(), name="partition_list"),
    path("partition/add/", views.PartitionEdit.as_view(), name="partition_add"),
    path("partition/delete/", views.PartitionBulkDelete.as_view(), name="partition_bulk_delete"),
    path("partition/delete/", views.PartitionBulkEditView.as_view(), name="partition_bulk_edit"),
    path("partition/<int:pk>/", views.PartitionView.as_view(), name="partition"),
    path("partition/<int:pk>/edit/", views.PartitionEdit.as_view(), name="partition_edit"),
    path("partition/<int:pk>/delete/", views.PartitionDelete.as_view(), name="partition_delete"),
    path("partition/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="partition_changelog", kwargs={"model": Partition}),

    path("devicef5/", views.Devicef5ListView.as_view(), name="devicef5_list"),
    path("devicef5/add/", views.Devicef5Edit.as_view(), name="devicef5_add"),
    path("devicef5/delete/", views.Devicef5BulkDelete.as_view(), name="devicef5_bulk_delete"),
    path("devicef5/delete/", views.Devicef5BulkEditView.as_view(), name="devicef5_bulk_edit"),
    path("devicef5/<int:pk>/", views.Devicef5View.as_view(), name="devicef5"),
    path("devicef5/<int:pk>/edit/", views.Devicef5Edit.as_view(), name="devicef5_edit"),
    path("devicef5/<int:pk>/delete/", views.Devicef5Delete.as_view(), name="devicef5_delete"),
    path("devicef5/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="devicef5_changelog", kwargs={"model": Devicef5}),

    path("irule/", views.IruleListView.as_view(), name="irule_list"),
    path("irule/add/", views.IruleEdit.as_view(), name="irule_add"),
    path("irule/delete/", views.IruleBulkDelete.as_view(), name="irule_bulk_delete"),
    path("irule/delete/", views.IruleBulkEditView.as_view(), name="irule_bulk_edit"),
    path("irule/<int:pk>/", views.IruleView.as_view(), name="irule"),
    path("irule/<int:pk>/edit/", views.IruleEdit.as_view(), name="irule_edit"),
    path("irule/<int:pk>/delete/", views.IruleDelete.as_view(), name="irule_delete"),
    path("irule/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="irule_changelog", kwargs={"model": Irule}),
)