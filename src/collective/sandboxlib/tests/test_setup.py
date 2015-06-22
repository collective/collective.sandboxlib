# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.sandboxlib.testing import COLLECTIVE_SANDBOXLIB_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.sandboxlib is properly installed."""

    layer = COLLECTIVE_SANDBOXLIB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.sandboxlib is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.sandboxlib'))

    def test_uninstall(self):
        """Test if collective.sandboxlib is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.sandboxlib'])
        self.assertFalse(self.installer.isProductInstalled('collective.sandboxlib'))

    def test_browserlayer(self):
        """Test that ICollectiveSandboxlibLayer is registered."""
        from collective.sandboxlib.interfaces import ICollectiveSandboxlibLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveSandboxlibLayer, utils.registered_layers())
