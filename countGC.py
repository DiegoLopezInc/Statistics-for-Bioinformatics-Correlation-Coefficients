#!/usr/bin/env python
import math
import re
import sys


def gcContent(dna):
    "This function passes a string and counts the A's and T's"
    total = float(dna.count("G"))
    total = total + float(dna.count("C"))
    return (round((total / len(dna)),2))

