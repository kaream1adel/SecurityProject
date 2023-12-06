from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad, unpad

def encrypt_file_aes(input_file, output_file,key):

    # Generate a random initialization vector (IV)

    iv = get_random_bytes(AES.block_size)
    
    # Create an AES cipher object with the generated key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        # Write the IV to the output file
        outfile.write(iv)

        # Read and encrypt the file in chunks
        chunk_size = 16 * 1024
        while True:
            chunk = infile.read(chunk_size)
            if not chunk:
                break
            # Pad the last chunk before encryption
            if len(chunk) % AES.block_size != 0:
                chunk = pad(chunk, AES.block_size)
            # Encrypt the chunk and write to the output file
            encrypted_chunk = cipher.encrypt(chunk)
            outfile.write(encrypted_chunk)
            

    print(f'Encryption complete. Output file: {output_file}')
    print(f'Generated key: {key.hex()}')

def decrypt_file_aes(encrypted_file, decrypted_file, key):
    # Read the IV from the encrypted file
    with open(encrypted_file, 'rb') as infile:
        iv = infile.read(AES.block_size)

    # Create an AES cipher object with the provided key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(encrypted_file, 'rb') as infile, open(decrypted_file, 'wb') as outfile:
        # Skip the IV in the input file
        infile.seek(AES.block_size)

        # Read and decrypt the file in chunks
        chunk_size = 16 * 1024
        while True:
            chunk = infile.read(chunk_size)
            if not chunk:
                break
            # Decrypt the chunk and write to the output file
            decrypted_chunk = cipher.decrypt(chunk)
            # Unpad the last chunk after decryption
            decrypted_chunk = unpad(decrypted_chunk, AES.block_size)
            outfile.write(decrypted_chunk)

    print(f'Decryption complete. Output file: {decrypted_file}')

# Example usage:

key = get_random_bytes(16)  # 16 bytes for AES-128, change to 24 or 32 for AES-192 or AES-256


encrypt_file_aes('input.txt', 'encrypted_file.enc',key)

decrypt_file_aes('encrypted_file.enc', 'decrypted_file.txt', key)
