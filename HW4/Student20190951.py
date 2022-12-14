import numpy as np
import operator
import sys
from os import listdir

def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	print(maxVals)
	ranges = maxVals - minVals
	normDataSet = np.zeros(np.shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - np.tile(minVals, (m, 1))
	normDataSet = normDataSet / np.tile(ranges, (m, 1))
	return normDataSet, ranges, minVals

def classify0(inX, dataSet, labels, k):
    	dataSetSize = dataSet.shape[0]
    	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    	sqDiffMat = diffMat ** 2
    	sqDistances = sqDiffMat.sum(axis = 1)
    	distances = sqDistances ** 0.5
    	sortedDistIndicies = distances.argsort()
    	classCount = {}
    	for i in range(k):
        	voteIlabel = labels[sortedDistIndicies[i]]
        	classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    	sortedClassCount = sorted(classCount.items(),
            	key = operator.itemgetter(1), reverse = True)
    	return sortedClassCount[0][0]

def img2vector(filename):
	returnVect = np.zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0, 32*i+j] = int(lineStr[j])
	return returnVect

def handwriting(k):
	labels = []
	trainingFileList = listdir('trainingDigits')
	m = len(trainingFileList)
	trainingMat = np.zeros((m, 1024))
	for i in range(m):
		fileNameStr = trainingFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		labels.append(classNumStr)
		trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
	testFileList = listdir('testDigits')
	errorCount = 0.0
	mTest = len(testFileList)
	for i in range(mTest):
		fileNameStr = testFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
		classifierResult = classify0(vectorUnderTest, trainingMat, labels, k) //k
		if (classifierResult != classNumStr): errorCount += 1.0
	errorT = (errorCount/float(mTest))*100
	print(int(errorT))

a = sys.argv[1]
b = sys.argv[2]
for i in range(1, 21):
	handwriting(i)
