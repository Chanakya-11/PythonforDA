import numpy as np

p = np.array([[1, 2], [2, 3]])
q = np.array([[4, 5], [6, 7]])

result_multiplication = np.dot(p, q)

p_flat = p.flatten()
q_flat = q.flatten()
data = np.vstack([p_flat, q_flat]) 
covariance_matrix = np.cov(data)

print("result is:")
print(result_multiplication)
print("\nCovariance Matrix:")
print(covariance_matrix)