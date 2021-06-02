from odoo import api, models, fields, _
from odoo.exceptions import UserError

class EmployeeRequisition(models.Model):
    _name = 'employee.requisition'
    _description = 'Employee Requisition'

    name = fields.Many2one('hr.employee', string='Employee Name')
    date = fields.Date(string="Date")
    requisition_line = fields.One2many('employee.requisition.line', 'requisition_id', string='Requisition Line')

class EmployeeRequisitionLine(models.Model):
    _name = 'employee.requisition.line'
    _description = 'Employee Requisition'

    product_id = fields.Many2one('product.template', string='Product Name')
    product_qty = fields.Integer(string='Quantity', default=1)
    requisition_id = fields.Many2one('employee.requisition', string='Requisition By')