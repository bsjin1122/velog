<h2 id="gui">gui</h2>
<ul>
<li><a href="https://www.oracle.com/jp/a/tech/docs/technical-resources/19c-racdb-installationguide.pdf">RAC설치</a></li>
<li><a href="https://docs.oracle.com/cd/F19136_01/rilin.pdf">19c rac 설치 가이드</a></li>
</ul>
<pre><code class="language-shell"># xhost +
# su - grid
$ export DISPLAY=:0.0
엔진 설치 --&gt; $ORACLE_HOME 
[grid@cowjin1 20250211-19:01:13]:+ASM1:[/oramedia]
$ unzip p35319490_190000_Linux-x86-64.zip -d $ORACLE_HOME ---&gt; RU 압축풀기
Opatch 패치 
gridsetup.sh -applyRU RU압축푼장소 지정

# xhost +
# su - grid
$ export DISPLAY=:0.0
-- $ORACLE_HOME에서 ./gridSetup.sh -applyRU /oramedia/35319490
</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/51e0e4b1-f8ef-4d7a-9c1a-298a39b6fa4e/image.png" /></p>
<ul>
<li>✅ <strong>Configure Oracle Grid Infrastructure for a New Cluster</strong><ul>
<li>다중 노드(2개 이상의 서버)로 구성된 클러스터 환경</li>
<li>CRS, ASM, GNS, SCAN 등을 포함</li>
</ul>
</li>
<li>Configure Oracle Grid Infrastructure for a Standalone Server (Oracle Restart)<ul>
<li>단일 인스턴스 환경, RAC가 아닌 Standalone 서버(싱글 노드)에서 ASM 제공하기 위해 Grid Infrastructure 설정하는 과정</li>
</ul>
</li>
<li>Upgrade Oracle Grid Infrastructure</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/3f5138fd-2d0a-490b-97fc-aeec8616175e/image.png" /></p>
<ul>
<li>✅ <strong>Configure an Oracle Standalone Cluster</strong></li>
<li>Configure an Oracle Domain Services Cluster</li>
<li>Configure an Oracle Member Cluster for Oracle Databases</li>
<li>Configure an Oracle Member Cluster for Applications</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/3d535626-f3eb-4b9e-9240-c7d54d7242dc/image.png" /></p>
<ul>
<li><p>Cluster명, Scan명, SCAN Port를 입력. SCAN명에는 사전에 DNS에 등록했던 이름을 입력한다.</p>
</li>
<li><p>GNS사용한 동적 IP 주소 할당</p>
<ul>
<li>이 옵션을 선택한 경우, 네트워크 관리자는 GNS(표준 혹은 멀티 클러스터)에 따라 정해지도록 sub domain을 위임한다.</li>
</ul>
</li>
<li><p>정적 IP주소 할당</p>
<ul>
<li>이 옵션을 선택하면, 네트워크 관리자는 고정IP 주소를 클러스터 각 물리 호스트명과 Oracle Clusterware관리 VIP에 할당한다. 또한 DNS에 기반한 정적 name resolution이 각 노드에 할당된다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/3573eda5-6bb0-44b4-9658-f4d977867433/image.png" />
<img alt="" src="https://velog.velcdn.com/images/greendev/post/0c7ca1c7-066b-4374-8a74-41b40832282e/image.png" /></p>
</li>
</ul>
<blockquote>
<ul>
<li>catjin2</li>
</ul>
</blockquote>
<ul>
<li>catjin2-vip</li>
</ul>
<pre><code>1,2 호기
[root@cowjin1 ~]# passwd grid
Changing password for user grid.
New password:
Retype new password:
passwd: all authentication tokens updated successfully.
</code></pre><p><img alt="" src="https://velog.velcdn.com/images/greendev/post/69cbd8a8-8c55-4b00-826e-6b68b4ceb571/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/848d68dd-39e9-4a87-9c52-d64f0d00dc4f/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/57bce343-7680-4901-9fbf-dc6075afe3da/image.png" /></p>
<pre><code class="language-shell">-- 테스트용으로 4개 만들었는데 보통은 하나만 사용한다
10.10.0.1   cowjin-priv1
10.10.0.2   catjin-priv1
20.20.0.1   cowjin-priv2
20.20.0.2   catjin-priv2
30.30.0.1   cowjin-priv3
30.30.0.2   catjin-priv3
40.40.40.1  cowjin-priv4
40.40.40.2  catjin-priv4</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/5498509a-faa7-435e-9d6f-a987a3214ac0/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/bc61838c-87b2-4e4f-a5fc-fac76d3c8530/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/1eab7c34-a519-4b4f-906e-5f7761365313/image.png" /></p>
<ul>
<li>RAC 성능정보 분석하는 DB를 만들 것인지 선택항목으로, no</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/cd6fde9f-05da-4138-a1ff-44ad37608149/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/fef3e09b-e8a0-4ef6-8345-7958219c64e5/image.png" /></p>
<p>이렇게 구성하려고 함..! </p>
<blockquote>
<ul>
<li>External : 복제x</li>
</ul>
</blockquote>
<ul>
<li>normal: 이중화<ul>
<li>normal일 때 Failure Group: 스토리지 내 같은 LUN에 이중화가 되어 있는데, 이를 다른 LUN에 이중화 구성할 수 있도록 명시적으로 경로를 지정해준다.
<img alt="" src="https://velog.velcdn.com/images/greendev/post/48beadd2-7ab2-4e00-9f14-d258a17ebf38/image.png" /></li>
</ul>
</li>
<li>High: 삼중화</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/35bc37ff-23b7-49fe-9c7b-37c8fee7885a/image.png" /></p>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/7d07a291-168c-4081-98ff-d991d28d9779/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/5a6544a0-1095-422d-b826-51d841d46776/image.png" /></p>
<h3 id="ipmi"><a href="https://docs.oracle.com/cd/E40704_01/html/E40350/z400000c1396369.html#scrolltoc">IPMI</a></h3>
<blockquote>
<p>DB는 <strong>데이터 정합성</strong> </p>
</blockquote>
<ul>
<li>Self Check / Disk Misscount / Inter connect --&gt; 장애 요인 3가지</li>
<li>zombie처럼 process가 증가하는 경우 / memory나 os가 응답이ㅣ 없어서 서버를 재부팅 해야 하는 경우 
=&gt; ocssd, ohasd가 os를 재기동하는데 process다보니까 os재기동 명령어가 정상적으로 수행되지 않을 때도 있음<blockquote>
<p>IPMI를 사용하면 h/w 자체의 기능을 이용해서 서버를 제어 가능함</p>
</blockquote>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/ad6fbbdb-d378-4278-bc4f-564d27279e19/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/384c7247-c30a-4a53-ae40-012ff9ddacd8/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/37459e11-db48-428f-9f80-c4a99a1d6bdd/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/6ce42825-35f0-4b55-b742-e6a8a61b349f/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/8bcd2771-95cd-45b5-9f90-e74c310f923c/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/3d66ac0b-2255-4ac3-ad60-63d72efca0b3/image.png" /></p>
<pre><code>[root@catjin2 ~]# sh /tmp/GridSetupActions2025-02-13_06-42-21PM/CVU_19_grid_2025-02-13_18-44-20_337240/runfixup.sh
All Fix-up operations were completed successfully.

