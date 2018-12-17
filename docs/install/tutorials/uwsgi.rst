.. _how_to_uwsgi:

Multicore w/ uWSGI
==================

This section will expand into a tutorial for using Kolibri with uWSGI. It will
initially be made accessible through a Debian package which configures Nginx and
uWSGI together.

The benefits are on multitude level with the number of cores on the device
hosting Kolibri. This means that for instance, a Raspberry Pi 3 with 4 cores
is expected to serve 3-4x as many users with this setup.

.. note::
  If you are an experienced system administrator or Django user, it is possible to deploy Kolibri using conventional methods - for instance with uWSGI and Nginx.
