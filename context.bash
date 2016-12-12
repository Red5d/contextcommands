#! /bin/bash

c() {
  oldpwd="$OLDPWD"
  cd ~/.local/bin/contextcommands
  cmd=$(lastcmd=$(history 2 | head -1 | awk '{$1=""; print $0}'); python context.py $1 $lastcmd)
  if [[ "$cmd" != "false" ]];then
    echo "$cmd"
  fi

  cd - 1>/dev/null
  OLDPWD="$oldpwd"
  if [ "$cmd" != "false" ];then
    history -s "$cmd"
    eval "$cmd"
  else
    echo "No context commands found."
  fi
}
