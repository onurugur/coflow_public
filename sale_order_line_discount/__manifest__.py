
{
    'name': 'Order Line Discount',
    "version": "17.0.1.1.0",
    'website': 'https://www.andar.com.tr',
    'author':'OnurUGUR',
    'category': 'Sales',
    'summary': 'Sale Order Line Discount',
    "license": "AGPL-3",
    'description': """ Desciption of order line discount
	 """,
    'depends': [
        'sale','account'
    ],
    'data': [
            'security/ir.model.access.csv',
            'wizard/update_discount_view.xml',
            'views/sale_order_view.xml',
            
    ],
    'installable' : True,
    'auto_install' : False,
}
