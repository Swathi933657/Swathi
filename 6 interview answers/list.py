#Write a function that partitions a list into n nearly equal parts and returns a list of lists.

def partition_list(lst, n):
    if n <= 0:
        raise ValueError("Number of partitions must be positive")
    
    length = len(lst)
    avg = length / n
    partitions = []
    last = 0.0

    while last < length:
        next_index = int(last + avg)
        partitions.append(lst[int(last):next_index])
        last += avg

    return partitions

