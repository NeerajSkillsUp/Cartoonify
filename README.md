# Image Cartoonifier
This project converts input images into cartoon-like versions using OpenCV and Python.
It applies edge detection and color smoothing techniques to create a cartoon effect.


## Features
- Converts regular images to cartoon-style images
- Uses edge detection and bilateral filtering
- Simple and efficient implementation


## Requirements
- Python 3.x
- OpenCV (cv2) library
- NumPy (usually installed with OpenCV)


## Installation
1. Install Python 3.x from https://www.python.org/downloads/
2. Install required libraries using pip: 
    pip install opencv-python numpy


## How to Run
1. Place your input image (e.g., "input.jpg") in the same directory as the script
2. Run the script: 
    python cartoonify.py
3. The output will be saved as "cartoon_output.jpg" in the same directory


## Parameters
You can modify these parameters in the code for different effects:
- `medianBlur` kernel size (currently 5)
- `adaptiveThreshold` block size (currently 9)
- `bilateralFilter` parameters (d=9, sigmaColor=300, sigmaSpace=300)


## Sample Input/Output
Input: Any standard image file (JPG/PNG) named "input.jpg"
Output: Cartoonified version saved as "cartoon_output.jpg"


## Algorithm Steps
1. Read input image
2. Convert to grayscale
3. Apply median blur to reduce noise
4. Detect edges using adaptive thresholding
5. Apply bilateral filter for color smoothing
6. Combine edges with smoothed color image
7. Save the output


## Troubleshooting
- If you get "Image not found" error, ensure:
- The input image exists in the same directory
- The filename matches exactly (including extension)
- The image is not corrupted
- For installation issues, try: 
    pip install --upgrade pip
    pip install opencv-python-headless


## License
This project is open-source and free to use/modify/distribute.
