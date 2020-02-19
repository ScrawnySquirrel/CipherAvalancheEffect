import argparse

# Define script description and the arugment list
parser = argparse.ArgumentParser(description='Perform XOR comparision of 2 hashes to calculate the Avalanche Effect.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-b', '--base', help='the base ciphertext to compare to the updated ciphertext(s)')
parser.add_argument('-u', '--updated', nargs='+', help='the updated ciphertext(s)')
group.add_argument('-i', '--input', help='name of the input file (newline separated); uses the first line as the base ciphertext')
parser.add_argument('-o', '--output', help='name of the output CSV file')
args = parser.parse_args()

# Use file or argument provided ciphertext
if args.input is not None:
    with open(args.input) as f:
        content = f.readlines()
    updated_hex_list = [x.strip() for x in content]
    # Pop base ciphertext from file and convert base hex to binary without the integer literals
    base_hex = updated_hex_list.pop(0)
    base_binary = bin(int(base_hex, 16))[2:]
else:
    # Convert base hex to binary without the integer literals
    base_hex = args.base
    base_binary = bin(int(args.base, 16))[2:]
    updated_hex_list = args.updated

# Create and open CSV file for writing
if args.output is not None:
    f = open(args.output, "w")
    f.write("round,base_hex,base_binary,updated_hex,updated_binary,xor_binary,changed_bit_count,length,percentage\n")

bin_len = len(base_binary)
round_count = 1

for updated_hex in updated_hex_list:
    print("Round: {}".format(round_count))
    # Convert updated hex to binary without the integer literals
    updated_binary = bin(int(updated_hex, 16))[2:]

    # Perform XOR comparison on binary values and output to screen
    xor_binary = '{0:0{1}b}'.format(int(base_binary,2) ^ int(updated_binary, 2), len(base_binary))
    print("XOR Result: {}".format(xor_binary))
    changed_bit_count = xor_binary.count("1")

    # Print how many bits have been changed compared to the base
    print("Bits changed: {} out of {}".format(changed_bit_count, len(base_binary)))

    # Output to CSV file if specified
    if args.output is not None:
        f.write("{},{},{},{},{},{},{},{},{:.2f}%\n".format(round_count, base_hex, base_binary, updated_hex, updated_binary, xor_binary, changed_bit_count, bin_len, float(changed_bit_count) / float(bin_len) * 100))
    round_count += 1

if args.output is not None:
    f.close()
