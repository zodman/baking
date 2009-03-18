#!bash

where="ssh fdev.foresightlinux.org rmake"
#where=rmake
context="fl:2-devel"
recipes="$1{x86} $1{x86_64}"
notify-send -t 5000  "Doing bake remote" "Pkg: $1"
result=`$where build --quiet --context \"$context\" $recipes `
#result=222
status=`$where q $result`
echo $status
notify-send -t 7000 "Bake $1 finished" "$status"

