""" OGC Env Plugin - environment variable discovery
"""

import os
import click
import sys
from dotenv.main import DotEnv
from pprint import pformat
from melddict import MeldDict
from pathlib import Path
from ogc import log
from ogc.spec import SpecPlugin


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
    """

    NAME = "Env Plugin"
    options = [("requires", True), ("properties_file", False)]

    def __load_dotenv(self, env, path):
        if not path.exists():
            return env
        _merge_env = DotEnv(dotenv_path=path, encoding="utf8").dict()
        return env + _merge_env

    def process(self):
        """ Processes env options
        """
        env = MeldDict(os.environ.copy())
        check_requires = self.get_option("requires")

        # Check for a relative .env and load thoes
        relative_env_path = Path(".") / ".env"
        env = self.__load_dotenv(env, relative_env_path)
        properties_file = self.get_option("properties_file")
        if properties_file:
            env = self.__load_dotenv(env, Path(properties_file))
        log.debug(f"{self.NAME} - requires {', '.join(check_requires)}")
        log.debug(f"{self.NAME} - testing against\n  {pformat(env)}")
        if check_requires and not set(check_requires) < set(env):
            env_differ = ", ".join(list(set(check_requires).difference(env)))
            log.error(f"{self.NAME} - {env_differ} not found in host environment")
            sys.exit(1)
        return
