# 2s = "5,0 6,1 6,2 5,3 4,3 3,3 2,2 1,1 0,0 0,1 0,2 0,3"
# ms = "6,4 5,4 4,4 3,4 2,4 1,4 0,4 5,3 4,2 5,1 6,0 5,0 4,0 3,0 2,0 1,0 0,0"

# 1
s = "6,2 5,2 4,2 3,2 2,2 1,2 0,2 0,1 0,3 5,1"

s = "0,4 1,3 2,2 4,2 5,3 6,4 6,1 5,1 4,1 3,1 2,1 1,1 0,1"  # k

s = "0,3 0,2 0,1 5,4 4,4 3,4 2,4 1,4 6,3 6,2 6,1 6,0 5,0 4,0 3,0 2,0 1,0 0,0"  # d
s = "6,4 5,4 4,4 3,4 2,4 3,3 4,2 5,1 6,0 5,0 4,0 3,0 2,0"  # n
s = "6,4 6,3 6,2 6,1 5,0 4,0 3,1 3,2 3,3 1,4 2,4 0,3 0,2 0,1 0,0"  # s
s = "6,4 6,3 6,2 6,1 5,0 4,0 3,1 3,2 3,3 2,4 1,4 0,3 0,2 0,1 0,0"  # s

# s8 = "6,2 6,1 5,0 4,0 3,1 3,2 2,3 1,3 0,2 0,1 1,0 2,0 4,3 5,3"
iss = s.split(" ")
print(iss)

sss = []
ss = []

for i in range(len(iss)):
    ss.append(iss[i].split(","))
    sss.append(ss.copy())

mat = [[0 for i in range(7)] for ii in range(5)]
mats = []


def d(m):
    dd = [[0 for i in range(len(m[0]))] for i in range(len(m))]
    for j, i in enumerate(m):
        for k, mm in enumerate(i):
            dd[j][k] = mm
    return dd


for i in sss:
    for y in i:
        print(y)
        mat[int(y[1])][int(y[0])] = 1

    p = d(mat)
    mats.append(p)

for i in mats:
    p = ''
    print('             db', end=" ")
    for m in i:
        p = p + ('0' + ''.join(map(str, m)) + 'b,')
    print(p[:-1])

"""
// for 7 segment array 

td = [[0 for x in range(7)] for _ in range(5)]

tdn = [[0 for x in range(7)] for _ in range(5)]


for i in range(5):
    for y in range(7):
        tdn[i][y]= [i,y]  

for i in tdn:
    print(i)
// 7 segment end

// for showing matrix position
k= "[1, 0]a [1, 1]a [1, 2]a [1, 3]a [1, 4]a [1, 5]a [1, 6]a[4,6]a[3,5]a[2,4]a[2,2]a[3,1]a [4,0]"
s = "[4,6]a[3,6]a[2,6]a[1,6]a[0, 5]a [0, 4]a[1, 3]a[2,3]a[3,3]a[4, 1]a[4, 2]a[3,0]a[2,0]a[1,0]a[0,0]"
d = "[0, 0]a [0, 1]a [0, 2]a [0, 3]a [0, 4]a [0, 5]a [0, 6]a [1,6]a[2,6]a[3,6]a [4, 1]a [4, 2]a [4, 3]a [4, 4]a [4, 5]a[1,0]a[2,0]a[3,0]"
n = " [0, 2]a [0, 3]a [0, 4]a [0, 5]a [0, 6]a [1,5]a[2,4]a[3,3]a[4, 2]a [4, 3]a [4, 4]a [4, 5]a [4, 6]"
ss = n.replace("a", " ")
sss = ss.replace("[", "")
ssss = sss.replace("]","")
#print(ssss)
def ins(dd):

    for d in dd:
        temp = d[0]
        d[0] = d[1]
        d[1] = temp
kk = "0,2 0,3 0,4 0,5 0 6 1,5 2,4 3,3 4,2 4,3 4,4 4,5 4,6"
print(kk[::-1])


#1,0 1,1 1,2 1,3 1,4 1,5 1,6 4,6 3,5 2,4 2,2 3,1 4,0 = k

#4,6 3,6 2,6 1,6 0,5  0,4 1,3 2,3 3,3 4,1 4,2 3,0 2,0 1,0 0,0=s

#0,0 0,1 0,2 0,3 0,4 0,5 0,6 1,6 2,6 3,6 4,1 4,2 4,3 4,4 4,5 1,0 2,0 3,0=d

#0,2 0,3 0,4 0,5 0 6 1,5 2,4 3,3 4,2 4,3 4,4 4,5 4,6=n
// end showing matrix position
//
;segment1

 mov dx ,2030h
 mov cx , 2 
 mov si, 0

 seg1:  

 mov al, s1[si]
 out dx, al
 inc si

 mov bx, 30
 delay:



 dec bx
 cmp bx, 0
 jne delay

 loop seg1


;segmentend  
i = ""#"00000000b,
	01000010b,
	01111111b,
	01000000b,
	00000000b,

	01111111b, 
    00000010b, 
    00000100b, 
    00000010b, 
    01111111b,


	01000010b,
	01100001b,
	01010001b,
	01001110b,
	00000000b,       

	01111111b, 
    00000010b, 
    00000100b, 
    00000010b, 
    01111111b,


	00110110b,
	01001001b,
	01001001b,
	00110110b,
	00000000b
	""#"

iss = i.split(",")
s = iss[0].strip()
for y, ii in enumerate(iss):
    if y != 0:
        s = s+','+ii.strip()
print(s)


"""

"""


3 = 6,5,0,4,3
7 = 6,5,4
9 = 0,1,6,5,4
4 = 1,0,5,4
5 = 6,1,0,4,3
00000001b,00000011b,01000011b,01000111b,01001111b
00000001b,00000011b,00000111b
01000000b,01100000b,01100001b,01100011b,01100111b
00100000b,01100000b,01100010b,01100110b
00000001b,00100001b,01100001b,01100101b,01101101b


s = "6,1,0,4,3"
s = s.split(",")
s = list(map(int, s))
ls = [ [ 1 for i in range(7)] for i in range(7)]
def cp(d):
    ar = [[0 for i in range(7)] for ii in range(7)]

    for y, i in enumerate(d):
        ar[y] = i  

    return ar

mat = [0,0,0,0,0,0,0]
mats = []
for i in s:
    mat[i] = 1 
    mats.append(cp(mat))

for i in mats:

    s = ''.join(map(str,i))
    print("0"+s+"b", end=",")


//some reason 

s = "0,0 0,1 0,2 0,3 2,4 1,4 3,3 3,2 3,1 4,0 5,0 6,1 6,2 6,3 6,4"#s
ls = s.split(" ") 

ln = ls[::-1]
ss = " ".join(ln)
print(ss)

"""
