《机器学习实战》中涉及到的python知识点

> `from numpy import *`

## chapter 02

- 创建数组

  `arr = array([[1, 1], [0, 1], [0, 0]])`

- 获取数组的行数

  `arr.shape[0]`

- 将数组在行或列上重复指定的次数

  `tile(arr, (2, 1))`

  > 在行上复制2次：[[1, 1], [0, 1], [0, 0], [1, 1], [0, 1], [0, 0]]

- 返回数组值从小到大所对应的下标

  `arr.argsort()`

  > [[0, 1], [0, 1], [0, 1]]

- 元组获取指定的值

  `dict.get(key, default=None)`

```python
sorted(dict.iteritems(),  # 生成一个迭代器
       # operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值
       # operator.itemgetter(1)表示获取下标为1的元素
       key=operator.itemgetter(1),  
  		 reverse=True)  # 降序
```

- `zeros((m, n))`

  创建m行n列的全0矩阵

- `arr[index, :]`

  获取index行的数据

- `arr.min[0]`

  获取每列的最小值

- `arr.max[0]`

  获取每列的最大值

- `arr[m:n, :]`

  m行到n行的数据





