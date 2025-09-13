alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(dir, text, shift):
    if dir == "encode":
        for i in text.lower():
            encr_num_pos = alphabet.index(i) + shift
            encr_num_pos %= len(alphabet)
            shifted_pos = alphabet[encr_num_pos]
            print(shifted_pos)

    elif dir == "decode":
        for i in text:
            forward_pos = alphabet.index(i)
            backwards_pos = forward_pos - shift
            print(alphabet[backwards_pos])

caesar(dir=direction, text=text, shift=shift)
