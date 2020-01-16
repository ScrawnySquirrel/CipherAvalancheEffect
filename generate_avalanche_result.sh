#!/bin/bash

while read p; do echo "$p" | openssl aes-128-cbc -K 00000000000000000000000000000000 -iv 00000000000000000000000000000000 | xxd -p -c 256 >> pthash; done < plaintext_list
while read p; do echo "ooooooooooooooooooooooooooooo" | openssl aes-128-cbc -K $p -iv 00000000000000000000000000000000 | xxd -p -c 256 >> khash; done < key_list
python avalancheeffect.py -i pthash -o pt_avalance.csv
python avalancheeffect.py -i khash -o k_avalanche.csv
