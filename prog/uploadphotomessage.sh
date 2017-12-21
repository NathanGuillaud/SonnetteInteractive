
#!/bin/bash
./gdrive mkdir "$3"
id=`./gdrive list -q "name contains '$3'" | sed '1d' | cut -d " " -f 1`

./gdrive upload -p "$id" "$1"
./gdrive upload -p "$id" "$2"
