# encoding:utf-8

'''
最优时间复杂度：O(n)
最坏时间复杂度：O(n^2)
稳定性：稳定
'''

def bubble_sort(alist):
	'''冒泡排序'''
	for j in range(len(alist)-1,0,-1):
		count=0
		# j表示每次遍历需要比较的次数，是逐渐减小的
		for i in range(j):
			if alist[i]>alist[i+1]:
				count+=1
				alist[i],alist[i+1]=alist[i+1],alist[i]

		if count==0:
			break

'''
最优时间复杂度：O(n^2)
最坏时间复杂度：O(n^2)
稳定性：不稳定（考虑升序每次选择最大的情况）
'''
def selection_sort(alist):
	'''选择排序'''
	n=len(alist)
	for i in range(n-1):
		min_index=i
		for j in range(i+1,n):
			if alist[j]<alist[min_index]:
				min_index=j
		if min_index!=i:
			alist[i],alist[min_index]=alist[min_index],alist[i]

'''
最优时间复杂度：O(n)
最坏时间复杂度：O(n^2)
稳定性：稳定
'''
def insert_sort(alist):
	'''插入排序'''
	# 从第二个位置，即下标为1的元素开始向前插入
	for i in range(1,len(alist)):# 从第i个元素开始向前比较，如果小于前一个元素，交换位置
		for j in range(i,0,-1):
			if alist[j]<alist[j-1]:
				alist[j],alist[j-1]=alist[j-1],alist[j]

'''

'''
def quick_sort(alist,start,end):
	'''快速排序'''
	if start>=end:
		return
	# 设定起始元素为要寻找位置的基准元素
	mid=alist[start]
	low=start
	high=end
	while low<high:
		while low < high and alist[high]>=mid:
			high-=1
		alist[low]=alist[high]

		while low < high and alist[low] < mid:
			low+=1
		alist[high]=alist[low]
	alist[low]=mid
	quick_sort(alist,start,low-1)
	quick_sort(alist,low+1,end)



def quick_sort1(alist,start,end):
	'''快速排序'''
	if start>end:
		return
	low=start
	high=end
	mid=alist[start]

	while low<high:
		while low and high and alist[high]>=mid:
			high-=1
		alist[low]=alist[high]

		while low<high and alist[low]<mid:
			low+=1
		alist[high]=alist[low]

	alist[low]=mid
	quick_sort1(alist,start,low-1)
	quick_sort1(alist,low+1,end)


def insert_sort1(alist):
	n=len(alist)
	for i in range(1,n):
		for j in range(i,0,-1):
			if alist[j-1]>alist[j]:
				alist[j-1],alist[j]=alist[j],alist[j-1]


def selection_sort1(alist):
	for i in range(0,len(alist)):
		min_index=i
		for j in range(i+1,len(alist)):
			if alist[min_index]>alist[j]:
				min_index=j
		if min_index!=i:
			alist[min_index],alist[i]=alist[i],alist[min_index]

if __name__ == '__main__':
	li=[54,26,93,17,77,31,44,55,20]
	#li=[5,2,3,8,6]
	# bubble_sort(li)
	# print("bubble_sort:",li)

	li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	selection_sort(li)
	print("selection_sort:",li)

	li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	selection_sort1(li)
	print("selection_sort1:",li)


	# li = [54, 26, 93, 17, 77, 31, 44, 55,55, 20]
	# #li = [8,4,2,5]
	# quick_sort1(li,0,len(li)-1)
	# print("quick_sort:",li)