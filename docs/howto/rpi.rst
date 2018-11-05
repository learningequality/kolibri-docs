Raspberry Pi
============

There are several varieties of operating systems for Raspberry Pi. This guide is intended for and tested on `Raspian <https://www.raspberrypi.org/>`__, the most popular choice of OS, based on Debian.

Prerequisites
-------------

* Raspberry Pi Model 3+
* Formatted MicroSD Card > 4GB (64 GB recommended or attached USB storage)
* Card reader for a laptop or computer to write to the MicroSD card
* Latest Raspbian Stretch OS .img file

  * `Raspbian Desktop <http://downloads.raspberrypi.org/raspbian/>`__
  * `Raspbian Lite <http://downloads.raspberrypi.org/raspbian_lite/>`__
  * **Or** `Installation of Raspbian via NOOBS <https://www.raspberrypi.org/documentation/installation/noobs.md>`__
* Internet connectivity (for setting up the device)

Getting started guides
----------------------

This guide provides a step-by-step setup of Kolibri but does not try to explain basic concepts for your Raspberry Pi. If you are new to the system, you are encouraged to read the official `Getting Started <https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started>`__ guide for basic knowledge about setting up your device.

This guide installs Kolibri as the very final step. But please read and complete all the prior steps!

Setting up the SD card
----------------------

The following commands work on Linux/macOS for setting up the .img files provided. You will also need to know the *device node* for the SD Card reader. On Linux, this is typically ``/dev/mmcblk0`` for the 0th card in your card reader.

.. code-block:: console

  # Unpack the .zip into memory and write it to <device node>
  unzip -p /path/to/raspbian-stretch-lite.zip | sudo dd of=/dev/mmcblk123 bs=4M conv=fsync

.. tip:: Read the official guides for setting up your card: `Copying .img files <https://www.raspberrypi.org/documentation/installation/installing-images/README.md>`__


Updating the software
---------------------

After installing and starting up your Raspberry Pi, it is recommended that you upgrade all the software on the device:
  
.. code-block:: console

  sudo apt update
  sudo apt upgrade
  sudo reboot  # Ensure that updates are active

Updating the firmware
---------------------

Run ``sudo rpi-update`` to update the firmware. Nothing in this howto necessitates this, but it's always recommended because hardware issues may be solved over time and performance improved. You cannot replicate this by copying MicroSD cards, you would have to repeat this step for every new Raspberry Pi device that you are installing.

General system configuration
----------------------------

Run ``sudo raspi-config`` for the general setup options such as keyboard layout, timezone etc.

.. warning:: Always change your password after setting up device. The default password for the user ``pi`` is ``raspberry``.

Setting up a hotspot
--------------------

The Raspberry Pi 3 has a WIFI adapter which can also serve as an access point, thus giving other devices the ability to connect to the Raspberry Pi through WIFI.

We assume that you will need to connect the RPi to the internet both before and after setting up the hotspot. The easiest way to achieve this is through the Raspberry Pi's ethernet cable connection.

* The device can be setup such that it automatically uses the ethernet interface as *gateway* to the internet when a cable is connected.
* If you need to connect to the internet through WIFI, you will have to disable the hotspot and connect through the normal network management.

.. note: If you already have a WIFI network at the location where the device will be setup, you should NOT setup an additional hotspot. You can connect the Raspberry Pi to an existing network and access it from there. Skip this step and the Capitive Portal step.

Installing hostapd and dnsmasq
******************************

In order to serve clients on a local WIFI hotspot, you need the Raspberry Pi to act as:

* an Access point
* a DHCP server
* a DNS server

The access point is handled by the package ``hostapd`` and the DHCP and DNS server are both available through the ``dnsmasq`` package. We will install and configure both in this section. For more detailed information, see `the online Raspberry Pi docs <https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md>`__.

.. code-block:: console

  sudo apt install dnsmasq hostapd

Setting a static IP
*******************

Firstly, the server's WIFI interface ``wlan0`` needs to have a predictable IP address and not try to obtain it from another server. We call this a *static IP*.

It is defined in the configuration file ``/etc/dhcpcd.conf``, which you can edit through the below command.

.. code-block:: console

  sudo nano /etc/dhcpcd.conf

Use the arrow keys to navigate to the end of the file, then copy and paste the following text and press :guilabel:`CTRL` + :guilabel:`X` to save and exit.

