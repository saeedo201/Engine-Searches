#! /bin/bash
#colors
g='\033[1;32m'
p='\033[1;35m'
cyan='\033[1;36m'
green='\033[1;32m'
red='\033[1;31m'
yellow='\033[1;33m'
blue='\033[1;34m'
purple='\033[1;35m'
reset='\033[0m'
y='\033[1;33m'
sleep 1
 clear
#welcome
	echo """
        +=========================================+
        |..........   Wellcome Guys    ...........|
        +-----------------------------------------+
"""
printf $y
echo -e " Now You Need Install This Library ::search_engie_parser::"
sleep 0.5
printf $reset
read -p " Do you want to install this library [y/n] : " choice
if [[ $choice == "y" ]]; then
clear
sleep 1
echo -e "$g+++++++++++++++>$p[Please Wait]$g<+++++++++++++++++"
pip install search_engine_parser -y
sleep 0.9
clear
printf "\e[1;45m Well Done!  \e[0m\n"
printf "\e[1;45m Just Type python engine.py -h for more help \e[0m\n"
cd $HOME/Engine-Searches && mv .engine.py engine.py && rm start.sh && python engine.py
fi
if [[ $choice == "n" ]]; then 
clear
printf $red
echo -e "If You Dont Install This Libarary u cant run this tool"
fi
