ARRAY_LENGTH = 5

def replaceData(numData):
        retData = [] 

        for i in range(len(numData)):
                for j in range(len(numData[i])):
                        if numData[i][j] < 0:
                                numData[i][j] = 0
                        if numData[i][j] > 100:
                                numData[i][j] %= 100

        retData = numData

        return retData

def getMaxSum(numData):
        maxSum = 0

        for i in range(len(numData)-1):
                for j in range(len(numData[i])-1):
                        thisTime = numData[i][j] + numData[i+1][j] + numData[i][j+1] + numData[i+1][j+1]
                        if maxSum < thisTime:
                                maxSum = thisTime

        return maxSum

numData =[]
ARRAY_LENGTH = 5

def main() :
        global numData

        loadData()

        print(' ----- 초기 배열 -----')
        printData()

        numData = replaceData(numData)
        print(' ----- 치환 후 배열 -----')
        printData()

        maxSum = getMaxSum(numData)
        print('최대 영역의 합: %d' % maxSum)

       

def  loadData() :
        global numData

        numData = \
        [
                [ 5, 7, -5, 100, 73 ],
                [ 35, 23, 4, 190, 33 ],
                [ 49, 85, 662, 39, 81 ],
                [ 124, -59, 86, 46, 52 ],
                [ 27, 7, 8, 33, -56 ] 
        ]
    

def printData() :
        for i in range(0, ARRAY_LENGTH) :
                for k in range(0, ARRAY_LENGTH) :
                        try :
                                print("%5d" % numData[i][k], end='')
                        except :
                                pass
                print()
        print('--------------------------------------')

if __name__ == "__main__" :
    main()