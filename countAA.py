#!/usr/bin/env python

def aaCount(dna):
    "This function passes a string and counts the M's R's and Y's"
    totalM = float(dna.count("M"))
    totalR =  float(dna.count("R"))
    totalY = float(dna.count("Y"))
    totalL = float(dna.count("L"))
    dnaN = dna.replace("L","l")
    total = float(totalM+totalR+totalY+totalL) / len(dna)
    return dnaN, totalM, totalR, totalY, totalL, total


