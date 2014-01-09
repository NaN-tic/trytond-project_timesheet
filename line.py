#This file is part project_timesheet module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Line']
__metaclass__ = PoolMeta


class Line:
    __name__ = 'timesheet.line'

    @classmethod
    def __setup__(cls):
        super(Line, cls).__setup__()
        cls._order.insert(0, ('date', 'DESC'))
