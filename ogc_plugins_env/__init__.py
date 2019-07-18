""" OGC Env Plugin - environment variable discovery
"""

from ogc.state import app
from ogc.spec import SpecPlugin, SpecProcessException


class Env(SpecPlugin):
    """ OGC Env Plugin

    [Env]
    # OGC Env looks for environment variables in the following order
    # 1. Parses current host ENV
    # 2. Checks for a .env in the cwd, merging left and overwriting vars from #1
    # 3. Checks for `properties_file`, merging left overwriting vars from #1 and #2
    # Test plans require certain environment variables to be set prior to running.
    # This module allows us to make sure those requirements are met before
    # proceeding.
    requires = ["CHARMCREDS", "JUJUCREDS"]

    # Optionally, define a location of KEY=VALUE line items to use as this specs
    # environment variables. This will meld into host environment updating any variables overlapping
    properties_file = "/home/user/env.properties"

    # Convert certain spec options to ane environment variable, these variables
    # will be set in the host environment in the form of VAR=VAL. Note: this
    # will convert the dot '.' notation to underscores
    add_to_env = ['Juju.cloud', 'Juju.controller']

    """

    friendly_name = "Env Plugin"
    slug = "env-plugin"
    options = [("requires", False), ("properties_file", False)]

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
                f"{self.friendly_name} - {env_differ} not found in host environment. Did you forget to add them to `add_to_env`?"
            )
