#! /bin/bash

c() {
  cmd=$(lastcmd=$(HISTTIMEFORMAT="" history 2 | head -1 | awk '{$1=""; print $0}'); python $(dirname $0)/context.py $1 $lastcmd)
  if [[ "$cmd" != "false" ]];then
    echo "$cmd"
  else
    cmd=$(python ~/.local/bin/contextcommands/pathcontext.py $(pwd) $1)
    if [[ "$cmd" != "false" ]];then
      echo "$cmd"
    fi
  fi

  #cd - 1>/dev/null
  #OLDPWD="$oldpwd"
  if [ "$cmd" != "false" ];then
    history -s "$cmd"
    eval "$cmd"
  else
    echo "No context commands found."
  fi
}
