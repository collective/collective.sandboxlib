# -*- coding: utf-8 -*-
"""Init and utils."""

from AccessControl import allow_class, ModuleSecurityInfo
from Products.PythonScripts.Utility import allow_module
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.sandboxlib')

# Whitelist pdf functions
allow_module('pretaweb.plomino2pdf.api')
pdf_api = ModuleSecurityInfo('pretaweb.plomino2pdf.api')
pdf_api.declarePublic('generate_pdf')
