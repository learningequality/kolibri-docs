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


Configure Supported Languages
*****************************

You can configure Kolibri to display just a specific set of languages that your implementation supports, as opposed to the full list of languages Kolibri has been localized into. Edit the ``options.ini`` file to include the key ``LANGUAGES`` under the section ``[Deployment]``, with a comma separated list of ``intl_code`` language codes. 

Below example will display only English, Gujarati, Hindi, Marathi and Telugu languages in the :ref:`language selector <change_language>` window.

  .. code-block:: ini
    
     [Deployment]
     LANGUAGES = 'en', 'gu-in', 'hi-in', 'mr', 'te'

Kolibri currently supports the following locales:

+---------------------------+-----------------+
| Language                  | ``intl_code``   |
+===========================+=================+
| English                   | ``en``          |
+---------------------------+-----------------+
| Arabic                    | ``ar``          |                
+---------------------------+-----------------+
| Bengali                   | ``bn-bd``       | 
+---------------------------+-----------------+
| Bulgarian                 | ``bg-bg``       | 
+---------------------------+-----------------+
| Burmese                   | ``my``          | 
+---------------------------+-----------------+
| Chinese (simplified)      | ``zh-hans``     | 
+---------------------------+-----------------+
| Chinyanja                 | ``nyn``         | 
+---------------------------+-----------------+
| Farsi                     | ``fa``          | 
+---------------------------+-----------------+
| French                    | ``fr``          | 
+---------------------------+-----------------+
| Fulfulde Mbororoore       | ``ff-cm``       | 
+---------------------------+-----------------+
| German                    | ``de``          | 
+---------------------------+-----------------+
| Gujarati                  | ``gu-in``       | 
+---------------------------+-----------------+
| Hindi (India)             | ``hi-in``       | 
+---------------------------+-----------------+
| Italian                   | ``it``          | 
+---------------------------+-----------------+
| Khmer                     | ``km``          | 
+---------------------------+-----------------+
| Korean                    | ``ko``          | 
+---------------------------+-----------------+
| Marathi                   | ``mr``          | 
+---------------------------+-----------------+
| Portuguese (Brazil)       | ``pt-br``       | 
+---------------------------+-----------------+
| Spanish (Latin America)   | ``es-419``      | 
+---------------------------+-----------------+
| Spanish (Spain)           | ``es-es``       | 
+---------------------------+-----------------+
| Swahili (Tanzania)        | ``sw-tz``       | 
+---------------------------+-----------------+
| Telugu                    | ``te``          | 
+---------------------------+-----------------+
| Urdu (Pakistan)           | ``ur-pk``       | 
+---------------------------+-----------------+
| Yoruba                    | ``yo``          | 
+---------------------------+-----------------+
| Vietnamese                | ``vi``          | 
+---------------------------+-----------------+


..    .. _content_fallback_ini:


    Add Content Fallback Directories
    ********************************

    If you need to specify alternative locations for content to be available to Kolibri after install, you can use the ``CONTENT_FALLBACK_DIRS`` variable in the ``options.ini`` file.


      .. code-block:: ini
        
         [Paths]
         CONTENT_FALLBACK_DIRS = ['/media/user/kolibri-content'; '/media/user2/kolibri-content-backup']
    
