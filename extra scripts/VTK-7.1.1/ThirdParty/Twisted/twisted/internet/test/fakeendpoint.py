# -*- test-case-name: twisted.internet.test.test_endpoints -*-
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Fake client and server endpoint string parser plugins for testing purposes.
"""

from zope.interface.declarations import implementer
from twisted.plugin import IPlugin
from twisted.internet.interfaces import (
    IStreamClientEndpoint, IStreamServerEndpoint,
    IStreamClientEndpointStringParser, IStreamServerEndpointStringParser,
    IStreamClientEndpointStringParserWithReactor)


@implementer(IPlugin)
class PluginBase(object):

    def __init__(self, pfx):
        self.prefix = pfx



@implementer(IStreamClientEndpointStringParser)
class FakeClientParser(PluginBase):

    def parseStreamClient(self, *a, **kw):
        return StreamClient(self, a, kw)



@implementer(IStreamClientEndpointStringParserWithReactor)
class FakeClientParserWithReactor(PluginBase):

    def parseStreamClient(self, *a, **kw):
        return StreamClient(self, a, kw)



@implementer(IStreamServerEndpointStringParser)
class FakeParser(PluginBase):

    def parseStreamServer(self, *a, **kw):
        return StreamServer(self, a, kw)



class EndpointBase(object):

    def __init__(self, parser, args, kwargs):
        self.parser = parser
        self.args = args
        self.kwargs = kwargs



@implementer(IStreamClientEndpoint)
class StreamClient(EndpointBase):
    pass



@implementer(IStreamServerEndpoint)
class StreamServer(EndpointBase):
    pass



# Instantiate plugin interface providers to register them.
fake = FakeParser('fake')
fakeClient = FakeClientParser('cfake')
fakeClientWithReactor = FakeClientParserWithReactor('crfake')
fakeClientWithoutPreference = FakeClientParser('cpfake')
fakeClientWithReactorAndPreference = FakeClientParserWithReactor('cpfake')
