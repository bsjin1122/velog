<p>작업명    명령어    시작시간    종료시간    실행시간    결과    alert.log
n4    export NLS_DATE_FORMAT='yyyy-mm-dd hh24:mi:ss'<br />    create user sdbadmin identified by sdbadmin;<br />    grant dba to sdbadmin;                &quot;16:00:23 SQL&gt; grant dba to sdbadmin;</p>
<p>Grant succeeded.</p>
<p>Elapsed: 00:00:00.01&quot;<br />    &quot;create table sdbadmin.basedt (
       sys_dt date, current_scn number);&quot;                &quot;16:02:04 SQL&gt; create table sdbadmin.basedt (
16:02:12   2      sys_dt date, current_scn number);</p>
<p>Table created.&quot;<br />    &quot;insert into sdbadmin.basedt (sys_dt, current_scn) 
select sysdate, current_scn from v$database;&quot;                &quot;16:02:37 SQL&gt; insert into sdbadmin.basedt (sys_dt, current_scn)
select sysdate, current_scn from v$database;16:04:15   2</p>
<p>1 row created.&quot;<br />    commit;                &quot;16:04:16 SQL&gt; commit;</p>
<p>Commit complete.</p>
<p>Elapsed: 00:00:00.00&quot;<br />n4 level0 백업    &quot;#!/bin/bash</p>
<p>$ORACLE_HOME/bin/rman target / nocatalog &lt;&lt; EOF</p>
<p>run {
allocate channel c1 device type disk;
allocate channel c2 device type disk;
allocate channel c3 device type disk;
allocate channel c4 device type disk;</p>
<h1 id="level-0">level 0</h1>
<p>backup
incremental level 0
database
not backed up 1 times
format '/BSJ/BACKUP/dbf.%t_%s_%d_%U'
section size 10g
filesperset 2;</p>
<h1 id="archivelog">archivelog</h1>
<p>sql 'alter system archive log current';
backup (archivelog all format '/BSJ/BACKUP/arc.%t_%s_%d' DELETE ALL INPUT);</p>
<h1 id="controlfile">controlfile</h1>
<p>backup format '/BSJ/BACKUP/ctl.%t_%s_%d_%U'(current controlfile);</p>
<h1 id="spfile">spfile</h1>
<p>backup spfile format '/BSJ/BACKUP/spfile.%d_%s_%T';</p>
<p>release channel c1;
release channel c2;
release channel c3;
release channel c4;
}</p>
<p>exit
EOF&quot;    16:06    16:08<br />n4 bct 확인    select * from v$block_change_tracking;                &quot;STATUS     FILENAME                  BYTES     CON_ID</p>
<hr />
<p>DISABLED&quot;<br />n4 bct enable alter database enable block change tracking using file '/BSJ/BACKUP/block_change.bct';                &quot;16:14:17 SQL&gt; alter database enable block change tracking using file '/BSJ/BACKUP/block_change.bct';</p>
<p>Database altered.&quot;<br />n4 bct 확인    select * from v$block_change_tracking;                &quot;16:20:00 SQL&gt; select * from v$block_change_tracking;</p>
<p>STATUS     FILENAME                  BYTES     CON_ID</p>
<hr />
<p>ENABLED    /BSJ/BACKUP/block_ch   11599872          0
           ange.bct&quot;<br />n4 dbid 확인    select dbid from v$database;                &quot;16:24:45 SQL&gt; select dbid from v$database;</p>
