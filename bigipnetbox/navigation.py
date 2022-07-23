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
        link="plugins:bigipnetbox:status",
        link_text="Status",
        permissions=["bigipnetbox.admin_full"],
        buttons=(
            PluginMenuButton(
                link="plugins:bigipnetbox:sync_full",
                title="Settings",
                icon_class="mdi mdi-all-inclusive",
                color=ButtonColorChoices.BLUE,
                permissions=["bigipnetbox.admin_full"],
            ),
            PluginMenuButton(
                link="plugins:bigipnetbox:settings",
                title="Settings",
                icon_class="mdi mdi-cog",
                color=ButtonColorChoices.BLUE,
                permissions=["bigipnetbox.admin_full"],
            ),
        ),
    ),
)