from extras.plugins import PluginConfig
from .version import __version__


class BigipnetboxConfig(PluginConfig):
    name = 'bigipnetbox'
    verbose_name = "BigIP Sync Plugin"
    description = ''
    version = __version__
    author = ''
    author_email = ''
    required_settings = []
    default_settings = {}


config = BigipnetboxConfig # noqa
