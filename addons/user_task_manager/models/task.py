from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Task(models.Model):
    _name = "user.task"
    _description = "User Task"
    _order = "deadline asc"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    priority = fields.Selection(selection=[
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ], string="Priority", default="low")
    
    state = fields.Selection(selection=[
        ("draft", "Draft"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
        ("cancel", "Cancelled"),
    ], string="State", default="draft")

    deadline = fields.Date(string="Deadline")
    is_done = fields.Boolean(string="Done", compute="_compute_is_done", store=True)
    user_id = fields.Many2one(comodel_name="res.users", string="Assigned to", default=lambda self: self.env.user, required=True)

    @api.depends("state")
    def _compute_is_done(self):
        for task in self:
            task.is_done = task.state == "done"

    @api.constrains("deadline")
    def _check_deadline(self):
        for task in self:
            if task.deadline and task.deadline < fields.Date.today():
                raise ValidationError("The deadline cannot be earlier than the minimum sale date.")
