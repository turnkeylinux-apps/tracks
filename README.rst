Tracks - Getting Things Done (GTD) Application
==============================================

`Tracks`_ is a web-based application implemented in Rails to help you
implement David Allen's Getting Things Done methodology.  Features
include multi-user support, a powerful todo list, RSS syndication,
tagging and starring support, and progress graphs.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Tracks configurations:
   
   - Installed from upstream source code to /var/www/tracks
   - Using Phusion Passenger for Apache web server (mod_rails)

- SSL support out of the box.
- Postfix MTA (bound to localhost) to allow sending of email (e.g., todo
  updates).
- Webmin modules for configuring Apache2, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, Webshell, SSH, MySQL: username **root**


.. _Tracks: http://www.getontracks.org
.. _TurnKey Core: http://www.turnkeylinux.org/core