<pre><code>    DBID</code></pre><hr />
<p>   332146788&quot;<br />scp로 백업 파일 전송    nohup scp -r <code>ls .|grep -v block_change.bct</code> ./* <a href="mailto:oracle@192.168.0.128">oracle@192.168.0.128</a>:/n4backup &amp;<br />n4 size 확인    select sum(bytes)/1024/1024/1024 gb from dba_data_files;                &quot;16:41:57 SQL&gt; select sum(bytes)/1024/1024/1024 gb from dba_data_files;</p>
<pre><code>    GB</code></pre><hr />
<p>131.066956&quot;<br />n5에서 백업 받을 여유 공간 확인    df -h                &quot;[oracle@kidjin5 20250401-16:22:18]:CUBJIN:[/home/oracle]
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        3.8G  3.8G     0 100% /dev
tmpfs           3.8G  1.1G  2.7G  30% /dev/shm
tmpfs           3.8G  369M  3.4G  10% /run
tmpfs           3.8G     0  3.8G   0% /sys/fs/cgroup
/dev/sda2       304G  165G  140G  55% /
tmpfs           766M   36K  766M   1% /run/user/0&quot;    </p>
<p>n5 db shutdown    shutdown immediate;<br />n5 ORACLE_SID     &quot;export NLS_DATE_FORMAT='yyyy-mm-dd hh24:mi:ss'
export ORACLE_SID=CUBJIN&quot;<br />n4 spfile 백업 이후 확인    RMAN&gt; list backup of spfile;                &quot;RMAN&gt; list backup of spfile;</p>
<h1 id="list-of-backup-sets">List of Backup Sets</h1>
<p>BS Key  Type LV Size       Device Type Elapsed Time Completion Time</p>
<hr />
<p>82      Full    10.20M     DISK        00:00:00     2025-04-01 16:08:15
        BP Key: 126   Status: AVAILABLE  Compressed: NO  Tag: TAG20250401T160815
        Piece Name: /u01/app/oracle/product/19c/dbhome_1/dbs/c-332146788-20250401-02
  SPFILE Included: Modification time: 2025-03-31 17:33:17
  SPFILE db_unique_name: CUBJIN</p>
<p>BS Key  Type LV Size       Device Type Elapsed Time Completion Time</p>
<hr />
<p>86      Full    96.00K     DISK        00:00:00     2025-04-01 16:08:20
        BP Key: 130   Status: AVAILABLE  Compressed: NO  Tag: TAG20250401T160820
        Piece Name: /BSJ/BACKUP/spfile.CUBJIN_188_20250401
  SPFILE Included: Modification time: 2025-03-31 17:33:17
  SPFILE db_unique_name: CUBJIN</p>
<p>BS Key  Type LV Size       Device Type Elapsed Time Completion Time</p>
<hr />
<p>87      Full    10.20M     DISK        00:00:00     2025-04-01 16:08:21
        BP Key: 131   Status: AVAILABLE  Compressed: NO  Tag: TAG20250401T160821
        Piece Name: /u01/app/oracle/product/19c/dbhome_1/dbs/c-332146788-20250401-03
  SPFILE Included: Modification time: 2025-03-31 17:33:17
  SPFILE db_unique_name: CUBJIN&quot;<br />    RMAN-04014: startup failed: ORA-27104: system-defined limits for shared memory was misconfigured<br />    pfile 확인                &quot;17:28:39 SQL&gt; create pfile from spfile='?/dbs/spfileCUBJIN.ora';</p>
<p>File created.</p>
<p>Elapsed: 00:00:00.00&quot;<br />    &quot;vi init(pfile) 
*.use_large_pages='true'&quot;<br />    restore controlfile from '/n4backup/ctl.1197302898_187_CUBJIN_5r3lqp3i_187_1_1'                &quot;RMAN&gt; restore controlfile from '/n4backup/ctl.1197302898_187_CUBJIN_5r3lqp3i_187_1_1'
2&gt; ;</p>
<p>Starting restore at 2025-04-01 17:45:20
allocated channel: ORA_DISK_1
channel ORA_DISK_1: SID=264 device type=DISK</p>
<p>channel ORA_DISK_1: restoring control file
channel ORA_DISK_1: restore complete, elapsed time: 00:00:01
output file name=+DATA/CUBJIN/CONTROLFILE/current.286.1197308721
Finished restore at 2025-04-01 17:45:21&quot;<br />pfile 수정 -&gt; control file    *.control_files='+DATA/CUBJIN/CONTROLFILE/current.286.1197308721'<br />    RMAN&gt; catalog start with '/n4backup';                &quot;RMAN&gt; catalog start with '/n4backup';</p>
<p>searching for all files that match the pattern /n4backup</p>
<h1 id="list-of-files-unknown-to-the-database">List of Files Unknown to the Database</h1>
<p>File Name: /n4backup/afiedt.buf
File Name: /n4backup/arc.1197302896_185_CUBJIN
File Name: /n4backup/arc.1197302896_186_CUBJIN
File Name: /n4backup/ctl.1197302898_187_CUBJIN_5r3lqp3i_187_1_1
File Name: /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_1_1
File Name: /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_2_1
File Name: /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_3_1
File Name: /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_4_1
File Name: /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_5_1
File Name: /n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_1_1
File Name: /n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_2_1
File Name: /n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_3_1
File Name: /n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_4_1
File Name: /n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_1_1
File Name: /n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_2_1
File Name: /n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_3_1
File Name: /n4backup/dbf.1197302809_168_CUBJIN_583lqp0p_168_1_1
File Name: /n4backup/dbf.1197302869_178_CUBJIN_5i3lqp2l_178_1_1
File Name: /n4backup/dbf.1197302870_179_CUBJIN_5j3lqp2m_179_1_1
File Name: /n4backup/dbf.1197302872_180_CUBJIN_5k3lqp2o_180_1_1
File Name: /n4backup/dbf.1197302872_181_CUBJIN_5l3lqp2o_181_1_1
File Name: /n4backup/dbf.1197302888_182_CUBJIN_5m3lqp38_182_1_1
File Name: /n4backup/dbf.1197302888_183_CUBJIN_5n3lqp38_183_1_1
File Name: /n4backup/spfile.CUBJIN_188_20250401
File Name: /n4backup/block_change.bct</p>
<p>Do you really want to catalog the above files (enter YES or NO)? yes
cataloging files...
cataloging done</p>
<h1 id="list-of-cataloged-files">List of Cataloged Files</h1>
<p>File Name: /n4backup/arc.1197302896_185_CUBJIN
File Name: /n4backup/arc.1197302896_186_CUBJIN
File Name: /n4backup/ctl.1197302898_187_CUBJIN_5r3lqp3i_187_1_1
File Name: /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_1_1
File Name: /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_2_1
File Name: /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_3_1
File Name: /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_4_1
File Name: /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_5_1
File Name: /n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_1_1
File Name: /n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_2_1
File Name: /n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_3_1
File Name: /n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_4_1
File Name: /n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_1_1
File Name: /n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_2_1
File Name: /n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_3_1
File Name: /n4backup/dbf.1197302809_168_CUBJIN_583lqp0p_168_1_1
File Name: /n4backup/dbf.1197302869_178_CUBJIN_5i3lqp2l_178_1_1
File Name: /n4backup/dbf.1197302870_179_CUBJIN_5j3lqp2m_179_1_1
File Name: /n4backup/dbf.1197302872_180_CUBJIN_5k3lqp2o_180_1_1
File Name: /n4backup/dbf.1197302872_181_CUBJIN_5l3lqp2o_181_1_1
File Name: /n4backup/dbf.1197302888_182_CUBJIN_5m3lqp38_182_1_1
File Name: /n4backup/dbf.1197302888_183_CUBJIN_5n3lqp38_183_1_1
File Name: /n4backup/spfile.CUBJIN_188_20250401</p>
<h1 id="list-of-files-which-were-not-cataloged">List of Files Which Were Not Cataloged</h1>
<p>File Name: /n4backup/afiedt.buf
  RMAN-07517: Reason: The file header is corrupted
File Name: /n4backup/block_change.bct
  RMAN-07529: Reason: catalog is not supported for this file type&quot;<br />    rman&gt; crosscheck backup;                &quot;RMAN&gt; crosscheck backup;</p>
<p>allocated channel: ORA_DISK_1
channel ORA_DISK_1: SID=12 device type=DISK
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218109_77_CUBJIN_2d3lo69t_77_1_1 RECID=23 STAMP=1197218109
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218109_77_CUBJIN_2d3lo69t_77_2_1 RECID=35 STAMP=1197218158
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218109_77_CUBJIN_2d3lo69t_77_3_1 RECID=33 STAMP=1197218173
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218195_91_CUBJIN_2r3lo6cj_91_1_1 RECID=34 STAMP=1197218195
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218181_88_CUBJIN_2o3lo6c5_88_1_1 RECID=36 STAMP=1197218181
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218220_93_CUBJIN_2t3lo6dc_93_1_1 RECID=38 STAMP=1197218220
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218220_92_CUBJIN_2s3lo6dc_92_1_1 RECID=39 STAMP=1197218220
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218279_98_CUBJIN_323lo6f7_98_1_1 RECID=41 STAMP=1197218279
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218279_97_CUBJIN_313lo6f7_97_1_1 RECID=42 STAMP=1197218279
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218279_97_CUBJIN_313lo6f7_97_3_1 RECID=51 STAMP=1197218417
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218279_95_CUBJIN_2v3lo6f7_95_1_1 RECID=43 STAMP=1197218279
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218279_95_CUBJIN_2v3lo6f7_95_2_1 RECID=45 STAMP=1197218315
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218279_95_CUBJIN_2v3lo6f7_95_3_1 RECID=47 STAMP=1197218321
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218279_95_CUBJIN_2v3lo6f7_95_4_1 RECID=48 STAMP=1197218321
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218279_95_CUBJIN_2v3lo6f7_95_5_1 RECID=46 STAMP=1197218330
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218279_96_CUBJIN_303lo6f7_96_1_1 RECID=44 STAMP=1197218279
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218279_96_CUBJIN_303lo6f7_96_2_1 RECID=50 STAMP=1197218346
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218279_96_CUBJIN_303lo6f7_96_3_1 RECID=52 STAMP=1197218383
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218279_96_CUBJIN_303lo6f7_96_4_1 RECID=49 STAMP=1197218400
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218451_109_CUBJIN_3d3lo6kj_109_1_1 RECID=53 STAMP=1197218451
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197218451_110_CUBJIN_3e3lo6kj_110_1_1 RECID=54 STAMP=1197218451
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302809_168_CUBJIN_583lqp0p_168_1_1 RECID=107 STAMP=1197302809
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302809_168_CUBJIN_583lqp0p_168_1_1 RECID=144 STAMP=1197309252
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302870_179_CUBJIN_5j3lqp2m_179_1_1 RECID=118 STAMP=1197302871
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302870_179_CUBJIN_5j3lqp2m_179_1_1 RECID=146 STAMP=1197309252
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302872_181_CUBJIN_5l3lqp2o_181_1_1 RECID=121 STAMP=1197302872
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302872_181_CUBJIN_5l3lqp2o_181_1_1 RECID=148 STAMP=1197309252
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302872_180_CUBJIN_5k3lqp2o_180_1_1 RECID=122 STAMP=1197302872
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302872_180_CUBJIN_5k3lqp2o_180_1_1 RECID=147 STAMP=1197309252
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302869_178_CUBJIN_5i3lqp2l_178_1_1 RECID=123 STAMP=1197302870
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302869_178_CUBJIN_5i3lqp2l_178_1_1 RECID=145 STAMP=1197309252
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302888_183_CUBJIN_5n3lqp38_183_1_1 RECID=124 STAMP=1197302888
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302888_183_CUBJIN_5n3lqp38_183_1_1 RECID=150 STAMP=1197309252
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302888_182_CUBJIN_5m3lqp38_182_1_1 RECID=125 STAMP=1197302888
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302888_182_CUBJIN_5m3lqp38_182_1_1 RECID=149 STAMP=1197309252
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/u01/app/oracle/product/19c/dbhome_1/dbs/c-332146788-20250401-02 RECID=126 STAMP=1197302895
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/arc.1197302896_185_CUBJIN RECID=127 STAMP=1197302896
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/arc.1197302896_185_CUBJIN RECID=129 STAMP=1197309252
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/arc.1197302896_186_CUBJIN RECID=128 STAMP=1197302896
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/arc.1197302896_186_CUBJIN RECID=130 STAMP=1197309252
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/ctl.1197302898_187_CUBJIN_5r3lqp3i_187_1_1 RECID=131 STAMP=1197309252
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302809_165_CUBJIN_553lqp0p_165_1_1 RECID=108 STAMP=1197302809
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302809_165_CUBJIN_553lqp0p_165_2_1 RECID=111 STAMP=1197302824
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302809_165_CUBJIN_553lqp0p_165_3_1 RECID=113 STAMP=1197302824
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302809_165_CUBJIN_553lqp0p_165_4_1 RECID=114 STAMP=1197302826
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302809_165_CUBJIN_553lqp0p_165_5_1 RECID=112 STAMP=1197302827
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_1_1 RECID=132 STAMP=1197309252
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_2_1 RECID=133 STAMP=1197309252
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_3_1 RECID=134 STAMP=1197309252
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_4_1 RECID=135 STAMP=1197309252
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_5_1 RECID=136 STAMP=1197309252
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302809_166_CUBJIN_563lqp0p_166_1_1 RECID=110 STAMP=1197302809
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302809_166_CUBJIN_563lqp0p_166_2_1 RECID=116 STAMP=1197302834
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302809_166_CUBJIN_563lqp0p_166_3_1 RECID=119 STAMP=1197302842
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302809_166_CUBJIN_563lqp0p_166_4_1 RECID=115 STAMP=1197302845
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_1_1 RECID=137 STAMP=1197309252
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_2_1 RECID=138 STAMP=1197309252
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_3_1 RECID=139 STAMP=1197309252
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_4_1 RECID=140 STAMP=1197309252
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302809_167_CUBJIN_573lqp0p_167_1_1 RECID=109 STAMP=1197302809
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302809_167_CUBJIN_573lqp0p_167_2_1 RECID=120 STAMP=1197302845
crosschecked backup piece: found to be 'EXPIRED'
backup piece handle=/BSJ/BACKUP/dbf.1197302809_167_CUBJIN_573lqp0p_167_3_1 RECID=117 STAMP=1197302853
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_1_1 RECID=141 STAMP=1197309252
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_2_1 RECID=142 STAMP=1197309252
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_3_1 RECID=143 STAMP=1197309252
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/n4backup/spfile.CUBJIN_188_20250401 RECID=151 STAMP=1197309252
Crosschecked 66 objects&quot;<br />    &quot;$ cat newname.cmd
run {
allocate channel ch1 device type disk;
allocate channel ch2 device type disk;
allocate channel ch3 device type disk;
allocate channel ch4 device type disk;
set newname for database to '+DATA';
set newname for tempfile 1 to '+DATA';
restore database;
switch datafile all;
switch tempfile all;
release channel ch1;
release channel ch2;
release channel ch3;
release channel ch4;
}&quot;                rman&gt; @/oramedia/script/newname.cmd    &quot;RMAN&gt; run {
2&gt; allocate channel ch1 device type disk;
3&gt; allocate channel ch2 device type disk;
4&gt; allocate channel ch3 device type disk;
5&gt; allocate channel ch4 device type disk;
6&gt; set newname for database to '+DATA';
7&gt; set newname for tempfile 1 to '+DATA';
8&gt; restore database;
9&gt; switch datafile all;
10&gt; switch tempfile all;
11&gt; release channel ch1;
12&gt; release channel ch2;
13&gt; release channel ch3;
14&gt; release channel ch4;
15&gt; }
allocated channel: ch1
channel ch1: SID=12 device type=DISK</p>
<p>allocated channel: ch2
channel ch2: SID=13 device type=DISK</p>
<p>allocated channel: ch3
channel ch3: SID=263 device type=DISK</p>
<p>allocated channel: ch4
channel ch4: SID=391 device type=DISK</p>
<p>executing command: SET NEWNAME</p>
<p>executing command: SET NEWNAME</p>
<p>Starting restore at 2025-04-01 18:02:45</p>
<p>channel ch1: starting datafile backup set restore
channel ch1: specifying datafile(s) to restore from backup set
channel ch1: restoring datafile 00007 to +DATA
channel ch1: reading from backup piece /n4backup/dbf.1197302809_168_CUBJIN_583lqp0p_168_1_1
channel ch2: starting datafile backup set restore
channel ch2: specifying datafile(s) to restore from backup set
channel ch2: restoring datafile 00005 to +DATA/CUBJIN/DATAFILE/soe.284.1197309767
channel ch2: restoring section 1 of 5
channel ch2: reading from backup piece /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_1_1
channel ch3: starting datafile backup set restore
channel ch3: specifying datafile(s) to restore from backup set
channel ch3: restoring datafile 00003 to +DATA
channel ch3: reading from backup piece /n4backup/dbf.1197302870_179_CUBJIN_5j3lqp2m_179_1_1
channel ch4: starting datafile backup set restore
channel ch4: specifying datafile(s) to restore from backup set
channel ch4: restoring datafile 00006 to +DATA/CUBJIN/DATAFILE/shtbs.282.1197309767
channel ch4: restoring section 1 of 4
channel ch4: reading from backup piece /n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_1_1
channel ch3: piece handle=/n4backup/dbf.1197302870_179_CUBJIN_5j3lqp2m_179_1_1 tag=TAG20250401T160649
channel ch3: restored backup piece 1
channel ch3: restore complete, elapsed time: 00:00:03
channel ch3: starting datafile backup set restore
channel ch3: specifying datafile(s) to restore from backup set
channel ch3: restoring datafile 00005 to +DATA/CUBJIN/DATAFILE/soe.284.1197309767
channel ch3: restoring section 2 of 5
channel ch3: reading from backup piece /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_2_1
channel ch1: piece handle=/n4backup/dbf.1197302809_168_CUBJIN_583lqp0p_168_1_1 tag=TAG20250401T160649
channel ch1: restored backup piece 1
channel ch1: restore complete, elapsed time: 00:00:18
channel ch1: starting datafile backup set restore
channel ch1: specifying datafile(s) to restore from backup set
channel ch1: restoring datafile 00005 to +DATA/CUBJIN/DATAFILE/soe.284.1197309767
channel ch1: restoring section 3 of 5
channel ch1: reading from backup piece /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_3_1
channel ch2: piece handle=/n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_1_1 tag=TAG20250401T160649
channel ch2: restored backup piece 1
channel ch2: restore complete, elapsed time: 00:00:18
channel ch2: starting datafile backup set restore
channel ch2: specifying datafile(s) to restore from backup set
channel ch2: restoring datafile 00005 to +DATA/CUBJIN/DATAFILE/soe.284.1197309767
channel ch2: restoring section 4 of 5
channel ch2: reading from backup piece /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_4_1
channel ch3: piece handle=/n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_2_1 tag=TAG20250401T160649
channel ch3: restored backup piece 2
channel ch3: restore complete, elapsed time: 00:00:15
channel ch3: starting datafile backup set restore
channel ch3: specifying datafile(s) to restore from backup set
channel ch3: restoring datafile 00005 to +DATA/CUBJIN/DATAFILE/soe.284.1197309767
channel ch3: restoring section 5 of 5
channel ch3: reading from backup piece /n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_5_1
channel ch4: piece handle=/n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_1_1 tag=TAG20250401T160649
channel ch4: restored backup piece 1
channel ch4: restore complete, elapsed time: 00:00:18
channel ch4: starting datafile backup set restore
channel ch4: specifying datafile(s) to restore from backup set
channel ch4: restoring datafile 00006 to +DATA/CUBJIN/DATAFILE/shtbs.282.1197309767
channel ch4: restoring section 2 of 4
channel ch4: reading from backup piece /n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_2_1
channel ch3: piece handle=/n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_5_1 tag=TAG20250401T160649
channel ch3: restored backup piece 5
channel ch3: restore complete, elapsed time: 00:00:25
channel ch3: starting datafile backup set restore
channel ch3: specifying datafile(s) to restore from backup set
channel ch3: restoring datafile 00006 to +DATA/CUBJIN/DATAFILE/shtbs.282.1197309767
channel ch3: restoring section 3 of 4
channel ch3: reading from backup piece /n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_3_1
channel ch4: piece handle=/n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_2_1 tag=TAG20250401T160649
channel ch4: restored backup piece 2
channel ch4: restore complete, elapsed time: 00:00:41
channel ch4: starting datafile backup set restore
channel ch4: specifying datafile(s) to restore from backup set
channel ch4: restoring datafile 00006 to +DATA/CUBJIN/DATAFILE/shtbs.282.1197309767
channel ch4: restoring section 4 of 4
channel ch4: reading from backup piece /n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_4_1
channel ch1: piece handle=/n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_3_1 tag=TAG20250401T160649
channel ch1: restored backup piece 3
channel ch1: restore complete, elapsed time: 00:00:44
channel ch1: starting datafile backup set restore
channel ch1: specifying datafile(s) to restore from backup set
channel ch1: restoring datafile 00011 to +DATA/CUBJIN/DATAFILE/soe_tb2.281.1197309829
channel ch1: restoring section 1 of 3
channel ch1: reading from backup piece /n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_1_1
channel ch2: piece handle=/n4backup/dbf.1197302809_165_CUBJIN_553lqp0p_165_4_1 tag=TAG20250401T160649
channel ch2: restored backup piece 4
channel ch2: restore complete, elapsed time: 00:00:44
channel ch2: starting datafile backup set restore
channel ch2: specifying datafile(s) to restore from backup set
channel ch2: restoring datafile 00011 to +DATA/CUBJIN/DATAFILE/soe_tb2.281.1197309829
channel ch2: restoring section 2 of 3
channel ch2: reading from backup piece /n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_2_1
channel ch4: piece handle=/n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_4_1 tag=TAG20250401T160649
channel ch4: restored backup piece 4
channel ch4: restore complete, elapsed time: 00:00:19
channel ch4: starting datafile backup set restore
channel ch4: specifying datafile(s) to restore from backup set
channel ch4: restoring datafile 00011 to +DATA/CUBJIN/DATAFILE/soe_tb2.281.1197309829
channel ch4: restoring section 3 of 3
channel ch4: reading from backup piece /n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_3_1
channel ch3: piece handle=/n4backup/dbf.1197302809_166_CUBJIN_563lqp0p_166_3_1 tag=TAG20250401T160649
channel ch3: restored backup piece 3
channel ch3: restore complete, elapsed time: 00:01:01
channel ch3: starting datafile backup set restore
channel ch3: specifying datafile(s) to restore from backup set
channel ch3: restoring datafile 00012 to +DATA
channel ch3: restoring datafile 00014 to +DATA
channel ch3: reading from backup piece /n4backup/dbf.1197302872_181_CUBJIN_5l3lqp2o_181_1_1
channel ch4: piece handle=/n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_3_1 tag=TAG20250401T160649
channel ch4: restored backup piece 3
channel ch4: restore complete, elapsed time: 00:00:26
channel ch4: starting datafile backup set restore
channel ch4: specifying datafile(s) to restore from backup set
channel ch4: restoring datafile 00004 to +DATA
channel ch4: restoring datafile 00008 to +DATA
channel ch4: reading from backup piece /n4backup/dbf.1197302872_180_CUBJIN_5k3lqp2o_180_1_1
channel ch3: piece handle=/n4backup/dbf.1197302872_181_CUBJIN_5l3lqp2o_181_1_1 tag=TAG20250401T160649
channel ch3: restored backup piece 1
channel ch3: restore complete, elapsed time: 00:00:26
channel ch3: starting datafile backup set restore
channel ch3: specifying datafile(s) to restore from backup set
channel ch3: restoring datafile 00009 to +DATA
channel ch3: reading from backup piece /n4backup/dbf.1197302869_178_CUBJIN_5i3lqp2l_178_1_1
channel ch1: piece handle=/n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_1_1 tag=TAG20250401T160649
channel ch1: restored backup piece 1
channel ch1: restore complete, elapsed time: 00:01:15
channel ch1: starting datafile backup set restore
channel ch1: specifying datafile(s) to restore from backup set
channel ch1: restoring datafile 00001 to +DATA
channel ch1: restoring datafile 00013 to +DATA
channel ch1: reading from backup piece /n4backup/dbf.1197302888_182_CUBJIN_5m3lqp38_182_1_1
channel ch4: piece handle=/n4backup/dbf.1197302872_180_CUBJIN_5k3lqp2o_180_1_1 tag=TAG20250401T160649
channel ch4: restored backup piece 1
channel ch4: restore complete, elapsed time: 00:00:36
channel ch4: starting datafile backup set restore
channel ch4: specifying datafile(s) to restore from backup set
channel ch4: restoring datafile 00002 to +DATA
channel ch4: restoring datafile 00010 to +DATA
channel ch4: reading from backup piece /n4backup/dbf.1197302888_183_CUBJIN_5n3lqp38_183_1_1
channel ch2: piece handle=/n4backup/dbf.1197302809_167_CUBJIN_573lqp0p_167_2_1 tag=TAG20250401T160649
channel ch2: restored backup piece 2
channel ch2: restore complete, elapsed time: 00:01:25
channel ch1: piece handle=/n4backup/dbf.1197302888_182_CUBJIN_5m3lqp38_182_1_1 tag=TAG20250401T160649
channel ch1: restored backup piece 1
channel ch1: restore complete, elapsed time: 00:00:20
channel ch3: piece handle=/n4backup/dbf.1197302869_178_CUBJIN_5i3lqp2l_178_1_1 tag=TAG20250401T160649
channel ch3: restored backup piece 1
channel ch3: restore complete, elapsed time: 00:00:27
channel ch4: piece handle=/n4backup/dbf.1197302888_183_CUBJIN_5n3lqp38_183_1_1 tag=TAG20250401T160649
channel ch4: restored backup piece 1
channel ch4: restore complete, elapsed time: 00:00:17
Finished restore at 2025-04-01 18:05:23</p>
<p>datafile 1 switched to datafile copy
input datafile copy RECID=18 STAMP=1197309923 file name=+DATA/CUBJIN/DATAFILE/system.274.1197309903
datafile 2 switched to datafile copy
input datafile copy RECID=19 STAMP=1197309923 file name=+DATA/CUBJIN/DATAFILE/sysaux.273.1197309907
datafile 3 switched to datafile copy
input datafile copy RECID=20 STAMP=1197309923 file name=+DATA/CUBJIN/DATAFILE/undotbs1.283.1197309767
datafile 4 switched to datafile copy
input datafile copy RECID=21 STAMP=1197309923 file name=+DATA/CUBJIN/DATAFILE/users.277.1197309871
datafile 5 switched to datafile copy
input datafile copy RECID=22 STAMP=1197309923 file name=+DATA/CUBJIN/DATAFILE/soe.284.1197309767
datafile 6 switched to datafile copy
input datafile copy RECID=23 STAMP=1197309923 file name=+DATA/CUBJIN/DATAFILE/shtbs.282.1197309767
datafile 7 switched to datafile copy
input datafile copy RECID=24 STAMP=1197309923 file name=+DATA/CUBJIN/DATAFILE/tcpd.285.1197309767
datafile 8 switched to datafile copy
input datafile copy RECID=25 STAMP=1197309923 file name=+DATA/CUBJIN/DATAFILE/tpcdslikeindexes.278.1197309871
datafile 9 switched to datafile copy
input datafile copy RECID=26 STAMP=1197309923 file name=+DATA/CUBJIN/DATAFILE/tcph.276.1197309897
datafile 10 switched to datafile copy
input datafile copy RECID=27 STAMP=1197309923 file name=+DATA/CUBJIN/DATAFILE/tpchindexes.272.1197309907
datafile 11 switched to datafile copy
input datafile copy RECID=28 STAMP=1197309923 file name=+DATA/CUBJIN/DATAFILE/soe_tb2.281.1197309829
datafile 12 switched to datafile copy
input datafile copy RECID=29 STAMP=1197309923 file name=+DATA/CUBJIN/DATAFILE/mov.280.1197309871
datafile 13 switched to datafile copy
input datafile copy RECID=30 STAMP=1197309923 file name=+DATA/CUBJIN/DATAFILE/json.275.1197309903
datafile 14 switched to datafile copy
input datafile copy RECID=31 STAMP=1197309923 file name=+DATA/CUBJIN/DATAFILE/hr.279.1197309871</p>
<p>renamed tempfile 1 to +DATA in control file</p>
<p>released channel: ch1</p>
<p>released channel: ch2</p>
<p>released channel: ch3</p>
<p>released channel: ch4</p>
<p>RMAN&gt; <strong>end-of-file</strong>&quot;
    recover database<br />                    &quot;18:07:55 SQL&gt; alter database open read only;</p>
<p>Database altered.&quot;<br />    alter database read only;                &quot;SQL*Plus: Release 19.0.0.0.0 - Production on Tue Apr 1 18:07:09 2025
Version 19.20.0.0.0</p>
<p>Copyright (c) 1982, 2022, Oracle.  All rights reserved.</p>
<p>Connected to:
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.20.0.0.0</p>
<p>18:07:09 SQL&gt; alter database open read only;
alter database open read only
*
ERROR at line 1:
ORA-16004: backup database required recovery
ORA-01152: file 1 was not restored from a sufficiently old backup
ORA-01110: data file 1: '+DATA/CUBJIN/DATAFILE/system.274.1197309903'</p>
<p>Elapsed: 00:00:00.06
18:07:25 SQL&gt; alter database open resetlogs;
alter database open resetlogs
*
ERROR at line 1:
ORA-01152: file 1 was not restored from a sufficiently old backup
ORA-01110: data file 1: '+DATA/CUBJIN/DATAFILE/system.274.1197309903'</p>
<p>Elapsed: 00:00:00.02
18:07:55 SQL&gt; alter database open read only;</p>
<p>Database altered.</p>
<p>Elapsed: 00:00:00.96
18:08:57 SQL&gt;&quot;<br />                    &quot;18:16:10 SQL&gt; alter session set NLS_DATE_FORMAT='yyyy-mm-dd hh24:mi:ss';</p>
<p>Session altered.</p>
<p>Elapsed: 00:00:00.00
18:16:28 SQL&gt; select * from sdbadmin.basedt;</p>
<p>SYS_DT              CURRENT_SCN</p>
<hr />
<p>2025-04-01 16:04:16     7820649</p>
<p>Elapsed: 00:00:00.01
18:16:38 SQL&gt; select current_scn from v$database;</p>
<h2 id="current_scn">CURRENT_SCN</h2>
<pre><code>7820889</code></pre><p>Elapsed: 00:00:00.01&quot;    </p>