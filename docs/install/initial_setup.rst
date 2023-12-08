.. _setup_initial:

Initial setup
=============

Setting up Kolibri will be different depending on your learning environment:

* If you plan to use Kolibri at home or for supplemental learning outside any facility, use the **On my own** option.       
* If you are installing Kolibri to be used in a formal facility like school, or in non-formal ones like libraries or community centers, use the **Group learning** option.

.. note::
  You will only need to do the initial setup once, when you first start Kolibri after the installation. You can change all the settings later.

.. _on_my_own:


On my own
---------

To do the initial setup of Kolibri for use at home, follow these steps.


#. **Select the On my own** setup option.
   
  	.. figure:: /img/on-my-own.png
	   :alt:  

	   Select On my own for personal or home use of Kolibri.


#. **Select the default language** for Kolibri.

  	.. figure:: /img/select-language.png
	   :alt:  

	   Select the default Kolibri language.


	.. warning::
	  The default language configured for content in your browser preferences might override the language you choose in this step. To ensure that Kolibri displays in the desired language, make sure to configure it as default in the browsers of all the devices that will be used to view Kolibri content.

#. **Create a super admin account.** This user will be a **super admin**, able to manage all the content and all other Kolibri users on this device.

	.. warning::
	  **Make sure to save these super admin credentials in a safe place!** 

	  Device super admin credentials cannot be retrieved when lost, and you will have to manually create another super admin account to manage your device.

  	.. figure:: /img/super-admin.png
	   :alt:  

	   Select the username and password for the super admin.


Once you finish the initial setup, proceed to :ref:`import some learning resources <manage_resources_ref>`, and :ref:`create users <manage_users_ref>` if more people at your home are going to be using Kolibri. Make sure to check how to :ref:`configure other devices <access_LAN>` (computers, tablets or smartphones) in the home network to access Kolibri.


Group learning
--------------

Here are definitions of concepts necessary to understand the available options in the *Advanced setup* of Kolibri.

.. glossary::

    Facility
      A facility in Kolibri connects a set of user accounts, classes, and associated data such as assignments and learner progress. The same facility can be shared across multiple devices, and there can also be multiple facilities on a single device. A facility could represent physical schools, temporary learning hubs, organizations distributing devices across multiple locations, parent or family programs, and other types of learning environments featuring continuity between learners' activities.

    Device
      The physical or virtual machine that has the Kolibri server installed on it. Kolibri server device will minimally include a processor, storage, and memory. It may also include a screen, a network connection, a battery, etc. Common examples of server devices are: a desktop or laptop computer; a rack-mounted server; a Raspberry Pi; a virtual machine running in the cloud.

		    * **Full device**

		      A device that is a fully-featured Kolibri server and can be used by admins, coaches and learners. A full device enables access to all learner, coach and admin features.

		    * **Learn-only device**

		      Unlike a 'full device', a 'learn-only device' will have available only the features for learners. Coaches and admins can sign in but will only see the *Learn* page. Learn-only devices also include automated data syncing functionality.

	  Sync
		  Syncing is the process of synchronizing facility data (learners, groups, classes, learner progress, assignments) between devices that have the same facility. The facility is created once on a full device, and can subsequently be imported to other devices. Facility data can afterwards be synced between devices as long as they are on the same local network.		 


#. **Select the Group learning** option, recommended for schools, educational programs, organizations, or other group learning settings that will share Kolibri. 
   
	  .. figure:: /img/group-learning.png
		   :alt:  

		   Select Group learning for use of Kolibri in group learning environments.		
	

#. **Select the name of the device** on which Kolibri server will be running from. Choose a meaningful and recognizable name because it will help you identify it during syncing and importing processes later on. If many devices are connected to your local network at the same time, the device where the Kolibri server is running must be easily recognizable for users on other devices who need to sync with it.

	  .. figure:: /img/device-name.png
		   :alt:  

		   Select a meaningful name for the device.	


#. **Select device type**. If you want to set up a **full device** (keep reading the following section), you can create a new facility, or import it from another device in your local network. To import only one or more learner accounts, :ref:`select the learn-only device <learn_only_device>`. 

	  .. figure:: /img/select-device-type.png
		   :alt:  

		   Select the how do you want to set up your device.
   
Full device
***********

Create a new learning facility
""""""""""""""""""""""""""""""

#. Select the **Create a new learning facility** option.

	  .. figure:: /img/create-facility.png
		   :alt:  

#. **Type of facility**. When you create a new learning facility you can choose between **Non-formal** (libraries, orphanages, correctional facilities, youth centers, computer labs and similar), or a **Formal** type of learning facility (schools and other formal learning contexts).

	  .. figure:: /img/facility-type-name.png
		   :alt: Step 1 of 5. 

		   Select what type of learning environment is your learning facility and give it a name.

