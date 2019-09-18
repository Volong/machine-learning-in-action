#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    """
    inX 未知数据，一个二维数组
    dataSet 样本数据，上述的group
    labels 样本标签，上述的labels，group中每一行对应一个标签
    k 取前几个点
    """

    # shape用来获取数组的行与列的数量，结果为元组()
    dataSetSize = dataSet.shape[0]  # 获取行数
    print("dataSetSize", dataSetSize)

    # 欧几里得距离计算两个坐标的距离
    # 构造一个与dataSet维度一样的二维数组
    n = tile(inX, (dataSetSize, 1))
    print(n)

    # 进行数组运算（其实就是坐标的加减运算）
    diffMat = n - dataSet
    print("diffMat", diffMat)

    # 各个点的平方
    sqDiffMat = diffMat ** 2

    # 求和
    sqDistances = sqDiffMat.sum(axis=1)

    # 开根号
    distances = sqDistances ** 0.5
    print("distances", distances)

    # 返回数组值从小到大所对应的下标
    sortedDistIndicies = distances.argsort()
    print("sortedDistIndicies", sortedDistIndicies)

    classCount = {}

    # 选择距离最小的K个点
    for i in range(k):
        # 获取下标对应的标签值
        voteIlabel = labels[sortedDistIndicies[i]]
        # 对标签进行计数
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    # 排序
    # sorted：对所有可迭代的对象进行排序操作
    # 表示对classCount中标签的数量进行降序排序。{标签名:数量, 标签名:数量, 标签名:数量}
    sortedClassCount = sorted(classCount.iteritems(),  # 生成一个迭代器
                              key=operator.itemgetter(1),  # operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值
                                                           # operator.itemgetter(1)表示获取下标为1的元素
                              reverse=True)  # 降序

    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    array0lines = fr.readlines()
    numberOfLines = len(array0lines)  # 得到文件行数

    returnMat = zeros((numberOfLines, 3))  # 创建numberOfLines行3列的零矩阵

    classLabelVector = []
    index = 0

    for line in array0lines:
        line = line.strip()  # 去掉首尾的空白字符
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]  # 给矩阵第index行赋值
        classLabelVector.append(int(listFromLine[-1]))  # -1表示数组最后一个元素
        index += 1

    print(classLabelVector[0:3])
    return returnMat, classLabelVector


if __name__ == "__main__":
    file2matrix("datingTestSet2.txt")


