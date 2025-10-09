# Yg -> Gas Gravity of Solution Gas 
# Yo -> Oil Gravity of Stock Tank Oil
# Temp -> Temperature (°R)
# Rs -> Solution Gas-Oil Ratio (scf/STB)

import math
class Calculations:

    def __init__(self, Yg, Yo, Temp):
        self.Yg = Yg
        self.Yo = Yo
        self.Temp = Temp

    def calc_Rs(self, method, P):
        api = 141.5/self.Yo - 131.5
        if method == "Standing": # Standing's Correlation, Applicable for P <= Pb
            x = 0.0125 * api - 0.00091 * (self.Temp - 460)
            self.Rs = self.Yg * (((P/18.2) + 1.4)*10**x)**1.2048
            return self.Rs
        elif method == "Glaso": # Glaso's Correlation
            x = 2.8869 - (14.1811 - 3.3093*math.log10(P)) ** 0.5
            Pb_star = 10**x
            self.Rs = self.Yg * (Pb_star * ((api**0.989)/((self.Temp - 460)**0.172)))**1.225
            return self.Rs
        elif method == "Marhoun": # Marhoun's Correlation
            a = 185.843208
            b = 1.877840
            c = -3.1437
            d = -1.32657
            e = 1.398441
            self.Rs = (a * (self.Yg**b) * (self.Yo**c) * (self.Temp**d) * P)**e
            return self.Rs

    def calc_Bo(self, method, Rs):

        if method == "Standing": # Standing's Correlation
            self.Bo = 0.9759 + 0.00012 * (Rs * (self.Yg / self.Yo)**0.5 + 1.25 * (self.Temp - 460))**1.2
            return self.Bo
        elif method == "Marhoun": # Marhoun's Correlation
            a = 0.742390
            b = 0.323294
            c = - 1.202040
            F = (Rs**a) * (self.Yg**b) * (self.Yo**c)
            self.Bo = 0.497069 + (0.862963*(10**-3) * self.Temp) + (0.182594 * (10**-2)*F) + (0.318099 * (10**-5)*(F**2) )
            return self.Bo
        elif method == "Glaso": # Glaso's Correlation
            Bob = Rs * (self.Yg / self.Yo)**0.526 + 0.968 * (self.Temp - 460)
            A = -6.58511 + 2.91329*math.log10(Bob) - 0.27683*(math.log10(Bob)**2)
            self.Bo = 1.0 + 10**A
            return self.Bo

    def calc_Pb(self, method, Rsi):
        api = 141.5/self.Yo - 131.5
        if(method == "Standing"):
            a = 0.00091 * (self.Temp - 460) - 0.0125 * api
            self.Pb = 18.2 * (((Rsi/self.Yg)**0.83) * (10**a) - 1.4)
            return self.Pb
        elif(method == "Glaso"):
            a = 0.816
            b = 0.172
            c = -0.989
            Pb_star = (Rsi/self.Yg)**(a) * (self.Temp - 460)**b * (api**c)
            self.Pb = 10**(1.7660 + 1.7447 * math.log10(Pb_star) - 0.30218 * (math.log10(Pb_star)**2))
            return self.Pb
        elif(method == "Marhoun"):
            a = 5.38088e-3
            b = 0.715082
            c = -1.87784
            d = 3.1437
            e = 1.32657
            self.Pb = a * (Rsi**b) * (self.Yg**c) * (self.Yo**d) * (self.Temp**e)
            return self.Pb