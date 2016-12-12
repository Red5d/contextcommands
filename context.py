#! /usr/bin/env python

import os, sys, importlib


modules = {}
for module in os.listdir('modules'):
    if module.endswith(".py"):
        module = module.split('.')[0]
        modules[module] = importlib.import_module("modules."+module)

sys.argv.pop(0)
word = sys.argv.pop(0)
lastcmd = sys.argv

nocmd = "false"

try:
    list(modules.keys()).index(lastcmd[0])
    target = lastcmd[0]
except (ValueError, IndexError):
    try:
        list(modules.keys()).index(lastcmd[1])
        target = lastcmd[1]
    except (ValueError, IndexError):
        print(nocmd)
        sys.exit(1)

cmd = modules[target].context(lastcmd, word)
if cmd != None:
    print(cmd)
    sys.exit(0)
else:
    print(nocmd)
    sys.exit(1)
