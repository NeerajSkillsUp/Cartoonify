import cv2

def cartoonify_image(img_path,output_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)
    edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
    color = cv2.bilateralFilter(img,9,300,300)
    cartoon = cv2.bitwise_and(color,color,mask=edges)
    
    # Save the cartoonified image
    cv2.imwrite(output_path,cartoon)
    print(f"Cartoonified image saved as {output_path}")

input_image = "input.jpg"
output_image = "cartoon_output.jpg"
cartoonify_image(input_image,output_image)