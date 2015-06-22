# -*- coding: utf-8 -*-
"""Init and utils."""

from AccessControl import allow_class, ModuleSecurityInfo
from Products.PythonScripts.Utility import allow_module
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.sandboxlib')

allow_module('collective.sandboxlib')
