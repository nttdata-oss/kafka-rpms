%define kafka_name kafka
%define kafka_branch 0.7
%define kafka_ver 0.7.2
%define kafka_version 0.7.2
%define kafka_home /var/lib/kafka/default
%define kafka_user kafka
%define kafka_group kafka

%define kafka_version 0.7.2

Summary: A Daemon Package of Apache Kafka
Name: kafka-service
Version: %{kafka_version}
Release: 1
License: Apache License v2.0
Group: Applications/Databases
URL: http://incubator.apache.org/kafka/
Source0: kafka-service-0.7.2.tgz
BuildRoot: %{_tmppath}/%{name}-%{kafka_version}-%{release}-root
Requires: jdk, kafka
Requires(post): chkconfig initscripts
Requires(pre): chkconfig initscripts
AutoReqProv: no

%description

Apache Kafka is a distributed publish-subscribe messaging system. It
is designed to support the following:

* Persistent messaging with O(1) disk structures that provide constant
  time performance even with many TB of stored messages.

* High-throughput: even with very modest hardware Kafka can support
  hundreds of thousands of messages per second.

* Explicit support for partitioning messages over Kafka servers and
  distributing consumption over a cluster of consumer machines while
  maintaining per-partition ordering semantics.

* Support for parallel data load into Hadoop.

Kafka provides a publish-subscribe solution that can handle all
activity stream data and processing on a consumer-scale web site. This
kind of activity (page views, searches, and other user actions) are a
key ingredient in many of the social feature on the modern web. This
data is typically handled by "logging" and ad hoc log aggregation
solutions due to the throughput requirements. This kind of ad hoc
solution is a viable solution to providing logging data to an offline
analysis system like Hadoop, but is very limiting for building
real-time processing. Kafka aims to unify offline and online
processing by providing a mechanism for parallel load into Hadoop as
well as the ability to partition real-time consumption over a cluster
of machines.

The use for activity stream processing makes Kafka comparable to
Facebook's Scribe or Apache Flume (incubating), though the
architecture and primitives are very different for these systems and
make Kafka more comparable to a traditional messaging system. See our
design page for more details.

%define _kafka_noarch_libdir %{_noarch_libdir}/kafka

%prep
%setup -q

# This SPEC build is Only Packaging.
%build

%install
# Clean out any previous builds not on slash (lol)
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

# Copy the kafka file to the right places
%{__mkdir_p} %{buildroot}/etc/sysconfig
%{__mkdir_p} %{buildroot}/etc/init.d
%{__mkdir_p} %{buildroot}/etc/kafka
%{__mkdir_p} %{buildroot}/var/run/kafka
%{__mkdir_p} %{buildroot}/var/log/kafka

%{__mv} init.d/kafka-server %{buildroot}/etc/init.d
%{__mv} kafka/server.properties kafka/log4j.properties %{buildroot}/etc/kafka
%{__mv} sysconfig/kafka %{buildroot}/etc/sysconfig/kafka

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(755,root,root)
/etc/init.d/kafka-server
/etc/sysconfig/kafka
%defattr(-,%{kafka_user},%{kafka_group},-)
/etc/kafka
/etc/kafka/server.properties
/etc/kafka/log4j.properties
/var/run/kafka
/var/log/kafka

%pre
getent group %{kafka_group} >/dev/null || groupadd -r %{kafka_group}
getent passwd %{kafka_user} >/dev/null || /usr/sbin/useradd --comment "Kafka Daemon User" --shell /bin/bash -M -r -g %{kafka_group} --home %{kafka_home} %{kafka_user}

%changelog
* Thu Aug 16 2013 dobachi - 0.7.2
- Initial Packaging
