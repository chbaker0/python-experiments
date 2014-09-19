def quicksort_pivot_select(l, b, e):
    return b + (e - b) // 2

def quicksort_partition(l, b, e):
    pivot_index = quicksort_pivot_select(l, b, e)
    l[pivot_index], l[e-1] = l[e-1], l[pivot_index]

    left_div = 1
    right_div = e-1

    while left_div < right_div:
        if l[left_div] < l[e-1]:
            left_div += 1
        else:
            right_div -= 1
            l[left_div], l[right_div] = l[right_div], l[left_div]

    l[left_div], l[e-1] = l[e-1], l[left_div]

    return left_div
        
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
