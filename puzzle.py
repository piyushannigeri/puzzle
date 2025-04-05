# Stage 2: Requires solution from Stage 1
number = int(input("Enter the Stage 1 solution: "))

# Binary reversal logic
binary_str = bin(number)[2:]
reversed_binary = binary_str[::-1]
new_number = int(reversed_binary, 2)

# URL generation
url_fragment = chr(ord('a') + new_number) + hex(number)[2:]
base_url = "https://yourusername.github.io/engineering-puzzle/"
print(f"Next clue: {base_url}{url_fragment}")
