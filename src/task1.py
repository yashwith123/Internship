# -*- coding: utf-8 -*-


######task1
import numpy as np

scores = np.random.randint(50, 101, size=(5, 3))

subject_mean = scores.mean(axis=0)

centered_scores = scores - subject_mean

print("Original Scores:\n", scores)
print("\nSubject-wise Mean:\n", subject_mean)
print("\nCentered (Normalized) Scores:\n", centered_scores)



###task2########
import numpy as np

data = np.arange(24)
reshaped = data.reshape(4, 3, 2)
final_data = reshaped.transpose(0, 2, 1)

print("Final Shape:", final_data.shape)
print("\nFinal Array:\n", final_data)

