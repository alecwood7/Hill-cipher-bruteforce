# Hill-cipher-bruteforce
Python script to take ciphertext and conduct brute force decryption to reveal matrix key

# USAGE

Be sure to replace the ciphertext at line 6. More ciphertext the better to allow the scripts to find known word occurence's. 

Run hill_decoder.py to create a text file that includes matrix used and "decrypted" output for each matrix iteration. There will be thousands of entries. 
This output txt file can then be run through scan.py, the integer value at line 33 can be increased or decreased. The script will output a new text file with all matrix iterations that contain more than "X" amount of known english words. In my case, this narrowed down the original 89k outputs to about 50. The remaining 50 were then manually scanned for most likely english sentence output.

This also assumes that "A" is indexed at 1 instead of 0. 
