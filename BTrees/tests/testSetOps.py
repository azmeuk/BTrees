##############################################################################
#
# Copyright (c) 2002 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
import unittest

from .common import MultiUnion
from .common import SetResult
from .common import Weighted
from .common import itemsToSet
from .common import makeBuilder

# Check that various special module functions are and aren't imported from
# the expected BTree modules.
class TestImports(unittest.TestCase):
    def testWeightedUnion(self):
        from BTrees.IIBTree import weightedUnion
        from BTrees.OIBTree import weightedUnion

        try:
            from BTrees.IOBTree import weightedUnion
        except ImportError:
            pass
        else:
            self.fail("IOBTree shouldn't have weightedUnion")

        from BTrees.LLBTree import weightedUnion
        from BTrees.OLBTree import weightedUnion

        try:
            from BTrees.LOBTree import weightedUnion
        except ImportError:
            pass
        else:
            self.fail("LOBTree shouldn't have weightedUnion")

        try:
            from BTrees.OOBTree import weightedUnion
        except ImportError:
            pass
        else:
            self.fail("OOBTree shouldn't have weightedUnion")

    def testWeightedIntersection(self):
        from BTrees.IIBTree import weightedIntersection
        from BTrees.OIBTree import weightedIntersection

        try:
            from BTrees.IOBTree import weightedIntersection
        except ImportError:
            pass
        else:
            self.fail("IOBTree shouldn't have weightedIntersection")

        from BTrees.LLBTree import weightedIntersection
        from BTrees.OLBTree import weightedIntersection

        try:
            from BTrees.LOBTree import weightedIntersection
        except ImportError:
            pass
        else:
            self.fail("LOBTree shouldn't have weightedIntersection")

        try:
            from BTrees.OOBTree import weightedIntersection
        except ImportError:
            pass
        else:
            self.fail("OOBTree shouldn't have weightedIntersection")

    def testMultiunion(self):
        from BTrees.IIBTree import multiunion
        from BTrees.IOBTree import multiunion

        try:
            from BTrees.OIBTree import multiunion
        except ImportError:
            pass
        else:
            self.fail("OIBTree shouldn't have multiunion")

        from BTrees.LLBTree import multiunion
        from BTrees.LOBTree import multiunion

        try:
            from BTrees.OLBTree import multiunion
        except ImportError:
            pass
        else:
            self.fail("OLBTree shouldn't have multiunion")

        try:
            from BTrees.OOBTree import multiunion
        except ImportError:
            pass
        else:
            self.fail("OOBTree shouldn't have multiunion")


def test_suite():
    return unittest.TestSuite((

        unittest.makeSuite(TestImports),
    ))
