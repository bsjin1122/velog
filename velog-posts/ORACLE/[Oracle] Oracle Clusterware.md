<blockquote>
<ul>
<li><a href="https://www.oracle.com/technetwork/jp/ondemand/branch/20130821-rac-1998356-ja.pdf">PPT: &quot;RAC&quot;를 숙달하자! 기본부터 최신 기능까지(oracle 11g)</a></li>
</ul>
</blockquote>
<ul>
<li><a href="https://docs.oracle.com/en/database/oracle/oracle-database/21/cwadd/introduction-to-oracle-clusterware.html#GUID-7612C5C2-AC7C-4311-97B2-CF189268969A">그림: Clusterware Administration and Deployment Guide</a></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/9eb4a9b6-0394-456a-a25b-130ca802dcfe/image.png" /></p>
<h2 id="oracle-clusterware">Oracle Clusterware</h2>
<ul>
<li>여러 개 의 서버를 1개의 서버인 것처럼 연결시켜주는 software</li>
<li>RAC를 구성하는 component로서 Oracle 10g release</li>
<li><strong>역할</strong>: instance와의 통신을 수행하며, 장애를 감지</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/b5481f37-8959-47c4-911d-29851d6b6d1a/image.png" /></p>
<h2 id="3개-주요-컴포넌트-및-데몬">3개 주요 컴포넌트 (및 데몬)</h2>
<h3 id="crs-cluster-ready-service">CRS (Cluster Ready Service)</h3>
<ul>
<li>노드간 장애는 crs가 감지</li>
<li>고가용성, workload 관리</li>
<li>리소스 감시, 정지, 기동</li>
<li>클러스터 리소스의 기동, 정지, 감시 및 failover를 행함</li>
<li>장애를 감지하면, resource 재기동을 수행함</li>
</ul>
<blockquote>
<p>** CRS가 관리하는 리소스들**</p>
</blockquote>
<ul>
<li>Oracle Database </li>
<li>Oracle Instance</li>
<li>Oracle Listener</li>
<li>Service</li>
<li>ASM Instance</li>
<li>가상 IP address</li>
<li>ONS</li>
<li>GSD (Global Service Daemon); Oracle 데이터베이스에서 클러스터 데이터베이스의 노드를 관리하기 위해 사용되는 서비스</li>
</ul>
<h3 id="css-cluster-synchronization-services">CSS (Cluster Synchronization Services)</h3>
<ul>
<li>inter connect 장애, storage path 장애는 css가 감지</li>
<li>멤버십 정보 관리: 신규 노드 추가 및 삭제</li>
<li>private interconnect 상에서 heart beat 통신을 수행, 장애를 감지<ul>
<li>node 장애, interconnect 장애, storage path 장애 등
<img alt="" src="https://velog.velcdn.com/images/greendev/post/492113af-d6dc-4e12-912e-de32550eb19b/image.png" /></li>
</ul>
</li>
<li>oclsomon, oprocd --&gt; 더 이상 사용되지 않음</li>
</ul>
<h4 id="css에-의한-노드간-장애-시-감지-예시">CSS에 의한 노드간 장애 시 감지 예시</h4>
<ul>
<li>heart beat를 통한 감시<ul>
<li>voting disk의 타임 아웃: disktimeout (초)<ul>
<li><code>crsctl get css disktimeout</code></li>
</ul>
</li>
<li>network 통신의 타임 아웃: misscount (초)<ul>
<li><code>crsctl get css misscount</code></li>
</ul>
</li>
</ul>
</li>
<li>heartbeat 감시가 타임아웃되면, node 배제하는 절차로 진행됨</li>
<li>노드간 장애 발생 시의 문제: Split Brain<ul>
<li>정합성이 지켜지지 않는 문제 (동시에 read/write 수행 시)</li>
</ul>
</li>
<li>Split Brain 의 해결<ul>
<li>Voting Disk에 자신이 접속 가능한 노드임을 등록</li>
<li>가장 많이 연결된 노드 그룹으로 클러스터를 재구성</li>
</ul>
</li>
<li>Instance Recovery 시작<ul>
<li>정상인 노드가 장애 노드의 redo로그 파일 및 undo 테이블스페이스에 접근하여 recovery를 실행<ul>
<li>각각의 인스턴스별로 전용 redo log file, undo tablespace를 가짐</li>
</ul>
</li>
<li>1st pass long read
: 장애가 일어난 인스턴스의 redo로그를 읽음, 복구에 필요한 블록 이외는 사용 가능하도록 됨.</li>
<li>2nd pass long read
: 실제로 recovery가 실시되어, recovery를 행한 block으로부터 사용 가능한 상태로 복구</li>
</ul>
</li>
</ul>
<h2 id="배제할-노드의-결정">배제할 노드의 결정</h2>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/b0fcae5d-17fa-4627-9b96-075acb4fa2ca/image.png" /></p>
<ul>
<li>voting disk를 통해서, sub cluster를 파악</li>
<li>node 수가 최대 서브 클러스터에 속하는 노드가 생존, 속하지 않은 노드가 배제</li>
<li>subcluster에 속하는 노드 수가 동일한 경우에는, node 번호가 최신인 노드가 속한 sub cluster가 생존, 그 외에는 배제 </li>
</ul>
<h3 id="evm-event-manager">EVM (Event Manager)</h3>
<ul>
<li>application 에 대한 이벤트 전송
<img alt="" src="https://velog.velcdn.com/images/greendev/post/23739e59-f96d-42e8-afb0-7dcaeea2e49c/image.png" /></li>
<li>Fast Connection Failover : Application이 정상적인 노드와 재접속할 수 있도록 함</li>
<li>Fast Application Notification: Instance가 다운된 것을 알림<ul>
<li>가동중인 서버로의 재접속</li>
</ul>
</li>
</ul>
<h2 id="2개의-공유-디스크-영역">2개의 공유 디스크 영역</h2>
<h3 id="ocr-oracle-cluster-registry">OCR (Oracle Cluster Registry)</h3>
<ul>
<li>클러스터 구성 정보 저장<h3 id="voting-disk">Voting Disk</h3>
</li>
<li>Split Brain 시 이용하는 영역</li>
</ul>
<hr />
<h2 id="용어">용어</h2>
<h3 id="server-pool">Server Pool</h3>
<ul>
<li><p><strong>Server Pool</strong>: server resource의 최적화를 가능하게 하는 인프라</p>
<ul>
<li>Cluster 밑단의 서버를 server group으로 그룹화</li>
<li>어느 서버 group에도 속하지 않는 서버는 free 그룹으로 배치</li>
<li>서버의 할당은 정책에 따른다.<ul>
<li>server 수(최소, 최대), 중요도</li>
</ul>
</li>
<li>RAC 데이터베이스나 application을 server pool에 배치</li>
</ul>
</li>
<li><p><strong>Single Client Access Name(SCAN)</strong>: 동적 인프라에 대응한 접속 방식</p>
</li>
<li><p><strong>Grid Plug and Play(GPnP)</strong>: 네트워크 고유의 설정을 배제한 도메인의 구축</p>
</li>
<li><p><strong>Oracle ASM Cluster File System(ACFS)</strong>: 어느 서버 상에서도 접근 가능한 filesystem</p>
</li>
</ul>
<h2 id="manualpolicy-management">Manual/Policy Management</h2>
<h3 id="manual-management">Manual Management</h3>
<ul>
<li>RAC 데이터베이스가 기동하는 서버를 고정한 database</li>
</ul>
<h3 id="policy-management">Policy Management</h3>
<ul>
<li>server pool의 policy에 따라 유연하게 관리가 가능한 rac database</li>
<li>노드 추가 시 필요한 영역(redo log, file등) 자동으로 생성됨</li>
<li>GPnP</li>
</ul>
<h2 id="service-기본-구성">Service 기본 구성</h2>
<ul>
<li>Rac에 접속하는 application을 service라는 단위로 관리<ul>
<li>부하분산이나 workload관리를 목적으로서 oracle 10g 부터 도입
```sql</li>
</ul>
</li>
<li>--&gt; n2에만 설정
SQL&gt; show parameter service_names</li>
</ul>
<p>NAME                                 TYPE        VALUE</p>
<hr />
<p>service_names                        string      ORACOW,ORAJIN,ORASEO
SQL&gt; show spparameter service_names</p>
<p>SID      NAME                          TYPE        VALUE</p>
<hr />
<ul>
<li>service_names                 string      ORACOW,ORAJIN
ORACOW2  service_names                 string      ORACOW,ORAJIN,ORASEO</li>
</ul>
<p>grid 계정에서 lsnrctl status 로 확인 했을 때 * &lt;&lt; 에서는 n1, n2 공통으로 확인되는 부분, </p>
<p>SQL&gt; alter system set service_names = 'ORACOW,ORAJIN,ORASEO' scope=both sid='ORACOW2';</p>
<p>System altered.
---&gt; ORACOW2에만 지정했을 경우에 확인되는 ORASEO</p>
<pre><code>
## SCAN (Single Client Access Name)
- Cluster에 access 할 경우의 단일 alias
- Client/Server 접속 설정의 복잡도를 제거 
  - failover, road balance 기능을 설정
  - node 추가, 삭제 시의 설정 변경 
- **LOCAL NAMING**: `sqlplus scott/tiger@ORCL`
- **EZCONNECT**: `sqlplus scott/tiger@SCAN명:1521/서비스명`
![](https://velog.velcdn.com/images/greendev/post/b50b0163-d994-4fba-8d0d-0ef1e5f3a650/image.png)

&gt; **SCAN 명**: port번호, 서비스명
&gt; - 자동으로 접속 시 failover, loadbalance를 실행
&gt; - node 추가 / 삭제 시에도 설정 변경은 불가
- 물리적인 서버에 의존하지 않는 접속

![](https://velog.velcdn.com/images/greendev/post/2794f938-fe1a-4f58-a4c4-bcbfc5d340a6/image.png)
- 하나의 alias로 access 가능
- 서비스가 어느 한 쪽 서버에 배치되어 있어도, 같은 설정으로 접속이 가능
- tnsnames.ora: scan명, port번호, service명 -&gt; 항상 하나의 scan명으로  접속 가능
  - SCAN이 각 서비스로의 접속을 자동적으로 REDIRECT

## SCAN을 사용하여 접속한 경우의 이점
![](https://velog.velcdn.com/images/greendev/post/da06fbb4-ca3b-47ee-af77-ccf45ee7f3d4/image.png)

&gt; 1. 자동으로 접속 시 failover (명시적인 설정은 불필요)
2. RAC 인스턴스간에 자동적으로 분산하여 접속 (server side load balancing)
3. DNS Server와 연계하여 node 추가, 삭제 시에도 client 서버의 접속 설정의 변경은 불필요함


```sql
MYDB =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = scan.example.com)(PORT = 1521)) -- HOST: SCAN명을 사용하여 연결
    ) -- PORT: SCAN 리스너가 사용하는 포트
    (CONNECT_DATA =
      (SERVICE_NAME = myservice) -- SCAN을 통해 연결할 서비스
    )
  )
