import matplotlib.pyplot as plt
import numpy as np

# 1. 设置画布与坐标轴
plt.figure(figsize=(10, 6))
x = np.arange(-2, 3, 0.5)  # x 轴刻度位置:-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2
ax = plt.gca()

# 2. 绘制 π 成分的谱线 (上方谱线) 
pi_heights = [0, 0, 0, 3, 4, 3, 0, 0, 0]  # 各 x 位置的谱线高度
for i, height in enumerate(pi_heights):
    if height > 0:
        ax.plot([x[i], x[i]], [0, height], color='black', linewidth=2)
        # 标注谱线高度数值
        ax.text(x[i], height + 0.2, str(height), ha='center')

# 3. 绘制 σ 成分的谱线 (下方谱线) 
sigma_heights = [0.5, 1.5, 3, 0, 0, 0, 3, 1.5, 0.5]  # 各 x 位置的谱线高度
for i, height in enumerate(sigma_heights):
    if height > 0:
        ax.plot([x[i], x[i]], [0, -height], color='black', linewidth=2)
        # 标注谱线高度数值
        ax.text(x[i], -height - 0.3, f'$\\frac{{{int(height*2)}}}{{2}}$' if height % 1 != 0 else str(height), ha='center')

# 4. 标注 π 和 σ
ax.text(2.5, 4.5, '$\\pi$', fontsize=12)
ax.text(2.5, -0.8, '$\\sigma$', fontsize=12)

# 5. 坐标轴样式调整
ax.set_xticks(x)
ax.set_xticklabels([str(int(val)) if val.is_integer() else f'$\\frac{{{int(val*2)}}}{{2}}$' for val in x])
ax.set_xlabel('$x$')
ax.set_yticks([])  # 隐藏 y 轴刻度
ax.spines['bottom'].set_position('center') 
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.yaxis.set_ticks_position('none')

plt.tight_layout()
plt.show()