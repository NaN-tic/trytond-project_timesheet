# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta

__all__ = ['TimesheetWork', 'TimesheetLine']
__metaclass__ = PoolMeta


class TimesheetWork:
    __name__ = 'timesheet.work'

    project_works = fields.One2Many('project.work', 'work', 'Project Works',
        readonly=True)


class TimesheetLine:
    __name__ = 'timesheet.line'

    project_work = fields.Function(fields.Many2One('project.work',
            'Project Work', required=True),
        'get_project_work', setter='set_project_work',
        searcher='search_project_work')

    def get_project_work(self, name):
        if not self.work.project_works:
            return None
        return self.work.project_works[0].id

    @classmethod
    def set_project_work(cls, lines, name, value):
        ProjectWork = Pool().get('project.work')
        work_id = None
        if value:
            project_work = ProjectWork(value)
            work_id = project_work.work.id
        cls.write(lines, {
                'work': work_id,
                })

    @classmethod
    def search_project_work(cls, name, clause):
        return [('work.project_works',) + tuple(clause[1:])]

    @classmethod
    def create(cls, vlist):
        ProjectWork = Pool().get('project.work')
        for vals in vlist:
            if not vals.get('work') and vals.get('project_work'):
                project_work = ProjectWork(vals['project_work'])
                vals['work'] = project_work.work.id
        return super(TimesheetLine, cls).create(vlist)
