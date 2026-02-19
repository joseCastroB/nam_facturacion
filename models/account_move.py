from odoo import models, fields, api

class NamCaja(models.Model):
    _name = 'nam.caja'
    _description = 'Listado de Cajas NAM'

    name = fields.Char(string='Nombre o Número de Caja', required=True)

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    nam_caja_id = fields.Many2one(
        comodel_name='nam.caja', 
        string='Nro. Caja'
    )

class AccountMove(models.Model):
    _inherit = 'account.move'

    # 1. NUEVO CAMPO: Fecha de Vencimiento formateada en dd/mm/aa
    nam_fecha_vencimiento_formato = fields.Char(
        string='Fecha de vencimiento', 
        compute='_compute_nam_fecha_vencimiento_formato'
    )

    # 2. Campo Analítica (Lo mantenemos)
    nam_analitica_nombres = fields.Char(
        string='Analítica', 
        compute='_compute_nam_analitica_nombres'
    )

    @api.depends('invoice_date_due')
    def _compute_nam_fecha_vencimiento_formato(self):
        for move in self:
            if move.invoice_date_due:
                # strftime('%d/%m/%y') fuerza el formato exacto: día/mes/año(2 dígitos)
                move.nam_fecha_vencimiento_formato = move.invoice_date_due.strftime('%d/%m/%y')
            else:
                move.nam_fecha_vencimiento_formato = ""

    @api.depends('invoice_line_ids.analytic_distribution')
    def _compute_nam_analitica_nombres(self):
        for move in self:
            nombres = []
            for line in move.invoice_line_ids:
                if line.analytic_distribution:
                    for account_id_str in line.analytic_distribution.keys():
                        account = self.env['account.analytic.account'].browse(int(account_id_str))
                        if account.exists() and account.name not in nombres:
                            nombres.append(account.name)
            
            move.nam_analitica_nombres = ", ".join(nombres) if nombres else ""


    # COMENTAR LAS SIGUIENTES LINEAS CUANDO SE SUBA A PRODUCCION: 

    #exchange_rate = fields.Float(string='Tipo de Cambio')
    #error_dialog = fields.Text(string='Mensaje de Error')

    #nam_caja_id = fields.Char(string='Nro. Caja')

    