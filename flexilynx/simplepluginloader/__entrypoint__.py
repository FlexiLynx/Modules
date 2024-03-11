#!/bin/python3

#> Imports
from FlexiLynx.core.frameworks.plugin import Plugin, loader
#</Imports

#> Header
#</Header

#> Main >/
class SimplePluginLoader(loader.BasePluginLoader):
    '''Loads simple Python plugins'''

    def load(self, plugin: Plugin):
        '''
            Loads the plugin, importing its entrypoint if present
                and calling its entrypoint's `__load__()` function if present
        '''
        ...
    def setup(self, plugin: Plugin):
        '''
            Loads the plugin, importing its entrypoint if present
                and calling its entrypoint's `__setup__()` function if present
        '''
        ...
