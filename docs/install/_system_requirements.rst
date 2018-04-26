.. _sys_reqs:

Hardware requirements
=====================

.. tip:: Below you will find general recommendations regarding hardware requirements. To read more detailed information and find out examples of hardware setups that have been implemented by our partners and users, download the full `Kolibri Hardware Guide <https://learningequality.org/r/hardware-guide>`_ and examples of `Hardware Configurations for Kolibri <https://learningequality.org/r/hardware>`_ (PDF documents).

Servers
-------

Minimum hardware requirements to run Kolibri as a server:

 - 500 MB RAM (1 GB recommended)
 - 500 MHz CPU (1 GHz recommended)
 - Hard drive space depends on the size of the content channels you intend to import from `Kolibri Studio <https://studio.learningequality.org/>`_ or a local storage device.

If you have a facility with less than 30 computers, a device as simple as a `Raspberry Pi <https://www.raspberrypi.org/>`_ is known to work fine as a server.

   .. note:: In case you are deploying on Linux and want an efficient setup, use the ``kolibri-raspberry-pi`` package, it doesn't require a specific architecture, but it's required to use if you deploy on a system with specs equivalent to or smaller than Raspberry Pi.


Clients
-------

Very old desktops and very low-power computers can be used as client devices to access Kolibri. For instance, some deployments are known to use first-gen Raspberry Pi as desktop computers.

It is always a good idea to do a practical test, but when you want to deploy Kolibri, usually it's not necessary to scale your hardware. The main concern is that your system needs a video card and driver that can play the videos.
