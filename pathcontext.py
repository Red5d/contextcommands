#! /usr/bin/env python

import os, sys, importlib, fnmatch


os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
modules = {}
paths = {}
for module in os.listdir('pathmodules'):
    if module.endswith(".py") and module != "__init__.py":
        module = module.split('.')[0]
        modules[module] = importlib.import_module("pathmodules."+module)
        for modpath in modules[module].paths():
            paths[modpath] = module

sys.argv.pop(0)
path = sys.argv.pop(0)
word = sys.argv[0]

nocmd = "false"

for pathmatch in list(paths.keys()):
    if fnmatch.fnmatch(path, pathmatch):
        target = modules[paths[pathmatch]]

cmd = target.context(path, word)
if cmd != None:
    print(cmd)
    sys.exit(0)
else:
    print(nocmd)
    sys.exit(1)
