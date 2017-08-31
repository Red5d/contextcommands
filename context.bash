#! /bin/bash

c() {
  cmd=$(lastcmd=$(history 2 | head -1 | awk '{$1=""; print $0}'); python $(dirname $0)/context.py $1 $lastcmd)
  if [[ "$cmd" != "false" ]];then
    echo "$cmd"
  fi

  if [ "$cmd" != "false" ];then
    history -s "$cmd"
    eval "$cmd"
  else
    echo "No context commands found."
  fi
}
