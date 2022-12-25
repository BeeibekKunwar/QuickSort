def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            # swap(start, end, elements)
            #x,y = y,x
            elements[start],elements[end] = elements[end],elements[start]

    #swap(pivot_index, end, elements)
    elements[pivot_index],elements[end] = elements[end],elements[pivot_index]

    return end


if __name__ == '__main__':
    elements = [56,9,29,7,2,15,28]
    print("Unssorted array is :",elements)
    quick_sort(elements, 0, len(elements)-1)
    print("Sorted array is :",elements)