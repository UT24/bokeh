# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2019, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Boilerplate
# -----------------------------------------------------------------------------
import pytest  # noqa isort:skip

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Bokeh imports
from bokeh._testing.util.api import verify_all

# Module under test
# import bokeh.sampledata.us_cities as bsu # isort:skip

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

ALL = ("data",)

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------

Test___all__ = pytest.mark.sampledata(verify_all("bokeh.sampledata.us_cities", ALL))


@pytest.mark.sampledata
def test_data():
    import bokeh.sampledata.us_cities as bsu

    assert isinstance(bsu.data, dict)

    # don't check detail for external data


# -----------------------------------------------------------------------------
# Dev API
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Private API
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Code
# -----------------------------------------------------------------------------