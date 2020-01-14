#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='bulk-mail-sender',
    version='0.1',
    description='Send emails in bulk with a CSV listing and a email template.',
    author='Clément Martinez',
    author_email='clementmartinezdev@gmail.com',
    url='https://github.com/moverest/bulk-mail-sender',
    install_requires=('click', 'mako'),
    packages=('bulk_mail_sender', ),
    entry_points={
        'console_scripts': [
            'bulk-mail-sender=bulk_mail_sender.main:main',
        ]
    },
)
