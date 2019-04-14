def get_water_capacity(area):

    width = len(area)

    highest_from_left = [0] * width
    highest_from_right = [0] * width

    highest_from_left[0] = area[0]
    for index in range(1, width):
        highest_from_left[index] = max(highest_from_left[index-1], area[index])

    highest_from_right[width-1] = area[width-1]
    for index in range(width-2,-1,-1):
        highest_from_right[index] = max(highest_from_right[index+1], area[index])

    capacity = 0

    for index in range(1, width-1):
        capacity += min(highest_from_left[index], highest_from_right[index]) - area[index]

    return capacity

print(get_water_capacity([3, 0, 1, 3, 0, 5]))
