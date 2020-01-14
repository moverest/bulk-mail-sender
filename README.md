# bulk-mail-sender

Send personalized emails to a list of people.

The listing is defined in a CSV file like this one:

```csv
email,firstname,lastname,greeting
john.smith@example.com,John,Smith,Hi
jane.johnson@example.com,Jane,Johnson,Hello
```

You can then use the fields defined in the listing in a Mako template:

```html
<html>
  <body>
    ${greeting} ${firstname},

    Here is a message.
  </body>
</html>
```

To send the emails, use the `bulk-mail-sender` command.

```bash
bulk-mail-sender template.html listing.csv \
    --subject 'A message for you ${firstname}' \
    --sender-name 'Clément Martinez'
```

You can use the `--dry-run` and `--verbose` option to preview the messages before sending them.


`bulk-mail-sender --help` for usage.

## Settings

The SMTP settings should be present in these environment variables:
 - `SMTP_HOST`
 - `SMTP_PORT`
 - `SMTP_USERNAME`
 - `SMTP_PASSWORD`


## Install

You can install this tool with `pip`:

```bash
pip install bulk-mail-sender
```
