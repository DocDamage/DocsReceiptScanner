def preprocess_image(image_path):
    import cv2

    # Load the image
    image = cv2.imread(image_path)

    # Resize the image to a standard size
    image = cv2.resize(image, (800, 600))

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Apply thresholding to get a binary image
    _, binary_image = cv2.threshold(blurred_image, 150, 255, cv2.THRESH_BINARY_INV)

    return binary_image