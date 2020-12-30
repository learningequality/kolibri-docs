.. _user_roles:

Default User Roles
##################

By default Kolibri users can have one of 3 roles with respective permissions to access different features. 

Learner
=======

**Learners** have access to the |learn| **Learn** dashboard with the tabs |classes| **Classes**, |channel| **Channels**, and |recommended| **Recommended**.

	.. figure:: /img/navbar-learner.png
	   :alt:

Learners can:

* View resources and have their progress tracked

Coach
=====

**Coaches** have access to the same tabs as learners, but they also have permissions to access the |coach| **Coach** dashboard with the tabs |dashboard| **Class Home**, |reports| **Reports**, and |edit| **Plan**.

	.. figure:: /img/navbar-coach.png
	   :alt:

Coaches can:

* View resources and have their progress tracked
* Access the *Coach* dashboard

    - Track progress of other users and usage stats for individual exercises (in the *Reports* tab)
    - (in the *Plan* tab)

    	- Create/Edit/Delete *Groups* in *Classes* and add users to them
    	- Create/Edit/Delete *Quizzes* and assign them to users
    	- Create/Edit/Delete *Lessons* and assign them to users

.. note:: *Facility coaches* have access to all classes, *class coaches* only to ones they are assigned to		

Facility Admin
==============

**Facility admins** have access to the same tabs as learners and coaches, but they also have permissions to access the |facility| **Facility** dashboard with tabs |classes| **Classes**, |people| **Users**, |settings| **Settings**, and |data| **Data**.

	.. figure:: /img/navbar-admin.png
	  :alt: 

Admins can:

* View resources and have their progress tracked
* Access the *Coach* dashboard to:

 	- Track progress of other users and usage stats for individual exercises
 	- Create/Edit/Delete *Groups* in *Classes* and add users to them
 	- Create/Edit/Delete *Quizzes* and assign them to users
 	- Create/Edit/Delete *Lessons* and assign them to users

* Access the *Facility* dashboard to:

    - Create/Edit/Delete *Classes* and enroll users in them (in the *Classes* tab)
    - Create/Edit/Delete other **admins**, **coaches**, and **learners** (in the *Users* tab)
    - View/Edit facility configuration settings (in the *Settings* tab)
    - Export *Detail* and *Summary* logs usage data (in the *Data* tab)

Super Admin
===========

Kolibri **super admin** users have access to the same tabs as learners, coaches, and facility admins, but they also have permissions to access the |device| **Device** dashboard with tabs |channel| **Channels**, |permissions| **Permissions**, |facility| **Facilities**, |deviceInfo| **Info**, and |settings| **Settings**. Super admins have all device permissions, and are able to :ref:`assign them to other users <permissions>`. 

	.. figure:: /img/navbar-superadmin.png
	  :alt: 

Super admin users can:

* View resources and have their progress tracked
* Access the *Coach* dashboard to:

 	- Track progress of other users and usage stats for individual exercises
 	- Create/Edit/Delete *Groups* in *Classes* and add users to them
 	- Create/Edit/Delete *Quizzes* and assign them to users
 	- Create/Edit/Delete *Lessons* and assign them to users

* Access the *Facility* dashboard to:

    - Create/Edit/Delete *Classes* and enroll users in them (in the *Classes* tab)
    - Create/Edit/Delete other **admins**, **coaches**, and **learners** (in the *Users* tab)
    - View/Edit *Facility configuration* settings (in the *Settings* tab)
    - Export *Detail* and *Summary* logs usage data (in the *Data* tab)

* Access the *Device* dashboard to

    - Import/Export channels (in the *Channels* tab)
    - View/Edit permissions of other users (in the *Permissions* tab)
    - View/Import/Sync/Delete facilities (in the *Facilities* tab)
    - View device hardware and system details (in the *Info* tab)
    - View/Edit device configuration settings (in the *Settings* tab)

.. tip:: If you are unable to retrieve the username and password for the super admin account in your facility, you can :ref:`create a new super admin account using the command line <create_superuser>`.

Assign Additional Permissions
-----------------------------

By default, only **super admin** users can view the |device| **Device** dashboard, import/export channels in Kolibri, and modify |permissions| **Permissions** for other users. However, depending on the needs of the institution, **super admin** users can also :ref:`grant these permissions <permissions>` to other users.
