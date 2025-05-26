import zipfile
import os

def unique_path(path):
    """
    Return a unique file path by appending a counter if the file exists.
    E.g., file.txt → file(1).txt, file(2).txt, etc.
    """
    base, ext = os.path.splitext(path)
    counter = 1
    new_path = path
    while os.path.exists(new_path):
        new_path = f"{base}({counter}){ext}"
        counter += 1
    return new_path

def decompress_file(input_zip, output_file):
    """
    Extract the first entry from a ZIP archive to a specified output file,
    ensuring no existing file is overwritten.
    """
    # Compute a unique output path so we don't overwrite
    output_file = unique_path(output_file)

    with zipfile.ZipFile(input_zip, 'r') as zipf:
        names = zipf.namelist()
        if not names:
            raise Exception('Arhiva ZIP este goală')
        # Assume single-file archive
        name = names[0]
        temp_dir = os.path.dirname(output_file) or os.getcwd()
        os.makedirs(temp_dir, exist_ok=True)
        zipf.extract(name, path=temp_dir)
        src = os.path.join(temp_dir, name)
        os.replace(src, output_file)

    print(f"Decompressed '{input_zip}' → '{output_file}'")

if __name__ == '__main__':
    # Exemplu de utilizare:
    decompress_file(
        r"C:\Users\matei\Desktop\Algoritm\LZMA\sample_compressed.zip",
        r"C:\Users\matei\Desktop\Algoritm\LZMA\sample_decompressed.pdf"
    )