#!/bin/bash

# Copyright (C) 2020 by sandy1709

echo "
                 ____  __ __ _____   __________ 
                / __ \/ //_//  _/ | / /  _/ __ \ 
               / / / / ,<   / //  |/ // // / / /
              / /_/ / /| |_/ // /|  // // /_/ / 
              \____/_/ |_/___/_/ |_/___/\____/ \n\n"

FILE=/app/.git

if [ -d "$FILE" ] ; then
    echo "$FILE directory exists already."
else
    rm -rf userbot
    rm -rf .github
    rm -rf requirements.txt
    git clone https://github.com/allianceprojects/catuserbot cat_ub
    mv cat_ub/userbot .
    mv cat_ub/.github . 
    mv cat_ub/.git .
    mv cat_ub/requirements.txt .
    rm -rf cat_ub
    python ./.github/update.py
fi

FILE=/app/bin/
if [ -d "$FILE" ] ; then
    echo "$FILE directory exists already."
else
    bash ./.github/bins.sh
fi

python -m userbot
