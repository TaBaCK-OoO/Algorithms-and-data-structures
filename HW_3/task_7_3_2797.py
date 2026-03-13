import sys
"""
input.txt

5
978285527 979972887 979972887 964400127 978285527

"""
def main():
    with open("input.txt", "r") as f:
        input_data = f.read().split()
    if not input_data:
        return
    unique_contacts = set(input_data[1:])
    print(len(unique_contacts))

if __name__ == '__main__':
    main()