# -*- encoding:utf-8 -*-
from osv import fields,osv

class oecn_training_lesson(osv.osv):
    _name = 'oecn.training.lesson'
    _description = 'a test demo'
    _columns={
        'name':fields.char('LessonName',size=64,select=True),
        'date_start':fields.date('StartDate',select=True),
        'total_day':fields.float('Total Days',digits=(16,1)),
        'teacher':fields.many2one('res.users','Teacher'),
        'students':fields.many2many('res.partner',string='Student'),
        'price':fields.float('Price',digits=(16,2))
    }

oecn_training_lesson()
