# SignSense

## Overview

SignSense is a software developed as part of a college curriculum mini project, aimed at assisting deaf and dumb individuals. Leveraging computer vision and machine learning, SignSense provides an intuitive and accessible interface for communication and creativity through two main features: hand sign recognition and virtual drawing.

![SignSense_Main](https://github.com/abey003/SignSense/assets/96768878/09c8089d-1cc1-4291-a5f6-2e0c07bd1c47)


## Main Features

### Hand Sign Recognition
Identifies hand signs shown by users.
Matches the signs with pre-trained data to detect and display the recognized sign.

### Virtual Drawing
Allows users to draw by moving a pen in the air over a camera.
The software detects the pen's direction and creates a virtual drawing along its path.

## Project Structure

### Main File
The main file contains the interface with two buttons: "Launch Drawing" and "Launh Sign Language."
Users can select either feature to start using the software.

### Virtual Drawing
Includes all necessary files for implementing the virtual drawing feature.

### Sign Detection
Contains files for different stages of the hand sign recognition process:

Data Collection: Capture of images for training data.

Data Extraction: Extract the required parts of the images.

Train Data: Train the data for hand sign recognition.

Main Sign Language Detection: File for detecting hand signs using the trained data.

### Technology
The entire program is written in Python, utilizing various libraries for computer vision and machine learning.
