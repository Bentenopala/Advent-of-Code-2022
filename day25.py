
def list_snafu(data):
    snafu = []
    for n in data:
        c = 1
        num = []
        for d in n:
            num.append((len(n)-c, d))
            c += 1
        snafu.append(num)
    return snafu


def to_decimal(data):
    decimal = []
    for n in data:
        c, num, l = 1, [], len(n)
        for d in n:
            exp = l-c
            match d:
                case '0':
                    n = 0
                case '1':
                    n = 1
                case '2':
                    n = 2
                case '=':
                    n = -2
                case '-':
                    n = -1
            num.append(n*(5**exp))
            c += 1
        decimal.append(sum(num))
    return decimal


def to_snafu(decimal_number):
    div, snafu = decimal_number, ""
    while div != 0:
        rem = div%5
        div = div//5
        match rem:
            case 0:
                snafu += '0'
            case 1:
                snafu += '1'
            case 2:
                snafu += '2'
            case 3:
                snafu += '='
                add = True
                div += 1
            case 4:
                snafu += "-"
                add = True
                div += 1
    return snafu[::-1]


with open('day25.txt') as myfile:
    data = myfile.read().strip().split("\n")

decimal = sum(to_decimal(data))

print(to_snafu(decimal))



'''
122-12==0-01=00-0=02
'''