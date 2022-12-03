#!/usr/bin/python3
"""Set Tracks admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively
"""

import os
import re
import sys
import getopt
import inithooks_cache
import subprocess

import bcrypt
import hashlib

from libinithooks.dialog_wrapper import Dialog
from mysqlconf import MySQL


def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)


def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError as e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Tracks Password",
            "Enter new password for the Tracks 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "Tracks Email",
            "Enter email address for the Tracks 'admin' account.",
            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)

    hashpass = bcrypt.hashpw(password.encode(), bcrypt.gensalt(prefix=b"2a")).decode('utf8')
    token = hashlib.sha1(os.urandom(128)).hexdigest()

    m = MySQL()
    m.execute('UPDATE tracks_production.users SET crypted_password="%s", token="%s" WHERE login="admin";' % (hashpass, token))

    config = "/var/www/tracks/config/site.yml"
    subprocess.check_output(['sed', '-i', '\|^admin_email|s|:.*$|: {}|'.format(email), config])

if __name__ == "__main__":
    main()
