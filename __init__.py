# This file is part project_timesheet module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .work import *

def register():
    Pool.register(
        WorkOpenTimesheetLine,
        WorkOpenAllTimesheetLine,
        module='project_timesheet', type_='wizard')
