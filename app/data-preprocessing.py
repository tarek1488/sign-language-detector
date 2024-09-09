import mediapipe as mp
import cv2
import os
import matplotlib.pyplot as plt
import pickle
from sklearn.preprocessing import LabelEncoder

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

#the directory containing data
DATA_PATH = r"data_svm" 

DATA_LANDMARKS = []
LABELS = []
#interating through images

for image in os.listdir(DATA_PATH): 
    #getting the image label
    temp = image.split('-')
    label = temp[0]
    #image_aux
    data_aux = []
    #image paths
    img_path =  os.path.join(DATA_PATH,image) 
    #reading image
    image = cv2.imread(img_path) 
    #convertign channels from bgr to rgb
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    # Process the image with MediaPipe
    results = hands.process(image)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                X = hand_landmarks.landmark[i].x
                Y = hand_landmarks.landmark[i].y
                data_aux.append(X)
                data_aux.append(Y)
        DATA_LANDMARKS.append(data_aux)
        LABELS.append(label)
encoder = LabelEncoder()
coded_labels = encoder.fit_transform(LABELS)         
f = open('data.pickle','wb')
pickle.dump({'data': DATA_LANDMARKS, 'labels': coded_labels},f)
f.close()