# DocsReceiptScanner

A simple receipt scanner application built with Python.

## Overview

This project aims to provide a tool for scanning receipts and extracting key information such as purchase date, total amount, vendor name, and item details using optical character recognition (OCR) technology. It can be useful for personal expense tracking, business accounting, or automating receipt processing.

## Features

- **Image Upload**: Support for uploading receipt images in common formats (e.g., JPEG, PNG).
- **OCR Processing**: Utilizes Tesseract OCR to extract text from images.
- **Data Parsing**: Parses extracted text into structured data fields.
- **Export Options**: Ability to export scanned data to CSV, JSON, or other formats.
- **User-Friendly Interface**: Simple command-line or GUI interface for ease of use.

## Requirements

- Python 3.7 or higher
- Tesseract OCR engine installed on the system
- Required Python libraries (install via pip):
  - `pytesseract`
  - `Pillow`
  - `opencv-python`
  - `pandas` (for data handling)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/DocDamage/DocsReceiptScanner.git
   cd DocsReceiptScanner
   ```

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR:
   - On Ubuntu/Debian: `sudo apt-get install tesseract-ocr`
   - On macOS: `brew install tesseract`
   - On Windows: Download from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki) and add to PATH.

## Usage

1. Run the application:
   ```
   python scanner.py
   ```

2. Upload a receipt image when prompted.

3. The app will process the image, extract text, and display or save the parsed data.

For more advanced usage, refer to the code comments or documentation.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.