import numpy as np
import string
from itertools import product

# Given ciphertext (up to 50 characters)
ciphertext = "yhwdpkpduupdzaxudabvirfkmbfkmrzwcksueinuqdgcyalicc"  # Example ciphertext, replace with your 50-character input

# Ensure the ciphertext is no longer than 50 characters
ciphertext = ciphertext[:50]

# Convert characters to numerical values (A = 1, B = 2, ..., Z = 26)
alphabet = string.ascii_lowercase
char_to_num = {char: idx + 1 for idx, char in enumerate(alphabet)}  # Start at 1
num_to_char = {idx + 1: char for idx, char in enumerate(alphabet)}  # Start at 1

# Function to calculate the modular inverse of a matrix modulo 26
def mod_inverse_matrix(matrix, mod):
    det = int(round(np.linalg.det(matrix)))  # Determinant
    det = det % mod  # Determinant modulo 26
    try:
        det_inv = pow(det, -1, mod)  # Modular inverse of the determinant modulo 26
    except ValueError:
        return None  # If not invertible

    # Calculate the adjugate (adjoint) of the matrix
    adjugate = np.array([[matrix[1][1], -matrix[0][1]],
                         [-matrix[1][0], matrix[0][0]]])
    
    # Apply the modular inverse of the determinant to the adjugate matrix
    inv_matrix = (det_inv * adjugate) % mod
    return inv_matrix

# Function to decrypt the ciphertext using the decryption matrix
def decrypt(ciphertext, decryption_matrix):
    decrypted_text = ""
    for i in range(0, len(ciphertext), 2):
        if i + 1 < len(ciphertext):
            pair = ciphertext[i:i + 2]
            vector = np.array([[char_to_num[pair[0]]], [char_to_num[pair[1]]]])

            # Decrypt using the decryption matrix
            decrypted_vector = np.dot(decryption_matrix, vector) % 26
            decrypted_vector[decrypted_vector == 0] = 26  # Adjust for modulus

            # Convert numbers back to letters
            decrypted_text += num_to_char[int(decrypted_vector[0][0])]
            decrypted_text += num_to_char[int(decrypted_vector[1][0])]
    return decrypted_text

# Check against known English words or common letter pairs
def is_english_word(word, known_words):
    return word in known_words

# List of known English words (you can extend this list)
known_words = set([
    "the", "and", "that", "have", "for", "not", "this", "with", "you", "be", 
    "on", "are", "as", "it", "at", "he", "was", "is", "I", "his", 
    "they", "said", "she", "we", "their", "there", "who", "do", 
    "up", "go", "if", "my", "to", "of", "in", "for", "on", "at", "by", "an", "as"
])

# Common letter pairs
common_pairs = ["th", "he", "in", "er", "an", "re", "nd", "at", "on", "to", "is", "it"]

# Function to brute-force the Hill cipher
def brute_force_hill_cipher(ciphertext, output_file):
    # Open the output file
    with open(output_file, 'w') as f:
        # Try all possible combinations of 2x2 matrices with values from 1 to 26
        for a, b, c, d in product(range(1, 27), repeat=4):
            # Create the matrix
            matrix = np.array([[a, b], [c, d]])

            # Check if the matrix is invertible
            if np.linalg.det(matrix) % 26 == 0:
                continue  # Skip non-invertible matrices

            # Calculate the modular inverse of the matrix
            decryption_matrix = mod_inverse_matrix(matrix, 26)
            if decryption_matrix is None:
                continue  # Skip if decryption matrix is not valid

            # Decrypt the ciphertext
            decrypted_text = decrypt(ciphertext, decryption_matrix)

            # Check for known English words or common letter pairs in the decrypted text
            if any(is_english_word(word, known_words) for word in decrypted_text.split()) or \
               any(pair in decrypted_text for pair in common_pairs):
                # Write the result to the file
                f.write(f"Matrix:\n{matrix}\nDecrypted Text: {decrypted_text}\n\n")

# Specify the output file name
output_file = "hill_cipher_results.txt"

# Run the brute force Hill cipher and write results to file
brute_force_hill_cipher(ciphertext, output_file)

print(f"Results have been written to {output_file}.")
