# Histologic Detection and Grading of Breast Cancer (IDC)

## Overview
This repository implements a deep learning pipeline for detecting and grading **Invasive Ductal Carcinoma (IDC)** in breast cancer histopathology images. IDC, comprising ~80% of breast cancer cases, originates in milk ducts and can spread to surrounding tissues. Early detection via whole-slide images (WSI) is critical for high survival rates. The project combines:

- **CNN (VGG16)**: Classifies 50x50 image patches as benign or malignant using transfer learning.
- **Gradient Traversal**: Traverses from random seed pixels to cancer regions (ROI) using Sobel filters for gradient magnitude/orientation.
- **Mask SLIC**: Identifies cancer ROIs via supervoxel segmentation.
- **BiLSTM**: Classifies directional paths (N, S, E, W) for enhanced grading, combining with CNN outputs.

**Author**: Sathyanarayanan Dhorali  
**Date**: June 20, 2022  
**Dataset**: Histopathology slides from 162 women (Cancer Institute of NJ & U. Pennsylvania), downsampled to 4 µm/pixel.  
**Reference**: [Project.pdf](Project.pdf) for full methodology and IDC stages/treatments.

## Files
- **Breast Cancer.ipynb**: CNN implementation using VGG16 for patch classification (75% train, 25% test split).
- **mask slic.ipynb**: Supervoxel segmentation to detect cancer ROIs using Mask SLIC.
- **sequence classification Rnn.ipynb**: BiLSTM model for classifying directional paths to ROIs.
- **Image Intensity.ipynb**: Gradient traversal using Sobel filters to compute paths to cancer regions.
- **Project.pdf**: Detailed report on methodology, IDC stages, and treatments.
- **.gitattributes**: Git configuration file.
