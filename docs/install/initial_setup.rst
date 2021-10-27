.. _setup_initial:

Initial Setup
=============

Setting up Kolibri will be different depending on your learning environment:

* If you plan to use Kolibri at home or for supplemental learning outside any facility, use **Quick start**
* If you are installing Kolibri to be used by many learners at formal facilities like schools, or non-formal like libraries or community centers, use **Advanced setup**.

.. note::
  You will only need to do the initial setup once, when you first start Kolibri after the installation. You can change all the settings later.

..  raw:: html

    <iframe width="670" height="380" src="https://www.youtube-nocookie.com/embed/knrGjxejHUM?rel=0&modestbranding=1&cc_load_policy=1&iv_load_policy=3" frameborder="0" allow="accelerometer; gyroscope" allowfullscreen></iframe><br /><br />


Quick Start
-----------

To do the initial setup of Kolibri for use at home, follow these steps.


#. **Select the default language** for Kolibri.

  	.. figure:: /img/select-language.png
	   :alt:  

	   Select the default Kolibri language.


	.. warning::
	  The default language configured for content in your browser preferences might override the language you choose in this step. To ensure that Kolibri displays in the desired language, make sure to configure it as default in the browsers of all the devices that will be used to view Kolibri content.


#. **Select the Quick start** setup option.
   
  	.. figure:: /img/quick-start.png
	   :alt:  

	   Select Quick start for personal or home use of Kolibri.


#. **Create a super admin account.** This user will be a **super admin**, able to manage all the content and all other Kolibri users on this device.

  	.. figure:: /img/super-admin.png
	   :alt:  

	   Select the username and password for the super admin.

	.. tip::
	  Make sure to save these super admin credentials in a safe place! Device super admin credentials cannot be retrieved when lost, and you will have to manually create another super admin account to manage your device.


Once you finish the initial setup, proceed to :ref:`import some learning resources <manage_resources_ref>`, and :ref:`create users <manage_users_ref>` if more people at your home are going to be using Kolibri. Make sure to check how to :ref:`configure other devices <access_LAN>` (computers, tablets or smartphones) in the home network to access Kolibri.


Advanced Setup
--------------

Here are definitions of concepts necessary to fully understand the available options in the *Advanced setup* of Kolibri.

.. glossary::

    Facility
      A facility in Kolibri connects a set of user accounts, classes, and associated data such as assignments and learner progress. The same facility can be shared across multiple devices, and there can also be multiple facilities on a single device. A facility could represent physical schools, temporary learning hubs, organizations distributing devices across multiple locations, parent or family programs, and other types of learning environments featuring continuity between learners' activities.

    Device
      The physical or virtual machine that has the Kolibri server installed on it. Kolibri server device will minimally include a processor, storage, and memory. It may also include a screen, a network connection, a battery, etc. Common examples of server devices are: a desktop or laptop computer; a rack-mounted server; a Raspberry Pi; a virtual machine running in the cloud.

		    * **Full device**

		      A device that is a fully-featured Kolibri server and can be used by admins, coaches and learners. A full device enables access to all learner, coach and admin features.

		    * **Learn-only device**

		      Unlike a 'full device', on a learn-only device only the features for learners are. Coaches and admins can sign in but will only see the *Learn* page. Learn-only devices also include automated data syncing functionality.

	  Sync
		  Syncing is the process of synchronizing facility data (classes, groups, learner progress, assignments) between devices that have the same facility. The facility is created once on a full device, and subsequently imported to other devices. Facility data can afterwards subsequently synced between devices as long as they are on the same local network.		 


#. **Select the default language for Kolibri.**

  	.. figure:: /img/select-language.png
	   :alt:  

	   Select the default Kolibri language.


	.. warning::
	  The default language configured for content in your browser preferences might override the language you choose in this step. To ensure that Kolibri displays in the desired language, make sure to configure it as default in the browsers of all the devices that will be used to view Kolibri content.


#. **Select the Advanced setup** option, recommended for schools, educational programs, organizations, or other group learning settings that will share Kolibri. 
   
	  .. figure:: /img/advanced-setup.png
		   :alt:  

		   Select Advanced setup for use of Kolibri in group learning environments.			
   

#. **Select the name of the device** on which Kolibri server will be running from. Choose a meaningful and recognizable name because it will help you identify it during syncing and importing processes later on. If many devices are connected to your local network at the same time, the device where the Kolibri server is running must be easily recognizable for users on other devices who need to sync with it.

	  .. figure:: /img/device-name.png
		   :alt:  

		   Select a meaningful name for the device.	

#. **Select a facility setup for this device**. 
   
Full device
***********

