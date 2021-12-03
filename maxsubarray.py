import math

def max_subarray(list1):
    l=len(list1)
    if l==1:
        return list1;
    else:
        mid=math.floor(l/2)
       
        sublist1=list1[0:mid]
        sublist2=list1[mid:l]
        max_sub1=max_subarray(sublist1)
        max_sub2=max_subarray(sublist2)
        max_sub3=max_mid_subarray(list1,mid)
        sum1=sum(max_sub1)
        sum2=sum(max_sub2)
        sum3=sum(max_sub3)
        maxsum=max(sum1,sum2,sum3)
        if maxsum==sum1:
            return max_sub1
        elif maxsum==sum2:
            return max_sub2
        else:
            return max_sub3
    

def max_mid_subarray(list1,mid):
    l=len(list1)
    left_maxindex=mid-1
    left_maxsum=-1000000
    left_sum=0
    right_sum=0
    right_maxsum=-100000;
    right_index=mid
    right_maxindex=mid;
    for i in range(mid-1,0,-1):
        left_sum=left_sum+list1[i]
        if left_sum>left_maxsum :
            left_maxsum=left_sum
            left_maxindex=i


    for j in range(mid,l-1):
        
            right_sum=right_sum+list1[j]
            if right_sum>right_maxsum :
                right_maxsum=right_sum
                right_maxindex=j


    return list1[left_maxindex:right_maxindex+1]




testlist=[1,-3,-5,9,11,13,-4,5,-70,9,100,3,-8,9,-11,4]
result=max_subarray(testlist)
print(result)
