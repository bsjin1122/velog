<h2 id="oracle-rac">Oracle RAC</h2>
<ul>
<li><p><strong>다중 노드 환경에서 하나의 데이터베이스를 공유하는 클러스터 데이터베이스 솔루션</strong></p>
</li>
<li><p>Oracle Database를 확장하는 것으로, 다른 서버 상에서 여러 개의 데이터베이스 인스턴스를 사용해서 data를 동시에 저장하고, 변경 및 효과적으로 조회가 가능하도록 한다</p>
</li>
<li><p>Oracle RAC는 여러 서버 이른바 클러스터 동작을 가능하게 하는 소프트웨어를 제공한다.</p>
</li>
<li><p>Database를 구성하는 데이터파일은, 클러스터에 포함되는 모든 서버로부터 Access 가능한 Shared Disk에 존재해야 한다.</p>
</li>
<li><p>Cluster 내 각 서버에서의 Oracle RAC Software가 실행된다.</p>
</li>
<li><p>RAC환경에서는 여러 개의 인스턴스에 따라 1개의 Database File에 Access 가능하다. </p>
</li>
<li><p>Instance는 다른 여러 개의 서버(Host 혹은 Node라고 불림) 위에 올라간다.</p>
</li>
<li><p>Oracle RAC는 Cache fusion을 사용해서 각 데이터베이스 인스턴스의 Buffer Cache에 저장된 데이터를 동기화한다.</p>
</li>
<li><p><code>srvctl</code></p>
</li>
</ul>
<h3 id="cache-fusion">Cache Fusion</h3>
<ul>
<li><p>Cache Fusion에서는 어떤 데이터베이스 인스턴스가 Data Block을 디스크에 쓰도록 하여 다른 데이터베이스 인스턴스에도 데이터 블록을 디스크로부터 재요청해서 읽도록 하지 않고 현재 데이터 블록(memory에 상주)을 데이터베이스 인스턴스간 이동한다. </p>
</li>
<li><p>어떤 인스턴스의 Buffer Cache에 존재하는 데이터블록이 별도의 인스턴스에서 필요하게 되면, Cache Fusion은 Inter connect를 사용해서 그 데이터 블록을 Instance간에 직접 전송한다. </p>
</li>
<li><p>그렇기 때문에, Oracle Database에서는 Data Access 및 데이터 변경을 데이터가 1개의 버퍼 캐시로 존재하는 것처럼 수행이 가능하다.</p>
</li>
</ul>
<h2 id="oracle-clusterware">Oracle Clusterware</h2>
<ul>
<li><strong>클러스터 환경을 구성하고, 관리 및 운영하는 클러스터 관리 솔루션</strong>이다.<ul>
<li>클러스터 노드 간 통신 및 조정</li>
<li>Oracle RAC의 필수 구성 요소 (RAC환경에서 노드를 관리)</li>
<li>서버 장애 감지 및 자동 복구(failover)</li>
<li>OCR 및 Voting Disk 관리</li>
<li>SCAN Listener 및 VIP 관리</li>
<li>다른 애플리케이션도 클러스터링 가능</li>
<li><code>crsctl</code></li>
</ul>
</li>
<li>Oracle Clusterware는 Oracle RAC 없이도 독립적으로 사용 가능하다.<ul>
<li>ex) Oracle ASM, 비 RAC 환경의 애플리케이션 클러스터링</li>
</ul>
</li>
<li>OS와 직접적으로 연동해서 동작하기 떄문에, 일부 Install Task에서는 System 관리자로서의 접근이 필요하게 된다. </li>
<li>또한 root유저로서 실행이 필요한 것도 있다.</li>
</ul>