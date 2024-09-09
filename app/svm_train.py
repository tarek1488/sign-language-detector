import pickle
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
#from keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import accuracy_score

# Load the data
data_dict = pickle.load(open('sklearn/data.pickle','rb'))
data = data_dict['data']
labels = data_dict['labels']


# Convert to NumPy arrays
X = np.asarray(data)
Y = np.asarray(labels)

model = SVC(kernel='linear', C=10)

model.fit(X,Y)

_y = model.predict(X)

print(f"accuracy: {accuracy_score(_y,Y)}")

f = open('model.p','wb')
pickle.dump({'model': model},f)
f.close



