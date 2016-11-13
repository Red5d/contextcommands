#! /bin/bash

mkdir ~/.local/bin/contextcommands
cp -r -t ~/.local/bin/contextcommands context.bash context.py modules

echo "Add the following line to your ~/.bashrc file:"
echo
echo "source ~/.local/bin/contextcommands/context.bash"
echo

