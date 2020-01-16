#!/bin/bash

while read p; do echo "$p" | openssl aes-128-cbc -K 00000000000000000000000000000000 -iv 00000000000000000000000000000000 | xxd -p -c 256 >> test_data/pthash; done < test_data/plaintext_list
while read p; do echo "ooooooooooooooooooooooooooooo" | openssl aes-128-cbc -K $p -iv 00000000000000000000000000000000 | xxd -p -c 256 >> test_data/khash; done < test_data/key_list
python avalancheeffect.py -i test_data/pthash -o test_data/pt_avalanche.csv
python avalancheeffect.py -i test_data/khash -o test_data/k_avalanche.csv
