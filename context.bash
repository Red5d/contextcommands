#! /bin/bash

c() {
  cd ~/.local/bin/contextcommands
  cmd=$(lastcmd=$(history 2 | head -1 | cut -d ' ' -f 2-); python context.py $1 $lastcmd)
  if [[ $cmd != echo* ]];then
    echo $cmd
  fi

  history -s "$cmd"
  eval "$cmd"
}
