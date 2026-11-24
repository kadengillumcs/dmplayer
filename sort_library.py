def merge_sort(tracks, key):
    """
    Sorts a list of Track objects based on a specified key using the merge sort algorithm.
    """
    if len(tracks) <= 1:
        return tracks

    mid = len(tracks) // 2
    left_half = merge_sort(tracks[:mid], key)
    right_half = merge_sort(tracks[mid:], key)

    return merge(left_half, right_half, key)

def merge(left, right, key):
    """
    Merges two sorted lists of Track objects into a single sorted list based on a specified key.
    """
    sorted_tracks = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            sorted_tracks.append(left[i])
            i += 1
        else:
            sorted_tracks.append(right[j])
            j += 1

    sorted_tracks.extend(left[i:])
    sorted_tracks.extend(right[j:])

    return sorted_tracks