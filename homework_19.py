#Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    '''this function calculate amount of positive numbers and sum of negatives numbers'''
    count_1 = 0
    sum_1 = 0
    for i in arr:
        if i>0:
            count_1+=1
        elif i<=0:
            sum_1+=i
    count_1 = [count_1]
    count_1.append(sum_1)
    if count_1[0]>0 or count_1[1]<0:
    	return count_1
    elif arr == []:
    	return []
    else:
    	return [0,0]