import random
import itertools
import time
import sys

# Set the recursion depth to 1000
sys.setrecursionlimit(1000000000)

lst = [1, 4, 532, 34, 2341, 6, 6, 6, 23, 36, 37, 38, 372, 31, 3000]
lao = []
# for i in range(100):
#     lao.append(random.randint(0, 1000))
# print("lao")
# print(lao)
# lao1 = []
# for i in range(100):
#     lao1.append(random.randint(0, 1000))
# print("lao1")
# print(lao1)
# lao2 = []
# for i in range(100):
#     lao2.append(random.randint(0, 1000))
# print("lao2")
# print(lao2)
# lao3 = []
# for i in range(100):
#     lao3.append(random.randint(0, 1000))
# print("lao3")
# print(lao3)
# lao4 = []
# for i in range(100):
#     lao4.append(random.randint(0, 1000))
# print("lao4")
# print(lao4)


def quicksort(pivotindex, liste):

    if len(liste) <= 1:
        return liste
    if len(liste) == 2 and liste[0] < liste[1]:
        return liste

    if len(liste) == 2 and liste[1] < liste[0]:
        ilk = liste[0]
        liste[0] = liste[1]
        liste[1] = ilk

        return liste

    indexFromRight = len(liste) - 1
    indexFromLeft = 0
    pivotNumber = liste[pivotindex]

    liste[pivotindex] = liste[indexFromRight]
    liste[indexFromRight] = pivotNumber
    indexFromRight -= 1
    # print("start ", liste)
    # print(pivotNumber)
    while indexFromRight > indexFromLeft:
        while pivotNumber < liste[indexFromRight]:
            indexFromRight = indexFromRight-1
        while pivotNumber > liste[indexFromLeft]:
            indexFromLeft = indexFromLeft+1
        # print("****icstart", liste)

        if not indexFromRight > indexFromLeft:
            break

        # print(indexFromLeft, indexFromRight)
        smaller = liste[indexFromRight]
        liste[indexFromRight] = liste[indexFromLeft]
        liste[indexFromLeft] = smaller

        indexFromRight = indexFromRight - 1
        indexFromLeft = indexFromLeft + 1
        # print("****icend", liste)

    # print("INDEXFROMLEF ", indexFromLeft)

    liste[len(liste)-1] = liste[indexFromLeft]
    liste[indexFromLeft] = pivotNumber
    # print("end ", liste)

    l1 = liste[0:indexFromLeft]
    l2 = liste[indexFromLeft+1:len(liste)]

    pivotList = [pivotNumber]
    return quicksort(1, l1) + pivotList + quicksort(1, l2)


print(quicksort(0, lao))
worst = quicksort(0, lao)


def randomizedquicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomizedquicksort(left) + middle + randomizedquicksort(right)


def medianQuickSort(array):
    if len(array) <= 1:
        return array

    first = array[0]
    last = array[-1]
    middle = array[len(array) // 2]
    pivot = sorted([first, middle, last])[1]

    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return medianQuickSort(left) + middle + medianQuickSort(right)


# VERSION1:
print(quicksort(1, lst))

# VERSION2:
# randomInt = random.randint(0, len(lst) - 1)
# print(randomizedquicksort(randomInt, lst))

# VERSION3:
# shuffled = lst.copy()
# random.shuffle(shuffled)
# print(quicksort(1, shuffled))

# VERSION4:
# print("median", medianQuickSort(lst))
f = open('file.txt', 'a')
liste1 = []
for i in range(5):
    random_numbers1 = [random.randint(0, 10*10000) for i in range(10000)]
    strr = "Input" + str(i+1) + "(average)=" + str(random_numbers1)+"\n"
    f.write(strr)
    # print("Input", i+1, "(average)=", random_numbers1)
    # print()
    liste1.append(random_numbers1)

liste2 = []
for i in range(5):
    random_numbers2 = [random.randint(0, 0.75*10000) for i in range(10000)]
    # print(random_numbers2)
    # print()
    liste2.append(random_numbers2)

liste3 = []

for i in range(5):
    random_numbers3 = [random.randint(0, 0.25*10000) for i in range(10000)]

    liste3.append(random_numbers3)

# # INP TYPE 1:
random_numbers4 = [1 for i in range(10000)]



def averageTimeCalculator(liste, versionNo):
    sum = 0
    for i in liste:
        startTime = time.time()
        if (versionNo == 1):
            quicksort(0, i)
        if (versionNo == 2):

            randomizedquicksort(i)
        if (versionNo == 3):
            shuffled = i.copy()
            random.shuffle(shuffled)
            quicksort(1, shuffled)

        if (versionNo == 4):

            medianQuickSort(i)
        endTime = time.time()
        sum = sum+(endTime-startTime)
    return sum / len(liste)


def timeCalculator(liste):
    print("Ver1 Average=", averageTimeCalculator(liste, 1))
    worst1 = quicksort(0, liste[0])
    start = time.time()
    quicksort(0, worst1)
    end = time.time()
    print("Ver1 Worst=", (end-start))
    print("Ver2 Average=", averageTimeCalculator(liste, 2))
    start = time.time()
    randomizedquicksort(worst1)
    end = time.time()
    print("Ver2 Worst=", (end-start))

    print("Ver3 Average=", averageTimeCalculator(liste, 3))
    start = time.time()
    shuffled = worst1.copy()
    random.shuffle(shuffled)
    quicksort(1, shuffled)

    end = time.time()
    print("Ver3 Worst=", (end-start))
    print("Ver4 Average=", averageTimeCalculator(liste, 4))
    start = time.time()
    medianQuickSort(worst1)
    end = time.time()
    print("Ver4 Worst=", (end-start))


timeCalculator(liste1)
f.close()
