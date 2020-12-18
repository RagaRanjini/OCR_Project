#project name: OCR (optical character recognition) , reference given: tesseract ocr, I tried tesseract ocr after installing its setup and converted an image to text document as given in the description , the proof is submitted under the filename "tesseract ocr"
#since the project output demanded to convert an image to pdf or word document , I have done my coding to convert an image to pdf
#proof that my code is converting an image to pdf is submitted in github under the filename "OCR project output"
#try to give correct path for both image to be stored and pdf to be created in .
#once the path is correct and pdf is created , you will get an indication from the codes given that successfully pdf is created .


# importing necessary libraries 
import img2pdf 
from PIL import Image 
import os 

# storing image path 
img_path = r"C:\Users\Welcome\Desktop\sample1.jpeg"

# storing pdf path 
pdf_path = r"C:\Users\Welcome\Desktop\test2.pdf"

# opening image 
image = Image.open(img_path) 

# converting into chunks using img2pdf 
pdf_bytes = img2pdf.convert(image.filename) 

# opening or creating pdf file 
file = open(pdf_path, "wb") 

# writing pdf files with chunks 
file.write(pdf_bytes) 

# closing image file 
image.close() 

# closing pdf file 
file.close() 

# output 
print("Successfully pdf file is created in the given path storing the given image , you may check out !") 
