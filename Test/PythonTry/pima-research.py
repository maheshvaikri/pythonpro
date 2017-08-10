import pandas as pd                    # panda is a dataframe libraries
import matplotlib.pyplot as plt        # matplotlib.pyplot plots data
import numpy as np                     # numpy provides N-dim object support

# do plotting inline instead of a separate window
%matplotlib inline

print("Original True Cases  : {0}  ({1:0.2f}%)".format(len(df.loc[df['diabetes'] == 1]), (len(df.loc[df['diabetes'] == 1])/(df.index))*100))
print("Original False Cases : {0}  ({1:0.2f}%)".format(len(df.loc[df['diabetes'] == 0]), (len(df.loc[df['diabetes'] == 0])/(df.index))*100))
print("   ")

print("Training True Cases  : {0}  ({1:0.2f}%)".format(len(y_train[y_train[:] == 1]), (len(y_train[y_train[:] == 1])/len(y_train) * 100))
print("Training False Cases  : {0}  ({1:0.2f}%)".format(len(y_train[y_train[:] == 0]), (len(y_train[y_train[:] == 0])/len(y_train) * 100))
print("   ")

print("Test True Cases  : {0}  ({1:0.2f}%)".format(len(y_test[y_test[:] == 1]), (len(y_test[y_test[:] == 1])/len(y_test) * 100))
print("Test False Cases  : {0}  ({1:0.2f}%)".format(len(y_test[y_test[:] == 0]), (len(y_test[y_test[:] == 0])/len(y_test) * 100))