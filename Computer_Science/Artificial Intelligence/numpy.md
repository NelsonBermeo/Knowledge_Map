# Linear Algebra Operations

**Eigen Values**

We can use numpy to find eigenvalues and vectors:

```python
C = np.array([[13, -12, 2],
              [-12, 13, 2],
              [2, 2, 8]])

eigvals, eigvecs = np.linalg.eig(C)

print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)
```
