"""
---
targets: ['docs/plugins/env.md']
---
"""

import textwrap
from ogc.state import app
from ogc.spec import SpecPlugin, SpecProcessException


__version__ = "1.0.1"
__author__ = "Adam Stokes"
__author_email__ = "adam.stokes@gmail.com"
__maintainer__ = "Adam Stokes"
__maintainer_email__ = "adam.stokes@gmail.com"
__description__ = "ogc-plugins-env, a ogc plugin for environment discovery"
__git_repo__ = "https://github.com/battlemidget/ogc-plugin-env"

__example__ = """
## Example

```yaml
setup:
  - env:
      requires: [CHARMCREDS, JUJUCREDS]
      properties-file: "/home/user/env.properties"
```
"""


class Env(SpecPlugin):
    """ OGC Env Plugin

    """

    friendly_name = "OGC Env Plugin"
    options = [
        {
            "key": "requires",
            "required": False,
            "description": "Environment variables that need to exist before the spec can be run",
        },
        {
            "key": "properties-file",
            "required": False,
            "description": "A path to a DotEnv or the like for loading environment variables",
        },
    ]

    def __str__(self):
        return __description__

    def conflicts(self):
        """ Handles any environment conflicts
        """
        # Parse requirements
        check_requires = self.opt("requires")
        check_requires = [item.replace(".", "_").upper() for item in check_requires]
        existing_env_vars = [*app.env]
        if check_requires and not set(check_requires) < set(existing_env_vars):
            env_differ = ", ".join(
                list(set(check_requires).difference(existing_env_vars))
            )
            raise SpecProcessException(
                f"{self.friendly_name} - {env_differ} not found in host environment. See `ogc spec-doc Env`."
            )


__class_plugin_obj__ = Env
