# O(nlog(n)) time | O(1) space - where n is the number of tandem bicycles

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):

    redShirtSpeeds.sort()

    blueShirtSpeeds.sort()

    if not fastest:
        reverseArrayInPlace(redShirtSpeeds)

    totalSpeed = 0

    for idx in range(len(redShirtSpeeds)):

        rider1 = redShirtSpeeds[idx]

        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - idx - 1]

        totalSpeed += max(rider1, rider2)

    return totalSpeed

def reverseArrayInPlace(array):
    start = 0

    end = len(array) - 1

    while start < end:

        array[start], array[end] = array[end], array[start]

        start += 1
        end -= 1

'''
My solution

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):

    # Write your code here.

    redShirtSpeeds.sort()

    blueShirtSpeeds.sort()

    if not fastest:
        rev(redShirtSpeeds)

    res=0

    for i in range(len(redShirtSpeeds)):
        r1=redShirtSpeeds[i]
        r2=blueShirtSpeeds[len(blueShirtSpeeds)-1-i]

        res+=max(r1,r2)

    return res

def rev(arr):
    r=len(arr)-1

    while l<r:
        arr[l],arr[r]=arr[r],arr[l]

        l+=1

        r-=1

'''