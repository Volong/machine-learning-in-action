#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from math import log
import operator


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
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]

    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def splitDataSet(dataSet, axis, value):
    """
    :param dataSet: 待划分的数据集
    :param axis: 划分数据集的位置
    :param value: 划分数据集的特征
    :return:
    """
    retDataSet = []
    for featVec in dataSet:
        # 以 axis 为临界点对数据进行划分
        if featVec[axis] == value:
            # 保留前axis个数组元素（含头不含尾）
            reducedFeatVec = featVec[:axis]
            # 直接添加到数组中，类似Java中list.add
            reducedFeatVec.extend(featVec[axis+1:])
            # 如果数据是数组，则数组整个放入
            retDataSet.append(reducedFeatVec)

    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    """
    :param dataSet: 三列数据，前两列为特征，最后一列为具体分类
    :return:
    """
    # 特征数量
    numFeatures = len(dataSet[0]) - 1
    # 计算数据集的熵
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1

    # 只会对dataSet前两列数据进行处理
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]

        uniqueVals = set(featList)
        newEntropy = 0.0

        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)

        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i

    return bestFeature


def majorityCnt(classList):
    """
    返回出现次数最多的分类
    :param classList:
    :return:
    """
    classCount = {}
    # 统计分类出现的次数
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0

        classCount[vote] += 1

    # 对分类的次数进行讲叙排
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1),
                              reverse=True)
    # 获取分类次数最多的分类
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    """
    创建一个决策树
    :param dataSet: 数据集，前两列为特征，最后一列为具体分类
    :param labels: 标签列表
    :return:
    """
    # 获取所有的标签
    classList = [example[-1] for example in dataSet]

    # 如果某个分类出现的次数与列表的长度相等，说明分类都一样，则直接返回
    if classList.count(classList[0]) == len(classList):
        return classList[0]

    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}

    del(labels[bestFeat])

    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)

    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)

    return myTree


myDat, lables = createDataSet()
feature = chooseBestFeatureToSplit(myDat)
print(feature)
print(myDat)

