from odoo import models, fields, api

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    
    # Creamos el nuevo campo calculado
    nam_importe_usd = fields.Float(string='Importe USD', compute='_compute_nam_importe_usd')

    @api.depends('amount', 'date')
    def _compute_nam_importe_usd(self):
        # Buscamos la moneda USD en la base de datos
        usd_currency = self.env['res.currency'].search([('name', '=', 'USD')], limit=1)
        
        for line in self:
            # Si no hay USD configurado o el apunte no tiene fehca, lo dejamos en 0 
            if not usd_currency or not line.date:
                line.nam_importe_usd = 0.0
                continue
            
            moneda_base = line.company_id.currency_id or self.env.company.currency_id

            # MAGIA DE ODOO: Convertimos pasándole estrictamente la fecha del apunte (line.date)
            line.nam_importe_usd = moneda_base._convert(
                line.amount, 
                usd_currency, 
                line.company_id or self.env.company, 
                line.date  
            )