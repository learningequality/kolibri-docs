.. _win:

Windows
=======

Compatibility
-------------

* Supported: Windows 7, 8.1 and 10, with IE 11+, Chrome or Firefox
* **Not supported:** Windows XP cannot be used to install Kolibri server, but could potentially work as a client device if the browsers are `as up-to-date as possible <https://support.mozilla.org/en-US/questions/1173904>`_.

..  raw:: html

    <iframe width="670" height="380" src="https://www.youtube-nocookie.com/embed/yR9SBVeyeWY?rel=0&modestbranding=1&cc_load_policy=1&iv_load_policy=3" frameborder="0" allow="accelerometer; gyroscope" allowfullscreen></iframe><br /><br />


Install
-------

#. Download the `Windows installer <https://learningequality.org/download/>`_ for Kolibri **version** |version-b|.
#. Double-click the downloaded ``.exe`` file.
#. Select the language for the installation.
#. Python 3 installer is included, confirm the installation or the upgrade to proceed.
#. Follow the rest of the instructions in the Kolibri installation setup wizard. 
#. Once the installation finishes, Kolibri will auto-start and open in the default browser on your computer at http://127.0.0.1:8080. This may take a moment, so please be patient.
#. Proceed with the :ref:`setup_initial` of your facility.

.. warning::
  Windows firewall will prompt you to allow the Python process needed to run Kolibri. Click **Allow access** to accept and proceed.

	.. figure:: /img/windows-firewall.png
	 :alt: Windows security alert window that opens when Windows firewall needs your permission to allow the Python process, needed to run Kolibri, to be executed on your computer.

	 Allow the Python process needed to run Kolibri.


Uninstall
---------

1. Open the Windows Control Panel.
2. Select **Programs and Features** option.
3. Select Kolibri from the list of programs.
4. Click the button :guilabel:`Uninstall/Change` and follow the instructions.
   
.. tip:: To remove all the user data and the downloaded channels, delete the ``.kolibri`` folder (go to **Device > Info** to find the exact location of the folder on your system). If you install Kolibri again, you will have to go through the :ref:`Initial Setup <setup_initial>` steps from the beginning.


Upgrade
-------

.. warning:: We recommend making sure Kolibri is not running before upgrading.  

To upgrade Kolibri, follow these steps.

#. Download the new version of Kolibri `Windows installer <https://learningequality.org/download/>`_.
#. Double-click the downloaded ``.exe`` file.
#. Follow the instructions in the installation wizard window.
#. Once the installation of the upgrade is finished, Kolibri will auto-start and open in the default browser on your computer.
#. Go explore the new and improved Kolibri features.

