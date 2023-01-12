inp1 = input("Ketik angka pertama\t: ")
inp2 = input("Ketik angka kedua\t: ")

num1 = int(inp1)
num2 = int(inp2)

def fpb(a,b):
    while b > 0:
        a, b = b, a % b
        nilaifpb = a
    return nilaifpb
    
def kpk(a, b):
    nilaikpk = int(a * b / fpb(a, b))
    return nilaikpk


print("FPB dari ", num1, " dan ", num2, " adalah = ", fpb(num1, num2))
print("KPK dari ", num1, " dan ", num2, " adalah = ", kpk(num1, num2))