</code></pre><h2 id="grid-plug-and-play-gpnp">Grid Plug and Play (GPnP)</h2>
<ul>
<li><strong>노드 고유의 설정을 배제하는 것으로, cluster 구성의 변경이나 관리를 용이하게 함</strong></li>
<li>노드의 추가, 삭제 시 수동조작의 배제<ul>
<li>human error의 방지</li>
<li>보다 대규모의 cluster 구성 시에 용이하게 사용됨<h3 id="gpnp의-구성-요소">GPnP의 구성 요소</h3>
<blockquote>
<ul>
<li>Dynamic Host Configuration Protocol (<em><strong>DHCP</strong></em>)의 support</li>
</ul>
</blockquote>
</li>
</ul>
</li>
<li>Single Client Access Name (SCAN)</li>
<li>Grid Naming Service (GNS)<ul>
<li>cluster의 node명, scan명, vip를 동적으로 관리</li>
<li>dhcp 서버와 통합하여 ip address 할당하는 것을 자동화</li>
<li>client 접속관리를 간소화하여, network 구성 변경 시의 영향을 최소화함</li>
</ul>
</li>
</ul>
<p><em><strong>DHCP</strong></em></p>
<ul>
<li><p>네트워크에 접속하는 클라이언트 장치(PC, 스마트폰, 서버 등)에 자동으로 IP 주소와 네트워크 설정을 할당하는 프로토콜</p>
</li>
<li><p>수동으로 네트워크 설정을 입력하는 Static IP(고정 IP) 방식과 달리, DHCP를 사용하면 IP 주소를 자동으로 할당하고, 중복 충돌을 방지</p>
</li>
</ul>
<h2 id="acfs-oracle-asm-cluster-file-system">ACFS (Oracle ASM Cluster File System)</h2>
<ul>
<li>확장성에 우수한 범용적인 file system<ul>
<li>일반 파일 시스템처럼 사용가능: OS에서 마운트하여 일반적인 파일, 로그, 백업 파일 등을 저장 가능</li>
</ul>
</li>
<li>RAC 환경에서 파일 공유 및 데이터 저장소 역할</li>
<li>NAS 프로토콜(NFS, CIFS)에서의 접속 가능<ul>
<li>NAS처럼 원격에서 접근 가능 &lt;&lt; ?? </li>
</ul>
</li>
<li>ACFS Snapshot 기능 : 과거 데이터 복구 및 백업 지원<ul>
<li>특정 시점의 파일 시스템 상태를 읽기 전용(또는 읽기/쓰기 가능)으로 캡쳐하여 저장하는 기능</li>
<li>변경된 블록만 저장(효율적)</li>
</ul>
</li>
</ul>
<ul>
<li>TDE(Transparent Data Encryption)지원: 파일 시스템 단위에서 데이터 암호화 가능</li>
</ul>
<pre><code class="language-text">┌──────────────────────────────────┐
│       ACFS 파일 시스템          │
│  (Oracle ADVM을 통해 관리됨)    │
└──────────────────────────────────┘
          │
          ▼
