import numpy as np
v1 = np.array([[1, 2], [5, 2], [6, 9]])  # shape: (3, 2)
v2 = np.array([[8, 4], [9, 2], [3, 4]])
v = v2 - v1
print(v)

v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

print(v)

result = np.einsum('ij,ij->i', v[[0], :], v[[1], :])
print(result)

angle = np.arccos(result)

angle2 = np.degrees(angle)

print(angle)
print(angle2)