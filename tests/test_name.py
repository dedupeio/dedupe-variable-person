import unittest
from dedupe.variables.person import WesternPersonNameType

import numpy

class TestName(unittest.TestCase):

    def test_sounds_like_company(self) :
        name = WesternPersonNameType({'field' : 'foo'})
        distance = name.comparator('Goldman Sachs Co', 
                                   'Goldman, Sachs Co.')
        assert len(distance) == 65

def prettyPrint(variable, comparison) :
    for e in zip(variable.higher_vars, comparison) :
        print("%s:\t %s" % e)

