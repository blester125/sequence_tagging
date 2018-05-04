from sequence_tagging.perceptron import AveragedPerceptron

from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
X_train, y_train = shuffle(X_train, y_train)

clf = svm.SVC()
clf.fit(X_train, y_train)

y_ = clf.predict(X_test)
print(f"Accuracy of SVM: {accuracy_score(y_, y_test)}")


def get_features(x):
    features = {}
    features['bias'] = 1
    for i, v in enumerate(x):
        features[str(i)] = v
    return features

m = AveragedPerceptron(y_train, 0.01)

MAXITERS = 100
train_acc = 0
i = 0
while train_acc < .99:
    X_train, y_train = shuffle(X_train, y_train)
    for x, y in zip(X_train, y_train):
        features = get_features(x)
        guess = m.predict(features)
        m.update(y, guess, features)
    y_ = []
    for x in X_train:
        y_.append(m.predict(get_features(x)))
    train_acc = accuracy_score(y_, y_train)
    # print(f"Iter {i + 1}: {accuracy_score(y_, y_train)}")
    i += 1
    if i >= MAXITERS:
        break
m.average_weights()

y_ = []
for x in X_test:
    y_.append(m.predict(get_features(x)))
print(f"Accuracy of AP: {accuracy_score(y_, y_test)}")
