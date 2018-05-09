######################################################################
# Author: Dostonbek Toirov
# Username: Dostonbek1
#
# Assignment: Original: A10: Caesar Cipher
#
# Purpose: The class imports a file, encrypts or decrypts the file, and exports the cipher to a new file.
######################################################################
# Acknowledgements:
#
# Acknowledgements: The original code was created by Dr. Scott Heggen
#                       and modified by Dr. Jan Pearce. Then later modified by Dostonbek Toirov.
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################


class CaesarCipher:
    '''
    This class is used to import an existing file to encrypt or decrypt
    and then creates a new file that is either encrypted or decrypted.
    '''

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"            # The alphabet, which will be used to do our shifts

    def __init__(self, input_file = "message_input.txt", key = 0, crypt_type = "encrypt"):
        """
        A constructor for the CaesarCipher class

        :param input_file: The file to be encrypted/decrypted
        :param key: The amount each message/cipher needs shifted
        :param crypt_type: Either encrypt or decrypt
        """
        self.input_file = input_file                            # The file to be encrypted or decrypted
        self.key = key                                          # The amount each message/cipher will be shifted
        self.message = ""                                       # A placeholder for the message
        self.cipher = ""                                        # A placeholder for the cipher
        self.crypt_type = crypt_type                            # Either "encrypt" or "decrypt"
        self.import_file()                                      # Calls the import_file() method below


    def import_file(self):
        """
        Imports a file stored in the variable self.input_file

        :return: a string representing the contents of the file
        """
        f = open(self.input_file, "r")
        if self.crypt_type == "encrypt":
            self.message = f.read()                  # Set self.message to the file contents
        elif self.crypt_type == "decrypt":
            self.cipher = f.read()                   # Set self.cipher to the file contents
        f.close()


    def export_file(self, text_to_export, filename):
        """
        Exports a file called filename

        :param text_to_export: the string to be written to the exported file
        :param filename: a string representing the name of the file to be exported to
        """
        f = open(filename, "w")
        f.write(text_to_export)
        print("File exported to " + filename)


    def encrypt(self):
        """
        Converts an original message into a ciphered message with each letter shifted to the right by the key
        :return: a string representing the ciphertext
        """
        output = ""
        for i in self.message:
            if i.upper() in self.alphabet:
                old_letter = self.alphabet.find(i.upper())
                # Uses modulus to return the correct index for each letter after the shift
                # (for cases where the index is outside the range of self.alphabet,
                #  it wraps back to the beginning of the alphabet)
                output += self.alphabet[(old_letter + self.key) % 26]
            else:
                output += i         # Adds non-alphabet characters directly
        return output


    def decrypt(self):
        """
        Converts a cipher text into an original message by shifting each letter to the left by the key

        :return: a string representing the original message
        """
        output = ""
        for i in self.cipher:
            if i.upper() in self.alphabet:
                old_letter = self.alphabet.find(i.upper())
                # Uses modulus to return the correct index for each letter after the shift
                # (for cases where the index is outside the range of self.alphabet,
                #  it wraps back to the end of the alphabet)
                output += self.alphabet[(old_letter - self.key) % 26]
            else:
                output += i         # Adds non-alphabet characters directly
        return output           # Obviously this should output something else

def main():
    # A sample encryption
    type = input("Do you want to encrypt (E) or decrypt (D) [E/D]: ")
    if type == "E":
        message = input("Write the name of txt file to encrypt (should be in the same folder with this program): ")
        key = int(input("Give me the key number to encrypt it (any number other than 0): "))
        cipher0 = CaesarCipher(message, key, "encrypt")
        cipher_text0 = cipher0.encrypt()
        cipher0.export_file(cipher_text0, message)                       # Writes the output to a file

    elif type == "D":
        message = input("Write the name of txt file to decrypt: ")
        key = int(input("Give me the key number to decrypt it (any number other than 0): "))
        cipher0 = CaesarCipher(message, key, "decrypt")
        cipher_text0 = cipher0.decrypt()
        cipher0.export_file(cipher_text0, message)                      # Writes the output to a file
    else:
        main()


if __name__ == "__main__":
    main()
