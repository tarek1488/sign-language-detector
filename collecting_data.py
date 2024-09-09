import cv2
import uuid
import time
import os

def read_data():
    # our signs
    labels = ['no', 'hello']
    
    # the path to the folder that will contain the images
    data_path = 'sklearn\data_svm'
    
    # create the folder if it doesn't exist
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    
    # setting capture
    cap = cv2.VideoCapture(0)
    
    for label in labels:
        print(f'collecting images for {label}')    
        
        # sleep before start taking images for each label
        time.sleep(5) # 5 seconds 
        
        for i in range(50):
            # reading a frame
            print(f'be ready image num {i+1} will be taken after 2 seconds')
            
            #time.sleep(2) # sleep for 2 seconds 
            
            # capturing a frame 
            ret, frame = cap.read()
            
            if not ret: # ret is a boolean that is true if the image is taken
                print("Failed to capture image")
                continue
            
            # setting image name
            image_name = os.path.join(data_path, label + '-' + '{}.jpg'.format(str(uuid.uuid1())))
            
            # saving image to sign-language-dataset directory 
            cv2.imwrite(image_name, frame)
            
            # showing the captured image
            cv2.imshow('frame', frame)
            
            # wait for 1 seconds
            print(f'image number #{i+1} taken now change position')
            
            time.sleep(1)
    
            if cv2.waitKey(40) and 0xff == ord('q'):
                break
    
    cap.release()
    cv2.destroyAllWindows()
            
read_data()
