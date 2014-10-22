"""Unit test for roman1.py"""

import roman1
import unittest

class KnownValues(unittest.TestCase):
    knownValues = ( (1, 'I'),
                    (2, 'II'),
                    (3, 'III'),
                    (4, 'IV'),
                    (5, 'V'),
                    (6, 'VI'),
                    (7, 'VII'),
                    (8, 'VIII'),
                    (9, 'IX'),
                    (10, 'X'),
                    (50, 'L'),
                    (100, 'C'),
                    (500, 'D'),
                    (1000, 'M'),
                    (31, 'XXXI'),
                    (148, 'CXLVIII'),
                    (294, 'CCXCIV'),
                    (312, 'CCCXII'),
                    (421, 'CDXXI'),
                    (528, 'DXXVIII'),
                    (621, 'DCXXI'),
                    (782, 'DCCLXXXII'),
                    (870, 'DCCCLXX'),
                    (941, 'CMXLI'),
                    (1043, 'MXLIII'),
                    (1110, 'MCX'),
                    (1226, 'MCCXXVI'),
                    (1301, 'MCCCI'),
                    (1485, 'MCDLXXXV'),
                    (1509, 'MDIX'),
                    (1607, 'MDCVII'),
                    (1754, 'MDCCLIV'),
                    (1832, 'MDCCCXXXII'),
                    (1993, 'MCMXCIII'),
                    (2074, 'MMLXXIV'),
                    (2152, 'MMCLII'),
                    (2212, 'MMCCXII'),
                    (2343, 'MMCCCXLIII'),
                    (2499, 'MMCDXCIX'),
                    (2574, 'MMDLXXIV'),
                    (2646, 'MMDCXLVI'),
                    (2723, 'MMDCCXXIII'),
                    (2892, 'MMDCCCXCII'),
                    (2975, 'MMCMLXXV'),
                    (3051, 'MMMLI'),
                    (3185, 'MMMCLXXXV'),
                    (3250, 'MMMCCL'),
                    (3313, 'MMMCCCXIII'),
                    (3408, 'MMMCDVIII'),
                    (3501, 'MMMDI'),
                    (3610, 'MMMDCX'),
                    (3743, 'MMMDCCXLIII'),
                    (3844, 'MMMDCCCXLIV'),
                    (3888, 'MMMDCCCLXXXVIII'),
                    (3940, 'MMMCMXL'),
                    (3999, 'MMMCMXCIX'))

    def testToroman1KnownValues(self):
        """toroman1 should give known result with known input"""
        for integer, numeral in self.knownValues:
            result = roman1.toroman1(integer)
            self.assertEqual(numeral, result)

    def testFromroman1KnownValues(self):
        """fromroman1 should give known result with known input"""
        for integer, numeral in self.knownValues:
            result = roman1.fromroman1(numeral)
            self.assertEqual(integer, result)

class Toroman1BadInput(unittest.TestCase):
    def testTooLarge(self):
        """toroman1 should fail with large input"""
        self.assertRaises(roman1.OutOfRangeError, roman1.toroman1, 4000)

    def testZero(self):
        """toroman1 should fail with 0 input"""
        self.assertRaises(roman1.OutOfRangeError, roman1.toroman1, 0)

    def testNegative(self):
        """toroman1 should fail with negative input"""
        self.assertRaises(roman1.OutOfRangeError, roman1.toroman1, -1)

    def testNonInteger(self):
        """toroman1 should fail with non-integer input"""
        self.assertRaises(roman1.NotIntegerError, roman1.toroman1, 0.5)

class Fromroman1BadInput(unittest.TestCase):
    def testTooManyRepeatedNumerals(self):
        """fromroman1 should fail with too many repeated numerals"""
        for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman1.Invalidroman1NumeralError, roman1.fromroman1, s)

    def testRepeatedPairs(self):
        """fromroman1 should fail with repeated pairs of numerals"""
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(roman1.Invalidroman1NumeralError, roman1.fromroman1, s)

    def testMalformedAntecedent(self):
        """fromroman1 should fail with malformed antecedents"""
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman1.Invalidroman1NumeralError, roman1.fromroman1, s)

class SanityCheck(unittest.TestCase):
    def testSanity(self):
        """fromroman1(toroman1(n))==n for all n"""
        for integer in range(1, 4000):
            numeral = roman1.toroman1(integer)
            result = roman1.fromroman1(numeral)
            self.assertEqual(integer, result)

class CaseCheck(unittest.TestCase):
    def testToroman1Case(self):
        """toroman1 should always return uppercase"""
        for integer in range(1, 4000):
            numeral = roman1.toroman1(integer)
            self.assertEqual(numeral, numeral.upper())

    def testFromroman1Case(self):
        """fromroman1 should only accept uppercase input"""
        for integer in range(1, 4000):
            numeral = roman1.toroman1(integer)
            roman1.fromroman1(numeral.upper())
            self.assertRaises(roman1.Invalidroman1NumeralError,
                              roman1.fromroman1, numeral.lower())

if __name__ == "__main__":
    unittest.main()