[root@cowjin1 ~]# sh /tmp/GridSetupActions2025-02-13_06-42-21PM/CVU_19_grid_2025-02-13_18-44-20_337240/runfixup.sh
All Fix-up operations were completed successfully.
[root@cowjin1 ~]#
</code></pre><p><img alt="" src="https://velog.velcdn.com/images/greendev/post/702e1084-afbd-47dc-b512-15f734e769ff/image.png" />
<img alt="" src="https://velog.velcdn.com/images/greendev/post/17ac615a-11a8-4891-a821-79fda1a0cacf/image.png" />
<img alt="" src="https://velog.velcdn.com/images/greendev/post/f09eb671-2e1b-4efc-b500-a4a90ebd0201/image.png" />
<img alt="" src="https://velog.velcdn.com/images/greendev/post/583e24e8-cf4b-49ad-8a30-8cb47a9cb675/image.png" />
<img alt="" src="https://velog.velcdn.com/images/greendev/post/f2021d42-ef29-483c-ae5a-2a7ce855fc49/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/c33299b1-2caf-4a0b-9431-0fae1443d276/image.png" /></p>
<ol>
<li>root로 접속</li>
<li>script 수행</li>
<li>스크립트 하나당 노드 하나씩, 그 다음 노드 수행 -&gt; 다음 스크립트 실행</li>
<li>OK 버튼 클릭 </li>
</ol>
<h3 id="1-orainstrootsh">1. orainstRoot.sh</h3>
<pre><code class="language-shell">1. orainstRoot.sh
#node 1
[root@cowjin1 oraInventory]# sh orainstRoot.sh
Changing permissions of /u01/app/oraInventory.
Adding read,write permissions for group.
Removing read,write,execute permissions for world.

