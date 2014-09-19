def quicksort_pivot_select(l, b, e):
    return b + (e - b) // 2

def quicksort_partition(l, b, e):
    pivot_index = quicksort_pivot_select(l, b, e)
    l[pivot_index], l[b] = l[b], l[pivot_index]

    left_div = 1
    right_div = e

    while left_div < right_div:
        if l[left_div] <= l[b]:
            left_div += 1
        else:
            right_div -= 1
            l[left_div], l[right_div] = l[right_div], l[left_div]

    l[b], l[left_div-1] = l[left_div-1], l[b]
    return left_div-1
        
def quicksort_impl(l, b, e):
    if e - b <= 1:
        return

    part = quicksort_partition(l, b, e)

    quicksort_impl(l, b, part)
    quicksort_impl(l, part+1, e)

def quicksort(l):
    quicksort_impl(l, 0, len(l))

l = [2, 43, 64, 2, 324, 2, 4, 3, 45]
quicksort(l)

for i in l:
    print(i)
