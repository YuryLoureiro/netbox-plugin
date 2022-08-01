from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import views
from .models import Node

app_name = "bigipnetbox"

urlpatterns = (
    #Node
    path("node/", views.NodeView.as_view(), name="node"),
    path("node/add/", views.NodeEdit.as_view(), name="node_add"),
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