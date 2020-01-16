# CipherAvalancheEffect

Application for testing and measuring the Avalanche effect for the AES-128 ciphers.

## Getting Started

These instructions will help generate ciphertext in hex using AES-128 cipher and calculate the Avalanche effects via XOR comparison that will also provide a CSV file.

## Prerequisite

* Python2

## Calculate the Avalanche effect via XOR comparison

The main script that will perform the XOR comparison of the provided ciphertext (hex), is `avalancheeffect.py`. This can be done in 2 ways using: command line arguments or input files.

> You can create a CSV file with the relevant data by passing the `-o <csv_filename>` argument.
> The CSV file can be used to extract data easily.

### Using command line arguments

To use command line arguments, the script requires both `-b` (base hex) and `-u` (updated hex) arguments.
`-u` argument may contain more than 1 hex to compare to the base hex.

```
python avalancheeffect.py -b 492b32c51c863800deec39dbc2b617b7 -u D1E2A35FBA509B6432EDB96D850E119F b7d423ee14465b3535496db91e2b7056
```

### Using input files

To use the input files, the file just contain more than one hex values separated by newline.
The script with take the first line hex as the base and the rest as the updated hex values.

```
python avalancheeffect.py -i ptupdated -o whatever.csv
```

## Running the tests

All the test data and results are provided in the `Test Data` folder.

If you wish to use other test data and generate a new result, you can use the `generate_avalanche_result.sh`.

### Generate the AES-128 ciphertext in hex and calculate the Avalanche effect

`generate_avalanche_result.sh` will consume the `plaintext_list` and `key_list` to output a file with the AES-128 ciphertext in hex.

Afterwards, it will execute the `avalancheeffect.py` script to generate the CSV for the Avalanche effect data.

## Author

**Gabriel Lee** - [ScrawnySquirrel](https://github.com/ScrawnySquirrel)