Changing groupname of /u01/app/oraInventory to dba.
The execution of the script is complete.

#node 2
[root@catjin2 oraInventory]# ls
ContentsXML  logs  oraInst.loc  orainstRoot.sh
[root@catjin2 oraInventory]# sh orainstRoot.sh
Changing permissions of /u01/app/oraInventory.
Adding read,write permissions for group.
Removing read,write,execute permissions for world.

Changing groupname of /u01/app/oraInventory to dba.
The execution of the script is complete.</code></pre>
<h3 id="2-rootsh">2. root.sh</h3>
<pre><code class="language-shell">#node 1
Using configuration parameter file: /u01/app/oracle/product/19c/gridhome_1/crs/install/crsconfig_params
The log of current session can be found at:
  /u01/app/base/crsdata/cowjin1/crsconfig/rootcrs_cowjin1_2025-02-17_11-32-25PM.log
2025/02/17 23:32:31 CLSRSC-594: Executing installation step 1 of 19: 'ValidateEnv'.
2025/02/17 23:32:31 CLSRSC-594: Executing installation step 2 of 19: 'CheckFirstNode'.
2025/02/17 23:32:33 CLSRSC-594: Executing installation step 3 of 19: 'GenSiteGUIDs'.
2025/02/17 23:32:33 CLSRSC-594: Executing installation step 4 of 19: 'SetupOSD'.
Redirecting to /bin/systemctl restart rsyslog.service
2025/02/17 23:32:34 CLSRSC-594: Executing installation step 5 of 19: 'CheckCRSConfig'.
2025/02/17 23:32:34 CLSRSC-594: Executing installation step 6 of 19: 'SetupLocalGPNP'.
2025/02/17 23:32:41 CLSRSC-594: Executing installation step 7 of 19: 'CreateRootCert'.
2025/02/17 23:32:44 CLSRSC-594: Executing installation step 8 of 19: 'ConfigOLR'.
2025/02/17 23:32:58 CLSRSC-594: Executing installation step 9 of 19: 'ConfigCHMOS'.
2025/02/17 23:32:58 CLSRSC-594: Executing installation step 10 of 19: 'CreateOHASD'.
2025/02/17 23:33:02 CLSRSC-594: Executing installation step 11 of 19: 'ConfigOHASD'.
2025/02/17 23:33:02 CLSRSC-330: Adding Clusterware entries to file 'oracle-ohasd.service'
2025/02/17 23:33:21 CLSRSC-594: Executing installation step 12 of 19: 'SetupTFA'.
2025/02/17 23:33:21 CLSRSC-594: Executing installation step 13 of 19: 'InstallAFD'.
2025/02/17 23:33:22 CLSRSC-594: Executing installation step 14 of 19: 'InstallACFS'.
2025/02/17 23:33:47 CLSRSC-594: Executing installation step 15 of 19: 'InstallKA'.
2025/02/17 23:33:51 CLSRSC-594: Executing installation step 16 of 19: 'InitConfig'.
2025/02/17 23:33:22 CLSRSC-594: Executing installation step 14 of 19: 'InstallACFS'.
2025/02/17 23:33:47 CLSRSC-594: Executing installation step 15 of 19: 'InstallKA'.
2025/02/17 23:33:51 CLSRSC-594: Executing installation step 16 of 19: 'InitConfig'.

ASM has been created and started successfully.

[DBT-30001] Disk groups created successfully. Check /u01/app/base/cfgtoollogs/asmca/asmca-250217PM113420.log for details.

2025/02/17 23:34:58 CLSRSC-482: Running command: '/u01/app/oracle/product/19c/gridhome_1/bin/ocrconfig -upgrade grid dba'
CRS-4256: Updating the profile
Successful addition of voting disk e470e08d1a634fb6bf789a16d97a05cf.
Successfully replaced voting disk group with +OCRVOTE.
CRS-4256: Updating the profile
CRS-4266: Voting file(s) successfully replaced
##  STATE    File Universal Id                File Name Disk group
--  -----    -----------------                --------- ---------
 1. ONLINE   e470e08d1a634fb6bf789a16d97a05cf (ORCL:OCRVOTING02) [OCRVOTE]
