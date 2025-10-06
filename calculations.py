# Yg -> Gas Gravity of Solution Gas 
# Yo -> Oil Gravity of Stock Tank Oil
# Temp -> Temperature (°R)
# Rs -> Solution Gas-Oil Ratio (scf/STB)

import math
class Calculations:

    def __init__(self, Yg, Yo, Temp, Rs):
        self.Yg = Yg
        self.Yo = Yo
        self.Temp = Temp
        self.Rs = Rs 

    def calc_Bo(self, method):
        # 1 -> Standing's Correlation
        # 2 -> Marhoun's Correlation
        # 3 -> Glaso's Correlation

        if method == 1: # Standing's Correlation
            self.Bo = 0.9759 + 0.00012 * (self.Rs * (self.Yg / self.Yo)**0.5 + 1.25 * (self.Temp - 460))**1.2
            return self.Bo
        elif method == 2: # Marhoun's Correlation
            a = 0.742390
            b = 0.323294
            c = - 1.202040
            F = (self.Rs**a) * (self.Yg**b) * (self.Yo**c)
            self.Bo = 0.497069 + (0.862963*(10**-3) * self.T) + (0.182594 * (10**-2)*F) + (0.318099 * (10**-5)*F**2 )
            return self.Bo
        elif method == 3: # Glaso's Correlation
            Bob = self.Rs * (self.Yg / self.Yo)**0.526 + 0.968 * (self.Temp - 460)
            A = -6.58511 + 2.91329*math.log10(Bob) - 0.27683*(math.log10(Bob)**2)
            self.Bo = 1.0 + 10**A
            return self.Bo
    
   