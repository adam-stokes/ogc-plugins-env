"""
---
targets: ['docs/plugins/env.md']
---
"""

import textwrap
from ogc.state import app
from ogc.spec import SpecPlugin, SpecProcessException


class Env(SpecPlugin):
    """ OGC Env Plugin

    """

    friendly_name = "OGC Env Plugin"
    description = "Environment variable discovery"
    options = [
        {
            "key": "requires",
            "required": False,
            "description": "Environment variables that need to exist before the spec can be run",
        },
        {
            "key": "properties_file",
            "required": False,
            "description": "A path to a DotEnv or the like for loading environment variables",
        },
    ]

    def conflicts(self):
        """ Handles any environment conflicts
        """
        # Parse requirements
        check_requires = self.get_spec_option("Env.requires")
        check_requires = [item.replace(".", "_").upper() for item in check_requires]
        existing_env_vars = [*app.env]
        if check_requires and not set(check_requires) < set(existing_env_vars):
            env_differ = ", ".join(
                list(set(check_requires).difference(existing_env_vars))
            )
            raise SpecProcessException(
                f"{self.friendly_name} - {env_differ} not found in host environment. See `ogc spec-doc Env`."
            )

    @classmethod
    def doc_example(cls):
        return textwrap.dedent(
            """
        ## Example

        ```toml
        [Env]
        requires = ["CHARMCREDS", "JUJUCREDS"]

        properties_file = "/home/user/env.properties"

        add_to_env = ['Juju.cloud', 'Juju.controller']
        ```
        """
        )


__class_plugin_obj__ = Env
