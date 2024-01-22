from datetime import date, timedelta

from odoo import fields, models


class EstateProperties(models.Model):
    _name = "estate.property"
    _description = "Model for Real-Estate Properties"
    name = fields.Char(required=True)
    description = fields.Text(string="Description")
    #  sets today's date + 3 months as the default.
    date_availability = fields.Date(
        string="Date Availability",
        copy=False,
        default=fields.Date.today() + timedelta(days=90),
    )
    expected_price = fields.Float(string="Expected Price")
    selling_price = fields.Float(
        string="Selling Price (Read-Only)",
        compute="_compute_selling_price",
        readonly=True,
        copy=False,
    )

    bedrooms = fields.Integer(string="Bedrooms", default=2)  # default=2 for bedrooms sets 2 as the default room count.

    # Property features
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        [
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
        string="Garden Orientation",
    )
    state = fields.Selection(
        [
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="State",
        required=True,
        copy=False,
        default="new",
    )

    def _compute_selling_price(self):
        # Replace with your actual pricing calculation logic
        for record in self:
            # Example: calculate based on square footage and location
            selling_price = (
                    record.living_area * 500  # Placeholder calculation
            )
            record.selling_price = selling_price
