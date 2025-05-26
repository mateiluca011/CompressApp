import os

def delete_file(path):
    """
    Șterge fișierul specificat, dacă există.
    """
    if os.path.exists(path):
        os.remove(path)
        print(f"Deleted: {path}")
    else:
        print(f"Not found: {path}")

if __name__ == '__main__':
    delete_file('sample_compressed.zip')
    delete_file('sample_decompressed.txt')