# Real-Time Sign Language Detector using SVM and Mediapipe

This project implements a real-time sign language detection system using Support Vector Machines (SVM) and Mediapipe. The system allows you to either use a pre-trained model for a quick demo or train your own model on a custom dataset.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Demo](#demo)
- [Training on Custom Data](#training-on-custom-data)
  - [1. Collecting Data](#1-collecting-data)
  - [2. Preprocessing Data](#2-preprocessing-data)
  - [3. Training the SVM Model](#3-training-the-svm-model)
- [Running the Real-Time Detector](#running-the-real-time-detector)
- [Acknowledgments](#acknowledgments)

## Requirements

Make sure you have the following dependencies installed:

- Python 3.12
- Mediapipe
- OpenCV
- Scikit-learn
- NumPy
- Pandas

You can install the required dependencies with:

```bash
pip install -r requirements.txt
```
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/sign-language-detector.git
   cd sign-language-detector
   ```
2. Install the dependencies (as listed above).
## Demo
To try the demo with the pre-trained model, simply run
```bash
python realtime-svm.py
```
## Training on custom data:
1. Collecting data
   ```bash
   python collecting_data.py
   ```
   The script will guide you through the process of recording samples for each sign.
2. Preprocessing data:
   Once you have collected your data, you can preprocess it by running:
   ```bash
   python data-preprocessing.py
   ```
   This will clean and organize your data for training.
3. Training the SVM model
   After preprocessing, you can train the SVM model using:
   ```bash
   python svm_train.py
   ```
   This will train an SVM model on your collected and preprocessed data.
4. Running the Real-Time Detector
   Once you've trained your model, run the real-time sign language detection system with
   ```bash
   python realtime-svm.py
   ```
   This will start the webcam feed and use the trained model to recognize signs in real-time.
## Acknowledgments
This project utilizes Mediapipe for hand landmark detection and Scikit-learn for the SVM implementation.
```vbnet
Let me know if you need any modifications!
```


   


