import numpy as np
from sklearn import preprocessing
input_labels= ['red','black','red','green','yellow','white','purple']
#creating a label encoder and fit the labels(Create the label encoder object and train it:)
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)
#print the mapping between words and number
print("\nlabel mapping:")
for i,item in enumerate(encoder.classes_):
    print(item,'-->',i)
#encode set of labels using the encoder
test_labels = ['green','red','black','purple']
encoded_values = encoder.transform(test_labels)
print("\nlabels = ",test_labels)
print ("encoded values = ",list(encoded_values))
#decoding using encoder
encoded_values = [3,4,4,2,1,1,3,5]
decoder_list = encoder.inverse_transform(encoded_values)
print("\n Encodede values:==>",encoded_values)
print("\n decoded values:==>",list(decoder_list))