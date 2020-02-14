.. _access_win:

Windows
#######

To start the **Kolibri** server on Windows, just double-click the desktop shortcut. You will see the notification message *Kolibri is starting, please wait...*.

When you see the notification *Kolibri is running...*, **Kolibri** will open in the browser with the URL http://127.0.0.1:8080.


Kolibri Taskbar Options
***********************

While it is running, **Kolibri** will display an icon in the Windows taskbar (usually at bottom right, near the clock), that allows you to stop it and configure other settings.  

    .. figure:: ../img/taskbar-options.png
     :alt: When you right click the Kolibri taskbar icon, you can see the taskbar options.

     Kolibri taskbar options.


* Use the **Load in browser** option to open Kolibri in the browser.
* By default **Kolibri** will start running every time you start the computer where it is installed. Uncheck the **Run Kolibri at system startup** option if you prefer to start it manually from the desktop shortcut.
* When installed, **Kolibri** will open in the browser every time it is started. Uncheck the option **Open browser when Kolibri starts** if you prefer to have it running in the background, and to open it manually in the browser by typing the URL http://127.0.0.1:8080 in the address bar.
* Select **Exit** to stop **Kolibri**. You will be prompted to confirm the selection, after which **Kolibri** will stop. You will have to close the browser (or the tab) manually.

.. tip:: 
  If you close the browser window, Kolibri will still be running in the background. Use the **Load in browser** menu item to reopen it in the browser.


.. _ncomputing: 

.. warning::
  In some Windows multi-user environments (for example NComputing), you need to make sure that Kolibri is running **only from the admin account** to avoid having Kolibri started for each login/session. Confirm that the **Run Kolibri at system startup** taskbar option is checked only when the admin logs in, but unchecked when any other user of virtual desktops is logged in.

  It is also recommended that you remove the Kolibri desktop laucher icon from all non admin accounts in this type of setup, and substitute it with a regular shortcut that opens the Kolibri server IP. To add the desktop shortcut follow these steps.

  #. Right click anywhere on the desktop.
  #. Select *New > Shortcut*.
  #. Type in the Kolibri server IP (most probably ``http://127.0.0.1``), save and exit.
  #. Double-click the shortcut to test if it opens the browser and loads Kolibri.

.. note::
  Remember to :ref:`configure other computers <access_LAN>` in the network to access **Kolibri** content.
