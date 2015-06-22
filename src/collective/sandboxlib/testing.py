# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.sandboxlib


class CollectiveSandboxlibLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.sandboxlib)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.sandboxlib:default')


COLLECTIVE_SANDBOXLIB_FIXTURE = CollectiveSandboxlibLayer()


COLLECTIVE_SANDBOXLIB_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_SANDBOXLIB_FIXTURE,),
    name='CollectiveSandboxlibLayer:IntegrationTesting'
)


COLLECTIVE_SANDBOXLIB_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_SANDBOXLIB_FIXTURE,),
    name='CollectiveSandboxlibLayer:FunctionalTesting'
)


COLLECTIVE_SANDBOXLIB_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_SANDBOXLIB_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveSandboxlibLayer:AcceptanceTesting'
)
