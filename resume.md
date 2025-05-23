---
title: Juliette Attard - Resume
---

Linux OS Developer with hardware and systems engineering focus

> Open to remote roles in the US

# Technical Skills

* API generation
* Python `flask` application development
* Python packaging
* C program debugging and maintenance (cpython, linux kernel, fio, systemd)  
* From-scratch operating system build, packaging, testing
* Automated test development
* Linux storage mechanics (`scsi`/`pci-nvme`/`iSCSI`) 
* Linux networking diagnostics and management automation (ethtool, ip, bgp, iptables)
* Linux kernel debugging and diagnostics (bpftrace, strace) 
* Performance entitlement analysis using fio (flash, networking)
* CI/CD pipelines (`jenkins`/`travis`)
* x86 hardware verification and diagnostics


# Interpersonal skills

* Mentoring of new hires including new-grads and experienced developers into hardware development and OS development roles 
* Technical training and documentation for developers and support staff
* Issue triage and backlog management 
* Software feature planning and organization for small and medium size teams (up to 15 members) 

---

# Experience

IBM: Cloud Object Storage Hardware/Linux Engineer

> May 2013 - PRESENT

Develop a custom GNU/Linux debian-based operating system "ClevOS" deployed on tens of thousands of storage machines worldwide 


## Architect, maintain and implement the OS for IBM Cloud Object Storage 

* Write and maintain code for OS installation and upgrade
* Write and maintain code for hardware management 
* Write and maintain code for network configuration (LACP, 802.Q, BGP, iptables) 
* Architect and maintain code for configuration-driven disk, fan, psu, nic, hba monitoring


## Maintain Security Posture of all python-packages in ClevOS
* Write and maintain tool that converts [`.whl`](https://peps.python.org/pep-0427/) format PyPi packages into [`.deb`](https://www.debian.org/doc/debian-policy/ch-binary.html) binary debian archives.
    * Uses only PEP specified pip commands
    * Generates all binary packages from source archives
    * Self-building, single-file configuration
    * Automatically identifies debian dependencies via `virtualenv` integration
    * Elimination and coexistence of all debian-provided sources (no debian code outside of python3.9!)
* Migration of 40 projects to python3
* Manage and resolve issues created by automated scanning tools like dependabot and mend

## Hardware lifecycle 

* Architect a unittest framework for hardware without access to hardware under test
* Enable testing of devices of devices a decade out of production with the complete set of features supported
* Driver backporting and kernel maintenance to enable new hardware features on stable kernel versions
* Component selection and development of hardware verification procedures for manufacturing
* Working with vendors for components, servers and storage enclosures to identify and resolve firmware and hardware issues identified during development, deployment, and lifecycle (HPE, Cisco, Lenovo, Supermicro, Erricson, Dell/EMC, Seagate, Western Digital) 


## Open-Source Software Maintenance

* Debug and analysis of kernel/open source library issues through code inspection and system tracing (strace, perf, pdb, and gdb)
* Identify extensions and upstream patches to open source projects and the Linux kernel
* Static compilation of open-source packages for portability


## Python Application Performance

* Develop and maintain a framework for identifying timeout conditions for underlying calls in a `flask` application to "blame" bad hardware
* Develop a caching mechanism for a `flask` application that is thread-safe, one-memory-copy, and enables HTTP endpoint route caches for simultaneous `GET` actors (>100% reduction due to CPU savings)
* Use `graphviz`/`cProfile` to reduce test application performance by identifying memory copies, and data reorganization

## Custom Linux Distribution Development

* Author a tool to generate `debian-live` images supporting both `ubuntu` and `debian` bases
* Developed `docker` images supporting "build" and "prod" environments
* Generated application mocking frameworks using `docker`

## Hardware Engineering 

* Learn and use T10/SCSI Standards (SPC-4, SES-3, SAT, SBC, ZBC) daily to support storage operations and development on `SAS` and `SATA` disk drives
* Use internal IBM standards to develop integration within the IBM storage ecosystem
* Develop prototype solutions on `NVMe` platforms, including review of platform compatbility with `ZNS` 
* Identify critical performance characteristics of new servers, storage enclosures, networking components, drives, and flash through design analysis and empirical verification
* Port drivers intended for RHEL and other kernel versions to the ClevOS custom kernel

---

# Education

Illinois Institute of Technology - Master of Computer Science
> Chicago, 2013 - 2014

Illinois Institute of Technology - Bachelor of Computer Science
> Chicago, 2007 - 2013


Performed research with the Wireless Network and Communications Research Center with focus on data management and systems for managing large scale data generated by radio frequency monitoring 

---

# Public Contributions

## [systemd — Resolve hardware specific issue resulting in malformed drive VPD](http://ata-vpd-systemd.julietteattard.com)

* Identified the path which resulted in drives being recognized incorrectly by udev using strace
* Used SCSI Primary Commands and SCSI ATA Translation standards documents to identify the incorrect assertions made in the underlying utility ata_id
* Performed verification on different SAT implementations across HBA vendors to reproduce and verify the condition


## [Linux— Add sysfs attributes for ATA VPD](http://ata-vpd-linux.julietteattard.com)

* Supported the effort of the systemd project to migrate more hardware management functions out of their udev tree and into other distribution packages, as a long-term resolution to the systemd issue with malformed ATA VPD
* Related changes in the sg3-utils package leveraged the VPD attributes for SAS disks, but did not include support for SATA disks 
* Introduced a changeset to the SCSI subsystem with the knowledge identified by the fix for ata_id that enables all ATA specific handling to be relegated from udev and the systemd tree


## [Linux— Allow non-root users to perform ZBC commands](http://zbc-linux-permissions.julietteattard.com)

* Identified that a specific set of system calls being run under non-root accounts were returning -EPERM by using strace 
* Inspected the kernel sources for  the mechanism by which specific SG_IO commands are allowlisted for use by users based on capability flags 
* Extended the list of system calls to include  newly introduced ZBC commands under low privilege accounts which have write access

## [Patent US11023307B2 — Automatic remediation of distributed storage system node components](http://node-fix-patent.julietteattard.com)

* Fleets of hardware in distributed storage networks are typically assembled in multiple locations by hand, and may be modified during installation resulting in configuration differences that can impact performance, reliability, or function
* Devised mechanism by which fleets of similar hardware devices could identify nodes that required low-level configuration changes


## [Patent US10970149B2— Automatic node hardware configuration in a distributed storage system](http://node-config-patent.julietteattard.com)

* Deployments of distributed storage networks at scale typically involve large purchases of similar hardware and knowledge about previously deployments can provide information about new devices
* Devised mechanism by which device configuration could be determined by pre-existing members of a deployment to prevent operators from being required to intervene, in order to ensure a homogenous system for performance and maintenance 









