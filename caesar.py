def alphabet_position(letter):
    """Receives a letter and returns its position in the alphabet"""
    num = ord(letter)
    if str.isupper(letter):
        num = num - 65
    if str.islower(letter):
        num = num - 97        
    return num
	
def rotate_character(char, rot):
    """Receives a character and an integer and returns a char
       rotated to the right by rot characters"""
    if not str.isalnum(char):
        return char
    if str.isdigit(char):
        return char
    # Bring pos value to range of 0-25 for upper and lowercase and
    # add rot to it
    pos = alphabet_position(char) + rot
    if pos > 25:
        pos = pos % 26
    # Adjust back to proper ASCII range for upper and lowercase
    if str.isupper(char):
        pos = pos + 65
    if str.islower(char):
        pos = pos + 97
    return chr(pos)

def encrypt(text, rot):
    """Receives text and a rotation number"""
    encrypt_text = ""
    for char in text:
        encrypt_text = encrypt_text + rotate_character(char, rot)
    return encrypt_text

	