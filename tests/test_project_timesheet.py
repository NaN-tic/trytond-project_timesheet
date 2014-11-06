#!/usr/bin/env python
# This file is part project_timesheet module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_depends


class ProjectTimesheetTestCase(unittest.TestCase):
    'Test Project Timesheet module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('project_timesheet')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProjectTimesheetTestCase))
    return suite
