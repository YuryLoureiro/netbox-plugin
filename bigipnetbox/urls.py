from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import views
from .models import *

app_name = "bigipnetbox"

urlpatterns = (


    ######Node
    path("node/", views.NodeListView.as_view(), name="node_list"),
    path("node/add/", views.NodeEdit.as_view(), name="node_add"),
    path("node/<int:pk>/", views.NodeView.as_view(), name="node"),
    path("node/<int:pk>/edit/", views.NodeEdit.as_view(), name="node_edit"),
    path(
        "node/<int:pk>/delete/",
        views.NodeDelete.as_view(),
        name="node_delete",
    ),
    path(
        "node/delete/",
        views.NodeDeleteBulk.as_view(),
        name="node_delete_bulk",
    ),
    path("node/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="node_changelog", kwargs={"model": Node}),



    #######
    # Pool
    ########

    path("pool/", views.PoolListView.as_view(), name="pool_list"),
    path("pool/add/", views.PoolEdit.as_view(), name="pool_add"),
    path("Pool/<int:pk>/", views.PoolView.as_view(), name="pool"),
    path("pool/<int:pk>/edit/", views.PoolEdit.as_view(), name="pool_edit"),
    path(
        "pool/<int:pk>/delete/",
        views.PoolDelete.as_view(),
        name="pool_delete",
    ),
    path(
        "pool/delete/",
        views.PoolDeleteBulk.as_view(),
        name="pool_delete_bulk",
    ),
    path("pool/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="pool_changelog", kwargs={"model": Pool}),



    #########
    # VirtualServer
    #########

    path("virtualserver/", views.VirtualServerListView.as_view(), name="virtualserver_list"),
    path("virtualserver/add/", views.VirtualServerEdit.as_view(), name="virtualserver_add"),
    path("virtualserver/<int:pk>/", views.VirtualServerView.as_view(), name="virtualserver"),
    path("virtualserver/<int:pk>/edit/", views.VirtualServerEdit.as_view(), name="virtualserver_edit"),
    path(
        "virtualserver/<int:pk>/delete/",
        views.VirtualServerDelete.as_view(),
        name="virtualserver_delete",
    ),
    path(
        "virtualserver/delete/",
        views.VirtualServerDeleteBulk.as_view(),
        name="virtualserver_delete_bulk",
    ),
    path("virtualserver/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="virtualserver_changelog", kwargs={"model": VirtualServer}),



    ######
    # virtualAddress
    ########

    path("virtualaddress/", views.VirtualAddressListView.as_view(), name="virtualaddress_list"),
    path("virtualaddress/add/", views.VirtualAddressEdit.as_view(), name="virtualaddress_add"),
    path("virtualaddress/<int:pk>/", views.VirtualAddressView.as_view(), name="virtualaddress"),
    path("virtualaddress/<int:pk>/edit/", views.VirtualAddressEdit.as_view(), name="virtualaddress_edit"),
    path(
        "virtualaddress/<int:pk>/delete/",
        views.VirtualAddressDelete.as_view(),
        name="virtualaddress_delete",
    ),
    path(
        "virtualaddress/delete/",
        views.VirtualAddressDeleteBulk.as_view(),
        name="virtualaddress_delete_bulk",
    ),
    path("virtualaddress/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="virtualaddress_changelog", kwargs={"model": VirtualAddress}),



    ######
    # PoolMember
    ######

    path("poolmember/", views.PoolMemberListView.as_view(), name="poolmember_list"),
    path("poolmember/add/", views.PoolMemberEdit.as_view(), name="poolmember_add"),
    path("poolmember/<int:pk>/", views.PoolMemberView.as_view(), name="poolmember"),
    path("poolmember/<int:pk>/edit/", views.PoolMemberEdit.as_view(), name="poolmember_edit"),
    path(
        "poolmember/<int:pk>/delete/",
        views.PoolMemberDelete.as_view(),
        name="poolmember_delete",
    ),
    path(
        "poolmember/delete/",
        views.PoolMemberDeleteBulk.as_view(),
        name="poolmember_delete_bulk",
    ),
    path("poolmember/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="poolmember_changelog", kwargs={"model": PoolMember}),

    #######
    # CLUSTERf5
    ######

    path("clusterf5/", views.Clusterf5ListView.as_view(), name="clusterf5_list"),
    path("clusterf5/add/", views.Clusterf5Edit.as_view(), name="clusterf5_add"),
    path("clusterf5/<int:pk>/", views.Clusterf5View.as_view(), name="clusterf5"),
    path("clusterf5/<int:pk>/edit/", views.Clusterf5Edit.as_view(), name="clusterf5_edit"),
    path(
        "clusterf5/<int:pk>/delete/",
        views.Clusterf5Delete.as_view(),
        name="clusterf5_delete",
    ),
    path(
        "clusterf5/delete/",
        views.Clusterf5DeleteBulk.as_view(),
        name="clusterf5_delete_bulk",
    ),
    path("clusterf5/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="clusterf5_changelog", kwargs={"model": Clusterf5}),


    #######
    # PARTITION
    ######

    path("partition/", views.PartitionListView.as_view(), name="partition_list"),
    path("partition/add/", views.PartitionEdit.as_view(), name="partition_add"),
    path("partition/<int:pk>/", views.PartitionView.as_view(), name="partition"),
    path("partition/<int:pk>/edit/", views.PartitionEdit.as_view(), name="partition_edit"),
    path(
        "partition/<int:pk>/delete/",
        views.PartitionDelete.as_view(),
        name="partition_delete",
    ),
    path(
        "partition/delete/",
        views.PartitionDeleteBulk.as_view(),
        name="partition_delete_bulk",
    ),
    path("partition/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="partition_changelog", kwargs={"model": Partition}),


    #######
    # DEVICEf5
    ######

    path("devicef5/", views.Devicef5ListView.as_view(), name="devicef5_list"),
    path("devicef5/add/", views.Devicef5Edit.as_view(), name="devicef5_add"),
    path("devicef5/<int:pk>/", views.Devicef5View.as_view(), name="devicef5"),
    path("devicef5/<int:pk>/edit/", views.Devicef5Edit.as_view(), name="devicef5_edit"),
    path(
        "devicef5/<int:pk>/delete/",
        views.Devicef5Delete.as_view(),
        name="devicef5_delete",
    ),
    path(
        "devicef5/delete/",
        views.Devicef5DeleteBulk.as_view(),
        name="devicef5_delete_bulk",
    ),
    path("devicef5/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="devicef5_changelog", kwargs={"model": Devicef5}),


    #######
    # IRULE
    ######

    path("irule/", views.IruleListView.as_view(), name="irule_list"),
    path("irule/add/", views.IruleEdit.as_view(), name="irule_add"),
    path("irule/<int:pk>/", views.IruleView.as_view(), name="irule"),
    path("irule/<int:pk>/edit/", views.IruleEdit.as_view(), name="irule_edit"),
    path(
        "irule/<int:pk>/delete/",
        views.IruleDelete.as_view(),
        name="irule_delete",
    ),
    path(
        "irule/delete/",
        views.IruleDeleteBulk.as_view(),
        name="irule_delete_bulk",
    ),
    path("irule/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="irule_changelog", kwargs={"model": Irule}),
)





""" # Settings
    path("settings/", views.SettingsView.as_view(), name="settings"),
    path("settings/add/", views.SettingsEdit.as_view(), name="settings_add"),
    path("settings/<int:pk>/edit/", views.SettingsEdit.as_view(), name="settings_edit"),
    path(
        "settings/<int:pk>/delete/",
        views.SettingsDelete.as_view(),
        name="settings_delete",
    ),
    path(
        "settings/delete/",
        views.SettingsDeleteBulk.as_view(),
        name="settings_delete_bulk",
    ),
    path("settings/<int:pk>/changelog/", ObjectChangeLogView.as_view(), name="settings_changelog", kwargs={"model": Settings}), """