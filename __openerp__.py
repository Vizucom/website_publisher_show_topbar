# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2017 Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html.
#
##############################################################################
{
    'name': 'Website - Show top bar for Publishers',
    'summary': 'Website editing no longer requires being an Employee ',
    'version': '8.0.1.0.0',
    'category': 'Website',
    'website': 'http://www.vizucom.com',
    'author': 'Oy Tawasta OS Technologies Ltd.',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'website'
    ],
    'data': [
        'views/website_general.xml',
    ],
}