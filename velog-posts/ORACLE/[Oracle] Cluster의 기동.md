<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/8d345ad3-c975-4d71-af43-deb31d337d70/image.jpg" /></p>
<ul>
<li><a href="https://docs.oracle.com/cd/F32587_01/cwadd/introduction-to-oracle-clusterware.html#GUID-46D25024-1CEF-45CC-9C5F-04B0D9416C40">그림 </a></li>
</ul>
<h2 id="oracle-clusterware의-시작-과정">Oracle Clusterware의 시작 과정</h2>
<ol>
<li><p><code>INIT</code> 프로세스가 <code>OHASD</code>를 시작하고, 이 OHASD는 <code>oraagent, orarootagent, cssdagent</code>를 차례로 시작한다.</p>
</li>
<li><p><code>oraagent</code>는 <code>mdnsd, evmd, Oracle ASM, gpnpd, gipcd(Grid IPC데몬)</code>을 시작한다.</p>
</li>
<li><p><code>orarootagent</code> 는 <code>OSYSMOND</code>를 시작하여, 일부 노드에서는 OLOGGERD도 시작할 수 있다.(그림에는 표시되지 않음)</p>
<ul>
<li>그 외에도 ctssd, CSSD Monitor, diskmon(Disk Monitor Daemon), crsd를 시작한다. </li>
<li><code>crsd</code>는 다시 또 다른 <code>oraagent</code>와 <code>orarootagent</code>를 시작한다.</li>
</ul>
</li>
<li><p><code>oraagent</code> 는 Oracle Notification Service(ONS 및 eONS), Oracle ASM 인스턴스(oraagent가 시작한 Oracle ASM과 통신), 데이터베이스 인스턴스, 리스너, SCAN 리스너를 시작한다.</p>
</li>
<li><p><code>orarootagent</code>는 <code>gnsd, VIPs, SCAN VIP 및 네트워크 리소스를 시작</code>한다.</p>
</li>
</ol>
<ul>
<li>또한 <code>orarootagent</code>는 <code>Oracle ADVM볼륨, Oracle ACFS, NFS서비스, 고가용성 NFS 서비스, 고가용성 VIP를 시작</code>한다.</li>
</ul>
<ol start="6">
<li><code>cssdagent</code>는 <strong><code>클러스터 동기화 서비스(ocssd)</code></strong>를 시작한다.</li>
</ol>
<hr />
<h2 id="crs-cluster-ready-service">CRS (Cluster Ready Service)</h2>
<ul>
<li>CRSD는 각 리소스의 ocr에 저장되어있는 구성정보에 기반하여 cluster resource를 관리한다.</li>
<li>여기에는 기동, 정지, 감시 및 failover 조작 등이 포함되어 있다.</li>
<li>crs 프로세스는 resource의 상태가 변경되변 이벤트를 생성한다. </li>
<li>oracle rac가 설치되어 있는 경우, CRSD 프로세스는 Oracle Database instance나 listener 등을 감시하여, 장애가 발생되었을 경우에 이들의 컴포넌트를 자동으로 재기동한다.</li>
</ul>
<h2 id="cluster-synchronization-services-css">Cluster Synchronization Services (CSS)</h2>
<ul>
<li>Cluster의 memebership을 관리하여, node가 cluster에 대해 추가 혹은 삭제될 때 member에 알림하는 것에 의해, 클러스터 구성을 관리한다.</li>
<li>보증된 3rd part 클러스터웨어를 사용하는 경우, css 프로세스는 clusterware와 같이 동작하여, node의 membership에 관한 정보를 관리한다.</li>
</ul>
<h3 id="cssdagent-프로세스">cssdagent 프로세스</h3>
<ul>
<li>클러스터의 감시 및 I/O 펜싱을 실행한다.</li>
<li>이전에는 oprocd에 의해 제공되어 있었다. cssd 장애가 나면, Oracle Clusterware에서 노드가 재기동 되는 경우가 있다.</li>
</ul>
<h2 id="ctss-cluster-time-synchronization-service">CTSS (Cluster Time Synchronization Service)</h2>
<ul>
<li>Oracle CLusterware의 클러스터에서 시간관리가 제공된다.</li>
</ul>
<h2 id="evm-event-management">EVM (Event Management)</h2>
<ul>
<li>Oracle Clusterware에 의해 만들어진 이벤트를 발행하는 background process</li>
</ul>
<h2 id="gns-grid-naming-service">GNS (Grid Naming Service)</h2>
<ul>
<li>외부 dns 서버로부터 송신된 request를 처리하고, cluster에서 정의된 네이밍을 수행한다.</li>
</ul>
<h2 id="oracle-agent-oraagent">Oracle Agent (oraagent)</h2>
<ul>
<li>Clusterware를 확장하여, Oracle 고유의 요건 및 복잡한 resource를 support한다. 이 프로세스는, FAN 이벤트가 발생할 경우 server call out script를 실행한다. </li>
<li>이 프로세스는 Oracle Clusterware 11g 에서는 RACG 로 불려져있었다.</li>
</ul>
<h2 id="ons-oracle-notification-service">ONS (Oracle Notification Service)</h2>
<ul>
<li>Fast Application Notification(FAN) 이벤트 통신하기 위한 게시 및 구독 서비스</li>
</ul>
<h2 id="orarootagent-oracle-root-agent">orarootagent (Oracle Root Agent)</h2>
<ul>
<li>root가 소유하고 있는 네트워크나 Grid 가상 ip address등 resource를 CRSD가 관리하는 것을 지원하는 전용의 oraagent 프로세스. </li>
</ul>
<blockquote>
<p>CSS, EVM 및 ONS 컴포넌트는 같은 cluster database 환경에서, 다른 노드의 cluster component layer와 통신한다.</p>
</blockquote>
<ul>
<li>또한, 이러한 컴포넌트들은 Oracle Database, application 및 Oracle Clusterware의 고가용성 컴포넌트간에 주요 통신 링크이다.</li>
<li>게다가 이러한 background process는, database 조작 감시 및 관리한다. </li>
</ul>
<h2 id="osysmond-system-moritoring-service">osysmond (System moritoring Service)</h2>
<ul>
<li>감시하고, Data를 Cluster log 출력 서비스에 송신하는 Operating System Matrix를 수집하는 서비스. 이 서비스는 Cluster 내의 모든 노드에서 실행된다.</li>
</ul>
<h2 id="gpnpd-grid-plug-and-play">GPNPD (Grid Plug and Play)</h2>
<ul>
<li>Grid Plug and Play Profile로의 access를 제공하고, cluster node간에서 Profile의 update를 조정하여 모든 노드에서 최신의 profile이 유지될 수 있도록 한다.</li>
</ul>
<h2 id="gipc-grid-interprocess-communication">GIPC (Grid Interprocess Communication)</h2>
<ul>
<li>긴 inter connect를 사용 가능하게 하는 support daemon</li>
</ul>
<h2 id="multicast-domain-naming-service">Multicast Domain Naming Service</h2>
<ul>
<li>Cluster내 Profile을 특정하기 위해 Grid Plug and Play에 의해 사용되어, Naming을 실행하기 위해 GNS에 의해 사용된다.</li>
<li>mDNS 프로세스는 Linux, UNIX 및 Windows의 Background Process이다.</li>
</ul>
<hr />
<h2 id="clusterware에서-component-daemon-process의-역할">Clusterware에서 Component, Daemon, Process의 역할</h2>
<h3 id="1-컴포넌트">1. 컴포넌트</h3>
<ul>
<li>CRS, CSS, CTSS, GNS 등은 Oracle Clusterware의 주요 컴포넌트이다.</li>
<li>이들 컴포넌트는 클러스터의 전체적인 동작을 지원하며, 각각의 역할을 분담하여 클러스터의 안정성과 고가용성을 보장</li>
</ul>
<h3 id="2-데몬daemon">2. 데몬(Daemon)</h3>
<ul>
<li>CRSD, cssd, oraagent, EVM 등의 데몬은 백그라운드에서 지속적으로 실행되며, 클러스터 리소스를 관리하고 이벤트를 발생시키거나 상태 감시를 한다.</li>
<li>이들은 주기적으로/이벤트 기반으로 동작하여 클러스터를 모니터링하고, 필요한 동작을 실행한다.</li>
</ul>
<h3 id="3-프로세스process">3. 프로세스(Process)</h3>
<ul>
<li>각 데몬은 특정한 프로세스로 실행된다.</li>
<li>ex) oraagent는 Oracle 고유 리소스 관리를 위한 프로세스이며, ons는 이벤트 통신을 위한 프로세스로 작동한다.</li>
<li>이러한 프로세스들은 서비스 상태를 지속적으로 모니터링하며, 복구 작업을 수행한다.</li>
</ul>