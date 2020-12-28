#!/bin/bash

# Copyright (C) 2020

echo "



            ____  __ __ _____   __________ 
           / __ \/ //_//  _/ | / /  _/ __ \ 
          / / / / ,<   / //  |/ // // / / /
         / /_/ / /| |_/ // /|  // // /_/ / 
         \____/_/ |_/___/_/ |_/___/\____/



"

FILE=/app/.git

if [ -d "$FILE" ] ; then
    echo "$FILE direktory sudah ada."
else
    rm -rf userbot
    rm -rf .github
    rm -rf requirements.txt
    git clone https://github.com/allianceprojects/alliance-master cat_ub
    mv cat_ub/userbot .
    mv cat_ub/.github . 
    mv cat_ub/.git .
    mv cat_ub/requirements.txt .
    rm -rf cat_ub
    python ./.github/update.py
fi

FILE=/app/bin/
if [ -d "$FILE" ] ; then
    echo "$FILE direktory sudah ada."
else
    bash ./.github/bins.sh
fi

python -m userbot
