# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2015 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com       
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Deltatech Invoice Number",
    'version': '10.0.1.0.0',
    "author": "Terrabit, Dorin Hongu",
    "website": "www.terrabit.ro",
    "description": """

Functionalitati:
 - Validare data factura sa fie mai mare decat data din ultima factura
 - Posibilitatea de a modifica numarul unei facturi
 - posibilitatea de a numerota o factura char daca aceasta nu este validata. Dupa numerotare nu se mai poate modifca data


    """,
    "category": "Accounting",
    "depends": ["account"],

    "data": ['security/sale_security.xml',
             'views/account_invoice_view.xml',
             'wizard/account_invoice_change_number_view.xml'],
    "active": False,
    "installable": True,
}
