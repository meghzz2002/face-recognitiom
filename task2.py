#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install -q opencv-python')


# In[4]:


import cv2
# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the input image
image = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform face detection
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the output image
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:



