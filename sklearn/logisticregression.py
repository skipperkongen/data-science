from sklearn.linear_model import LogisticRegression
import numpy as np

#Numbers are class of tag
train_labels = np.array(['win', 'win', 'win', 'lose', 'lose', 'lose'])

#Acording to resultNER every row is another class so is another features
#but in this way every row have the same features
train_features = np.array([
    [43., 33., 2., 7., 50.],
    [39., 35., 1., 3., 57.],
    [29., 31., 4., 10., 49.],
    [27., 42., 5., 5., 51.],
    [39., 51., 7., 3., 42.],
    [34., 45., 8., 4., 42.]
    ])

#Assing resultsNER to y

#Create LogReg
logit = LogisticRegression()
#Learn LogReg
logit.fit(train_features, train_labels)

labels = np.array(['win', 'win', 'lose', 'lose', 'win'])
features = np.array([
    [36., 33., 3., 6., 50.],
    [52., 32., 0., 8., 52.],
    [27., 38., 4., 2., 42.],
    [34., 43., 5., 5., 51.],
    [38., 40., 2., 5., 51.]
    ])
#Some test vector to check wich class will be predict

print "expected: ", labels
print "predicted:", logit.predict(features)
print "predicted proba:", logit.predict_proba(features)
print logit.classes_