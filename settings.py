order_queue_config = {
    'default': {
        'user': 'rrd_user',
        'password': 'rrd_user',
        'host': '192.168.2.233',
        'port': 5672,
        'queue': 'rrd_order',
        'exchange': '',
        'routing_key': 'rrd_order'
    }
}
order_queue_param = order_queue_config['default']

check_queue_config = {
    'default': {
        'user': 'rrd_user',
        'password': 'rrd_user',
        'host': '192.168.2.233',
        'port': 5672,
        'queue': 'check_order',
        'exchange': '',
        'routing_key': 'check_order'
    }
}
check_queue_param = check_queue_config['default']

download_queue_config = {
    'default': {
        'user': 'rrd_user',
        'password': 'rrd_user',
        'host': '192.168.2.233',
        'port': 5672,
        'queue': 'download_order',
        'exchange': '',
        'routing_key': 'download_order'
    }
}
download_queue_param = download_queue_config['default']

mode_dict = {
	'order': order_queue_param,
	'status': check_queue_param,
	'download': download_queue_param
}