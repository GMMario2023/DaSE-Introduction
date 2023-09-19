def cube_root(a, max_iter=100, tol=1e-6):
    """
    使用牛顿法求解3次方根
    :param a: 需要求解3次方根的数
    :param max_iter: 最大迭代次数
    :param tol: 允许的误差范围
    :return: 3次方根的近似值
    """
    x = 1.0  # 选择一个初始点
    for _ in range(max_iter):
        f = x**3 - a
        if abs(f) < tol:  # 如果f接近0，则停止迭代
            return x
        x_new = x - f / (3*x**2)  # 计算新的点
        if abs(x_new - x) < tol:  # 如果新旧点之间的差接近0，则停止迭代
            return x_new
        x = x_new
    return x  # 如果达到最大迭代次数仍未收敛，返回最后一次迭代的值

# 示例：求解8的3次方根
print(cube_root(8))
