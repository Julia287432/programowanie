def convert_line_endings(file_path, to_windows=True):
    with open(file_path, 'rb') as f:
        content = f.read()

    if to_windows:
        new_content = content.replace(b'\n', b'\r\n')
    else:
        new_content = content.replace(b'\r\n', b'\n')

    with open(file_path, 'wb') as f:
        f.write(new_content)

#convert_line_endings('example1.txt', to_windows=True)  # z Unix na Windows
convert_line_endings('example1.txt', to_windows=False)  # z Windows na Unix