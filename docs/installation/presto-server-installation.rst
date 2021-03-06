==========================
Presto Server Installation
==========================
Prerequisites: :ref:`presto-admin-installation-label`, :ref:`java-installation-label` and :ref:`presto-admin-configuration-label`

The following describes how to install the Presto query engine on a cluster of nodes using the ``presto-admin`` software utility.

First download the `Presto RPM <https://repository.sonatype.org/service/local/artifact/maven/content?r=central-proxy&g=com.facebook.presto&a=presto-server-rpm&e=rpm&v=RELEASE>`_ and copy it to a location accessible by ``presto-admin``. Then, to install Presto, run the following:
::

 $ sudo ./presto-admin server install <local_path_to_rpm>


Presto! Presto is now installed on the coordinator and workers specified in your ``/etc/opt/prestoadmin/config.json`` file. Before you can issue your first query, you must start Presto:
::

 $ sudo ./presto-admin server start

This may take a few seconds, since the command doesn't exit until ``presto-admin`` verifies that Presto is fully up and ready to receive queries.
