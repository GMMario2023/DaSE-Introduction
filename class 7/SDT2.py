import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 创建一些随机数据并存储在 DataFrame 中
data = pd.DataFrame(np.random.rand(100, 2), columns=['X', 'Y'])

# 使用 Seaborn 创建散点图
sns.scatterplot(x='X', y='Y', data=data)

# 使用 Matplotlib 显示图表
plt.show()
