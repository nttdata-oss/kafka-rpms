##################################
README
##################################

.. sectnum::

==========================
Feature
==========================

* Deploy binaries of Kafka to /usr/lib/kafka.
* Manage the serice packages separately from the main sources of Kafka.
* Make "kafka" user and "kafka" group to start processes.
* Use the shell script function provided by the Kafka project to manage processes in the init script.
* Kafka 0.8.1.1 is used in the following procedure.

==========================
Requriement
==========================
* Internet access
* Linux distribution: CentOS6

  + We used CentOS 6.5 64bit

* JDK6 or JDK7

  + We used Oracle JDK7

* The following packages should be installed.

  + rpm-build
  + zip, unzip

==========================
How to make Kafka rpm
==========================

------------------
Clone spec files
------------------
Download spec files from the repository.

command example::

 $ cd <your working directory>
 $ git clone https://github.com/nttdata-oss/kafka-rpms.git
 $ cd kafka-rpms
 $ git checkout -b v0.8.1.1 refs/tags/0.8.1.1

------------------------
Download kafka binaries
------------------------
Download kafka binaries from the official download link.
The download URL is found at Apache Kafka official web site(http://kafka.apache.org)

command example::

 $ wget http://<url of the mirror site>/kafka_2.10-0.8.1.1.tgz

If you don't have ~/rpmbuild directory,
you need to make directories.

command sample::

 $ mkdir -p ~/rpmbuild/BUILD ~/rpmbuild/BUILDROOT ~/rpmbuild/RPMS ~/rpmbuild/SOURCES ~/rpmbuild/SPECS ~/rpmbuild/SRPMS

Copy tgz file and patch to the rpmbuild directory.

command example::

 $ cp kafka_2.10-0.8.1.1.tgz ~/rpmbuild/SOURCES
 $ cp kafka-rpm/patch/logs_default_change.patch ~/rpmbuild/SOURCES

------------------
Copy spec file
------------------

Copy spec file of kafka to the rpmbuild directory.

command example::

 $ cp kafka-rpm/kafka.spec  ~/rpmbuild/SPECS

-----------
Build rpm
-----------
Build rpm.

command example::

 $ rpmbuild -ba ~/rpmbuild/SPECS/kafka.spec

As a result of this command,
you get ~/rpmbuild/RPMS/x86_64/kafka-0.8.1.1-3.x86_64.rpm.

================================
How to make Kafka service rpm
================================

-------------------------------
Copy scripts and make tar file
-------------------------------
Copy scripts and config files to rpmbuild directory.

command example::

 $ mkdir ~/rpmbuild/SOURCES/kafka-service-0.8.1.1
 $ cp -r kafka-rpm/init.d ~/rpmbuild/SOURCES/kafka-service-0.8.1.1
 $ cp -r kafka-rpm/kafka ~/rpmbuild/SOURCES/kafka-service-0.8.1.1
 $ cp -r kafka-rpm/sysconfig ~/rpmbuild/SOURCES/kafka-service-0.8.1.1

Make tar file.

command example::

 $ cd ~/rpmbuild/SOURCES
 $ tar cvzf kafka-service-0.8.1.1.tgz kafka-service-0.8.1.1

------------------
Copy spec file
------------------
Copy spec file of kafka to the rpmbuild directory.

command example::

 $ cd <your working directory>
 $ cp kafka-rpm/kafka-service.spec  ~/rpmbuild/SPECS

-----------
Build rpm
-----------
Build rpm.

command example::

 $ rpmbuild -ba ~/rpmbuild/SPECS/kafka-service.spec

As a result of this command,
you get ~/rpmbuild/RPMS/x86_64/kafka-service-0.8.1.1-4.x86_64.rpm.

=========================
ToDo
=========================
The following is the main of ToDo.

* Bring init scripts into compliance with LSB.

  + http://refspecs.linuxbase.org/LSB_3.1.1/LSB-Core-generic/LSB-Core-generic/iniscrptact.html

* Gather configration files into /etc/kafka directory.
* Use alternatives.

.. vim: ft=rst tw=0
