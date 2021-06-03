# Copyright 2021, The Emissions API Developers
# https://emissions-api.org
# This software is available under the terms of an MIT license.
# See LICENSE fore more information.

import os

import yaml


__config = {}
__files = None


class NotInitializedError(Exception):
    """Raised if the module was not initialized."""

    def __init__(
        self, msg="Module was not initialized. Please call `init` before usage."
    ):
        super().__init__(msg)


def init(*configuration_files):
    """Initialize the configuration file.

    :param *configuration_files: Configuration file locations.
                                 The locations are taken into consideration in
                                 the given order.
    :type *configuration_files: list
    """
    globals()["__files"] = configuration_files


def __configuration_file():
    """Find the best match for the configuration file.
    :return: configuration file name or None
    """
    for f in __files:
        f = os.path.expanduser(f)
        if os.path.isfile(f):
            return f


def __update_configuration():
    """Update configuration."""
    cfgfile = __configuration_file()
    if not cfgfile:
        return {}
    with open(cfgfile, "r") as f:
        cfg = yaml.safe_load(f)
    globals()["__config"] = cfg
    return cfg


def config(*keys):
    """Get a specific configuration value or the whole configuration, loading
    the configuration file if it was not before.
    :param keys: optional list of configuration keys to return
    :type keys: list
    :return: dictionary containing the configuration or configuration value
    """
    if __files is None:
        raise NotInitializedError
    cfg = __config or __update_configuration()
    for key in keys:
        if cfg is None:
            return
        cfg = cfg.get(key)
    return cfg
