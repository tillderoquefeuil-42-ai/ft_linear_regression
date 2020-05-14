#!/bin/bash

printf "Install dependencies (numpy, pandas, matplotlib)?[Y/N]"
read d_install

if [ -z "$d_install" ] || [ $d_install == "Y" ]; then
    printf "\nInstalling numpy ..."
    pip3 install numpy -q
    printf " Done.\nInstalling pandas ..."
    pip3 install pandas -q
    printf " Done.\nInstalling matplotlib ..."
    pip3 install matplotlib -q
    printf " Done."
fi

printf "\n\nRun program?[Y/N]"
read p_run

if [ -z "$p_run" ] || [ $p_run == "Y" ]; then
    python3 main.py
fi