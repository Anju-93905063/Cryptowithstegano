from PIL import Image
from numpy import asarray
import numpy as np

class Steganography:
    def create_stegeo_image(self, directory, filename, cipher_text):
        try:
            img = Image.open(directory + filename)
            img_arr = asarray(img)

            flat_arr = img_arr.flatten()
            flat_list = flat_arr.tolist()

            for x in range(len(cipher_text)):
                temp = format(flat_list[x], '08b')  # Convert to 8-bit binary
                temp = temp[:-1] + cipher_text[x]  # Modify the last bit
                flat_list[x] = int(temp, 2)  # Convert back to integer

            modified_flat_arr = np.array(flat_list, dtype='uint8')
            modified_arr = modified_flat_arr.reshape(img_arr.shape)

            final_img = Image.fromarray(modified_arr, 'RGB')

            filename2 = directory + 'stego_' + filename
            final_img.save(filename2)
            print(f"File saved as: {filename2}")  # Debugging output
            return 'stego_' + filename
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

    def cypher_text_extracter(self, directory, filename):
        try:
            img = Image.open(directory + filename)
            img_arr = asarray(img)
            flat_arr = img_arr.flatten()
            flat_list = flat_arr.tolist()
            
            # Extract the length of the cipher text
            length_bin = ''.join(['1' if flat_list[x] % 2 else '0' for x in range(25)])
            cypher_txt_length = int(length_bin, 2)

            # Extract cipher text
            cypher_txt = ''.join(['1' if flat_list[x + 25] % 2 else '0' for x in range(cypher_txt_length)])

            return cypher_txt
        except Exception as e:
            print(f"Error occurred: {e}")
            return None
