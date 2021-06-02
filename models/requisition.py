from odoo import api, models, fields, _
from odoo.exceptions import UserError

class EmployeeRequisition(models.Model):
    _name = 'employee.requisition'
    _description = 'Employee Requisition'

    name = fields.Many2one('hr.employee', string='Employee Name')
    date = fields.Date(string="Date")
    requisition_state = fields.Char(string='Requisition State', default='Draft')

    requisition_line = fields.One2many('employee.requisition.line', 'requisition_id', string='Requisition Line')


    state = fields.Selection([('draft', 'Draft'), 
                ('requisition', 'Requisition'),
                ('approved', 'Approved'),
                ('confirmed', 'Confirmed'),
                ('cancelled', 'Cancelled')], 
                default='draft', string='State')

    def action_requisition(self):
        self.state = 'requisition'
        self.requisition_state = 'Draft'

    def action_approved(self):
        self.state = 'approved'
        self.requisition_state = 'Approved'

    def action_confirmed(self):
        self.state = 'confirmed'
        self.requisition_state = 'Confirmed'

    def action_cancelled(self):
        self.state = 'cancelled'
        self.requisition_state = 'Cancelled'


class EmployeeRequisitionLine(models.Model):
    _name = 'employee.requisition.line'
    _description = 'Employee Requisition'

    product_id = fields.Many2one('product.template', string='Product Name')
    product_qty = fields.Integer(string='Quantity', default=1)
    requisition_id = fields.Many2one('employee.requisition', string='Requisition By')