.. code-block:: text

  interface wlan0
      static ip_address=192.168.4.1/24
      nohook wpa_supplicant

After installing the new ``hostapd`` and ``dnsmasq`` packages and setting a static IP, you should reboot the system.

.. code-block:: console

  sudo reboot

After rebooting, you can ensure that your system is running with the static IP address by running the command ``ipconfig`` and reviewing that ``wlan0`` has the new IP address printed. It should contain this output (notice the IP address):

.. code-block:: text

  wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
          inet 192.168.4.1  netmask 255.255.255.0  broadcast 192.168.4.255
          inet6 fe80::e02e:4991:29ac:f076  prefixlen 64  scopeid 0x20<link>

Configure DHCP and DNS
**********************

We create a new configuration file for ``dnsmasq`` in the appropriate location and start editing it:

.. code-block:: console

  sudo nano /etc/dnsmasq.d/hotspot

Copy and paste the following text, then press :guilabel:`CTRL` + :guilabel:`X` to save and exit.

.. code-block:: text

	# Gateway + DNS server
	dhcp-option=3,192.168.4.1
	dhcp-option=6,192.168.4.1

	# Let the Raspberry Pi resolve to all DNS queries
	address=/#/192.168.4.1


Configure the access point
**************************

You will need to write a configuration file with information about your local WIFI network.

.. code-block:: console

  sudo nano /etc/default/hostapd

In the file, copy in the following configuration to specify the name of the network, its WIFI channel (frequency) and bandwidth mode (we recommend 2.4 GHz 'g' mode). Set ``hw_mode=a`` to use 5 GHz. Press :guilabel:`CTRL` + :guilabel:`X` to save and exit.

.. code-block:: text

  interface=wlan0
  driver=nl80211
  ssid=Offline Library 
  hw_mode=g
  channel=7
  wmm_enabled=0
  macaddr_acl=0
  auth_algs=1
  ignore_broadcast_ssid=0

  # Remove the '#' in front of below lines to set a password
  # wpa=2
  # wpa_passphrase=Password            
  # wpa_key_mgmt=WPA-PSK
  # wpa_pairwise=TKIP
  # rsn_pairwise=CCMP

Next, open the following file to enable the configuration file that we have just written:

.. code-block:: console

  sudo nano /etc/default/hostapd

At the bottom of the file, add the following text and press :guilabel:`CTRL` + :guilabel:`X` to exit and save.

.. code-block:: text

  DAEMON_CONF="/etc/hostapd/hostapd.conf"

Finally, start the access point system service ``hostapd`` and the DHCP and DNS server ``dnsmasq``:

.. code-block:: console

  sudo systemctl start hostapd
  sudo systemctl start dnsmasq


Setting up a "Captive portal"
-----------------------------

In the previous step, we have configured the Raspberry Pi to tell devices on the local offline hotspot that whatever resource they request such as ``http://domain.com``, it should resolve to the Raspberry Pi's static IP address ``192.168.4.1``.

In

Attaching USB storage
---------------------

Many people have a 4 GB or 16 GB MicroSD card that came along with the Raspberry Pi. In order to have more content, such as the full Khan Academy, you may want to attach a USB storage media -- a flash device or a hard drive.

.. tip:: Moving content: If you have a USB source for additional storage, you can use the ``kolibri manage movedirectory`` command or create your own symbolic links to have the data folder located elsewhere.
  
    Using the built-in management command:

    .. code-block:: console

        # Stop kolibri
        sudo systemctl kolibri stop
        # Move the data
        kolibri manage movedirectory /path/to/your/external_drive
        # Start kolibri
        sudo systemctl kolibri start
        
  
    **Or** using symbolic links, you need to start and stop Kolibri and to set the permissions correctly:

    .. code-block:: console

        # Stop kolibri
        sudo systemctl kolibri stop
        # Move its data
        sudo mv /var/kolibri/.kolibri /your/external/media/kolibri_data
        # Ensure that the kolibri system service user owns the folder
        sudo chown -R `cat /etc/kolibri/username` /your/external/media/kolibri_data
        # Restore the original location with a symbolic link
        sudo ln -s /your/external/media/kolibri_data /var/kolibri/.kolibri
        # Start kolibri
        sudo systemctl kolibri start


Saving your image for replication
---------------------------------


