#!/bin/bash

printf "Install dependencies (numpy, pandas, matplotlib)?[Y/N]"
read d_install

if [ -z "$d_install" ] || [ $d_install == "Y" ]; then
    printf "installing numpy ..."
    pip3 install numpy -q
    printf "done."
    printf "\ninstalling pandas ..."
    pip3 install pandas -q
    printf "done."
    printf "\ninstalling matplotlib ..."
    pip3 install matplotlib -q
    printf "done."
fi

printf "\n\nRun program?[Y/N]"
read p_run

if [ -z "$p_run" ] || [ $p_run == "Y" ]; then
    python3 main.py
fi