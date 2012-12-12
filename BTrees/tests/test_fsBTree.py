##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import unittest


class fsBucketBase(object):

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_toString(self):
        bucket = self._makeOne([(c*2, c*6) for c in 'abcdef'])
        self.assertEqual(bucket.toString(),
                         'aabbccddeeffaaaaaabbbbbbccccccddddddeeeeeeffffff')

    def test_fromString(self):
        before = self._makeOne([(c*2, c*6) for c in 'abcdef'])
        after = before.fromString(before.toString())
        self.assertEqual(before.__getstate__(), after.__getstate__())

    def test_fromString_empty(self):
        before = self._makeOne([(c*2, c*6) for c in 'abcdef'])
        after = before.fromString('')
        self.assertEqual(after.__getstate__(), ((),))

    def test_fromString_invalid(self):
        bucket = self._makeOne([(c*2, c*6) for c in 'abcdef'])
        self.assertRaises(ValueError, bucket.fromString, 'xxx')


class fsBucketTests(unittest.TestCase, fsBucketBase):

    def _getTargetClass(self):
        from BTrees.fsBTree import fsBucket
        return fsBucket


class fsBucketPyTests(unittest.TestCase, fsBucketBase):

    def _getTargetClass(self):
        from BTrees.fsBTree import fsBucketPy
        return fsBucketPy


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(fsBucketTests),
        unittest.makeSuite(fsBucketPyTests),
    ))
