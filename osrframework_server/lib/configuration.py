# -*- coding: utf-8 -*-
#
################################################################################
#
#   Copyright 2017 Félix Brezo and Yaiza Rubio
#       (i3visio, contacto@i3visio.com)
#
#   This file is part of osrframework_server. You can redistribute it and/or
#   modify it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the License,
#   or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful, but WITHOUT
#   ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#   FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License
#   for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import ConfigParser
import os
import pkg_resources
from shutil import copyfile

from osrframework.utils.general import error, warning, success, info, title, emphasis
import osrframework.utils.configuration as configuration


def getConfiguration(configuration_file="server.cfg", package="osrframework_server", section="osrframework_server"):
    """
    Method that recovers the configuration information osrframework_server.

    TODO: Grab the default file from the package data instead of storing it in the main folder.

    Args:
    -----
        configuration_file: The configuration file to be read.
        package: The package name where the default files are stored.
        section: The secction's name that will be read.

    Returns:
    --------
        A dictionary containing the default configuration.
    """

    VALUES = {}

    # If a api_keys.cfg has not been found, creating it by copying from default
    configPath = os.path.join(configuration.getConfigPath()["appPath"], configuration_file)

    # Checking if the configuration file exists
    if not os.path.exists(configPath):
        print(warning("[*] No configuration files found for OSRFramework Server."))
        print(warning("[*] Copying default configuration files to OSRFramework configuration folder at '" + configPath + "'."))

        # Copy the data from the default folder
        defaultConfigPath = pkg_resources.resource_filename(package, os.path.join('config', configuration_file))
        copyfile(defaultConfigPath, configPath)

    # Reading the configuration file
    config = ConfigParser.ConfigParser()
    config.read(configPath)

    # Iterating through all the sections, which contain the platforms
    for s in config.sections():
        incomplete = False
        if s.lower() == section.lower():
            # Iterating through parameters
            for (param, value) in config.items(s):
                if value != '':
                    VALUES[param] = value

    return VALUES
