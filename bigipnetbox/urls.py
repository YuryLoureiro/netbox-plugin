from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import views
from .models import Node, Pool, VirtualServer,VirtualAddress

app_name = "bigipnetbox"

urlpatterns = (
    #Node
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

    #Pool
    path("pool/", views.PoolListView.as_view(), name="pool_list"),
    path("pool/add/", views.PoolEdit.as_view(), name="pool_add"),
    #path("Pool/<int:pk>/", views.PoolView.as_view(), name="pool"),
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

    #VirtualServer
    path("virtualserver/", views.VirtualServerListView.as_view(), name="virtualserver_list"),
    path("virtualserver/add/", views.VirtualServerEdit.as_view(), name="virtualserver_add"),
    #path("virtualserver/<int:pk>/", views.virtualserverView.as_view(), name="virtualserver"),
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

    #virtualAddress
    path("virtualaddress/", views.VirtualAddressListView.as_view(), name="virtualaddress_list"),
    path("virtualaddress/add/", views.VirtualAddressEdit.as_view(), name="virtualaddress_add"),
    #path("virtualaddress/<int:pk>/", views.virtualserverView.as_view(), name="virtualserver"),
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