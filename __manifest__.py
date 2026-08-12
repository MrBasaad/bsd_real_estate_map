{
    'name': 'Real Estate Map Integration',
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Adds Map views and actions for Real Estate module using bsd_base_map framework',
    'version': '19.0.1.0.0',

    
    'depends': [
        'base',
        'web',
        'bsd_base_map', 
        'bsd_real_estate_base',
    ],
    
    'data': [
        'views/estate_property_map_views.xml',
    ],
    # 'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': False,
    'author': 'Basaad.co',
    'company': 'Basaad.co',
    'maintainer': 'Basaad.co',    
    'website': 'Basaad.co',
    'license': 'LGPL-3',
}