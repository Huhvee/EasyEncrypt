import subprocess
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import json

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()
directory_path=Path(file_path)

with open('data.json', 'w', encoding='utf-8') as d:
    json.dump(file_path, d, ensure_ascii=False, indent=4)