def merge_sort(list):

    n = len(list)
    if len(list) == 0:
        return 'List is empty. Nothing to sort'

    def merge(left, right, list_to_sort):
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list_to_sort[k] = left[i]
                i += 1
            else:
                list_to_sort[k] = right[j]
                j += 1

            k += 1

        if i == len(left):
            while j < len(right):
                list_to_sort[k] = right[j]
                j += 1
                k += 1
        else:
            while i < len(left):
                list_to_sort[k] = left[i]
                i += 1
                k += 1

        return list

    if n > 1:
        mid = n // 2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)

        merge_sort(right)

        return merge(left, right, list)

    else:
        return list
