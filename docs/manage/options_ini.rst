.. _options_ini:

Customize Kolibri Settings with the OPTIONS.INI File
####################################################

Installing Kolibri generates a default ``options.ini`` file with all the sections and values commented out with the ``#`` character at the beginning of the line. To see the ``options.ini`` file, open the ``.kolibri`` folder inside the :ref:`Home <home>` folder. 

.. warning:: Some of the values in the  ``options.ini`` file, especially in the sections ``[Cache]``, ``[Database]``, and ``[Server]`` can have serious effects on the performance of your Kolibri server. **Do not edit them if you are not sure how they work!** 
   
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


..    .. _content_fallback_ini:


    Add Content Fallback Directories
    ********************************

    If you need to specify alternative locations for content to be available to Kolibri after install, you can use the ``CONTENT_FALLBACK_DIRS`` variable in the ``options.ini`` file.


      .. code-block:: ini
        
         [Paths]
         CONTENT_FALLBACK_DIRS = ['/media/user/kolibri-content'; '/media/user2/kolibri-content-backup']
    
