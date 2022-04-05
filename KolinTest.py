from NaturalNumber import NaturalNumber
def gcd(x, y):
    """
         Евклидов алгоритм для нахождения наибольшего общего делителя двух чисел
         : параметр х: первое число
         : param y: второе число
         : return: наибольший общий делитель
    """
    # Держите большие числа первыми
    if y > x:
        x, y = y, x
    if y == 0:
        return x
        # Рекурсивный вызов, формула: gcd (a, b) = gcd (b, a% b) {a> b}
    return gcd(y, x % y)


def lcm(x, y):
    """
    Вычислить наименьшее общее кратное из двух чисел
         : параметр х: первое число
         : param y: второе число
         : return: наименее распространенный кратный
    """
    # Формула: наименьшее общее кратное a, b равно наибольшему общему делителю a * b, деленному на a, b
    return int(x * y / gcd(x, y))


def delim(a, b):
    res = ""
    k = len(b)
    num = a[:k]
    if int(b) > int(num):
        num += a[k]
        k += 1
    while k < len(a):
        ch = int(num) // int(b)
        res += str(ch)
        ost = int(num) - ch * int(b)
        num = str(ost) + a[k]
        k += 1
    if k == len(a):
        res += str(int(num) // int(b))
    return res


def vichet(a1, b1, a2, b2):
    b = lcm(b1, b2)
    a1_new = a1 * (b // b1)
    a2_new = a2 * (b // b2)
    a = a1_new - a2_new
    print(a, '/', b, sep="")

def proiz(deg: int, poli: list):
    rez = []
    act_deg = deg - 1
    for i in poli[1:]:
        rez.append((i - 1) * deg)
        deg -= 1
    return rez, act_deg

d = 4
a = [1, 2, 3, 4, 5]
for i in a:
    print(i, "x^", d, " ", sep="", end="")
    d -= 1
print("")
array, deg = proiz(4, a)
for i in array:
    print(i, "x^", deg, " ", sep="", end="")
    deg -= 1