┌───────────────────────────────────────┐
│  ASM Dynamic Volume Manager (ADVM) │ -- ASM 볼륨을 관리하는 계층
└───────────────────────────────────────┘
          │
          ▼
┌───────────────────────────────────┐
│      ASM 디스크 그룹 (DATA)      │
└───────────────────────────────────┘
</code></pre>
<h3 id="acfs-snapshot-동작-방식">ACFS Snapshot 동작 방식</h3>
<p><strong>1. ACFS 볼륨 생성</strong></p>
<pre><code class="language-sql"># ASM 디스크 그룹에서 ACFS 볼륨 생성 (50GB)
asmcmd volcreate -G DATA -s 50G acfs_vol

# ACFS 파일 시스템 생성
mkfs -t acfs /dev/asm/acfs_vol-123

# 마운트 포인트 생성
mkdir /acfs_data

# ACFS 마운트
mount -t acfs /dev/asm/acfs_vol-123 /acfs_data
</code></pre>
<p><strong>2. 스냅샷 생성</strong></p>
<pre><code class="language-sql"># 스냅샷 생성 (읽기 전용)
acfsutil snap create snap1 /acfs_data

# 읽기/쓰기 가능한 스냅샷 생성 (옵션 추가)
acfsutil snap create -w snap_rw1 /acfs_data
</code></pre>
<p><strong>3. 파일이 변경되면 스냅샷에 변경 전 데이터 저장</strong></p>
<pre><code class="language-sql"># 현재 존재하는 스냅샷 목록 확인
acfsutil snap info /acfs_data</code></pre>
<p><strong>4. 스냅샷을 통해 원래 데이터를 복구 가능</strong></p>
<pre><code class="language-sql">Snapshot Name: snap1
Snapshot ID: 12345
Creation Time: 2024-02-02 10:00:00
State: Read-Only
</code></pre>
<h2 id="data-block의-경합">Data Block의 경합</h2>
<ul>
<li><p>row수가 적은 table이나 row 길이가 짧은 table에 대해, 빈번하게 update나 select를 행하면, 전체 노드로부터 경합이 이루어진다.</p>
</li>
<li><p>application에서 사용하는 table예시</p>
<ul>
<li><p>queue에서 사용되는 table</p>
<ul>
<li>메시지 큐, 작업 대기열</li>
</ul>
</li>
<li><p>session이나 job의 상태관리 테이블</p>
<ul>
<li><p>session 상태 관리: 로그인 상태, 웹 애플리케이션의 세션 데이터</p>
</li>
<li><p>job 상태: 배치 작업의 실행 상태 </p>
</li>
</ul>
</li>
<li><p>마지막에 행한 처리를 확인하는 테이블</p>
<ul>
<li>ex) 최근 로그인 기록, 마지막 거래 내역 저장</li>
<li>최근 변경 내역이 빈번히 갱신됨</li>
</ul>
</li>
</ul>
</li>
<li><p>PCTFREE를 증가시키는 것으로, 1개 블록당 행 수를 감소시키는 것이 가능하다.</p>
</li>
</ul>
<hr />
<h2 id="pctfree-parameter">PCTFREE parameter</h2>
<ul>
<li><p>블록 내 기존의 행을 갱신할 경우에 대비하여 data block내에 빈 영역으로써 보관되는 비율을 최소치로 설정한다.</p>
</li>
<li><p>예를 들어, <code>CREATE TABLE문</code>에서 다음과 같이 parameter를 설정한다. <code>PCTFREE 20</code></p>
<pre><code class="language-sql">CREATE TABLE emp (
  emp_id NUMBER PRIMARY KEY,
  emp_name VARCHAR2(50),
  salary NUMBER
) PCTFREE 20;
</code></pre>
</li>
</ul>
<pre><code>- 이 값에 의해, 이 테이블의 Data segment 내 각 데이터, 블록의 20%가 빈 상태로 유지된다.
- 이 비어있는 영역은, 각 블록 내 기존 행이 갱신될 경우에 사용된다.
  - 만약 pctfree 공간이 부족하면, oracle은 행을 새로운 블록으로 이동(row migration)하거나, 블록을 분할(block split)하게 됨
