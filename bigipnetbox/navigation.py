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
        link="plugins:bigipnetbox:node",
        link_text="Node",
        permissions=["bigipnetbox.admin_full"],
        buttons=(
            PluginMenuButton(
                link="plugins:bigipnetbox:sync_full",
                title="Node",
                icon_class="mdi mdi-all-inclusive",
                color=ButtonColorChoices.BLUE,
                permissions=["bigipnetbox.admin_full"],
            ),
            PluginMenuButton(
                link="plugins:bigipnetbox:settings",
                title="Node",
                icon_class="mdi mdi-cog",
                color=ButtonColorChoices.BLUE,
                permissions=["bigipnetbox.admin_full"],
            ),
        ),
    ),
)