<p>ls -al $ORACLE_HOME/bin/extjob                   &gt;  pat_bin.rst<br />ls -al $ORACLE_HOME/bin/jssu                     &gt;&gt; pat_bin.rst
ls -al $ORACLE_HOME/bin/nmb                      &gt;&gt; pat_bin.rst
ls -al $ORACLE_HOME/bin/nmhs                     &gt;&gt; pat_bin.rst
ls -al $ORACLE_HOME/bin/nmo                      &gt;&gt; pat_bin.rst
ls -al $ORACLE_HOME/bin/oradism                  &gt;&gt; pat_bin.rst
ls -al $ORACLE_HOME/rdbms/admin/externaljob.ora  &gt;&gt; pat_bin.rst</p>
<p>을 수행시키면 permission / owner, group 이 나오는데요
아래의 형식대로 현재 설치된 엔진의 binary가 올바른지 확인 부탁드립니다.</p>
<pre><code># chown root $ORACLE_HOME/bin/oradism
# chmod 4750 $ORACLE_HOME/bin/oradism
# chown root $ORACLE_HOME/bin/extjob
# chmod 4750 $ORACLE_HOME/bin/extjob
# chown root $ORACLE_HOME/rdbms/admin/externaljob.ora
# chmod 640 $ORACLE_HOME/rdbms/admin/externaljob.ora
# chown root $ORACLE_HOME/bin/jssu
# chmod 4750 $ORACLE_HOME/bin/jssu
# chown root $ORACLE_HOME/bin/nmb
# chmod 4710 $ORACLE_HOME/bin/nmb
# chown root $ORACLE_HOME/bin/nmhs
# chmod 4710 $ORACLE_HOME/bin/nmhs
# chown root $ORACLE_HOME/bin/nmo
# chmod 4710 $ORACLE_HOME/bin/nmo</code></pre><p>'''
Executing &quot;relink all&quot; resets permission of extjob, jssu, oradism, externaljob.ora (Doc ID 1555453.1)<br />    Executing &quot;relink all&quot; will change the ownership of files to &quot;oracle&quot; as the relink command is executed by user &quot;oracle&quot;.  Permission and ownership of files extjob, jssu is set to &quot;4750&quot; and &quot;root&quot; by &quot;root.sh&quot; script, which in turn calls &quot;rootadd_rdbms.sh&quot;.
     This issue is explained in following bugs
     Bug 7361549 - CPUJUL2008 WILL CHANGE PERMISSIONS OF ROOT OWNED EXECUTABLES
    Bug 7497013 - RELINKING EXTJOB RESETS PERMISSIONS AND OWNERSHIP OF $ORACLE_HOME/BIN/EXTJOB
     snippet of &quot;rootadd_rdbms.sh&quot;
     # copy extjobo to extjob if it doesn't exist
    if [ ! -f $ORACLE_HOME/bin/extjob -a -f $ORACLE_HOME/bin/extjobo ]; then
      $CP -p $ORACLE_HOME/bin/extjobo $ORACLE_HOME/bin/extjob
    if [ -f $ORACLE_HOME/bin/extjob ]; then
      $CHOWN root $ORACLE_HOME/bin/extjob
      $CHMOD 4750 $ORACLE_HOME/bin/extjob
    if [ -f $ORACLE_HOME/rdbms/admin/externaljob.ora ]; then
      $CHOWN root $ORACLE_HOME/rdbms/admin/externaljob.ora
      $CHMOD 640 $ORACLE_HOME/rdbms/admin/externaljob.ora
    if [ -f $ORACLE_HOME/rdbms/admin/externaljob.ora.orig ]; then
      $RM -f $ORACLE_HOME/rdbms/admin/externaljob.ora.orig</p>
<pre><code>W/A
# chown root $ORACLE_HOME/bin/oradism
# chmod 4750 $ORACLE_HOME/bin/oradism
 # chown root $ORACLE_HOME/bin/extjob
# chmod 4750 $ORACLE_HOME/bin/extjob
 # chown root $ORACLE_HOME/rdbms/admin/externaljob.ora
# chmod 640  $ORACLE_HOME/rdbms/admin/externaljob.ora
 # chown root $ORACLE_HOME/bin/jssu
# chmod 4750 $ORACLE_HOME/bin/jssu
 # chown root $ORACLE_HOME/bin/nmb
# chmod 4710 $ORACLE_HOME/bin/nmb
 # chown root $ORACLE_HOME/bin/nmhs
# chmod 4710 $ORACLE_HOME/bin/nmhs
 # chown root $ORACLE_HOME/bin/nmo
# chmod 4710 $ORACLE_HOME/bin/nmo</code></pre><p>'''</p>