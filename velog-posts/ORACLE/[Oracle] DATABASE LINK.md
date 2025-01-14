<pre><code class="language-sql">[oracle@cubjin4 20250114-23:08:51]:ORACUB:[/u01/app/oracle/product/19c/dbhome_1/network/admin]
$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Tue Jan 14 23:08:56 2025
Version 19.20.0.0.0

Copyright (c) 1982, 2022, Oracle.  All rights reserved.


Connected to:
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.20.0.0.0

SQL&gt; create table CUBDBLINK.CUBTABLE as select * from dba_data_files;
create table CUBDBLINK.CUBTABLE as select * from dba_data_files
                                                 *
ERROR at line 1:
ORA-01950: no privileges on tablespace 'USERS'


SQL&gt; alter user CUBDBLINK default tablespace users quota unlimited on users;

User altered.

SQL&gt; grant select, insert, update, delete on CUBDBLINK.CUBTABLE TO CUBDBLINK;

Grant succeeded.


SQL&gt; create table CUBDBLINK.CUBTABLE as select * from dba_data_files;

Table created.

SQL&gt; create synonym cubtable for cubdblink.cubtable;

Synonym created.



----os에서
[root@cubjin4 ~]# systemctl status firewalld
● firewalld.service
   Loaded: masked (Reason: Unit firewalld.service is masked.)
   Active: inactive (dead)

--- n4 sqlplus / as sysdba
SQL&gt; alter system register;

System altered.

SQL&gt; exit;

--
[oracle@cubjin4 20250114-23:58:18]:ORACUB:[/home/oracle]
$ lsnrctl status LISTCUB

LSNRCTL for Linux: Version 19.0.0.0.0 - Production on 14-JAN-2025 23:58:25

Copyright (c) 1991, 2023, Oracle.  All rights reserved.

Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=cubjin4)(PORT=1521)))
STATUS of the LISTENER
------------------------
Alias                     LISTCUB
Version                   TNSLSNR for Linux: Version 19.0.0.0.0 - Production
Start Date                14-JAN-2025 23:55:18
Uptime                    0 days 0 hr. 3 min. 6 sec
Trace Level               off
Security                  ON: Local OS Authentication
SNMP                      OFF
Listener Parameter File   /u01/app/oracle/product/19c/dbhome_1/network/admin/listener.ora
Listener Log File         /u01/app/oracle/diag/tnslsnr/cubjin4/listcub/alert/log.xml
Listening Endpoints Summary...
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=cubjin4)(PORT=1521)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=EXTPROC1521)))
Services Summary...
Service &quot;ORACUB&quot; has 1 instance(s).
  Instance &quot;ORACUB&quot;, status READY, has 1 handler(s) for this service...
Service &quot;ORACUBXDB&quot; has 1 instance(s).
  Instance &quot;ORACUB&quot;, status READY, has 1 handler(s) for this service...
The command completed successfully



-----n3
SQL&gt; grant create database link to FOXDBLINK;

Grant succeeded.


SQL&gt; CREATE DATABASE LINK TNSN4
CONNECT TO CUBDBLINK IDENTIFIED BY &quot;cubdblink12!&quot;
USING 'TNSN4'  
;

Database link created.


---sqlplus 접속
SQL&gt; show user
USER is &quot;SYS&quot;
SQL&gt; /

FILE_NAME
--------------------------------------------------------------------------------
   FILE_ID TABLESPACE_NAME                     BYTES     BLOCKS STATUS
---------- ------------------------------ ---------- ---------- ---------
RELATIVE_FNO AUT   MAXBYTES  MAXBLOCKS INCREMENT_BY USER_BYTES USER_BLOCKS
------------ --- ---------- ---------- ------------ ---------- -----------
ONLINE_ LOST_WR
------- -------
/u02/oradata/ORACUB/system01.dbf
         1 SYSTEM                         1163919360     142080 AVAILABLE
           1 YES 3.4360E+10    4194302         1280 1162870784      141952
SYSTEM  OFF

</code></pre>