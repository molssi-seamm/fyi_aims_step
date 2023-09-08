# -*- coding: utf-8 -*-

"""
fhi_aims_step
A SEAMM plug-in for FHI-aims
"""

# Bring up the classes so that they appear to be directly in
# the fhi_aims_step package.

from .fhi_aims import FHIaims  # noqa: F401, E501
from .fhi_aims_step import FHIaimsStep  # noqa: F401, E501
from .tk_fhi_aims import TkFHIaims  # noqa: F401, E501

from .metadata import metadata  # noqa: F401

# Handle versioneer
from ._version import get_versions

__author__ = "Paul Saxe"
__email__ = "psaxe@molssi.org"
versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
