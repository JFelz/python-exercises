import random

char_list = ["A", "a","B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z",
];

num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

sym_list = ["#", "!", "$"]

print("Welcome to Jovanni\'s Password Generator")

char = int(input("How many letters do you want?"))
numb = int(input("How many numbers do you want?"))
sym = int(input("How many symbols do you want?"))


keygen = ""

for i in range(0, char):
	random_num = random.randint(0, len(char_list) + 1)
	keygen += char_list[random_num]

for i in range(0, numb):
	random_num = random.randint(0, len(num_list) + 1)
	keygen += num_list[random_num]

for i in range(0, len(sym_list) - 1):
	random_num = random.randint(0, len(sym_list) - 1)
	keygen += sym_list[random_num]

print(keygen)
