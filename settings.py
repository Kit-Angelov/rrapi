# конфиги к очередям (обьедини их с переприсваиванием если хочешь)

# конфиг к очереди заказа
order_queue_config = {
    'default': {
        'user': 'rrd_user',
        'password': 'rrd_user',
        'host': '192.168.2.233',
        'port': 5672,
        'queue': 'rrd_order',
        'exchange': '',
        'routing_key': 'rrd_order'
    },
    '1cloudDev': {
        'user': 'prqaihqx',
        'password': '3aMGiZ2tpYcm4ZGUzcvWEx_SfP4UCg80',
        'host': 'black-boar.rmq.cloudamqp.com',
        'port': 5672,
        'queue': 'rrd_order',
        'exchange': '',
        'routing_key': 'rrd_order',
        'virtual_host': 'prqaihqx'
    }

}
order_queue_param = order_queue_config['1cloudDev']

# конфиг к очереди проверки статуса
check_queue_config = {
    'default': {
        'user': 'rrd_user',
        'password': 'rrd_user',
        'host': '192.168.2.233',
        'port': 5672,
        'queue': 'check_order',
        'exchange': '',
        'routing_key': 'check_order'
    },
    '1cloudDev': {
        'user': 'prqaihqx',
        'password': '3aMGiZ2tpYcm4ZGUzcvWEx_SfP4UCg80',
        'host': 'black-boar.rmq.cloudamqp.com',
        'port': 5672,
        'queue': 'check_order',
        'exchange': '',
        'routing_key': 'check_order',
        'virtual_host': 'prqaihqx'
    }
}
check_queue_param = check_queue_config['1cloudDev']

# конфиг к очереди скачивания документа
download_queue_config = {
    'default': {
        'user': 'rrd_user',
        'password': 'rrd_user',
        'host': '192.168.2.233',
        'port': 5672,
        'queue': 'download_order',
        'exchange': '',
        'routing_key': 'download_order'
    },
    '1cloudDev': {
        'user': 'prqaihqx',
        'password': '3aMGiZ2tpYcm4ZGUzcvWEx_SfP4UCg80',
        'host': 'black-boar.rmq.cloudamqp.com',
        'port': 5672,
        'queue': 'download_order',
        'exchange': '',
        'routing_key': 'download_order',
        'virtual_host': 'prqaihqx'
    }
}
download_queue_param = download_queue_config['1cloudDev']

# словарь режимов работы воркера и соответсвущих конфигов очереди
mode_dict = {
	'order': order_queue_param,
	'status': check_queue_param,
	'download': download_queue_param
}

SENTRY_DSN = 'https://0ef101441e8d42f395a43feabd828e7e:e1060eea3c624f88b66fd7cc6f85ccc3@sentry.io/1274958'