if __name__ == '__main__':

    first_name = ['Kamil', 'Kuba', 'Pawel', 'Szymon', 'Ania', 'Agata', 'Ewa', 'Damian', 'Maryla', 'Asia']
    ages = [25, 31, 44, 55, 67, 11, 23, 87, 99, 21]
    height = [186.0, 172.0, 185.0, 182.0, 164.0, 172.0, 176.0, 176.0, 173.0, 165.0]

    print(first_name)
    print(ages)
    print(height)

    diction = [{'First Name': a, 'Age': b, 'Height': c} for a, b, c in zip(first_name, ages, height)]
    print(diction)

    for d in diction:
        d['Age'] = d['Age'] + 1
        d['First Name'] = d['First Name'].lower()

    print(diction)