#. Enable **Guest access**. 

  	.. figure:: /img/guest-access.png
	   :alt: Step 2 of 5. 

	   Select if guests can access Kolibri content without the need to create an account.


#. **User account creation**.

  	.. figure:: /img/sign-up.png
	   :alt: Step 3 of 5. 

	   Select if anyone can create a user account for themselves, or if user accounts must be created by Kolibri admins.


#. **Enable passwords for learners**. Simplified sign-in, without the password requirement, allows easier access for younger learners.

  	.. figure:: /img/enable-passwords.png
	   :alt: Step 4 of 5.

	   Select if learners must type in their passwords to sign in on Kolibri.


#. **Responsibilities of the administrator**. When you are setting up a Kolibri facility you need to take into consideration the relevant privacy laws and regulations. As **super admin**, you or someone you delegate, will be responsible for protecting and managing the user accounts and personal information stored on the device. Review the data usage and privacy statement before finishing the facility setup.

  	.. figure:: /img/super-admin-resp.png
	   :alt: Step 5 of 5.

	   Review the super admin responsibilities regarding the data usage and privacy.


#. **Create super admin account**. This admin user will be a **super admin**, able to manage not only the content, but also all users and  permissions in this facility.
   
	.. warning::
	  **Make sure to save these super admin credentials in a safe place!** 

	  Device super admin credentials cannot be retrieved when lost, and you will have to manually create another super admin account to manage your device.

  	.. figure:: /img/super-admin.png
	   :alt:  

	   Select the username and password for the facility super admin.


Once you finish the initial setup, proceed to :ref:`import some learning resources <manage_resources_ref>`, and :ref:`create users <manage_users_ref>` (if you chose the Admin-managed facility setup). Make sure to check how to :ref:`configure other computers <access_LAN>` in the network to access Kolibri.

.. _import_facility:


Import facility
"""""""""""""""

If you are part of a wider learning environment, where several learning facilities like schools or community centers are managed by one central organization, or you need to sync the learner progress data from your facility with another device where Kolibri is running, you can choose to import a facility that is already set up on that device.

#. Select the **Import all data from an existing learning facility** option.

  	.. figure:: /img/import-learning-facility.png
	   :alt: 

#. Any device that has Kolibri running in the local network should appear in the **Select device** window. Read more on how set up a local network in the `Kolibri Hardware Guide <https://learningequality.org/r/hardware-guide>`_.

	Select the device and click the :guilabel:`Continue` button.

	**TODO-screenshot**

  	.. figure:: /img/initial-setup-select-deviceZ.png
	   :alt: 

	   Select the device from which you want to import a facility.

		.. note:: If you do not see the address of the device listed, but you know the IP address, you can add it manually. Click the *Add new address* link, and fill in the required information.

		**TODO-screenshot**

			.. figure:: /img/initial-setup-add-deviceZ.png
				:alt: Add the network address of the device manually.

				Manually add the network address of the device.

		.. warning:: **Firewalls** may impede your ability to see other devices in your local network or add them as source. If you are unable to see other devices, make sure to:

			* disable the firewalls on all the devices that you need to sync
			* restart Kolibri for broadcast to take effect

#. **Select facility**. If there are several facilities on the device, select the one you want to import. 

  	.. figure:: /img/initial-setup-select-facility-to-import.png
	   :alt: Step 1 of 5.

	   Select the facility you want to import.

#. Provide the credentials (username and password) for either the **facility admin** of the facility you want to import, or for the **super admin** of the device you are importing from.

  	.. figure:: /img/import-facility-creds.png
	   :alt: Step 2 of 5.

	   Provide admin credentials for the facility you want to import.


#. **Create a super admin account**. The account you create in this step will be a **super admin for your device**, and be able to manage all the device content, all the facility users, and their permissions.

 	You can choose to create a new super admin account or to use the credentials of the super admin of the device from where you imported the facility.

 	.. warning::
		**Make sure to save the super admin credentials in a safe place!** 

		Device super admin credentials cannot be retrieved when lost, and you will have to manually create another super admin account to manage your device.			

  	.. figure:: /img/import-facility-create-super-admin.png
	   :alt: Step 4 of 5.

	   Select the super admin account.

#. **Responsibilities of the administrator**. When you are setting up a Kolibri facility, especially in formal environments like schools, you need to take into consideration the relevant privacy laws and regulations. As **super admin**, you or someone you delegate, will be responsible for protecting and managing the user accounts and personal information stored on the device. Review the data usage and privacy statement before finishing the facility setup.

  	.. figure:: /img/super-admin-resp.png
	   :alt: Step 5 of 5.

	   Review the super admin responsibilities regarding the data usage and privacy.

#. Wait for the facility data to load on your device. It may take some time, so please be patient. When you see the confirmation that the process is completed click the :guilabel:`Continue` button.
   
  	.. figure:: /img/initial-setup-loading-facility.png
	   :alt: Step 2 of 4.

	   Facility successfully imported onto your device.


.. _learn_only_device:



Learn-only device
*****************

The user accounts on learn-only devices are always part of a learning facility on another Kolibri device (usually managed by their coaches or facility admins), and have the automated syncing configured by default so all learner  interactions with the resources are synced with the main facility where coaches can oversee their progress. 

When setting up a learn-only device, you can choose to create a completely new account that will be associated with the main facility, or if you previously had an account on the main facility (when you used Kolibri at school or a community center) but now you have a personal device (tablet or a phone), you can import your original account from the main facility to this new personal device.

	.. warning::
	  **Learn-only devices only have enabled the features for learners (classes, lessons, quizzes, library, and bookmarks)**. 

	  Keep also in mind that if you have a coach or admin user account on the main facility, and you want to import it on a learn-only device, you will only have access to the learner features on this new device, and not the coach and admin permissions you used to have on the main facility the account is imported from.

#. Select the **Learn-only device** option and click the :guilabel:`Continue` button.

  	.. figure:: /img/learn-only-device.png
	   :alt:  

Create a new account for an existing facility
"""""""""""""""""""""""""""""""""""""""""""""

