nums1 = [1,2,3,0,0,0] # [1, 2, 2, 3, 5, 6]
nums2 = [2,5,6]

# nums1 = [1]
# nums2 = []

n = len(nums2)
m = len(nums1) - n

nums1pos = m - 1
nums2pos = n - 1

ending_pos = len(nums1)
while nums2pos >= 0 and nums1pos >= 0:
    ending_pos -= 1
    try:
        if nums2[nums2pos] > nums1[nums1pos]:
            nums1[ending_pos] = nums2[nums2pos]
            nums2pos -= 1
        elif nums1[nums1pos] > nums2[nums2pos]:
            nums1[ending_pos] = nums1[nums1pos]
            nums1pos -= 1
        else:
            nums1[ending_pos] = nums2[nums2pos]
            ending_pos -= 1
            nums1[ending_pos] = nums1[nums1pos]
            nums2pos -= 1
            nums1pos -= 1
    except:
        if nums2[nums2pos] is None:
            if nums1[nums1pos] is not None:
                nums1[ending_pos] = nums1[nums1pos]
                nums1pos -= 1
        if nums1[nums1pos] is None:
            if nums2[nums2pos] is not None:
                nums1[ending_pos] = nums2[nums2pos]
                nums2pos -= 1

    print(f'1:  {nums1pos}.  2: {nums2pos}.  nums1: {nums1}')

if nums2pos >= 0:
    nums1[0:nums2pos] = nums2[0:nums2pos]

if nums1pos >= 0:
    nums1[0:nums1pos] = nums1[0:nums1pos]

print(f'nums1: {nums1}')