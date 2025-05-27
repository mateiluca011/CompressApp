# Compresie și Decompresie LZMA

Unelte simple în Python pentru comprimarea și decompresarea fișierelor folosind LZMA într-un container ZIP, cu interfață GUI opțională.

## Funcționalități

* **Comprimare**: Creează un fișier ZIP cu compresie LZMA.
* **Decompresare**: Extrage conținutul unui fișier ZIP.
* **GUI** (Tkinter + ttkbootstrap): Interfață de bază pentru operațiuni rapide.
* **CLI**: Scripturi independente pentru compresie (`compress.py`), decompresie (`decompress.py`) și curățare fișiere temporare (`cleanup.py`).

## Cerințe

* Python 3.8+
* `ttkbootstrap` (pentru GUI)

Instalare dependențe:

```bash
pip install ttkbootstrap
```

## Utilizare

### GUI

```bash
python gui_main.py
```

Selectează fișierul și apasă butonul de compresie/decompresie.

### CLI

* **Comprimare**:

  ```bash
  python compress.py <input> <output.zip>
  ```
* **Decompresare**:

  ```bash
  python decompress.py <input.zip> <output>
  ```
* **Curățare**:

  ```bash
  python cleanup.py
  ```

## Structură

```text
compress.py

decompress.py
cleanup.py
gui_main.py
requirements.txt
README.md
```
