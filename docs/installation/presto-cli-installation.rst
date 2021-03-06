.. _presto-cli-installation-label:

======================
Running Presto Queries
======================

The Presto CLI provides a terminal-based interactive shell for running queries. The CLI is a self-executing JAR file, which means it acts like a normal UNIX executable.

Download the `presto-cli <https://repository.sonatype.org/service/local/artifact/maven/content?r=central-proxy&g=com.facebook.presto&a=presto-cli&v=RELEASE>`_ and copy it to the location you want to run it from. This location may be any node that has network access to the coordinator. Then rename it to presto and make it executable with chmod +x:
::

 $ mv presto-cli-0.115-executable.jar presto
 $ chmod +x presto

.. NOTE:: Presto must run with Java 8, so if Java 7 is the default on your cluster, you will need to explicitly specify the Java 8 executable. For example, ``<path_to_java_8_executable> -jar presto``. It may be helpful to add an alias for the Presto CLI: ``alias presto='<path_to_java_8_executable> -jar <path_to_presto>'``.

By default, ``presto-admin`` installs the TPC-H connector for you, which generates TPC-H data on-the-fly.  Using this connector, issue the following commands to run your first Presto query:
::

 $ ./presto --catalog tpch --schema tiny
 $ select count(*) from lineitem;

For more on connectors, including how to connect to Hive, see :ref:`connector-add`.

The above command assumes that you installed the Presto CLI on the coordinator, and that the Presto server is on port 8080. If either of these are not the case, then specify the server location in the command:
::

 $ ./presto --server <host_name>:<port_number> --catalog system

