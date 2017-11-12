

def fibDyn(n):
    numbers = [0,1]
    count   = 2
    while count <= n:
        numbers.append(numbers[count-1] + numbers[count-2])
        count += 1
    return numbers[count-1]


if __name__ == '__main__':
    print fibDyn(35)
