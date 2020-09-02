# Copyright 2012-2014 Numérigraphe SARL.
{
    'name': 'Xtendoo GS1 Barcode API',
    'summary': 'Decoding API for GS1-128 (aka UCC/EAN-128) and GS1-Datamatrix',
    'version': '12.0.1.0.0',
    'author': 'Numérigraphe, Odoo Community Association (OCA)',
    'website': 'http://numerigraphe.com',
    'category': 'Generic Modules/Inventory Control',
    'depends': [
        'base',
    ],
    'data': [
        'views/gs1_barcode.xml',
        'views/res_users.xml',
        'data/gs1_barcode.csv',
        "security/ir.model.access.csv",
    ],
    'installable': True,
    'license': 'AGPL-3',
}
