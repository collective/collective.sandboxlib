# -*- coding: utf-8 -*-
"""Init and utils."""

from AccessControl import allow_class, ModuleSecurityInfo
from Products.PythonScripts.Utility import allow_module
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.sandboxlib')

allow_module('collective.sandboxlib')

sandbox = ModuleSecurityInfo('collective.sandboxlib')

# Whitelist pdf functions
allow_module('collective.sandboxlib.pdf')
pdf_api = ModuleSecurityInfo('collective.sandboxlib.pdf')
pdf_api.declarePublic('generate_pdf')
