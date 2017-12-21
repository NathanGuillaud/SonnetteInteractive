#!/bin/bash
./gdrive mkdir "$2"
id=`./gdrive list -q "name contains '$2'" | sed '1d' | cut -d " " -f 1`

./gdrive upload -p "$id" "$1"
