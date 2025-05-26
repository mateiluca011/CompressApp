import zipfile
import os

def compress_file(input_file, output_zip):
    """
    Compress any file using the LZMA algorithm within a ZIP container for maximum compression.
    """
    # Ensure output directory exists
    out_dir = os.path.dirname(output_zip)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    # Create ZIP with LZMA compression (highest ratio)
    with zipfile.ZipFile(output_zip, 'w', compression=zipfile.ZIP_LZMA, compresslevel=9) as zipf:
        zipf.write(input_file, arcname=os.path.basename(input_file))

    in_size = os.path.getsize(input_file)
    out_size = os.path.getsize(output_zip)
    print(f"Compressed '{input_file}' → '{output_zip}' ({in_size} → {out_size} bytes)")

if __name__ == '__main__':
    compress_file('sample.txt', 'sample_compressed.zip')