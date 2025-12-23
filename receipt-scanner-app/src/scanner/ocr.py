class OCRScanner:
    def __init__(self):
        import pytesseract
        import cv2

        self.pytesseract = pytesseract
        self.cv2 = cv2

    def scan_image(self, image_path):
        image = self.cv2.imread(image_path)
        gray_image = self.cv2.cvtColor(image, self.cv2.COLOR_BGR2GRAY)
        text = self.pytesseract.image_to_string(gray_image)
        return text