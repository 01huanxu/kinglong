#!/usr/bin/env python
#-*-coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
@Authors:          chenqian09(chenqian09@baidu.com)
@Date:             2017/06/01 13:54:06
@Last Modified:    2017/06/01 13:54:06
@Summary:          Python-unittests GTest-Style adapter for CI 
"""

import sys
import time
import unittest

class GTestStyleTestResult(unittest.TestResult):
    """A GTest result class that can print formatted text results to a stream.

    Used by GTestStyleRunner.
    """
    separator1 = '[----------] '
    separator2 = '[==========] '
    def __init__(self, stream, descriptions, verbosity):
        """
        @note: init func
        """
        unittest.TestResult.__init__(self, stream, descriptions, verbosity)
        self.stream = stream
        self.showAll = verbosity > 1
        self.dots = verbosity == 1
        self.descriptions = descriptions

    def getDescription(self, test):
        """
        @note: get test desc
        """
        if self.descriptions:
            return test.shortDescription() or str(test)
        else:
            return str(test)

    def startTest(self, test):
        """
        @note: print all msg when test start
        """
        self.stream.write('[ RUN      ] ')
        self.stream.write(self.getDescription(test))
        self.stream.write('\n')

        unittest.TestResult.startTest(self, test)
        if self.showAll:
            self.stream.write(self.getDescription(test))
            self.stream.write(" ... ")

    def addSuccess(self, test):
        """
        @note: print all msg when test success
        """
        unittest.TestResult.addSuccess(self, test)
        if self.showAll:
            self.stream.write("ok")
            self.stream.write('\n')
        elif self.dots:
            self.stream.write('[       OK ] ')
            self.stream.write(self.getDescription(test))
            self.stream.write('\n')

    def addError(self, test, err):
        """
        @note: print all msg when test error
        """
        unittest.TestResult.addError(self, test, err)
        if self.showAll:
            self.stream.write("ERROR\n")
        elif self.dots:
            self.stream.write('E')

    def addFailure(self, test, err):
        """
        @note: print all msg when test failed
        """
        unittest.TestResult.addFailure(self, test, err)
        if self.showAll:
            self.stream.write("FAIL\n")
        elif self.dots:
            self.stream.write('[  FAILED  ] ')
            self.stream.write(self.getDescription(test))
            self.stream.write(self._exc_info_to_string(err, test))


class GTestStyleRunner(object):
    """
    @note: A GTest Style Output Runner
    """
    def __init__(self, stream=sys.stderr, descriptions=1, verbosity=1):
        """
        @note: init
        """
        self.stream = stream
        self.descriptions = descriptions
        self.verbosity = verbosity

    def run(self, test):
        """
        @note: run func
        """
        result = GTestStyleTestResult(self.stream, self.descriptions, self.verbosity)
        startTime = time.time()
        test(result)
        stopTime = time.time()
        timeTaken = stopTime - startTime
        self.stream.write(result.separator2)
        run = result.testsRun
        self.stream.write("Ran %d test%s in %.3fs\n" %
                            (run, run != 1 and "s" or "", timeTaken))

        failed, errored = map(len, (result.failures, result.errors))

        self.stream.write("[  PASSED  ] %d tests\n" % (run - failed - errored))

        if not result.wasSuccessful():
            errorsummary = ""
            if failed:
                self.stream.write("[  FAILED  ] %d tests, listed below:\n" % failed)
                for failedtest, failederorr in result.failures:
                    self.stream.write("[  FAILED  ] %s\n" % failedtest)
            if errored:
                self.stream.write("[  ERRORED ] %d tests\n" % errored)
                for erroredtest, erorrmsg in result.errors:
                    self.stream.write("[  ERRORED ] %s\n" % erroredtest)

            if failed:
                self.stream.write("%d ERRORED TEST\n" % failed)
            if errored:
                self.stream.write("%d ERRORED TEST\n" % errored)

        return result