import re

# Specify the path to the input output file and the results output file
input_file = "hill_cipher_results.txt"
results_file = "lines_with_known_words.txt"

# List of known English words (you can expand this list)
known_words = set([
    "the", "and", "that", "have", "for", "not", "this", "with", "you", "be", 
    "on", "are", "as", "it", "at", "he", "was", "is", "I", "his", 
    "they", "said", "she", "we", "their", "there", "who", "do", 
    "up", "go", "if", "my", "to", "of", "in", "for", "on", "at", "by", "an", "as"
])

def scan_output_file(file_path, known_words):
    results = []

    try:
        with open(file_path, 'r') as f:
            content = f.readlines()
            for line in content:
                # Extract decrypted text from the line
                if "Decrypted Text:" in line:
                    decrypted_text = line.split(":")[1].strip()
                    
                    # Normalize the text to lowercase
                    decrypted_text = decrypted_text.lower()
                    
                    # Count how many known words are in the decrypted text
                    count = sum(1 for word in known_words if word in decrypted_text)
                    
                    # If more than 3 known words are found, store the line
                    if count > 6:
                        results.append(f"{decrypted_text} (Known words: {count})")

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return results

def write_results_to_file(results, output_file):
    try:
        with open(output_file, 'w') as f:
            for line in results:
                f.write(line + "\n")
        print(f"Results have been written to {output_file}.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Run the scan and get found lines
found_lines = scan_output_file(input_file, known_words)

# Write the results to the output file
if found_lines:
    write_results_to_file(found_lines, results_file)
else:
    print("No lines with more than 3 known words were found in the output file.")
