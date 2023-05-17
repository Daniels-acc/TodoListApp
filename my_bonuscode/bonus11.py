def get_average():
    with open("files/data.txt", 'r') as file:
        data = file.readlines()
    #     slicing - start from first in array (pop out 'temperatures'):
    values = data[1:]
    values = [float(i) for i in values]
    average_local = sum(values) / len(values)
    return average_local

average= get_average()
print(f"Average temp was: {average}")