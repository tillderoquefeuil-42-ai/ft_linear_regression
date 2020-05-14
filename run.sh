#!/bin/bash

echo "Install dependencies (numpy, pandas, matplotlib)?[Y/N]"
read d_install

if [ $d_install = "Y" ]; then
    echo "installing numpy ..."
    pip3 install numpy -q
    echo "done."
    echo "installing pandas ..."
    pip3 install pandas -q
    echo "done."
    echo "installing matplotlib ..."
    pip3 install matplotlib -q
    echo "done."
fi

echo "Run program?[Y/N]"
read p_run

if [ $p_run = "Y" ]; then
    python3 main.py
fi