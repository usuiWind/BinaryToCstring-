def format_shellcode_for_cpp(input_file_path, output_file_path, bytes_per_line=80):
    """
    Converts shellcode into C++-compatible hex strings with wide lines (default: 80 bytes/line).
    - No padding inside quotes (e.g., "\x48\x83\xEC\x28...").
    - Silky-smooth for Visual Studio pasting.
    """
    with open(input_file_path, 'rb') as f:
        shellcode = f.read()

    hex_escaped = []
    for byte in shellcode:
        hex_escaped.append(f"\\x{byte:02x}")

    # Split into wider chunks (e.g., 80 bytes/line)
    full_hex_string = '"' + ''.join(hex_escaped) + '"'

    # Write to file in controllable-width lines
    with open(output_file_path, 'w') as f:
        for i in range(0, len(hex_escaped), bytes_per_line):
            chunk = hex_escaped[i:i + bytes_per_line]
            f.write(f'"{"".join(chunk)}"\n')  # No extra spaces inside quotes

    print(f"Formatted shellcode written to: {output_file_path}")

if __name__ == "__main__":
    input_file = input()
    output_file = input()
    output_file = output_file or "shellcode.cpp"

    bytes_per_line = 80
    format_shellcode_for_cpp(input_file, output_file, bytes_per_line)