Create a New Facility
"""""""""""""""""""""

#. **Type of facility**. When you create a new facility you can choose between **Non-formal** (libraries, orphanages, correctional facilities, youth centers, computer labs and similar), or a **Formal** type of facility (schools and other formal learning contexts).

	  .. figure:: /img/facility-type-name.png
		   :alt: Step 1 of 6. 

		   Select what type of learning environment is your facility and give it a name.

#. **Guest access**. 

  	.. figure:: /img/guest-access.png
	   :alt: Step 2 of 6. 

	   Select if guests can access Kolibri content without the need to create an account.


#. **User account creation**.

  	.. figure:: /img/sign-up.png
	   :alt: Step 3 of 6. 

	   Select if anyone can create a user account for themselves, or if user accounts must be created by Kolibri admins.


#. **Enable passwords for learners**. Simplified sign-in, without the password requirement, allows easier access for younger learners.

  	.. figure:: /img/enable-passwords.png
	   :alt: Step 4 of 6.

	   Select if learners must type in their passwords to sign in on Kolibri.


#. **Create super admin account**. This admin user will be a **super admin**, able to manage not only the content, but also all users and  permissions in this facility.

  	.. figure:: /img/super-admin.png
	   :alt: Step 5 of 6.

	   Select the username and password for the facility super admin.

	.. tip::
	  Make sure to save these super admin credentials in a safe place! Device super admin credentials cannot be retrieved when lost, and you will have to manually create another super admin account to manage your device.


#. **Responsibilities of the administrator**. When you are setting up a Kolibri facility you need to take into consideration the relevant privacy laws and regulations. As **super admin**, you or someone you delegate, will be responsible for protecting and managing the user accounts and personal information stored on the device. Review the data usage and privacy statement before finishing the facility setup.

  	.. figure:: /img/super-admin-resp.png
	   :alt: Step 6 of 6.

	   Review the super admin responsibilities regarding the data usage and privacy.


Once you finish the initial setup, proceed to :ref:`import some learning resources <manage_resources_ref>`, and :ref:`create users <manage_users_ref>` (if you chose the Admin-managed facility setup). Make sure to check how to :ref:`configure other computers <access_LAN>` in the network to access Kolibri.

.. _import_facility:


Import Facility
"""""""""""""""

If you are part of a wider learning environment, where several learning facilities like schools or community centers are managed by one central organization, or you need to sync the learner progress data from your facility with another device where Kolibri is running, you can choose to import a facility that is already set up on that device.

#. Click :guilabel:`Import facility` button in the **Create or import facility** setup step. 

#. Any device that has Kolibri running in the local network should appear in the **Select network address** window. Read more on how set up a local network in the `Kolibri Hardware Guide <https://learningequality.org/r/hardware-guide>`_.

	Select the device and click the :guilabel:`Continue` button.

  	.. figure:: /img/initial-setup-select-device.png
	   :alt: 

	   Select the network address of the device from which you want to import a facility.

		.. note:: If you do not see the address of the device listed, but you know the IP address, you can add it manually. Click the *Add new address* link, and fill in the required information.

			.. figure:: /img/initial-setup-add-device.png
				:alt: Add the network address of the device manually.

				Manually add the network address of the device.

		.. warning:: **Firewalls** may impede your ability to see other devices in your local network or add them as source. If you are unable to see other devices, make sure to:

			* disable the firewalls on all the devices that you need to sync
			* restart Kolibri for broadcast to take effect

#. **Select facility**. If there are several facilities on the device, select the one you want to import and provide the administrative credentials. 

  	.. figure:: /img/initial-setup-select-facility-to-import.png
	   :alt: Step 1 of 4.

	   Select the facility you want to import and provide credentials.

  	.. warning:: You must have the credentials (username and password) for either the **facility admin** of the facility you want to import, or for the **super admin** of the device you are importing from.

#. Wait for the facility data to load on your device. It may take some time, so please be patient. When you see the confirmation that the process is completed click the :guilabel:`Continue` button.
   
  	.. figure:: /img/initial-setup-loading-facility.png
	   :alt: Step 2 of 4.

	   Facility successfully imported onto your device.

#. **Create a super admin account**. The account you create in this step will be a **super admin for your device**, and be able to manage all the device content, all the facility users, and their permissions.

 	You can choose to create a new super admin account or to use the credentials of the super admin of the device from where you imported the facility.

  	.. figure:: /img/device-super-admin.png
	   :alt: Step 3 of 4.

	   Select the super admin account.

	.. tip::
	  Make sure to save the super admin credentials in a safe place! Device super admin credentials cannot be retrieved when lost, and you will have to manually create another super admin account to manage your device.

#. **Responsibilities of the administrator**. When you are setting up a Kolibri facility, especially in formal environments like schools, you need to take into consideration the relevant privacy laws and regulations. As **super admin**, you or someone you delegate, will be responsible for protecting and managing the user accounts and personal information stored on the device. Review the data usage and privacy statement before finishing the facility setup.

  	.. figure:: /img/super-admin-resp.png
	   :alt: Step 4 of 4.

	   Review the super admin responsibilities regarding the data usage and privacy.

Learn-only device
*****************




Once you finish the initial setup, proceed to :ref:`import some learning resources <manage_resources_ref>`. 

.. note:: After you close the welcoming message, you will be able to import content from the same device from which you just imported the facility.

    	.. figure:: /img/initial-setup-import-content-after-facility.png
	   :alt: 

	   You can use the same device from which you imported the facility also to import content.

Make sure to check how to :ref:`configure other computers <access_LAN>` in the network to access Kolibri.
