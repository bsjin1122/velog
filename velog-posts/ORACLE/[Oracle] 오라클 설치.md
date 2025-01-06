<h2 id="bash_profile">.bash_profile</h2>
<pre><code class="language-shell">(oracle 계정에서)
# User specific environment and startup programs
export TMP=/tmp
export TMPDIR=$TMP

export ORACLE_BASE=/u01/app/oracle
export ORACLE_HOME=$ORACLE_BASE/product/19c/dbhome_1
export ORA_INVENTORY=/u01/app/oraInventory
export ORACLE_SID=ORAFOX
#export INST_ID=1
#export DATA_DIR=/u02/oradata

export ORACLE_UNQNAME=ORAFOX
export ORACLE_UNQNAME_LOWER=`echo $ORACLE_UNQNAME | tr A-Z a-z`
export ORACLE_SID=${ORACLE_UNQNAME}$INST_ID
export PATH=$PATH:$ORACLE_HOME/bin:$ORACLE_HOME/OPatch
#export TNS_ADMIN=$ORACLE_HOME/network/admin
#export NLS_LANG=American_America.KO16KSC5601

export PATH=/usr/sbin:/usr/local/bin:$ORACLE_HOME/bin:$ORACLE_HOME/OPatch:$PATH
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
export CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib

export DIAGNOSTIC_DEST='/u01/app/oracle'
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
export PS1=&quot;[\u@\h \D{%Y%m%d-%H:%M:%S}]:\$ORACLE_SID:\$ORACLE_PDB_SID[\$PWD]
$ &quot;
alias unpdb='unset ORACLE_PDB_SID'
alias sd='sqlplus / as sysdba'
alias bdump='cd $DIAGNOSTIC_DEST/diag/rdbms/${ORACLE_UNQNAME_LOWER}/${ORACLE_SID}/trace'
alias t_dbalert='tail -30f $DIAGNOSTIC_DEST/diag/rdbms/${ORACLE_UNQNAME_LOWER}/${ORACLE_SID}/trace/alert*.log'
alias oratop='$ORACLE_HOME/suptools/oratop/oratop -r / as sysdba'
</code></pre>
<h2 id="user-생성">user 생성</h2>
<pre><code class="language-shell">[root@sjlabs ~]# id
uid=0(root) gid=0(root) groups=0(root) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023

&gt;&gt; 아래 명령어로 생성 후 

[root@foxjin3 20250106-22:57:48]:ORAPUPPY:[/root]
$ groupadd -g 54321 dba
[root@foxjin3 20250106-22:57:49]:ORAPUPPY:[/root]
$ useradd -u 54321 -g 54321 oracle
useradd: warning: the home directory already exists.
Not copying any file from skel directory into it.
Creating mailbox file: File exists
[root@foxjin3 20250106-22:57:56]:ORAPUPPY:[/root]
$ id oracle
uid=54321(oracle) gid=54321(dba) groups=54321(dba)

