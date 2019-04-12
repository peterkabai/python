# Basic colors
purple = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'

# Styles
bold = '\033[1m'
line = '\033[4m'
reverse = '\033[07m'

# Reset Code
reset = '\033[0m'
        
if __name__ == '__main__':
    print(purple, "Hello, World", reset, sep="")
    print(blue, "Hello, World", reset, sep="")
    print(green, "Hello, World", reset, sep="")
    print(yellow, "Hello, World", reset, sep="")
    print(red, "Hello, World", reset, sep="")
    print(bold, "Hello, World", reset, sep="")
    print(line, "Hello, World", reset, sep="")
    print(reverse, "Hello, World", reset, sep="")