# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.wizard import Wizard, StateAction
from trytond.pyson import PYSONEncoder
from trytond.transaction import Transaction

__all__ = ['WorkOpenTimesheetLine', 'WorkOpenAllTimesheetLine']
__metaclass__ = PoolMeta


class WorkOpenTimesheetLine(Wizard):
    'Open All Timesheet Lines from Project Work'
    __name__ = 'project.work.open.timesheet.line'
    start_state = 'open_'
    open_ = StateAction('timesheet.act_line_form')

    def do_open_(self, action):
        Work = Pool().get('project.work')

        active_id = Transaction().context['active_id']
        works = Work.search([('id', '=', active_id)])
        action['pyson_domain'] = PYSONEncoder().encode([
                ('work', 'in', [w.work.id for w in works if w.work]),
                ])

        return action, {}


class WorkOpenAllTimesheetLine(Wizard):
    'Open All Timesheet Lines from Project Work'
    __name__ = 'project.work.open.all.timesheet.line'
    start_state = 'open_'
    open_ = StateAction('timesheet.act_line_form')

    def do_open_(self, action):
        Work = Pool().get('project.work')

        active_id = Transaction().context['active_id']
        works = Work.search([('parent', 'child_of', [active_id])])
        action['pyson_domain'] = PYSONEncoder().encode([
                ('work', 'in', [w.work.id for w in works if w.work]),
                ])

        return action, {}
