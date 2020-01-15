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
    uhashlist = [x.strip() for x in content]
    # Pop base ciphertext from file and convert base hex to binary without the integer literals
    bhash = bin(int(uhashlist.pop(0), 16))[2:]
else:
    # Convert base hex to binary without the integer literals
    bhash = bin(int(args.base, 16))[2:]
    uhashlist = args.updated

for updatedhash in uhashlist:
    # Convert updated hex to binary without the integer literals
    uhash = bin(int(updatedhash, 16))[2:]

    # Perform XOR comparison on binary values and output to screen
    print('{0:0{1}b}'.format(int(bhash,2) ^ int(uhash, 2), len(bhash)))

    # Print how many bits have been changed compared to the base
    xorres = '{0:0{1}b}'.format(int(bhash,2) ^ int(uhash, 2), len(bhash))
    print("Bits changed: {} out of {}".format(xorres.count("1"), len(bhash)))
