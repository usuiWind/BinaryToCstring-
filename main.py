import os
import textwrap

def convert_to_shellcode(filename="regedit.bin", bytes_per_line=80):
    if not os.path.isfile(filename):
        print("file not found")
    
    with open(filename, "rb") as f:
         content = f.read()

    shellcode_raw = ''.join(f'\\x{byte:02x}' for byte in content)

    wrapped_shellcode = textwrap.wrap(shellcode_raw, bytes_per_line *4)
    print('unsigned char shellcode[] = ')
    print ('    "'+ '"\n "'.join(wrapped_shellcode) + '";')



if __name__ == "__main__":
    convert_to_shellcode()
