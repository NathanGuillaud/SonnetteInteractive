#!/bin/bash
a=`./gdrive list -q "name contains 'Rep2'" | cut -d " " -f 1`
echo $a
