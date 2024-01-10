class bin:
    def d(self, m):
        dd = [[0 for i in range(len(m[0]))] for i in range(len(m))]
        for j, i in enumerate(m):
            for k, mm in enumerate(i):
                dd[j][k] = mm
        return dd
    def binary(self, s):
        iss = s.split(" ")


        sss = []
        ss = []

        for i in range(len(iss)):
            ss.append(iss[i].split(","))
            sss.append(ss.copy())

        mat = [[0 for i in range(7)] for ii in range(5)]
        mats = []



        for i in sss:
            for y in i:

                mat[int(y[1])][int(y[0])] = 1

            p = self.d(mat)
            mats.append(p)

        for i in mats:
            p = ''
            print('             db', end=" ")
            for m in i:
                p = p + ('0' + ''.join(map(str, m)) + 'b,')
            print(p[:-1])


