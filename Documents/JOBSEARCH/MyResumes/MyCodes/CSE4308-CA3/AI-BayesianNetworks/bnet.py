from sys import argv
class bayesianNetwork:
    def __init__(self):
        self.Bt = 0.001
        self.Et = 0.002
        self.A_BtEt = 0.95
        self.A_BtEf = 0.94
        self.A_BfEt = 0.29
        self.A_BfEf = 0.001
        self.J_At = 0.9
        self.J_Af = 0.05
        self.M_At = 0.7
        self.M_Af = 0.01
    
    def computeProbability(self, b, e, a, j, m):
        b_val, e_val, a_val, j_val, m_val = 1, 1, 1, 1, 1
        if b == True:
            b_val = self.Bt
        elif b == False:
            b_val = 1 - self.Bt
        if e == True:
            e_val = self.Et
        elif e == False:
            e_val = 1 - self.Et
        if a == True:
            if j == True:
                j_val = self.J_At
            elif j == False:
                j_val = 1 - self.J_At
            if m == True:
                m_val = self.M_At
            elif m == False:
                m_val = 1 - self.M_At
        elif a == False:
            if j == True:
                j_val = self.J_Af
            elif j == False:
                j_val = 1 - self.J_Af
            if m == True:
                m_val = self.M_Af
            elif m == False:
                m_val = 1 - self.M_Af
        if b == True and e == True:
            if a == True:
                a_val = self.A_BtEt
            if a == False:
                a_val = 1 - self.A_BtEt
        if b == True and e == False:
            if a == True:
                a_val = self.A_BtEf
            if a == False:
                a_val = 1 - self.A_BtEf
        if b == False and e == True:
            if a == True:
                a_val = self.A_BfEt
            if a == False:
                a_val = 1 - self.A_BfEt
        if b == False and e == False:
            if a == True:
                a_val = self.A_BfEf
            if a == False:
                a_val = 1 - self.A_BfEf
        return b_val*e_val*a_val*j_val*m_val

def calc_alarm(x, final_res, B, E, A, J, M):
    if B == None and E == None:
        B = E = True
        final_res += x.computeProbability(B, E, A, J, M)
        B, E = True, False
        final_res += x.computeProbability(B, E, A, J, M)
        B, E = False, True
        final_res += x.computeProbability(B, E, A, J, M)
        B = E = False
        final_res += x.computeProbability(B, E, A, J, M)
    elif B == None:
        B = True
        final_res += x.computeProbability(B, E, A, J, M)
        B = False
        final_res += x.computeProbability(B, E, A, J, M)
    elif E == None:
        E = True
        final_res += x.computeProbability(B, E, A, J, M)
        E = False
        final_res += x.computeProbability(B, E, A, J, M)
    else:
        final_res += x.computeProbability(B, E, A, J, M)
    return final_res

def func(x, C):
    B = E = A = J = M = None
    for s in C:
        if s[0] == 'B':
            if s[1] == 't':
                B = True
            else:
                B = False
        if s[0] == 'E':
            if s[1] == 't':
                E = True
            else:
                E = False
        if s[0] == 'A':
            if s[1] == 't':
                A = True
            else:
                A = False
        if s[0] == 'M':
            if s[1] == 't':
                M = True
            else:
                M = False
        if s[0] == 'J':
            if s[1] == 't':
                J = True
            else:
                J = False
    final_res = 0
    flag = True
    if J != None:
        flag = False
        if A == None:
            A = True
            final_res = calc_alarm(x, final_res, B, E, A, J, M)
            A = False
            final_res = calc_alarm(x, final_res, B, E, A, J, M)
        else:
            final_res = calc_alarm(x, final_res, B, E, A, J, M)
    if M != None:
        flag = False
        if A == None:
            A = True
            final_res = calc_alarm(x, final_res, B, E, A, J, M)
            A = False
            final_res = calc_alarm(x, final_res, B, E, A, J, M)
        else:
            final_res = calc_alarm(x, final_res, B, E, A, J, M)
    if flag:
        final_res = calc_alarm(x, final_res, B, E, A, J, M)
    return final_res

if __name__ == '__main__':
    givenFlag = False
    C1 = []
    C2 = []

    for arg in range(1, len(argv)):
        if argv[arg] == 'given':
            givenFlag = True
        elif givenFlag:
            C2.append(argv[arg])
        else:
            C1.append(argv[arg])
    C3 = C1+C2
    x = bayesianNetwork()
    final_res = func(x, C3)
    
    if C2 != []:
        denominator = func(x, C2)
        
        print("Probability = ",final_res/denominator)
    else:
        print("Probability = ",final_res)