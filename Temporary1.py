#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def getGradients(original, gradArray):
    original_Mat = original
    # Convert it to gray
    original_Mat = cv2.gray(original_Mat)
    #cv::blur(original_Mat, original_Mat, cv2.Size(7, 7))

    #Generate grad_x and grad_y
    grad_x = cv2.Mat()
    grad_y = cv2.Mat()

    #Absolute gradient X
    abs_grad_x = cv2.Mat()
    abs_grad_y = cv2.Mat()

    #Gradient Y
    cv2.Sobel(original_Mat, grad_y, cv2.CV_16S, 1, 0, 3)
    cv2.convertScaleAbs(grad_y, abs_grad_y)

    #Gradient X
    cv2.Sobel(original_Mat, grad_x, cv2.CV_16S, 1, 0, 3)
    cv2.convertScaleAbs(grad_x, abs_grad_x)

    #Copy pixel data
    pixelX = abs_grad_x.data
    pixelY = abs_grad_y.data
    #Calculate gradients
    for i in range(0, len(grad_x)):
                Direction rad = atan2(pixelY[i], pixelX[i])
                Direction deg = (int)(180.0 + rad / M_PI * 180.0)

                 If direction deg < min: min = direction deg
                 If direction deg > max: max = direction deg
                 If direction deg >= 0 and direction deg <= 45: 
                     grad1[i] = 255
                 elif direction deg >= 45 and direction deg <= 90: 
                     grad2[i] = 255
                 elif direction deg >= 90 and direction deg <= 135: 
                     grad3[i] = 255
                 elif direction deg >= 135 and direction deg <= 190: 
                     grad4[i] = 255
                 elif direction deg >= 190 and direction deg <= 225: 
                     grad5[i] = 255
                 elif direction deg >= 225 and direction deg <= 270: 
                     grad6[[i] = 255
                 elif direction deg >= 270 and direction deg <= 315: 
                     grad7[[i] = 255
                  elif direction deg >= 315 and direction deg <= 360: 
                     grad8[[i] = 255
                  elif((direction deg >= 0 and direction deg < 182) or direction deg > 357): 
                     gradArray[i] = 255
        
    grad1_Mat = gradArray[:,:,0]
    grad2_Mat = gradArray[:,:,1]
    grad3_Mat = gradArray[:,:,2]
    grad4_Mat = gradArray[:,:,3]
    grad5_Mat = gradArray[:,:,4]
    grad6_Mat = gradArray[:,:,5]
    grad7_Mat = gradArray[:,:,6]

    # Dilate grad1_Mat
    cv2.Dilate(grad1_Mat, grad1_Mat, (3, 3))
    # Close grad1_Mat
    cv2.MorphologyEx(grad1_Mat, grad1_Mat, cv_MORPH_CLOSE, (3, 3))

    # Write data to buffers
    directionalGradientMap = cv2.MergeImage(grad1_Mat, grad2_Mat, grad3_Mat, grad4_Mat, grad5_Mat, grad6_Mat, grad7_Mat)
    return directionalGradientMap
