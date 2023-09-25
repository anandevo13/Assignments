"""
Q. Python function to print reverse of a binary representation of a given number
"""

def reverseBits(num, bitSize):
    binary = bin(num)
    reverse = binary[-1:1:-1]
    reverse = reverse + (bitSize - len(reverse))*'0'
    print(int(reverse,2))
    
# Driver program
if __name__ == "__main__":
    num = 1
    bitSize = 32
    reverseBits(num, bitSize)
    

# Another Method:
def reverse_bits(number, bit_size):
    max_value = (1 << bit_size) - 1
    return max_value - number

if __name__ == "__main__":
    num = 156
    size = 32
    print("Reverse bits of {} is {}".format(bin(num), reverse_bits(num , size)))