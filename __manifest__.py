{
    'name': 'AC Service',
    'version': '17.0',
    'summary': 'Manage Service',
    'sequence': 1,
    'description': 'Module to manage AC details, warranty start and end dates',
    'category': 'Vendor',
    'author': 'Sismatix',
    'website': 'http://sismatix.co',
    'depends': ['contacts', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/partner_asset_views.xml',
        'views/asset_brand_views.xml',
        'views/product_commission_views.xml',
        'views/partner_views.xml',
    ],
    
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
