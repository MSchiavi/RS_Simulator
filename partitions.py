from sympy import solve,Eq
from sympy.abc import A
import time
from fractions import Fraction
import random

start_time = time.time()


class partitions:
    
    Common = 1/16.0
    Uncommon = 1/32.0
    RDT = 1/16.0
    Elite = 1/350.0
    Legs = 1/512.0
    Visage = 1/(10000.0)
    
    Partitions = [0,0,0,0,0,0]

    def __init__(self,BinSize):
        self.BinSize = BinSize
    #self.Partitions = [55875,13968.8,27937.5,1277.14,873.047,44.0]
        #        self.Partitions = FindPartitions(BinSize)
        #        self.RC = Renormalization_constants(self.Partitions,BinSize)
   
   
    def setup(self):
        meh = self.FindPartitions()
        for i in range(0,6):
            self.Partitions[i] = meh[i]
    
    def Normalization_constant(self):
    
        B = solve(Eq(1,A*(self.Common + self.Uncommon + self.RDT + self.Elite + self.Legs + self.Visage)),A)
        #The solve function returns an array.
        return B


    def FindPartitions(self):
        #Order FindPartitions returns an array in
        # Common Uncommon RDT Elite Legs Visage
        B = self.Normalization_constant()
        Partitions = [0,0,0,0,0,0]
        Partitions[0]=(B[0]*self.BinSize*self.Common)
        Partitions[1]=(B[0]*self.BinSize*self.Uncommon)
        Partitions[2]=(B[0]*self.BinSize*self.RDT)
        Partitions[3]=(B[0]*self.BinSize*self.Elite)
        Partitions[4]=(B[0]*self.BinSize*self.Legs)
        Partitions[5]=(B[0]*self.BinSize*self.Visage)
        return Partitions



    def Renormalization_constants(self):
        Renormalizationconstants = [0,0,0,0,0,0]
        partitions = self.FindPartitions()
        Renormalizationconstants[0] = Fraction(float(solve(Eq(self.Common,(partitions[0]*A)/self.BinSize),A)[0])).limit_denominator()
        Renormalizationconstants[1] = Fraction(float(solve(Eq(self.Uncommon,(partitions[1]*A)/self.BinSize),A)[0])).limit_denominator()
        Renormalizationconstants[2] = Fraction(float(solve(Eq(self.RDT,(partitions[2]*A)/self.BinSize),A)[0])).limit_denominator()
        Renormalizationconstants[3] = Fraction(float(solve(Eq(self.Elite,(partitions[3]*A)/self.BinSize),A)[0])).limit_denominator()
        Renormalizationconstants[4] = Fraction(float(solve(Eq(self.Legs,(partitions[4]*A)/self.BinSize),A)[0])).limit_denominator()
        Renormalizationconstants[5] = Fraction(float(solve(Eq(self.Visage,(partitions[5]*A)/self.BinSize),A)[0])).limit_denominator()
        return Renormalizationconstants

    def Renormalize(self,constants):
        
        if random.randint(1,constants.denominator) <= constants.numerator:
            return True
        return False

parts1 = partitions(100000)
constants = parts1.Renormalization_constants()
print(constants)
for i in range(1,30):
    print(parts1.Renormalize(constants[0]))