- `즉, 한 블록이 완전히 꽉 차지 않도록 남겨둠으로써, update시 블록 분할(block split), 또는 row migration(행 마이그레이션)을 방지하는 역할을 한다.`

### PCTUSED (Percent Used)
- 데이터 블록이 다시 INSERT를 받을 수 있도록 허용되는 최소한의 사용률을 설정하는 파라미터
- PCTFREE+PCTUSED &lt;= 100%가 되어야 함

```sql
ex) PCTFREE 20, PCTUSED 40이면
- 블록이 80%까지 채워지면 insert 불가
- 데이터가 삭제되어 블록 사용률이 40% 미만이 되면 다시 insert 가능</code></pre><h3 id="freelist">FREELIST</h3>
<ul>
<li><p>새로운 데이터를 삽입할 때 사용할 수 있는 블록 목록</p>
</li>
<li><p>PCTFREE 설정이 높으면, 더 많은 블록이 FREELIST에 추가되어 새로운 데이터가 분산됨</p>
</li>
<li><p>DELETE가 발생하여 블록이 일정 수준 이하(PCTUSED미만)로 비워지면, 다시 FREELIST에 추가된다.</p>
<pre><code class="language-SQL">[ FREELIST에 추가 및 제거되는 과정 ]

  INSERT 가능 블록 목록 (FREELIST)
 ┌────────┬───────┬─────────┐
 │ BLK 1 │ BLK 2 │ BLK 3 │  ← INSERT 가능
 └────────┴───────┴─────────┘

  ↓ (INSERT 발생하여 BLK 1이 꽉 참 → FREELIST에서 제거됨)

 ┌────────┬───────┐
 │ BLK 2 │ BLK 3 │  ← INSERT 가능
 └────────┴───────┘

  ↓ (DELETE 발생하여 BLK 1이 일정 수준 이하로 비워짐)

 ┌─────────┬───────┬───────┐
 │ BLK 1  │ BLK 2 │ BLK 3│  ← INSERT 가능 (BLK 1 다시 추가)
 └─────────┴───────┴───────┘
</code></pre>
</li>
</ul>
<pre><code>### INITRANS (Initial Transactions)
- 하나의 데이터블록에서 동시에 실행할 수 있는 최소 트랜잭션 수를 정의하는 파라미터
- 다중 트랜잭션 환경에서 경합(Blocking)을 방지하는 역할을 함
- 테이블 생성 시 기본적으로 INITRANS = 1로 설정됨

** 동작 방식**
&gt; 1. 데이터블록에 트랜잭션 슬롯이 생성됨
2. 트랜잭션이 실행될 때마다 슬롯을 차지함
3. INITRANS를 초과하는 경우, 남은 공간을 사용하여 추가 슬롯 생성  (하지만 블록 내 공간이 부족하면 경합 발생이 가능)</code></pre>