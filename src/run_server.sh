#!/bin/sh

INSTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $INSTDIR
SOURCEDIR="$(dirname "$INSTDIR")"
echo $SOURCEDIR

cd /opt
source FileKeeperEnv/bin/activate
cd $INSTDIR
start()
{
python3 manage.py runserver 0.0.0.0:9090
}
start
