<h2 id="상황">상황</h2>
<blockquote>
<p>dbca에 올바르지 않은 값들... 빠진 값들도 너무 많고 .. 커널 값도 제대로 확인을 안하고 수행해서 다시 재설치를 해야할 것 같다고 생각했다.</p>
</blockquote>
<h3 id="절차">절차</h3>
<ul>
<li>shutdown immediate<pre><code class="language-sql">SQL&gt; shutdown immediate;
Database closed.
Database dismounted.
ORACLE instance shut down.</code></pre>
</li>
<li>STARTUP MOUNT RESTRICT EXCLUSIVE;</li>
</ul>
<pre><code class="language-sql">SQL&gt; STARTUP MOUNT RESTRICT EXCLUSIVE;
ORACLE instance started.

Total System Global Area 3221222440 bytes
Fixed Size                  8930344 bytes
Variable Size             654311424 bytes
Database Buffers         2550136832 bytes
Redo Buffers                7843840 bytes
Database mounted.
</code></pre>
<ul>
<li>drop database<pre><code class="language-sql">SQL&gt; drop database;
</code></pre>
</li>
</ul>
<p>Database dropped.</p>
<p>Disconnected from Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.20.0.0.0</p>
<p>--- alert.log 
2025-01-08T22:32:44.378052+09:00
drop database
2025-01-08T22:32:44.385059+09:00
Deleted file /u01/app/oracle/oradata/ORAFOX/system01.dbf
Deleted file /u01/app/oracle/oradata/ORAFOX/sysaux01.dbf
Deleted file /u01/app/oracle/oradata/ORAFOX/undotbs01.dbf
Deleted file /u01/app/oracle/oradata/ORAFOX/users01.dbf
Deleted file /u01/app/oracle/oradata/ORAFOX/soe.dbf
Deleted file /u01/app/oracle/oradata/ORAFOX/sh.dbf
Deleted file /u01/app/oracle/oradata/ORAFOX/TPCDSL.dbf
Deleted file /u01/app/oracle/oradata/ORAFOX/TPCDSLikeIndexes.dbf
Deleted file /u01/app/oracle/oradata/ORAFOX/data_tpchlike.dbf
Deleted file /u01/app/oracle/oradata/ORAFOX/tpchIndexes.dbf
Deleted file /u01/app/oracle/oradata/ORAFOX/redo01.log
Deleted file /u01/app/oracle/oradata/ORAFOX/redo02.log
Deleted file /u01/app/oracle/oradata/ORAFOX/redo03.log
Deleted file /u01/app/oracle/oradata/ORAFOX/temp01.dbf
Deleted file /u01/app/oracle/product/19c/dbhome_1/dbs/snapcf_ORAFOX.f
Shutting down archive processes
Archiving is disabled</p>
<pre><code>```sql
Version 19.20.0.0.0
SQL&gt; select * from v$instance;
SP2-0640: Not connected
</code></pre>