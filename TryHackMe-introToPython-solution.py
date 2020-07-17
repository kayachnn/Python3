import base64


base64_string = "";

try:
    base64_file = open("/home/cihan/Desktop/encodedflag.txt","r")
    base64_string= base64_file.read()
    base64_string_bytes = base64_string.encode('ascii')

    # decode base 16
    for i in range(5):
        decoded_str = base64.b16decode(base64_string_bytes)
        base64_string_bytes = decoded_str

    #decode base 32
    for i in range(5):
        decoded_str = base64.b32decode(base64_string_bytes)
        base64_string_bytes = decoded_str
    # decode base 64
    for i in range(5):
        decoded_str = base64.b64decode(base64_string_bytes)
        base64_string_bytes = decoded_str

    
    print(base64_string_bytes.decode('ascii'))

finally:
    base64_file.close()
