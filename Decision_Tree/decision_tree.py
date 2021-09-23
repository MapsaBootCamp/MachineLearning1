import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import graphviz

iris_data = load_iris()

print(iris_data.keys())
iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
iris_df["target"] = iris_data.target

X = iris_data.data
y = iris_data.target

dt_classifier = DecisionTreeClassifier(max_depth=2)

dt_classifier.fit(X, y)
# tree.plot_tree(dt_classifier)

dot_data = tree.export_graphviz(dt_classifier, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris")

print(iris_df)
