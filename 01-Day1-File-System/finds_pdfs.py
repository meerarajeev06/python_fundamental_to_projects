import os
import shutil

# Target directory to scan (e.g., current directory ".")
target_dir = "."

# Destination folder for PDFs
pdf_folder = os.path.join(target_dir, "Found_PDFs")

# Step 1: Create the Found_PDFs folder safelyn
os.makedirs(pdf_folder, exist_ok=True)

# Step 2: List items and count PDFs
pdf_count = 0
print(f"Scanning directory: {os.path.abspath(target_dir)}\n")

for filename in os.listdir(target_dir):
    # Separate the filename and extension
    name, ext = os.path.splitext(filename)
    
    # Check if file extension is .pdf (case-insensitive)
    if ext.lower() == ".pdf":
        pdf_count += 1
        print(f"[{pdf_count}] Found PDF: {filename}")

print(f"\nScan Complete! Total PDFs found: {pdf_count}")