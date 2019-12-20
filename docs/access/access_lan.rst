.. _access_lan:

Accessing Kolibri from Other Devices
####################################

After you have installed and started Kolibri on the computer that will act as a server, you need to configure other devices in the same `Local Area Network <https://en.wikipedia.org/wiki/Local_area_network>`_ (LAN), such as other computers, tablets or phones, so they can access the the learning content on the server.

Compatibility
*************

Kolibri currently supports the following combinations of operating systems and browsers for client devices:

* Windows 7, 8.1 and 10: IE 11+, Chrome and Firefox
* MacOS 10.6+: Safari, Chrome and Firefox
* Linux: any browser
* Android 4.4+: Chrome and Firefox
* iOS 10+: Safari, Chrome and Firefox

.. warning:: Videos are MP4 encoded. While most browsers do not require additional plugins or codecs, open source platforms will often require you to install MP4 codecs separately: For instance on Ubuntu, install the `restricted extras package <https://help.ubuntu.com/community/RestrictedFormats>`__.

Set up Access on Other Devices
******************************

To access content from other devices in the same network, you need to know the :ref:`IP address <ips>` of the computer where Kolibri is running. The default port is **8080**, and you must add it after the IP address.

For example, if Kolibri is installed and started on a computer with the address **192.168.8.134:8080**, you can access it from an Android tablet connected to the same network by opening the browser on the tablet and typing the address ``http://192.168.8.134:8080``.


.. tip::
  * You can check the IP (**Server URL**) of the device where Kolibri is running by going to **Info** tab in the **Device** dashboard.

    .. figure:: ../img/device-info.png
      :alt: Open the Device page and navigate to the Info tab to find the IP (Server URL) for your device.

      Find the IP/Server URL in the Device > Info tab.
  
  * You can also use the ``ipconfig`` command on Windows or ``ifconfig`` command on Linux/OSX to find the externally visible IP address of the device running the Kolibri.


.. warning::
  * When entering the URL in the browser, it may be required to explicitly include `http://`, for example `http://1.2.3.4:8080` or `http://1.2.3.4:80`. Many browsers will incorrectly interpret an IP address or local network hostname as a search term. In other cases, browsers may incorrectly add `https://` instead of `http://`.
  
  * In case you decide to make Kolibri available on the port 80, instead of the default 8080, you **must always include** ``http://`` in front of the server's IP.
    

.. note::
  * In case of network problems, see :ref:`troubleshooting tips <network>`.
  * Examples and comparison of `Hardware Configurations for Kolibri <https://learningequality.org/r/hardware>`__ (PDF document).


.. Access Kolibri on Android
.. *************************

.. Go to **Apps** on your device and tap the **Kolibri** icon.

.. figure: img/android-apps.png
..  :alt: Tap the Kolibri icon among your device apps to start.

..  Tap the Kolibri icon among your device apps to start.
