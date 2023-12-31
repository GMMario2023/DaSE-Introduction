import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
plt.plot(X,C)
plt.plot(X,S)
plt.show()
