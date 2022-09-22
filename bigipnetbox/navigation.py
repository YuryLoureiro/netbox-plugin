"""
from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:bigipnetbox:mylink',
        link_text='MyLink',
        buttons=(
            PluginMenuButton('home', 'Button A', 'mdi mdi-plus-thick-info', ButtonColorChoices.BLUE),
        )
    ),
)
"""

from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link="plugins:bigipnetbox:node_list",
        link_text="Node",
        permissions=["bigipnetbox.admin_full"],
        buttons=(
            PluginMenuButton(
                link='plugins:bigipnetbox:node_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['bigipnetbox.admin_full'],
            ),
        ),
        ),
    PluginMenuItem(
        link="plugins:bigipnetbox:pool_list",
        link_text="Pool",
        permissions=["bigipnetbox.admin_full"],
        buttons=(
            PluginMenuButton(
                link='plugins:bigipnetbox:pool_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['bigipnetbox.admin_full'],
            ),
        ),
        ),
    PluginMenuItem(
        link="plugins:bigipnetbox:virtualserver_list",
        link_text="Virtual Server",
        permissions=["bigipnetbox.admin_full"],
        buttons=(
            PluginMenuButton(
                link='plugins:bigipnetbox:virtualserver_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['bigipnetbox.admin_full'],
            ),
        ),
        ),
    PluginMenuItem(
        link="plugins:bigipnetbox:virtualaddress_list",
        link_text="Virtual Address",
        permissions=["bigipnetbox.admin_full"],
        buttons=(
            PluginMenuButton(
                link='plugins:bigipnetbox:virtualaddress_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['bigipnetbox.admin_full'],
            ),
        ),
        ),
    PluginMenuItem(
        link="plugins:bigipnetbox:poolmember_list",
        link_text="Pool Membro",
        permissions=["bigipnetbox.admin_full"],
        buttons=(
            PluginMenuButton(
                link='plugins:bigipnetbox:poolmember_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['bigipnetbox.admin_full'],
            ),
        ),
        ),
    PluginMenuItem(
        link="plugins:bigipnetbox:clusterf5_list",
        link_text="Clusterf5",
        permissions=["bigipnetbox.admin_full"],
        buttons=(
            PluginMenuButton(
                link='plugins:bigipnetbox:clusterf5_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['bigipnetbox.admin_full'],
            ),
        ),
        ),
    )
