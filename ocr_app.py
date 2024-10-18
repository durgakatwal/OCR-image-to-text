# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image
# import pytesseract

# # Uncomment and specify the path if necessary
# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if needed

# # Function to perform OCR
# def ocr_function(image_path):
#     try:
#         # Open the image file
#         image = Image.open(image_path)
#         print(f"Opened image: {image_path}")
        
#         # Display the image for debugging
#         image.show()
        
#         # Print image details
#         print("Image size:", image.size)  # Check the size of the image
#         print("Image mode:", image.mode)  # Check the mode of the image

#     except Exception as e:
#         print(f"Error opening image: {e}")
#         return None
    
#     try:
#         # Perform OCR on the image with specified Page Segmentation Mode (PSM)
#         extracted_text = pytesseract.image_to_string(image, config='--psm 6')
        
#         if not extracted_text.strip():  # Check if any text was extracted
#             print("No text was extracted from the image.")
#         else:
#             print("OCR Processed. Extracted Text:")
#             print(extracted_text)  # Print the extracted text
            
#         return extracted_text
#     except Exception as e:
#         print(f"Error during OCR: {e}")
#         return None

# # Function to open file dialog
# def upload_image():
#     root = tk.Tk()
#     root.withdraw()  # Hide the root window
#     image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
#     return image_path

# # Main block
# if __name__ == "__main__":
#     print("Please upload an image for OCR.")
#     image_path = upload_image()  # Opens the file dialog for user to select an image
#     if image_path:
#         ocr_function(image_path)  # Call the function with the uploaded image path
#     else:
#         print("No image selected.")












import streamlit as st
from PIL import Image
import pytesseract

# Function for OCR processing
def ocr_function(image):
    try:
        # Perform OCR on the image
        extracted_text = pytesseract.image_to_string(image, config='--psm 6')
        if extracted_text.strip():
            st.write("Extracted Text:")
            st.write(extracted_text)
        else:
            st.write("No text was extracted from the image.")
    except Exception as e:
        st.write(f"Error during OCR: {e}")

# Streamlit app structure
st.title("Image to Text OCR App")

# File uploader
uploaded_image = st.file_uploader("Please upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Perform OCR
    ocr_function(image)
else:
    st.write("Please upload an image to extract")
