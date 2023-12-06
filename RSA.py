from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA512

def RSA_generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    return private_key, public_key

def RSA_save_key_to_file(key, filename): #save the key to a file for debug
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def RSA_load_key_from_file(filename):
    with open(filename, 'rb') as key_file:
        key_data = key_file.read()
        key = RSA.import_key(key_data)
        return key

def RSA_encrypt_file(input_filename, output_filename, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)

    with open(input_filename, 'rb') as infile, open(output_filename, 'wb') as outfile:
        plaintext = infile.read()
        ciphertext = cipher.encrypt(plaintext)
        outfile.write(base64.b64encode(ciphertext))

def RSA_decrypt_file(input_filename, output_filename, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)

    with open(input_filename, 'rb') as infile, open(output_filename, 'wb') as outfile:
        ciphertext = base64.b64decode(infile.read())
        decrypted_text = cipher.decrypt(ciphertext)
        outfile.write(decrypted_text)

def RSA_sign_data(data, private_key):
    key = RSA.import_key(private_key)
    h = SHA512.new(data)
    signature = pkcs1_15.new(key).sign(h)
    return signature

def RSA_verify_signature(data, signature, public_key):
    key = RSA.import_key(public_key)
    h = SHA512.new(data)
    try:
        pkcs1_15.new(key).verify(h, signature)
        return True  # Signature is valid
    except (ValueError, TypeError):
        return False  # Signature is invalid

# Step 1: Generate key pair
private_key, public_key = RSA_generate_key_pair()

# Step 2: Save keys to files
RSA_save_key_to_file(private_key, 'private_key.pem')
RSA_save_key_to_file(public_key, 'public_key.pem')

# Step 3: Encrypt a file using the public key
RSA_encrypt_file('input.txt', 'encrypted_file.bin', public_key)

# Step 4: Decrypt the file using the private key
RSA_decrypt_file('encrypted_file.bin', 'decrypted_file.txt', private_key)

# Step 5: Sign some data using the private key
data_to_sign = b'This is some data to sign.'
signature = RSA_sign_data(data_to_sign, private_key)

# Step 6: Verify the signature using the public key
verification_result = RSA_verify_signature(data_to_sign, signature, public_key)

# Display results
print(f"Private Key: {private_key}")
print(f"Public Key: {public_key}")
print("Encryption and Decryption Successful")
print(f"Original Data: {data_to_sign}")
print(f"Signature: {signature}")
print(f"Signature Verification Result: {verification_result}")