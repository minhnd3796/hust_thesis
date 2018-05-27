import pandas as pd
import numpy as np
import pylab

red_indices = pd.read_csv('potsdam_train_acc.csv', header=None).iloc[:, 0].values
red_val = pd.read_csv('potsdam_train_acc.csv', header=None).iloc[:, 1].values * 100

blue_indices = pd.read_csv('potsdam_val_acc.csv', header=None).iloc[:, 0].values
blue_val = pd.read_csv('potsdam_val_acc.csv', header=None).iloc[:, 1].values * 100

pylab.plot(red_indices, red_val, 'r', label='Training')
pylab.plot(blue_indices, blue_val, 'b', label='Validation')
pylab.legend(loc='lower right')
pylab.title('Accuracies over epochs')
pylab.xlabel('Epoch')
pylab.ylabel('Accuracy (%)')
pylab.show()
