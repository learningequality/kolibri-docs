.. _manage_device_ref:

Manage Device
~~~~~~~~~~~~~

You can manage content and permissions, and view the detailed info of the device where Kolibri is running from the **Device** dashboard.

.. note::
  To manage device settings you must have the appropriate permissions.


.. _permissions:

Assign Permissions
------------------

You can assign additional permissions to Kolibri users which will provide them access to more features compared to their :ref:`user roles <user_roles>`. To manage permissions for Kolibri users, use the **Permission** tab in the  **Device** dashboard (|permissions| icon).

	.. figure:: img/manage-permissions.png
	  :alt: Open the Device page and navigate to Permissions tab to see permissions for every user  

Permission to Manage Content
****************************

To grant permission to another user to manage content channels in Kolibri, that is to import, export and delete them from the device, follow these steps.

#. Click **Edit permissions** for the chosen user.
#. Under **Device permissions** activate the option *Can import and export content channels*.
#. Click **Save changes** to apply and finish.

	.. figure:: img/manage-content-permissions.png
	  :alt: Use the checkbox to grant the chosen user permissions to manage content

The users who have been granted the permissions to manage content channels will have a black key indicator in front of their name, and will be able to see the **Device** dashboard with the **Channels** tab.


Super Admin Permissions
***********************

To grant **super admin** permissions to another user, follow these steps.

#. Click **Edit permissions** for the chosen user.
#. Activate the option *Make super admin*.
#. Click **Save changes** to apply and finish.

	.. figure:: img/coach-superuser.png
	  :alt: Use the checkbox to grant the chosen user super admin permissions

The users who have been granted the **super admin** permissions will have a yellow key indicator in front of their name, and will be able to see the **Device** dashboard with both the **Content** and **Permissions** tabs.

	.. figure:: img/permissions-keys.png
	  :alt: Users with additional permissions will have icon indicators in front of their username 


.. _device_info:


View Device Info
----------------

To view the detailed info of the device where Kolibri is running on, use the **Info** tab in the  **Device** dashboard (|info| icon). This information will be useful in case you need to report an issue with Kolibri on the :ref:`Learning Equality Community Forums <forums>`. 

#. Click the **Show** link to open the *Advanced* device info.
#. Make note or copy the following device details to clipboard.

	* Kolibri version
	* Server IP/URL(s)
	* Database path
	* Device name
	* Operating system 
	* Free disk space
	* Server time
	* Server timezone

		.. figure:: img/device-info.png
		  :alt: Open the Device page and navigate to the Info tab to find out the extended device info.

	  	Find out the extended device info in the Device > Info tab.	