Glossary of Kolibri terms
#########################

.. glossary::

    Server
      Any device that can make digital data (videos, files, etc.) available for browsing, either to other clients and peers on the local network, or publicly on the Internet. When Kolibri is installed and run on a device, it effectively turns that device into a ‘Kolibri server’, which means that device is capable of transmitting (‘serving’) educational resources in the local network.

    Client
      Any device in a local network that uses a browser to access the educational resources available on the Kolibri server device running in that same network.

    Facility
      A facility in Kolibri connects a set of user accounts, classes, and associated data such as assignments and learner progress. The same facility can be shared across multiple devices, and there can also be multiple facilities on a single device. A facility could represent physical schools, temporary learning hubs, organizations distributing devices across multiple locations, parent or family programs, and other types of learning environments featuring continuity between learners' activities.

    Device
      Physical or virtual machine that Kolibri Learning Platform is installed on. **Kolibri server** device will minimally include a processor, storage, and memory. It may also include a screen, a network connection, a battery, etc. Common examples of server devices are: a desktop or laptop computer; a rack-mounted server; a Raspberry Pi; a virtual machine running in the cloud.

		    * **Full device**

		      A device that is a fully-featured Kolibri server and can be used by admins, coaches and learners. A full device enables access to all learner, coach and admin features.

		    * **Learn-only device**
		      
		      Most commonly a mobile device (tablet or a smartphone) where Kolibri app is configured to be used only by one or more learners, and always associated with a full facility on a server device (:term:`read the full description below <Learn-only device>`).

    Learn-only device
      Setup modality to use Kolibri app on mobile devices by learners in **Group learning** environments, either formal (schools) or non-formal (libraries or community centers), that already have a Kolibri server device.

      In this setup Kolibri app has the **device auto-discovery** and **automated syncing** configured by default.

		    * **Device auto-discovery** allows Kolibri to recognize other instances of *Kolibris* in the local network, without the the need for user to know their :ref:`IP addresses <ips>` and set them up in advance, in order to connect (for user import, browsing libraries, and syncing).  

		    * **Automated syncing** enables seamless and automatic download of all the resources (assigned by coaches in lessons and quizzes) from the Kolibri server to learn-only devices associated with it, whenever they are connected to the same local network. The same process allows for all the progress data about learners' interactions with the assigned resources on learn-only devices, to be synced back to the Kolibri server, in order for coaches to oversee their progress.

      Unlike a 'full device', a 'learn-only device' will have available only the features for learners. Coaches and admins can sign in but will only see the *Learn* page.

    Sync
      The term **sync** is used to describe 2 similar processes in working with Kolibri learning platform, but you must keep in mind their differences for the optimum usage.

		    * **Full facility** sync is the process of synchronizing facility data (learners, groups, classes, learner progress, assignments) between devices that have the same full facility. The facility created on a full device can later be imported to other devices, which enables administrators to perform the facility data sync between those devices, when they are in the same local network. 

		    * **Learn-only device** syncs constantly with the device that has the full facility it is associated with, while both are in the same local network. This process is performed in the background, and does not need to be initiated manually. Syncing on learn-only device includes the data about learner's interactions with resources and their progress with class assignments (to be reviewed by coaches), **and** it also enables the resources assigned by coaches to be transferred seamlessly and automatically from the full device to learn-only device. 

    On my own
      Setup modality to use Kolibri at home, or for supplemental learning outside any larger facility. You will need Internet access or a data plan on your mobile device to download Kolibri and import learning resources, but no Internet or data is required thereafter to use the app. In this setup Kolibri will have full admin, coach and learner features.

