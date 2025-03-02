<blockquote>
<ul>
<li>bdump로 $ORACLE_BASE/diag/rdbms/cubjin 이 아니라 oracub으로 되어 있었고, </li>
</ul>
</blockquote>
<ul>
<li><a href="https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DIAGNOSTIC_DEST.html">DIAGNOSTIC_DEST</a>는 <code>&lt;diagnostic_dest&gt;/diag/rdbms/&lt;dbname&gt;/&lt;instname&gt;</code>인데 oracub으로 되어있었다. </li>
<li>sid와 db_name이 맞지 않았다</li>
</ul>
<pre><code>17:00:40 SQL&gt; show parameter db_name

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
db_name                              string      ORACUB


17:00:44 SQL&gt; !echo $ORACLE_SID
CUBJIN</code></pre><h2 id="절차">절차</h2>
<ol>
<li>Database의 유효한 cold/hot backup이 있는지 확인한다.</li>
</ol>
<ul>
<li>hot backup인 경우, 모든 archive log와 모든 online redo log의 backup도 있다는 것을 확인한다. </li>
<li><ul>
<li>db를 손상시킬 수 있다. mos에서 백업을 받고 시작. </li>
</ul>
</li>
</ul>
<ol start="2">
<li>export ORACLE_HOME=경로</li>
<li>cd $ORACLE_HOME/bin</li>
<li>dbconsole(EMCA) 삭제</li>
</ol>
<ul>
<li>Note.278100.1 How To Drop, Create And Recreate DB Control In A 10g Database.</li>
</ul>
<ol start="5">
<li>database를 mount상태로 한다.</li>
<li>TNS를 사용해서 데이터베이스에 접속해야할 경우에는 tnsnames.ora에 DB_OLD가 지정되고, LISTENER가 기동되어 있는 것을 확인한다.<ul>
<li>sqlplus sys/@DB_OLD</li>
</ul>
</li>
<li>nid target, setname 파라미터</li>
</ol>
<ul>
<li><code>nid TARGET=sys/&lt;password&gt;[@&lt;service&gt;선택] DBNAME=&lt;새로운 db명&gt;</code></li>
</ul>
<pre><code class="language-shell">
[oracle@cubjin4 20250302-18:03:01]:CUBJIN:[/u01/app/oracle/product/19c/dbhome_1/bin]
$ nid target=sys/baeseojin DBNAME=CUBJIN

DBNEWID: Release 19.0.0.0.0 - Production on Sun Mar 2 18:03:16 2025

Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.

Connected to database ORACUB (DBID=1372511915)

Connected to server version 19.20.0

Control Files in database:
    /u02/oradata/ORACUB/control01.ctl
    /u02/oradata/ORACUB/control02.ctl

Change database ID and database name ORACUB to CUBJIN? (Y/[N]) =&gt; y

Proceeding with operation
Changing database ID from 1372511915 to 332146788
Changing database name from ORACUB to CUBJIN
    Control File /u02/oradata/ORACUB/control01.ctl - modified
    Control File /u02/oradata/ORACUB/control02.ctl - modified
    Datafile /u02/oradata/ORACUB/system01.db - dbid changed, wrote new name
    Datafile /u02/oradata/ORACUB/sysaux01.db - dbid changed, wrote new name
    Datafile /u02/oradata/ORACUB/undotbs01.db - dbid changed, wrote new name
    Datafile /u02/oradata/ORACUB/users01.db - dbid changed, wrote new name
    Datafile /u02/oradata/ORACUB/soe.db - dbid changed, wrote new name
    Datafile /u02/oradata/ORACUB/sh.db - dbid changed, wrote new name
    Datafile /u02/oradata/ORACUB/tcpd.db - dbid changed, wrote new name
    Datafile /u02/oradata/ORACUB/tpcdidx.db - dbid changed, wrote new name
    Datafile /u02/oradata/ORACUB/tcph.db - dbid changed, wrote new name
    Datafile /u02/oradata/ORACUB/tpch.db - dbid changed, wrote new name
    Datafile /u02/oradata/ORACUB/soe2.db - dbid changed, wrote new name
    Datafile /u02/oradata/ORACUB/move.db - dbid changed, wrote new name
    Datafile /u02/oradata/ORACUB/json.db - dbid changed, wrote new name
    Datafile /u02/oradata/ORACUB/hr.db - dbid changed, wrote new name
    Datafile /u02/oradata/ORACUB/temp01.db - dbid changed, wrote new name
    Control File /u02/oradata/ORACUB/control01.ctl - dbid changed, wrote new name
    Control File /u02/oradata/ORACUB/control02.ctl - dbid changed, wrote new name
    Instance shut down

Database name changed to CUBJIN.
Modify parameter file and generate a new password file before restarting.
Database ID for database CUBJIN changed to 332146788.
All previous backups and archived redo logs for this database are unusable.
Database has been shutdown, open database with RESETLOGS option.
Succesfully changed database name and ID.
DBNEWID - Completed succesfully.</code></pre>
<blockquote>
<p>DBNEWID 유틸리티는 파일로의 I/O를 테스트 하기 전에, 데이터파일과 controlfile의 header의 검증을 실행한다.</p>
</blockquote>
<ul>
<li>검증이 성공한 경우에, 명령어를 확인하도록 요구된다.(log file을 지정할 경우, prompt가 표시되지 않는다.)</li>
<li>offline 읽기 전용 데이터파일을 포함한 데이터파일의 DBID(및 이러한 예처럼 지정한 경우 DBNAME)을 변경하고, 데이터베이스를 shutdown한 후 그 다음 종료한다.</li>
</ul>
<ol start="8">
<li>pfile/spfile DB_NAME 변경</li>
<li>ASM 사용 중인 데이터파일을 변경하고 싶을 때</li>
</ol>
<ul>
<li>Note 2881418.1 同じASMディスクグループ内のデータファイルの名前を変更/移動する方法</li>
</ul>
<ol start="10">
<li>startup mount</li>
</ol>
<h3 id="reference">Reference</h3>
<ul>
<li>NID ユーティリティを使用した DBID, DBNAME の変更方法 (Doc ID 2910175.1)    </li>
</ul>