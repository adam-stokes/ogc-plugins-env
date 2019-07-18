# ogc-plugin-env

env checker for ogc

# usage

In a ogc spec, place the following:

```toml
[Env]
# Test plans require certain environment variables to be set prior to running.
# This module allows us to make sure those requirements are met before
# proceeding.
requires = ["CHARMCREDS", "JUJUCREDS"]

# Optionally, define a location of KEY=VALUE line items to use as this specs
# environment variables
properties-file = "/home/user/env.properties"
```