Located 1 voting disk(s).
2025/02/17 23:35:44 CLSRSC-594: Executing installation step 17 of 19: 'StartCluster'.
2025/02/17 23:36:09 CLSRSC-4002: Successfully installed Oracle Trace File Analyzer (TFA) Collector.
2025/02/17 23:36:42 CLSRSC-343: Successfully started Oracle Clusterware stack
2025/02/17 23:36:42 CLSRSC-594: Executing installation step 18 of 19: 'ConfigNode'.
2025/02/17 23:37:29 CLSRSC-594: Executing installation step 19 of 19: 'PostConfig'.
2025/02/17 23:37:44 CLSRSC-325: Configure Oracle Grid Infrastructure for a Cluster ... succeeded



# node 2
[root@catjin2 gridhome_1]# sh root.sh
Performing root user operation.

The following environment variables are set as:
    ORACLE_OWNER= grid
    ORACLE_HOME=  /u01/app/oracle/product/19c/gridhome_1

Enter the full pathname of the local bin directory: [/usr/local/bin]:
The contents of &quot;dbhome&quot; have not changed. No need to overwrite.
The contents of &quot;oraenv&quot; have not changed. No need to overwrite.
The contents of &quot;coraenv&quot; have not changed. No need to overwrite.


Creating /etc/oratab file...
Entries will be added to the /etc/oratab file as needed by
Database Configuration Assistant when a database is created
Finished running generic part of root script.
Now product-specific root actions will be performed.
Relinking oracle with rac_on option
Using configuration parameter file: /u01/app/oracle/product/19c/gridhome_1/crs/install/crsconfig_params
The log of current session can be found at:
  /u01/app/base/crsdata/catjin2/crsconfig/rootcrs_catjin2_2025-02-17_11-40-28PM.log
2025/02/17 23:40:32 CLSRSC-594: Executing installation step 1 of 19: 'ValidateEnv'.
2025/02/17 23:40:32 CLSRSC-594: Executing installation step 2 of 19: 'CheckFirstNode'.
2025/02/17 23:40:33 CLSRSC-594: Executing installation step 3 of 19: 'GenSiteGUIDs'.
2025/02/17 23:40:33 CLSRSC-594: Executing installation step 4 of 19: 'SetupOSD'.
Redirecting to /bin/systemctl restart rsyslog.service
2025/02/17 23:40:34 CLSRSC-594: Executing installation step 5 of 19: 'CheckCRSConfig'.
2025/02/17 23:40:35 CLSRSC-594: Executing installation step 6 of 19: 'SetupLocalGPNP'.
2025/02/17 23:40:36 CLSRSC-594: Executing installation step 7 of 19: 'CreateRootCert'.
2025/02/17 23:40:36 CLSRSC-594: Executing installation step 8 of 19: 'ConfigOLR'.
2025/02/17 23:40:46 CLSRSC-594: Executing installation step 9 of 19: 'ConfigCHMOS'.
2025/02/17 23:40:46 CLSRSC-594: Executing installation step 10 of 19: 'CreateOHASD'.
2025/02/17 23:40:47 CLSRSC-594: Executing installation step 11 of 19: 'ConfigOHASD'.
2025/02/17 23:40:47 CLSRSC-330: Adding Clusterware entries to file 'oracle-ohasd.service'
2025/02/17 23:41:16 CLSRSC-594: Executing installation step 12 of 19: 'SetupTFA'.
2025/02/17 23:41:16 CLSRSC-594: Executing installation step 13 of 19: 'InstallAFD'.
2025/02/17 23:41:16 CLSRSC-594: Executing installation step 14 of 19: 'InstallACFS'.
2025/02/17 23:42:42 CLSRSC-594: Executing installation step 15 of 19: 'InstallKA'.
2025/02/17 23:42:43 CLSRSC-594: Executing installation step 16 of 19: 'InitConfig'.
2025/02/17 23:42:51 CLSRSC-594: Executing installation step 17 of 19: 'StartCluster'.
2025/02/17 23:43:51 CLSRSC-343: Successfully started Oracle Clusterware stack
2025/02/17 23:43:51 CLSRSC-594: Executing installation step 18 of 19: 'ConfigNode'.
2025/02/17 23:44:04 CLSRSC-594: Executing installation step 19 of 19: 'PostConfig'.
2025/02/17 23:44:08 CLSRSC-325: Configure Oracle Grid Infrastructure for a Cluster ... succeeded</code></pre>