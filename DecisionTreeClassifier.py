from sklearn import tree
# feature 1 = smooth
# feature 0 = bumpy 
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# label 1 = orange
# label 0 = apple 
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[160, 0]]))