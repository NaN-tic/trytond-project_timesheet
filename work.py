# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.wizard import Wizard, StateAction
from trytond.pyson import PYSONEncoder
from trytond.transaction import Transaction

__all__ = ['WorkOpenTimesheetLine']
__metaclass__ = PoolMeta


class WorkOpenTimesheetLine(Wizard):
    'Open Timesheet Lines from Project Work'
    __name__ = 'project.work.open.timesheet.line'
    start_state = 'open_'
    open_ = StateAction('timesheet.act_line_form')

    def do_open_(self, action):
        Work = Pool().get('project.work')

        active_id = Transaction().context['active_id']
        works = Work.search([('parent', 'child_of', [active_id])])
        action['pyson_domain'] = PYSONEncoder().encode([
                ('project_work', 'in', [w.id for w in works]),
                ])

        return action, {}
