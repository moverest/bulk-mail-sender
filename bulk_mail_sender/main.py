#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import os

import click
from mako.template import Template

from .sendmail import connect_smtp, create_email, html_to_text


def read_env():
    return {
        key: os.getenv(key.upper())
        for key in (
            'smtp_username',
            'smtp_password',
            'smtp_host',
            'smtp_port',
        )
    }


def open_listing(filename):
    with open(filename) as f:
        yield from csv.DictReader(f)


@click.command()
@click.argument('template_file', type=click.Path())
@click.argument('listing_file', type=click.Path())
@click.option('--dry-run', is_flag=True)
@click.option('--sender-name', default='')
@click.option('--sender-email', default=None)
@click.option('--subject', 'subject_template_str', required=True)
@click.option('--verbose', is_flag=True)
def main(template_file, listing_file, dry_run, sender_name, sender_email,
         subject_template_str, verbose):
    email_template = Template(filename=template_file)
    subject_template = Template(subject_template_str)
    env = read_env()

    if not dry_run:
        smtp_conn = connect_smtp(host=env['smtp_host'],
                                 port=int(env['smtp_port']),
                                 username=env['smtp_username'],
                                 password=env['smtp_password'])

    for row in open_listing(listing_file):
        subject = subject_template.render(**row)
        email_html = email_template.render(**row)

        if verbose:
            print('\x1b[32mSubject\x1b[0m:', subject)
            print(email_html)

        print(f"\x1b[33m::{row['email']}\x1b[0m ", flush=True)

        email = create_email(
            sender_name=sender_name,
            sender_addr=sender_email or env['smtp_username'],
            recipient_addr=(row['email'], ),
            subject=subject,
            html=email_html,
            text=html_to_text(email_html),
        )

        if not dry_run:
            smtp_conn.send_message(email)
            print('sent.')
        else:
            print()


if __name__ == '__main__':
    main()