$ su - oracle
[oracle@foxjin3 ~]$ id
uid=54321(oracle) gid=54321(dba) groups=54321(dba) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
</code></pre>
<ul>
<li>groupadd -g 54321 dba</li>
<li>useradd -u 54321 -g 54321 oracle</li>
<li>su - oracle</li>
<li>id</li>
</ul>
<blockquote>
<p>(scp용으로..)</p>
</blockquote>
<ul>
<li>(root로) passwd oracle</li>
<li>패스워드 2번 입력<pre><code class="language-shell"></code></pre>
</li>
</ul>
<p>$ passwd oracle
Changing password for user oracle.
New password:
Retype new password:</p>
<pre><code>
### /oramedia 경로 생성
```shell
[root@foxjin3 20250106-23:00:24]:ORAPUPPY:[/root]
$ mkdir /oramedia
[root@foxjin3 20250106-23:00:42]:ORAPUPPY:[/root]
$ chown oracle:dba /oramedia
[root@foxjin3 20250106-23:01:10]:ORAPUPPY:[/root]
$ ls -al /
total 28
dr-xr-xr-x.  18 root   root  240 Jan  6 23:00 .
dr-xr-xr-x.  18 root   root  240 Jan  6 23:00 ..
lrwxrwxrwx.   1 root   root    7 Oct  9  2021 bin -&gt; usr/bin
dr-xr-xr-x.   5 root   root 4096 Jan  6 02:21 boot
drwxr-xr-x.  18 root   root 3220 Jan  6 22:46 dev
drwxr-xr-x. 142 root   root 8192 Jan  6 22:57 etc
drwxr-xr-x.   4 root   root   36 Jan  6 22:52 home
lrwxrwxrwx.   1 root   root    7 Oct  9  2021 lib -&gt; usr/lib
lrwxrwxrwx.   1 root   root    9 Oct  9  2021 lib64 -&gt; usr/lib64
drwxr-xr-x.   2 root   root    6 Oct  9  2021 media
drwxr-xr-x.   2 root   root    6 Oct  9  2021 mnt
drwxr-xr-x.   2 root   root    6 Oct  9  2021 opt
drwxr-xr-x.   2 oracle dba     6 Jan  6 23:00 oramedia
</code></pre><h3 id="u01-u02-생성">/u01 /u02 생성</h3>
<pre><code class="language-shell">
[root@foxjin3 20250106-23:03:00]:ORAPUPPY:[/root]
$ ls -al /
total 28
dr-xr-xr-x.  20 root   root  262 Jan  6 23:02 .
dr-xr-xr-x.  20 root   root  262 Jan  6 23:02 ..
lrwxrwxrwx.   1 root   root    7 Oct  9  2021 bin -&gt; usr/bin
dr-xr-xr-x.   5 root   root 4096 Jan  6 02:21 boot
drwxr-xr-x.  18 root   root 3220 Jan  6 22:46 dev
drwxr-xr-x. 142 root   root 8192 Jan  6 22:57 etc
drwxr-xr-x.   4 root   root   36 Jan  6 22:52 home
lrwxrwxrwx.   1 root   root    7 Oct  9  2021 lib -&gt; usr/lib
lrwxrwxrwx.   1 root   root    9 Oct  9  2021 lib64 -&gt; usr/lib64
drwxr-xr-x.   2 root   root    6 Oct  9  2021 media
drwxr-xr-x.   2 root   root    6 Oct  9  2021 mnt
drwxr-xr-x.   2 root   root    6 Oct  9  2021 opt
drwxr-xr-x.   2 oracle dba     6 Jan  6 23:00 oramedia
dr-xr-xr-x. 270 root   root    0 Jan  6 22:46 proc
dr-xr-x---.  15 root   root 4096 Jan  6 22:46 root
drwxr-xr-x.  44 root   root 1240 Jan  6 22:48 run
lrwxrwxrwx.   1 root   root    8 Oct  9  2021 sbin -&gt; usr/sbin
drwxr-xr-x.   2 root   root    6 Oct  9  2021 srv
dr-xr-xr-x.  13 root   root    0 Jan  6 22:46 sys
drwxrwxrwt.  17 root   root 4096 Jan  6 23:01 tmp
drwxr-xr-x.   2 oracle dba     6 Jan  6 23:02 u01
drwxr-xr-x.   2 oracle dba     6 Jan  6 23:02 u02
drwxr-xr-x.  12 root   root  144 Jan  6 00:42 usr
drwxr-xr-x.  21 root   root 4096 Jan  6 00:53 var



[root@foxjin3 20250106-23:33:59]:ORAFOX:[/oramedia/19c_basemedia]
$ mkdir -p /u01/app/oracle/product/19c/dbhome_1
[root@foxjin3 20250106-23:34:06]:ORAFOX:[/oramedia/19c_basemedia]
$ chown oracle:dba /u01/app/oracle/product/19c/dbhome_1

</code></pre>
<hr />
<h3 id="19c_base-압축-풀기">19c_base 압축 풀기</h3>
<pre><code class="language-shell">[oracle@foxjin3 20250106-23:40:43]:ORAFOX:[/oramedia/19c_basemedia]
$ ls
LINUX.X64_193000_db_home.zip
[oracle@foxjin3 20250106-23:40:44]:ORAFOX:[/oramedia/19c_basemedia]
$ unzip LINUX.X64_193000_db_home.zip -d $ORACLE_HOME</code></pre>
<h3 id="압축풀기-opatch-유틸리티-설치-파일">압축풀기 (OPatch 유틸리티 설치 파일)</h3>
<pre><code class="language-shell">[oracle@foxjin3 20250106-23:41:00]:ORAFOX:[/oramedia/19.20]
$ ls -al
total 4894804
drwxr-xr-x. 2 oracle dba        174 Jan  6 23:24 .
drwxr-xr-x. 4 oracle dba         40 Jan  6 23:24 ..
-rwxr-xr-x. 1 oracle dba  127314614 Jan  6 23:23 OJVM_p35354406_190000_Linux-x86-64.zip
-rwxr-xr-x. 1 oracle dba 2990370786 Jan  6 23:23 p35319490_190000_Linux-x86-64.zip
-rwxr-xr-x. 1 oracle dba 1769419773 Jan  6 23:24 p35320081_190000_Linux-x86-64.zip
-rwxr-xr-x. 1 oracle dba  125167420 Jan  6 23:24 p6880880_190000_Linux-x86-64.zip

[oracle@foxjin3 20250106-23:41:02]:ORAFOX:[/oramedia/19.20]
$ unzip p6880880_190000_Linux-x86-64.zip -d $ORACLE_HOME

replace /u01/app/oracle/product/19c/dbhome_1/OPatch/docs/cversion.txt? [y]es, [n]o, [A]ll, [N]one, [r]ename: A &lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;


------ 압축 풀고 해당 경로에서 확인
[oracle@foxjin3 20250106-23:43:37]:ORAFOX:[/oramedia/19.20]
$ cd $ORACLE_HOME/OPatch
[oracle@foxjin3 20250106-23:44:24]:ORAFOX:[/u01/app/oracle/product/19c/dbhome_1/OPatch]
$ ./opatch version
OPatch Version: 12.2.0.1.39

OPatch succeeded.
[oracle@foxjin3 20250106-23:44:29]:ORAFOX:[/u01/app/oracle/product/19c/dbhome_1/OPatch]</code></pre>
<h3 id="rsp-파일-찾기">.rsp 파일 찾기</h3>
<pre><code class="language-shell">[oracle@foxjin3 20250106-23:46:32]:ORAFOX:[/u01/app/oracle/product/19c/dbhome_1]
$ find ./ -name *.rsp
./network/install/netca_typ.rsp
./network/install/netca_clt.rsp
./install/response/db_install.rsp
./inventory/response/db_install.rsp
./inventory/response/oracle.server_EE.rsp
./assistants/dbca/dbca.rsp
./assistants/netca/netca.rsp


&gt;&gt; 해당 파일 특정 경로에 복사
[oracle@foxjin3 20250106-23:48:27]:ORAFOX:[/u01/app/oracle/product/19c/dbhome_1]
$ cp ./install/response/db_install.rsp /oramedia

[oracle@foxjin3 20250106-23:48:27]:ORAFOX:[/u01/app/oracle/product/19c/dbhome_1]
$ scp /oramedia/db_install.rsp root@192.168.0.120:/oramedia
The authenticity of host '192.168.0.120 (192.168.0.120)' can't be established.
ECDSA key fingerprint is SHA256:uhOb2gfGZe8gS+m1cQ1fzF0Q4Q/PrMxCW3btaSGEcXg.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.0.120' (ECDSA) to the list of known hosts.
root@192.168.0.120's password:
Permission denied, please try again.
root@192.168.0.120's password:
db_install.rsp                                                                                                        100%   19KB  15.7MB/s   00:00
</code></pre>
<h3 id="oracle-database-19c용-패치patch-파일-압축-풀기">Oracle Database 19c용 패치(Patch) 파일 압축 풀기</h3>
<pre><code class="language-shell">[oracle@foxjin3 20250106-23:58:57]:ORAFOX:[/oramedia/19.20]
$ ls -al
total 4896520
drwxr-xr-x. 3 oracle dba       4096 Jan  6 23:58 .
drwxr-xr-x. 4 oracle dba         62 Jan  6 23:48 ..
drwxr-xr-x. 5 oracle dba         81 Jul 16  2023 35320081
-rwxr-xr-x. 1 oracle dba  127314614 Jan  6 23:23 OJVM_p35354406_190000_Linux-x86-64.zip
-rwxr-xr-x. 1 oracle dba 2990370786 Jan  6 23:23 p35319490_190000_Linux-x86-64.zip
-rwxr-xr-x. 1 oracle dba 1769419773 Jan  6 23:56 p35320081_190000_Linux-x86-64.zip
-rwxr-xr-x. 1 oracle dba  125167420 Jan  6 23:24 p6880880_190000_Linux-x86-64.zip
-rw-rw-r--. 1 oracle dba    1749054 Jul 18  2023 PatchSearch.xml
[oracle@foxjin3 20250106-23:59:04]:ORAFOX:[/oramedia/19.20]
$ unzip p35320081_190000_Linux-x86-64.zip
</code></pre>
<h3 id="필요한-패키지-설치">필요한 패키지 설치</h3>
<pre><code class="language-shell">[oracle@foxjin3 20250107-00:00:22]:ORAFOX:[/u01/app/oracle/product/19c/dbhome_1]
$ ./runInstaller -help=y
ERROR: Unable to verify the graphical display setup. This application requires X display. Make sure that xdpyinfo exist under PATH variable.
/u01/app/oracle/product/19c/dbhome_1/perl/bin/perl: error while loading shared libraries: libnsl.so.1: cannot open shared object file: No such file or directory



-- root로 설치
[root@foxjin3 20250107-00:01:58]:ORAFOX:[/root]
$ yum install -y libnsl
Last metadata expiration check: 0:34:59 ago on Mon 06 Jan 2025 11:27:02 PM KST.
Dependencies resolved.
========================================================================================================================================================
 Package                      Architecture                 Version                                        Repository                               Size
========================================================================================================================================================
Installing:
 libnsl                       x86_64                       2.28-251.0.2.el8_10.5                          ol8_baseos_latest                       113 k

Transaction Summary
========================================================================================================================================================
Install  1 Package

Total download size: 113 k
Installed size: 97 k
Downloading Packages:
libnsl-2.28-251.0.2.el8_10.5.x86_64.rpm                                                                                 332 kB/s | 113 kB     00:00
--------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                   330 kB/s | 113 kB     00:00
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                1/1
  Installing       : libnsl-2.28-251.0.2.el8_10.5.x86_64                                                                                            1/1
  Running scriptlet: libnsl-2.28-251.0.2.el8_10.5.x86_64                                                                                            1/1
  Verifying        : libnsl-2.28-251.0.2.el8_10.5.x86_64                                                                                            1/1

Installed:
  libnsl-2.28-251.0.2.el8_10.5.x86_64

Complete!
</code></pre>
<h2 id="runinstaller--helpy">./runInstaller -help=y</h2>
<pre><code class="language-shell">[oracle@foxjin3 20250107-00:02:53]:ORAFOX:[/u01/app/oracle/product/19c/dbhome_1]
$ ./runInstaller -help=y
ERROR: Unable to verify the graphical display setup. This application requires X display. Make sure that xdpyinfo exist under PATH variable.
[INS-04007] Invalid argument passed from command line: -help=y
Usage:  runInstaller [&lt;flag&gt;] [&lt;option&gt;]
Following are the possible flags:
        -help - display help.
        -silent - run in silent mode. The inputs can be a response file or a list of command line variable value pairs.
                [-ignorePrereqFailure - ignore all prerequisite checks failures.]
        -responseFile - specify the complete path of the response file to use.
        -logLevel - enable the log of messages up to the priority level provided in this argument. Valid options are: severe, warning, info, config, fine, finer, finest.
        -executePrereqs | -executeConfigTools | -createGoldImage
        -executePrereqs - execute the prerequisite checks only.
        -executeConfigTools - execute the config tools for an installed home.
        -createGoldImage - create a gold image from the current Oracle home.
                -destinationLocation - specify the complete path to where the created gold image will be located.
                [-exclFiles - specify the complete paths to the files to be excluded from the new gold image.]
        -debug - run in debug mode.
        -printdiskusage - log the debug information for the disk usage.
        -printmemory - log the debug information for the memory usage.
        -printtime - log the debug information for the time usage.
        -waitForCompletion - wait for the completion of the installation, instead of spawning the installer and returning the console prompt.
        -noconfig - do not execute the config tools.
        -noconsole - suppress the display of messages in the console. The console is not allocated.
        -ignoreInternalDriverError - ignore any internal driver errors.
        -noCopy - perform the configuration without copying the software on to the remote nodes.
        -applyRU - apply release update to the Oracle home.
        -applyOneOffs - apply one-off patch to the Oracle home. Multiple one-off patches can be passed as a comma separated list of locations.</code></pre>
<ul>
<li>db_install.rsp 수정 후</li>
<li>$ORACLE_HOME에서 <ul>
<li><code>./runInstaller -silent -applyRU /oramedia/19.20/35320081 -responseFile /oramedia/db_install.rsp</code></li>
</ul>
</li>
</ul>
<hr />
<h3 id="관련된-패키지-설치">관련된 패키지 설치</h3>
<p>(docs 참조)</p>
<h2 id="runinstaller">./runInstaller</h2>
<pre><code class="language-shell">[oracle@foxjin3 20250107-00:39:18]:ORAFOX:[/u01/app/oracle/product/19c/dbhome_1]
$ ./runInstaller -silent -applyRU /oramedia/19.20/35320081 -responseFile /oramedia/db_install.rsp
Preparing the home to patch...
Applying the patch /oramedia/19.20/35320081...

Successfully applied the patch.
The log can be found at: /tmp/InstallActions2025-01-07_00-39-46AM/installerPatchActions_2025-01-07_00-39-46AM.log
Launching Oracle Database Setup Wizard...

[WARNING] [INS-08101] Unexpected error while executing the action at state: 'supportedOSCheck'
   CAUSE: No additional information available.
   ACTION: Contact Oracle Support Services or refer to the software manual.
   SUMMARY:
       - java.lang.NullPointerException
Moved the install session logs to:
 /u01/app/oraInventory/logs/InstallActions2025-01-07_00-39-46AM
</code></pre>
<ul>
<li>해당 에러 조치<pre><code class="language-shell"></code></pre>
</li>
</ul>
<p>$ export CV_ASSUME_DISTID=RHEL7.6</p>
<pre><code></code></pre>