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
        ),
    PluginMenuItem(
        link="plugins:bigipnetbox:pool_list",
        link_text="Pool",
        permissions=["bigipnetbox.admin_full"],
        ),
    PluginMenuItem(
        link="plugins:bigipnetbox:virtualserver_list",
        link_text="Virtual Server",
        permissions=["bigipnetbox.admin_full"],
        ),
    )
