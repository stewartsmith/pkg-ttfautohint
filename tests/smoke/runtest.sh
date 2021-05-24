#!/bin/bash

# If one of the commands below returns non-zero then exit immediately
set -e

cd ../source

wget https://releases.pagure.org/lohit/lohit-devanagari-2.95.4.tar.gz
tar -xzvf ./lohit-devanagari-2.95.4.tar.gz
cd lohit-devanagari-2.95.4
make ttf
old_size=`stat -c "%s" /usr/share/fonts/lohit-devanagari/Lohit-Devanagari.ttf`
new_size=`stat -c "%s" Lohit-Devanagari.ttf`
if [ $old_size -ne $new_size ]; then
        echo "FAILED: ttfautohint generated different ttf file"
else
        echo "PASSED: ttfautohint generated same ttf file"
fi
