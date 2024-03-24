import os
import zipfile
import shutil

def extract_zip(zip_file, pdf_dir, text_dir):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        for member in zip_ref.namelist():
            filename = os.path.basename(member)
            if filename.lower().endswith('.pdf'):
                pdf_path = os.path.join(pdf_dir, filename)
                with open(pdf_path, 'wb') as f:
                    f.write(zip_ref.read(member))
            elif filename.lower().endswith('.txt'):
                text_path = os.path.join(text_dir, filename)
                with open(text_path, 'wb') as f:
                    f.write(zip_ref.read(member))

def extract_from_directory(directory, pdf_output_dir, text_output_dir):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.zip'):
                zip_file = os.path.join(root, file)
                extract_zip(zip_file, pdf_output_dir, text_output_dir)

# Example usage
if __name__ == "__main__":
    input_directory = r"C:\Users\kishu\Downloads\PDFs"  # Directory containing zip files
    pdf_output_dir = r"C:\Users\kishu\Downloads\Extracted"  # Directory to extract PDF files
    text_output_dir = r"C:\Users\kishu\Downloads\Text"  # Directory to extract text files

    # Create output directories if they don't exist
    os.makedirs(pdf_output_dir, exist_ok=True)
    os.makedirs(text_output_dir, exist_ok=True)

    # Extract from directory
    extract_from_directory(input_directory, pdf_output_dir, text_output_dir)

    print("Extraction completed.")
