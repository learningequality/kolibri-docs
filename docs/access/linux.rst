.. _access_lin:

Linux 
#####

Starting Kolibri on Linux will differ depending on the method you used to install it.

* If you used the **PEX** package, Kolibri will be accessible as long as the process is running in the `Terminal <https://help.ubuntu.com/community/UsingTheTerminal>`_. If you stop the process, close the Terminal window, or restart your system, you will need to :ref:`run the PEX again <pex>` to restart Kolibri. 

* If you installed Kolibri as a system service with the :ref:`DEB installer <lin_deb>`, it will run automatically on each system restart, and you do not need to start it manually. Proceed to step 2 below.

* If you installed Kolibri through the :ref:`PPA <ppa>`, or :ref:`generic installation <pip-installation>` with ``pip install`` command, follow these steps.

  1. Run this command in Terminal to start Kolibri:

    .. code-block:: bash

      kolibri start
      

  2. Open the default browser at ``http://127.0.0.1:8080``, and it will display the **Kolibri** start page.

    .. note::
      Remember to :ref:`configure other computers <access_LAN>` in the network to access **Kolibri** content.

  3. Run this command in Terminal to stop Kolibri:

    .. code-block:: bash

      kolibri stop
