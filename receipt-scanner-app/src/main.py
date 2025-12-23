from scanner.ocr import OCRScanner
import json

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def main():
    config = load_config('config.json')
    ocr_scanner = OCRScanner(config['ocr_settings'])
    
    # Example of scanning an image
    image_path = config['input_image_path']
    extracted_text = ocr_scanner.scan_image(image_path)
    
    print("Extracted Text from Receipt:")
    print(extracted_text)

if __name__ == "__main__":
    main()