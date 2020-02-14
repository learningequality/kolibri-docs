.. _options_ini:

Customize Kolibri Settings with the OPTIONS.INI File
####################################################

For certain configuration settings you need to use the ``options.ini`` file. Installing Kolibri does not generate this file by default, but you can easily add one yourself. Follow these steps.

#. Open the preferred text editor on your computer (eg. Notepad on Windows).
#. Write the required *sections* and *keys* (see details for available settings below) in the following format:
   
    .. code-block:: ini

      [section]
      key1 = a
      key2 = b

3. Save the resulting ``options.ini`` file in the ``.kolibri`` folder inside the :ref:`Home <home>` folder. 
   
.. note::
  ``options.ini`` file can contain several sections with one or more associated keys, depending on the requirements of your installation.   
   
.. _port:


Run Kolibri from a Different Port
*********************************

If you need Kolibri to start and run from a port different than the default ``8080``, add the section ``[Deployment]``, and the key ``HTTP_PORT`` with the value of your desired port, to the ``options.ini`` file.

  .. code-block:: ini
    
     [Deployment]
     HTTP_PORT = 1234 
     # Substitute 1234 with your desired port number


.. tip::
  If after setting the desired port in the ``options.ini`` file you still see Kolibri running from a different one, you probably have the environment variable ``KOLIBRI_HTTP_PORT`` from a previous installation, which takes precedence. Check the ``.bashrc`` file on Linux, or run the ``set`` command in Windows command prompt, to verify and correct if necessary.  


.. _profile_requests_ini:


Allow Profiling of Requests
***************************

If you need to :ref:`profile server requests <profile_requests>` to get a more detailed information about the Kolibri performance, add the following to the ``options.ini`` file.


  .. code-block:: ini
    
     [Server]
     PROFILE = 1
