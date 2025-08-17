
import arts
print(arts.logo)
alphabet_list = [ "a", "b", "c", "d", "e", "f", "g",
                  "h", "i", "j", "k", "l", "m", "n",
                  "o", "p", "q", "r", "s", "t", "u",
                  "v", "w", "x", "y", "z"]
def ceaser(original_text , shift_amount , encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet_list:
            output_text += letter
        else:
            shifted_position = alphabet_list.index(letter) + shift_amount
            shifted_position %= len(alphabet_list)
            output_text += alphabet_list[shifted_position]

    print(f"Here is the {encode_or_decode}d result : {output_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n ")
    text = input("type your message.\n").lower()
    shift = int(input("type the shift number\n"))

    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("type 'yes' to continue - otherwise 'no'.\n").lower()
    if restart == "no":
        print("Thank you for using CeaserCipher.!")
        should_continue = False








