#!/bin/bash

echo "Install dependencies (numpy, pandas, matplotlib)?[Y/N]"
read d_install

if [ -z "$d_install" ] || [ $d_install == "Y" ]; then
    echo "installing numpy ..."
    pip3 install numpy -q
    echo "done."
    echo "\ninstalling pandas ..."
    pip3 install pandas -q
    echo "done."
    echo "\ninstalling matplotlib ..."
    pip3 install matplotlib -q
    echo "done."
fi

echo "\n\nRun program?[Y/N]"
read p_run

if [ -z "$p_run" ] || [ $p_run == "Y" ]; then
    python3 main.py
fi