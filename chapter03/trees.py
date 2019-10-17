#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from math import log


# 计算熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}

    # 获取一行数据
    for featVec in dataSet:
        # 获取最后一列的数据
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0

        labelCounts[currentLabel] += 1

    shannonEnt = 0.0

    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)

    return shannonEnt


def createDataSet():
    dateSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]

    labels = ['no surfacing', 'flippers']
    return dateSet, labels


def splitDataSet(dataSet, axis, value):
    """
    :param dataSet: 待划分的数据集
    :param axis: 划分数据集的特征
    :param value: 需要返回的特征值
    :return:
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            # 保留前axis个数组元素
            reducedFeatVec = featVec[:axis]
            # 直接添加到数组中，类似Java中list.add
            reducedFeatVec.extend(featVec[axis+1:])
            # 如果数据是数组，则数组整个放入
            retDataSet.append(reducedFeatVec)

    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1


arr = [1, 2, 3]
print(arr[:0])