#. Select the **Create a new user account for an existing facility** option in the **Select a facility setup for this learn-only device** step. 

  	.. figure:: /img/create-account-learn-only-device.png
	   :alt:  

#. Any device that has Kolibri running in the local network should appear in the **Select device** window. Read more on how set up a local network in the `Kolibri Hardware Guide <https://learningequality.org/r/hardware-guide>`_.

	Select the device and click the :guilabel:`Continue` button.

	**TODO-screenshot**

  	.. figure:: /img/learn-only-select-device7.png
	   :alt:  

	   Select the network address of the device from which you want to import a facility.

		.. warning:: **Firewalls** may impede your ability to see other devices in your local network or add them as source. If you are unable to see other devices, make sure to:

			* disable the firewalls on all the devices that you need to sync
			* restart Kolibri for broadcast to take effect

#. **Select facility**. If there are several facilities on the device, select the one you want to associate the learner account with. 

	**TODO-screenshot**

  	.. figure:: /img/select-facility-import-individual-user-accounts7.png
	   :alt:  

	   Select the facility you want to import and provide credentials.

#. **Create learner accounts**. Enter the username and password of the learner you want to import to your device.

	**TODO-screenshot**

  	.. figure:: /img/import-individual-user-accounts7.png
	   :alt:  


#. When you see the confirmation that the process is completed, you can choose to create another learner account on the same device. Otherwise, click the :guilabel:`Continue` button.
   
Once you finish the initial setup, proceed to :ref:`import some learning resources <manage_resources_ref>`. 


Import one or more accounts from an existing facility
"""""""""""""""""""""""""""""""""""""""""""""""""""""

#. Select the **Import one or more user accounts from an existing facility** option in the **Select a facility setup for this learn-only device** step. 

#. Any device that has Kolibri running in the local network should appear in the **Select device** window. Read more on how set up a local network in the `Kolibri Hardware Guide <https://learningequality.org/r/hardware-guide>`_.

	Select the device and click the :guilabel:`Continue` button.

	**TODO-screenshot**

  	.. figure:: /img/learn-only-select-device7.png
	   :alt:  

	   Select the network address of the device from which you want to import a facility.

		.. warning:: **Firewalls** may impede your ability to see other devices in your local network or add them as source. If you are unable to see other devices, make sure to:

			* disable the firewalls on all the devices that you need to sync
			* restart Kolibri for broadcast to take effect

#. **Select facility**. If there are several facilities on the device, select the one you want to import the learner account from. 

	**TODO-screenshot**

  	.. figure:: /img/select-facility-import-individual-user-accounts7.png
	   :alt:  

	   Select the facility you want to import and provide credentials.

#. **Import individual learner accounts**. Enter the username and password of the learner you want to import to your device.
   
	**TODO-screenshot**
  
  	.. figure:: /img/import-individual-user-accounts7.png
	   :alt:  

	   Provide credentials to import learner account.

#. Wait for the learner data to load on your device. It may take some time, so please be patient. When you see the confirmation that the process is completed, you can choose to import another learner account on the same device. Otherwise, click the :guilabel:`Finish` button.
