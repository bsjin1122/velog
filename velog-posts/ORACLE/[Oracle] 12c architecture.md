<blockquote>
<p>최근에 못 그렸었는데 이번에 내가 정리한거 보면서 
나중에 그릴 때마다 알고(이해하고) 그리고 싶어서 시간이 꽤 걸렸지만 ....
적어도 이 용어 보고 뭐하는 역할이구나 정도까진 대강 알았다....
남은 것은 이해하면서 머릿속에 넣기..? 
근데 보면 볼수록 재밌다 (뭐지..) 정리하면서 명확하게 몰랐던걸 구분해나가는게 재밌었던 것 같다. 
공식문서에 설명이 잘 되어 있어서 계속해서 읽으면서 정리를 추가하려 한다.
<a href="https://docs.oracle.com/cd/F39414_01/cncpt/memory-architecture.html#GUID-4FF66585-E469-4631-9225-29D75594CD14">내용이 한곳에 응축되어있어서 양은 많지만 꼭 보면서 정리해야할 것 같다..!</a> 다시 아침마다 그려볼까..!😤🥺그림 이제 외울 수 있을 것 같은 기분</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/ca91b440-6214-4a18-bac3-0221b9f6faab/image.png" /></p>
<blockquote>
<ul>
<li>참고: <a href="https://docs.oracle.com/cd/F19136_01/racad.pdf">Oracle® Real Application Clusters Real Application Clusters 管理および
デプロイメント・ガイド 19c - 아키텍처</a></li>
</ul>
</blockquote>
<ul>
<li><a href="https://docs.oracle.com/cd/F32587_01/refrn/background-processes.html">백그라운드 프로세스</a></li>
<li><a href="https://docs.oracle.com/cd/F39414_01/tgdba/database-memory-allocation.html#GUID-BBEC24EB-DADD-4178-A553-F9C7FF684207">데이터베이스 메모리 튜닝 가이드</a></li>
</ul>
<h1 id="sga">SGA</h1>
<img src="https://velog.velcdn.com/images/greendev/post/c3c461d9-3bd9-4554-b23d-0791e09d6e85/image.png" width="300" />

<p><strong>SGA(System Global Area)</strong></p>
<ul>
<li>1개의 Oracle Database Instance에 대한 데이터 및 제어 정보가 저장되어 있다.</li>
<li>모든 Server와 Background Process에서 SGA를 공유한다. </li>
<li>SGA에 저장되는 데이터에는 Cache Data Block 및 Shared SQL 영역 등이 있다.</li>
<li>참고: <a href="https://docs.oracle.com/cd/F39414_01/cncpt/memory-architecture.html#GUID-02378E7A-865B-456B-8725-1E73D16A34BE">기본적인 메모리 구조</a></li>
</ul>
<blockquote>
<p><strong>SGA 내 구성 요소</strong></p>
<ol>
<li>Database Buffer Cache (데이터베이스 버퍼 캐시)</li>
<li>Shared Pool (공유 풀)</li>
<li>Large Pool(대형 풀)</li>
<li>Java Pool(자바 풀)</li>
<li>Streams Pool(스트림 풀)</li>
<li>Flash Buffer Area(플래시 버퍼 영역-&gt; Exadata 환경에서 사용)</li>
</ol>
</blockquote>
<h2 id="shared-pool">Shared Pool</h2>
<ul>
<li>SQL문과 실행 계획을 캐싱하여, 동일한 SQL문이 반복 실행될 때 파싱 과정을 생략하고, 성능을 향상시킨다.</li>
</ul>
<p><strong>Library Cache</strong></p>
<ul>
<li>SQL문, PL/SQL 코드, 실행 계획을 저장하는 공간</li>
<li>User Global Area(UGA): Shared Server 환경에서 사용자 세션 정보를 저장</li>
<li>동일한 SQL문이 반복될 경우, Library Cache에 캐싱된 정보를 재사용하여, SQL 파싱 과정을 최소화한다.</li>
</ul>
<p><strong>Data Dictionary Cache(Row Cache)</strong></p>
<ul>
<li>Oracle 데이터베이스의 오브젝트(테이블, 인덱스 등) 메타 정보를 캐싱하여 빠르게 참조할 수 있도록 지원한다.<ul>
<li>테이블 컬럼 정보</li>
<li>인덱스 정보</li>
<li>사용자 권한 정보</li>
</ul>
</li>
<li>데이터베이스 오브젝트에 접근할 때마다 데이터 딕셔너리에서 가져오는 것이 아니라, Row Cache에 캐싱된 정보를 사용하여 성능을 최적화한다. </li>
</ul>
<p><strong>Reserved Pool</strong> </p>
<ul>
<li><p>대규모 SQL문이나 PL/SQL 코드가 Shared Pool에서 할당 공간을 찾지 못할 경우를 대비해 미리 예약된 영역이다.</p>
</li>
<li><p>대규모 객체가 자주 파싱되는 환경에서 <code>ORA-04031: unable to allocate</code>와 같은 오류를 방지한다.</p>
</li>
</ul>
<p><strong>Result Cache</strong></p>
<ul>
<li>SQL 쿼리의 결과를 캐싱하여 동일한 쿼리가 반복되면, 캐시된 결과를 반환하여 성능을 개선한다.<ul>
<li>자주 조회되는 통계나 요약 데이터의 결과를 캐싱하여 응답 속도를 향상</li>
</ul>
</li>
</ul>
<p><strong>Latch, Enqueue</strong></p>
<ul>
<li>Oracle 내부에서 <strong>동시성 제어</strong>를 위해 사용</li>
<li><code>Latch</code>: 짧은 시간 동안 데이터 구조의 동시 접근을 제어하는 메커니즘</li>
<li><code>Enqueue</code>: 트랜잭션 간의 락을 관리하여 데이터의 무결성을 보장</li>
</ul>
<p><strong>ASH Buffers (Active Session History Buffers)</strong></p>
<ul>
<li>현재 활성 세션 정보를 일시적으로 저장하여, 성능 문제를 분석할 때 활용된다.</li>
</ul>
<p><strong>Global Resource Directory(RAC 전용)</strong> </p>
<ul>
<li>Oracle RAC 환경에서 각 노드 간의 리소스 정보(락, 데이터)를 공유하여 일관성을 유지하도록 지원한다.<ul>
<li>이를 위해, Global Cache Service(GCS)와 Global Enqueue Service(GES)가 협력하여 데이터의 일관성을 유지한다.</li>
</ul>
</li>
</ul>
<p><strong>ges</strong></p>
<ul>
<li><code>ges big msg bufferes</code>: GES에서 대용량 메시지를 처리하기 위한 버퍼</li>
<li><code>ges resource</code>: GES에서 관리하는 리소스 정보를 저장 </li>
<li><code>ges shared global area</code>: GES에서 공유되는 글로벌 영역으로, 락과 리소스 상태 관리</li>
<li><code>ges process array</code>: GES에서 관리하는 프로세스들의 배열</li>
<li><code>ges reserved msg bufferes</code>: GES에서 예약된 메시지 버퍼로, 특별한 메시지를 관리</li>
<li><code>ges enqueues</code>: GES에서 관리하는 엔큐(락)정보를 저장</li>
</ul>
<p><strong>gcs</strong></p>
<ul>
<li><code>gcs res hash bucket</code>: GCS에서 리소스 해시 테이블을 관리</li>
<li><code>gcs mastership buckets</code>: GCS에서 리소스 마스터 노드 정보를 관리</li>
<li><code>gcs resources</code>: GCS에서 관리하는 캐시된 리소스 정보</li>
<li><code>gcs shadows</code>: GCS에서 리소스의 그림자 복사본을 관리하여 일관성 보장</li>
<li><code>gcs affinity</code>: 특정 리소스가 어느 노드에 친화적으로 있는지 (노드 선호도) 관리</li>
</ul>
<h3 id="ilm-bitmap-tablesinformation-lifecycle-management">ILM Bitmap Tables(Information Lifecycle Management)</h3>
<ul>
<li>ILM: 데이터의 수명 주기를 관리하는 기능</li>
<li>Oracle은 데이터가 생성된 이후, 오래된 데이터를 효율적으로 관리하기 위해 ILM 기능을 사용한다.</li>
<li><em>역할*</em></li>
<li>데이터 액세스 빈도나, 수정 빈도를 기반으로 데이터를 분석하고, 관리 전략을 결정한다.</li>
</ul>
<h3 id="least-recently-usedlru-list">Least Recently Used(LRU) List</h3>
<ul>
<li>Oracle의 버퍼 캐시(Buffer Cache)에서 가장 오래 사용되지 않은 데이터 블록을 관리하는 리스트</li>
<li>Oracle은 LRU 알고리즘을 사용하여, 새로운 데이터가 캐시에 로드되어야 할 때 오래된 데이터를 제거</li>
</ul>
<h3 id="checkpoint-queue">Checkpoint Queue</h3>
<ul>
<li>변경된 블록(Dirty Blocks)을 Low RBA(Redo Byte Address) 순서로 정렬하여 디스크로 기록한다.</li>
<li>Redo 로그와 데이터 파일의 일관성을 유지 </li>
</ul>
<p><strong>동작 과정</strong></p>
<ol>
<li>데이터가 변경되면, 버퍼 캐시에 Dirty Block으로 표시된다.</li>
<li>이 Dirty Block은 Checkpoint Queue에 등록된다.</li>
<li>Checkpoint 이벤트 발생 시, Queue에서 데이터를 디스크로 기록한다.</li>
</ol>
<hr />
<h2 id="large-pool">Large Pool</h2>
<img src="https://velog.velcdn.com/images/greendev/post/33c778af-2e20-444b-9d28-6862f5013a9b/image.png" width="300" />

<ul>
<li>대용량 프로세스 및 백업/복구 작업을 위한 메모리 공간을 제공<ul>
<li>MTS(Multi-Threaded Server)환경, 병렬 쿼리, RMAN 백업 등에 필요하다.</li>
</ul>
</li>
<li>Response Qeueues: 병렬 처리(PX, Parallel Execution)및 Shared Server 환경에서 응답을 저장하는 큐</li>
<li>Request Queue: Shared Server 환경에서 클라이언트 요청을 저장하는 큐</li>
<li>Oracle XA Interface Pool: Distributed Transactions(분산 트랜잭션) 처리를 위한 XA 인터페이스 </li>
<li>Backup / Recovery Operations: RMAN(Recovery Manager) 백업 및 복구 작업을 위한 메모리 공간</li>
<li>Private SQL Area(Persistent Area) for Shared Servers: Shared Server 환경에서 개별 사용자 SQL문 실행 정보를 저장</li>
<li>PX msg pool: 병렬 쿼리 실행 시 프로세스 간 메시지 교환을 관리하는 영역</li>
</ul>
<h3 id="shared-io-pools-securefiles">Shared I/O Pools (SecureFiles)</h3>
<ul>
<li>SecureFiles(보안 파일 저장 기능)에서 대용량 I/O 처리를 위한 공간</li>
<li>LOB(Large Object) 데이터 저장 최적화 기술</li>
<li>기존 BasicFiles보다 빠른 읽기/쓰기 성능을 제공하며, 암호화, 압축, 중복 제거 등의 기능을 포함</li>
</ul>
<blockquote>
<ul>
<li>SecureFiles를 사용할 때 대량의 데이터 I/O 처리를 원활하게 하기 위해 Shared I/O Pool을 활용한다.</li>
</ul>
</blockquote>
<h3 id="streams-pool">Streams Pool</h3>
<ul>
<li>Oracle Streams 및 GoldenGate와 같은 데이터 스트리밍 기능을 위한 전용 메모리 공간</li>
<li>데이터 변경 로그를 관리하고, 데이터베이스 간 복제(replication)를 수행할 때 사용<ul>
<li>주로 데이터 복제 및 고가용성(HA) 아키텍처에서 필요하다.</li>
</ul>
</li>
</ul>
<h3 id="java-pool">Java Pool</h3>
<ul>
<li>JVM(Java Virtual Machine)에서 실행되는 Java 코드 및 클래스 데이터를 저장하는 메모리 영역<ul>
<li>Used Memory: 현재 사용중인 java공간</li>
<li>Free Memory: 사용 가능 메모리 공간</li>
</ul>
</li>
<li>Java Stored Procedures, Java-based 트리거, Java 애플리케이션이 데이터베이스 내에서 실행될 경우 필요. </li>
</ul>
<h3 id="fixed-sga">Fixed SGA</h3>
<ul>
<li>Oracle 고정 크기 메모리 영역으로, 핵심적인 데이터베이스 정보를 저장한다.</li>
<li>크기가 고정되며, 오버헤드를 최소화하도록 설계됨<blockquote>
<p>SGA 전체를 제어하는 핵심 정보(파라미터, 내부 프로세스 정보 등)를 관리</p>
</blockquote>
</li>
</ul>
<hr />
<ul>
<li>정식명 / 개요 / 상세 / 외부 프로퍼티<h2 id="background-process">Background Process</h2>
<img alt="" src="https://velog.velcdn.com/images/greendev/post/b5361851-5188-4d96-81dd-5043c92be3e2/image.png" /></li>
</ul>
<h3 id="lms0-z-global-cache-service">LMS0-Z (Global Cache Service)</h3>
<ul>
<li>개요: Resource를 관리하여 Oracle RAC Instance간 리소스를 제어함</li>
<li>상세: Global Cache Service(GCS)용 Lock Database와 Buffer Cache 리소스를 갖고 있다. (n은, 0~9 혹은 a-z) 또한 GCS Reeuqest, Block 전송 및 그 외 GCS관련된 메시지를 수신하고 처리하며 송신한다.</li>
<li>관련항목: <a href="https://docs.oracle.com/cd/F19136_01/racad/changes-in-this-release-for-oracle-real-application-clusters-administration-and-deployment-guide.html">Oracle Real Application Clusters管理およびデプロイメント・ガイド</a></li>
<li>외부 프로퍼티: 데이터베이스 인스턴스, ASM인스턴스, Oracle RAC</li>
</ul>
<h3 id="lmon-global-enqueue-service-monitor">LMON (Global Enqueue Service Monitor)</h3>
<ul>
<li>Oracle RAC 클러스터를 감시하여 Global Resource를 관리함</li>
<li>LMON은 Oracle RAC 내 인스턴스, 멤버십을 관리한다. 또한, 인스턴스 트랜잭션을 검출하여 GES Resource와 GCS Resource를 재구성한다.</li>
<li>외부 프로퍼티: 데이터베이스 인스턴스, ASM인스턴스, Oracle RAC</li>
</ul>
<h3 id="ping-interconnect-latency-measurement">PING (Interconnect Latency Measurement)</h3>
<ul>
<li>Interconnect 대기시간 측정 프로세스</li>
<li>클러스터 인스턴스 페어마다 통신에 수반되는 대기시간을 평가함</li>
<li>수 초마다, 하나의 인스턴스 내 프로세스로부터 각 인스턴스에 메시지가 송신된다.</li>
<li>타겟 인스턴스상의 ping에 의해 수신된다. <ul>
<li><code>Round Trip Delay</code>(통신에서 왕복 지연 또는 왕복 시간은 신호가 전송되는 데 걸리는 시간과 해당 신호가 수신되었음을 확인하는 데 걸리는 시간을 더한 것)에 걸리는 시간이 측정 혹은 수집된다.</li>
</ul>
</li>
<li>외부 프로퍼티: 데이터베이스 인스턴스, ASM인스턴스, Oracle RAC</li>
</ul>
<h3 id="rmsn-rac-management-process">RMSn (RAC Management Process)</h3>
<ul>
<li>Oracle RAC 관리 프로세스</li>
<li>Oracle RAC 관리 task를 실행</li>
<li>다양한 task를 실행한다. (클러스터에 새로운 인스턴스가 추가되었을 때, Oracle RAC에 관련된 Resource를 생성하는 등)</li>
</ul>
<h3 id="lmhb-global-cacheenqueue-heartbeat-monitor">LMHB (Global Cache/Enqueue Heartbeat Monitor)</h3>
<ul>
<li>LMON, LMD 및 LMS 프로세스의 Heart Beat를 감시함</li>
<li>LMON, LMD 및 LMS 프로세스를 감시하여 그것들이 Blocking 혹은 Spin 없이 정상적으로 실행되도록 한다.</li>
<li>외부 프로퍼티: 데이터베이스 인스턴스, ASM인스턴스, Oracle RAC</li>
</ul>
<h3 id="lmd0z-global-enqueue-service">LMD0,Z (Global Enqueue Service)</h3>
<h4 id="ldd0z">LDD0,Z</h4>
<ul>
<li>그 외 인스턴스로부터 수신되는 Remote Resource Request를 관리함</li>
<li>Global Enqueue Service에 의해 관리되는 Enqueue Resource를 관리한다.</li>
<li>특히, LMD0 프로세스는 수신된 Enqueue Request Message를 처리하여, Global Enqueue로의 Access를 제한한다. 또한, 분산 Deadlock의 검축도 수행한다.</li>
</ul>
<h3 id="lck01-lock-process">LCK0,1 (Lock Process)</h3>
<ul>
<li>Instance Enqueue Background Process</li>
<li>Global Eunqueue Request와 인스턴스간 BroadCast를 관리함</li>
<li>이 프로세스는, Data block 이외 리소스에 대한 모든 request를 처리한다.</li>
<li>예를 들면, LCK0는 라이브러리 캐시 요청 및 Row Cache Request를 관리한다.</li>
<li>외부 프로퍼티: 데이터베이스 인스턴스, ASM인스턴스, Oracle RAC</li>
</ul>
<h3 id="rsmn-remote-slave-monitor">RSMN (Remote Slave Monitor)</h3>
<ul>
<li>Oracle RAC 내 Remote Instance에서 Background Slave Process의 생성 및 통신을 관리함</li>
<li>이 백그라운드 프로세스는 Slave Process 생성을 관리하고, Slave Process의 Coordinator 및 Peer와의 통신을 관리한다.<ul>
<li>일반적으로 병렬 작업을 처리하거나, 특정 작업을 여러 노드로 분산할 때 사용된다.</li>
</ul>
</li>
<li>이 백그라운드 Slave Process는 그 외 클러스터 인스턴스에서 실행되고 있는 작업을 대신 수행하는 역할을 한다.<ul>
<li>예를 들어, 노드 A에서 특정 작업을 요청하면, RSMN이 노드 B에서 그 작업을 대신 수행할 수 있다.</li>
</ul>
</li>
</ul>
<h3 id="smco-space-management-coordinator">SMCO (Space Management Coordinator)</h3>
<ul>
<li>Space 관리 Coordinator Proces</li>
<li>다양한 Space관리 Task 실행을 조정한다. (사전 Space 할당, Space 재이용 등)</li>
<li>Automatic Space Management<ul>
<li>ASM과 통합되어 작동한다.</li>
<li>테이블 또는 인덱스 파티션의 공간 자동 할당, 테이블 압축, 공간 해제(<code>Free Space Reclamation</code>;삭제된 데이터의 공간을 다시 사용 가능하도록 정리함) 등의 기능을 수행한다.</li>
</ul>
</li>
</ul>
<h4 id="wnnn">Wnnn</h4>
<ul>
<li>SMCO가 할당한 작업을 병렬로 처리하여 효율성을 극대화한다.<ul>
<li>예) 대량의 공간 할당 작업이나 자동 압축 작업 등을 동시에 수행</li>
</ul>
</li>
<li>W000, W001, W002와 같은 형태로 표시된다.</li>
<li>모든 Wnnn 프로세스가 작업을 완료하면, 결과를 SMCO가 수집한다.</li>
</ul>
<p><strong>✅ SMCO와 Wnnn의 동작 원리 (작업 처리 흐름)</strong></p>
<pre><code class="language-text">1. 작업 요청 발생
- 사용자가 대량의 데이터 로드 작업 또는 공간 재사용 작업을 실행할 때 발생.

2. SMCO 프로세스 작동
- SMCO가 전체 작업을 조정하고, 작업을 적절히 분배합니다.
- 여러 개의 Worker Process (Wnnn)를 사용하여 병렬로 작업을 처리합니다.

3. Worker Process(Wnnn) 작업 실행
- Wnnn 프로세스는 지정된 작업을 수행하고 결과를 SMCO에게 보고합니다.
- 예를 들어, 테이블의 Free Space 정리 또는 ASM 디스크 그룹의 공간 재사용을 처리합니다.

4. 작업 완료 후 보고
- 모든 Wnnn 프로세스가 작업을 완료하면, 결과를 SMCO가 수집합니다.

5. 컨트롤 파일 업데이트 (필요 시)
- 작업이 완료되면, 관련 정보가 컨트롤 파일에 기록됩니다.</code></pre>
<h3 id="vkrm-virtual-scheduler-for-resource-manager">VKRM (Virtual Scheduler for Resource Manager)</h3>
<ul>
<li>Resource Manager Process용 Virtual Scheduler</li>
<li>Resource Mangaer의 Activity 수집 스케쥴러로서 기능함</li>
<li>관리대상의 모든 Oracle Process의 CPU 스케쥴을 관리한다.<ul>
<li>Active Resource Plan에 의해 관리 대상의 Process를 스케쥴한다.</li>
</ul>
</li>
</ul>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/4c5d462d-507b-461b-923b-c2a18424e1fc/image.png" /></p>
<h3 id="rcbg-result-cache">RCBG (Result Cache)</h3>
<ul>
<li><p>Result Cache Message를 처리함</p>
<ul>
<li>특히 <code>무효화 메시지 처리</code>; 데이터 변경 시 기존 캐시가 유효하지 않다는 신호</li>
<li>Result Cache: SQL쿼리 결과를 메모리에 저장하여 동일한 쿼리가 다시 실행될 때 빠르게 결과를 반환하도록 하는 기능</li>
</ul>
</li>
<li><p>RCBG는 Result Cache에 저장된 결과가 유효하지 않거나, 업데이트 된 경우 이를 반영하여 캐시를 무효화하는 역할을 한다.</p>
</li>
<li><p>Oracle RAC 내 그 외 인스턴스에 접속하고 있는 Server Process에 의해 생성된, 무효화 등의 메시지 처리할 때 사용된다.</p>
<blockquote>
<ul>
<li>RAC 환경에서 각 인스턴스는 자신의 Result Cache를 관리하며, 다른 인스턴스에서 발생한 무효화 작업을 반영하기 위해 서로 통신합니다.</li>
</ul>
</blockquote>
<ul>
<li>예를 들어, RAC의 노드 A에서 테이블 데이터를 업데이트하면, 노드 B의 Result Cache에 저장된 해당 데이터는 유효하지 않게 됩니다.</li>
<li>이 때, RCBG 프로세스가 무효화 메시지를 전송 및 수신하여 캐시를 올바르게 업데이트합니다.</li>
</ul>
</li>
</ul>
<h3 id="mman-memory-manager">MMAN (Memory Manager)</h3>
<ul>
<li>Instance Memory Component Size 변경을 담당한다.</li>
<li>Database Instance 및 ASM Instance </li>
</ul>
<h3 id="mmon-manageability-monitor">MMON (Manageability Monitor)</h3>
<h4 id="mnnn">Mnnn</h4>
<ul>
<li>MMON Slave Process</li>
<li>MMON에 관련되어 관리성에 관한 Task를 수행</li>
<li>MMON으로부터 Dispatch된 관리성에 관한 Task를 수행한다.</li>
<li>Task는 AWR Snapshot 조회, Automatic Database Diagnostic Monitor 분석 실행 등이 포함된다.</li>
</ul>
<h3 id="mmnl-manageability-monitor-life">MMNL (Manageability Monitor Life)</h3>
<ul>
<li>Manageability 에 관하 다수 task를 실행하거나 그 스케쥴을 설정함</li>
<li>Automatic Workload Repository Snapshot의 조회, Automatic Database Diagnostic Monitor 분석 실행 등 관리성에 관련된 Task를 수행함</li>
</ul>
<h3 id="pmon-process-monitor">PMON (Process Monitor)</h3>
<ul>
<li>다른 백그라운드 프로세스를 감시하여 Server Process 혹은 Dispatcher Process가 비정상종료한 경우에 프로세스의 복구를 실행함</li>
<li>정기적으로 다음과 같은 모든것을 Clean Up한다.<ul>
<li>비정상종료한 프로세스</li>
<li>강제종료된 세션</li>
<li>Idle Timeout을 초과한, 연결해제된 Transaction</li>
<li>Idele Timeout을 초과한, 연결 해제 된 네트워크 접속</li>
</ul>
</li>
<li>추가로 PMON은 필요에 의해 다음과 같은 프로세스를 감시, 기동, 정지한다.<ul>
<li>Dispatcher Process 및 Shared Server Process</li>
<li>Job Queue Process</li>
<li>Database 상주 접속 Pooling에 대한 Pool Server Process</li>
<li>재기동 가능한 백그라운드 프로세스</li>
</ul>
</li>
<li>또한 PMON은 인스턴스 및 Dispatcher Process에 관한 정보를 Network Listener에 등록하는 역할도 수행<h3 id="smon-system-monitor">SMON (System Monitor)</h3>
</li>
<li>중요한 Task (Instance Recovery, 무효해진 Transaction의 Recovery 등) 및 Maintenance Task(일시적 Space 재이용, Data Dictionary 의 Clean Up, UNDO 테이블스페이스 관리 등) 실행한다.</li>
<li>임시 테이블스페이스의 메타데이터를 생성 및 관리</li>
<li>트랜잭션 복구</li>
<li>데이터베이스 딕셔너리가 일시적으로 비일관성 상태일 경우 Clean Up</li>
<li>UNDO 테이블스페이스 관리<ul>
<li>UNDO 세그먼트 온라인/오프라인 전환</li>
<li>UNDO 세그먼트 축소(Shrink) 작업을 통해 공간 회수</li>
<li>UNDO 영역 사용 통계 수집을 통해 공간을 효율적으로 사용하도록 관리</li>
</ul>
</li>
<li>데이터 딕셔너리 정리 <ul>
<li>ex) DDL 작업 중 오류가 발생하면, 남아있는 불피룡한 정보를 정리</li>
</ul>
</li>
<li>Instance Recovery: 예기치 않은 장애로 인해 데이터베이스 인스턴스가 비정상 종료되었을 때, Redo 로그를 사용하여 데이터 일관성을 회복하는 과정<ul>
<li>SMON 프로세스는 데이터 파일과 Redo 로그 파일을 비교하여 손실된 변경 사항을 다시 적용함으로써 데이터 일관성을 보장한다.</li>
</ul>
</li>
<li>Oracle Flashback 기능을 지원하기 위해 SCN과 시간 정보 매핑 정보를 유지<blockquote>
<p>Oracle RAC 데이터베이스에서는 인스턴스의 SMON 프로세스는 장애가 발생한 다른 인스턴스에 대해 Instnace Recovery를 수행할 수 있다.</p>
</blockquote>
</li>
<li>SMON에는 Background Activity중에 발생한 내부 및 외부 Error에 대한 Resilience가 있다.</li>
<li>참고: <a href="https://docs.oracle.com/cd/E16338_01/server.112/b56306/intro.htm">Oracle Database 개요</a></li>
</ul>
<h3 id="reco-recovery-process">RECO (Recovery Process)</h3>
<ul>
<li>분산 Database에서의 네트워크 혹은 System 장애에 의해 보류 되어있는 분산 트랜잭션(Distributed Transaction)을 복구를 담당</li>
<li>특히 네트워크 장애 또는 시스템 장애로 인해 보류 상태로 남아있는 트랜잭션(In-Doubt Transaction)을 자동으로 복구한다.<ul>
<li>분산 트랜잭션이 실행되는 도중 네트워크 장애, 인스턴스 오류 등으로 트랜잭션이 중단되면, 트랜잭션은 'In-Doubt 상태'로 남게 된다.</li>
</ul>
</li>
<li>RECO는 보류중인 트랜잭션 테이블의 정보를 사용하여, IN-Doubt Transanction 상태를 해결한다.</li>
<li>보류된 트랜잭션이 원격데이터베이스와 관련된 경우, 주기적으로 원격데이터베이스와의 연결을 시도하고, 보류중인 분산 트랜잭션의 로컬 부분의 commit 혹은 rollback을 자동으로 완료시킨다.</li>
<li>RECO에 의해 자동해결된 트랜잭션은 모두 보류중인 트랜잭션 테이블로부터 삭제된다.</li>
<li><a href="https://docs.oracle.com/cd/F19136_01/netag/preface.html">Oracle Database Net Services 관리자 가이드</a></li>
</ul>
<h3 id="sann-sga-allocator">SAnn (SGA Allocator)</h3>
<ul>
<li>SGA 내에서 메모리 할당과 관련된 작업을 수행하는 프로세스</li>
<li>nn: 숫자로 표시, SAn0, SAn1, .. </li>
<li>SGA를 다양한 구성 요소로 나누어 관리하며, SAnn 프로세스는 특정 구성 요소에 대한 메모리 할당 및 조정을 수행한다. <ul>
<li>Buffer Cache: 데이터베이스 블록을 캐싱하여 I/O 성능을 향상</li>
<li>Shared Pool: SQL문, PL/SQL 코드, Data Dictionary 정보 등을 캐싱함</li>
<li>Large Pool: RMAN 백업, 병렬 처리 등을 위한 추가 메모리 공간</li>
<li>Java Pool : Oracle JVM(Java Virtual Machine)을 위한 메모리</li>
<li>Streams Pool: 데이터 스트리밍 작업(Oracle Streams 등)의 메모리</li>
<li>Shared I/O Pool: SecureFiles의 대규모 I/O 처리용 메모리</li>
</ul>
</li>
</ul>
<h3 id="dbrm-database-resource-manager">DBRM (Database Resource Manager)</h3>
<ul>
<li>Resource Plan을 설정하여 데이터베이스 Resource Manager에 관련된 그 외 task를 수행함</li>
<li>Resource Plan이 유효하지 않은 경우, 이 프로세스는 Idle 상태가 된다.</li>
<li>DBRM은 사용자가 정의한 리소스 플랜을 기반으로 작업의 우선순위를 설정<ul>
<li><code>Resource Plan</code>: 다중 사용자 환경에서 특정 사용자나 작업이 과도하게 시스템 리소스를 사용하는 것을 방지한다.</li>
<li>리소스 소비자 그룹(Consumer Group)관리: 사용자 또는 작업들을 그룹으로 분류하여 <strong>리소스 소비자 그룹</strong>을 만든다.<ul>
<li>각 그룹의 사용량을 모니터링하며, 설정된 리소스 플랜을 기반으로 리소스를 배분한다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="emnc-emon-coordinator">EMNC (EMON Coordinator)</h3>
<ul>
<li><p>데이터베이스 이벤트 관리 및 알림을 조정</p>
</li>
<li><p>Database에서의 Event 관리 및 알림 Activity(Streams에서의 Event 알림, 연속Query(Continuous Query Notification (CQN)) 알림, FAN 등) 조정함</p>
<ul>
<li>**FAN(Fast Application Notification)관리<ul>
<li>RAC 클러스터 내 노드 장애, 인스턴스 장애, 서비스 장애 등을 감지하고, 즉시 애플리케이션에 알린다.</li>
</ul>
</li>
<li>Continuous Query Notification(CQN)관리: 특정 조건에 따라 데이터베이스의 변경 사항이 발생하면, 애플리케이션으로 즉시 알림을 보내도록 설정할 수 있다.</li>
<li>Oracle Streams: 데이터베이스 간 데이터 변경 사항을 실시간으로 전송</li>
</ul>
</li>
</ul>
<h3 id="gen0-general-task-execution">GEN0 (General Task Execution)</h3>
<ul>
<li>SQL과 DML을 포함한 Request된 Task를 실행한다.</li>
</ul>
<h3 id="vktm-vitual-keeper-of-time">VKTM (Vitual Keeper of TIMe)</h3>
<ul>
<li><p>시간 간격 측정을 위해 실시간과 참조시간을 제공함</p>
</li>
<li><p>Oracle Instance에 대해 시간 Publisher로서 기능한다.</p>
</li>
<li><p>VKTM은 시간 간격 측정을 위해 실시간(초단위)와, 보다 고도의 분해시간(밀리초 이하의 매우 짧은 시간으로, 실시간과는 차이가 있음) 2종류의 시간을 발행한다.</p>
</li>
<li><p>VKTM Timer service는 시간 추적을 집중화하여, 그 외 Client로부터의 복수 Timer Goal을 Offload한다.</p>
<ul>
<li>Timer Goal Offload: 다양한 백그라운드 프로세스에서 발생하는 타이머 요청을 VKTM이 대신 처리하여 다른 프로세스의 부하를 줄인다.</li>
<li>예) 데이터베이스의 특정 이벤트가 일정 시간 후 발생해야 할 때, VKTM이 그 시간을 정확히 계산하고 알림을 제공한다.</li>
</ul>
</li>
</ul>
<h3 id="psp0-process-spawner-생성자">PSP0 (Process Spawner; 생성자)</h3>
<ul>
<li>초기 인스턴스 기동 후에 Oralce Background Process를 기동함<ul>
<li>인스턴스 기동 시 백그라운드 프로세스를 생성하고, 관리하는 기능</li>
</ul>
</li>
<li>동적 프로세스 생성 관리 (Dynamic Process Spawning)<ul>
<li>필요할 때마다 새로운 프로세스를 생성하여 추가 작업을 처리할 수 있음</li>
</ul>
</li>
<li>프로세스 요청 큐 관리(Process Request Queue Management)<ul>
<li>프로세스 생성 요청을 관리하기 위해 요청 큐(Request Queue)를 사용한다.</li>
<li>새로운 백그라운드 프로세스 생성 요청이 발생하면, PSP0는 이를 큐에 등록하고 순서대로 처리한다.</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/0d7ef36e-03a0-44a7-8874-7d56b4e9ba80/image.png" /></p>
<p><strong>AQ(Advanced Queuing)</strong></p>
<ul>
<li>메시지 기반 통신을 관리하는 기능</li>
<li>Oracle AQ는 주로 비동기 작업 처리, 데이터베이스 간 메시지 전송, 분산 시스템 통신 등에 사용된다.</li>
</ul>
<h3 id="aqpc-aq-process-coordinator">AQPC (AQ Process Coordinator)</h3>
<ul>
<li>전체 AQ 작업을 조정하고, QMnn 및 Qnnn 프로세스의 관리 역할을 수행한다.</li>
</ul>
<blockquote>
<p><strong>동작 원리</strong></p>
</blockquote>
<ol>
<li>인스턴스 기동 시 AQPC 프로세스가 시작됩니다.</li>
<li>Oracle AQ 기능을 활성화하여 필요한 프로세스를 자동으로 시작합니다.</li>
<li>큐에 대한 작업 요청을 감지하여 QMnn 또는 Qnnn 프로세스를 생성합니다.</li>
<li>QMnn 및 Qnnn 프로세스의 상태를 모니터링하고 필요 시 재시작합니다.</li>
</ol>
<h3 id="qmnn-aq-master-class">QMnn (AQ Master Class)</h3>
<ul>
<li>Advanced Queuing 주요 프로세스를 관리하고, 슬레이브 프로세스(Qnnn)에 작업을 분배한다.</li>
</ul>
<h3 id="qnnn-aq-server-class">Qnnn (AQ Server Class)</h3>
<ul>
<li>QMNC를 위해 다양한 AQ 관련 백그라운드 Task 수행함</li>
<li>QMNC의 Slave Process로서 동작하고, QMNC로부터 할당된 Task를 수행한다.</li>
</ul>
<h3 id="cjq0">CJQ0</h3>
<ul>
<li><p>Data Dictionary로부터 실행되는 필요한 Job을 선택하여 Job을 실행하는 Job Queue Slave Process(Jnnn)을 기동함</p>
<ul>
<li>Data Dictionary (DBA_SCHEDULER_JOBS) 에 정의된 작업(Job)들을 지속적으로 모니터링</li>
<li>실행 시간이 된 작업이 있는지 주기적으로 검사 </li>
</ul>
</li>
<li><p>필요에 의해 Oracle Scheduler에 의해 자동적으로 기동 및 정지된다. JOB_QUEUE_PROCESSES초기화 파라미터에는 Job 실행에 대해 생성 가능한 process 최대수를 지정한다. </p>
</li>
<li><p>CJQ0은 실행할 job 수와 사용 가능한 resource에 응하는 수의 job queue process만을 기동한다.</p>
<h4 id="jnnn-job-queue-coordinator">Jnnn (Job Queue Coordinator)</h4>
</li>
<li><p>Job Coordinator로부터 할당받은 job을 실행한다. (ex: 데이터 정리, 백업, 보고서 생성 등)</p>
<ul>
<li>하나의 Jnnn 프로세스는 하나의 작업(Job)만을 처리한다.</li>
</ul>
</li>
<li><p>job이 실행되는 시간에 job coordinator에 의해 생성 혹은 기동된다.</p>
</li>
<li><p>job slave는 job 실행에 필요한 모든 메타데이터를 Data Dictionary로부터 수집한다.</p>
</li>
<li><p>Slave Process는 job의 소유자로서 Database Session을 시작하여 Trigger를 실행하고, Job을 실행한다. Job이 완료되면, Slave Process는 commit하고 적절한 trigger를 실행하여 세션을 close한다.</p>
</li>
<li><p>그 외 job 실행이 필요한 경우 slave는 이 동작을 반복할 수 있다.</p>
</li>
</ul>
<h3 id="ofsd-oracle-file-server">OFSD (Oracle File Server)</h3>
<ul>
<li>Oracle에서 제공하는 파일 서버 프로세스</li>
<li>Oracle Database의 파일 I/O 처리를 관리하고, 특정한 파일 작업 요청을 처리하는 역할을 담당한다.</li>
<li><h3 id="rm-rat-masking-slave">RM (RAT Masking Slave)</h3>
</li>
<li>RAT(Real Application Testing)기능과 관련된 백그라운드 프로세스<ul>
<li>RAT: 데이터베이스의 성능 테스트 및 변경 사항을 검증하기 위한 기능</li>
<li>Data Masking과 관련된 작업을 수행하는 슬레이브 프로세스, 보안과 성능 테스트를 위해 사용된다.<ul>
<li>데이터 마스킹: 민감한 데이터를 반환하여 개인정보나 기밀 데이터를 보호하는 방법</li>
</ul>
</li>
</ul>
</li>
<li>Database Replay: RAT 기능 중 하나로, 실제 환경에서의 워크로드를 기록하고, 테스트 환경에서 재생하여 성능을 검증하는 기능<ul>
<li>RM 프로세스는 데이터 마스킹을 수행하고 데이터베이스 리플레이를 준비한다.</li>
</ul>
</li>
<li>성능 테스트 및 검증(Performance Testing &amp; Validation)<ul>
<li>변경된 환경에서 데이터베이스 성능이 어떻게 영향을 받는지 테스트한다.</li>
<li>ex) 패치 적용 전후의 성능차이를 검증하거나, 구성 변경의 영향을 분석한다.</li>
</ul>
</li>
</ul>
<h3 id="rpnn-capture-processing-worker">RPnn (Capture Processing Worker)</h3>
<ul>
<li>DBMS_WORKLOAD_REPLAY.PROCESS_CAPTURE(cpature_dir, parallel_level)을 call하여 기동되는 worker process이다. <ul>
<li>Database Replay 기능에서 캡쳐된 워크로드 파일을 처리하는 백그라운드 프로세스 </li>
</ul>
</li>
<li>각 worker process에는 처리할 일련의 workload 조회 file이 할당된다.</li>
<li>Worker process는 parallel로 실행되어, 상호간 통신할 필요가 없다. 각 프로세스는 할당된 파일의 처리를 완료하면, 종료하여 부모 프로세스(PROCESS_CAPTURE)에 알린다.</li>
<li>Worker Process 수는 DBMS_WORKLOAD_REPLAY.PROCESS_CAPTURE의 parallel_level 파라미터에서 제어된다.</li>
<li>default는 parallel_level은 null로 설정되어 있다.</li>
<li>Worker Process는 다음과 같이 계산된다.<pre><code class="language-SQL">SELECT VALUE
FROM V$PARAMETER
WHERE NAME='cpu_count';</code></pre>
</li>
<li>parallel_level이 1인 경우, worker process는 기동되지 않는다.</li>
</ul>
<h3 id="ocfn-asm-cf-connection-pool">OCFn (ASM CF Connection Pool)</h3>
<ul>
<li>메타데이터 작업용으로 ASM Instance로의 접속을 유지함</li>
<li>ASM 인스턴스와의 연결을 유지하는 프로세스, 주로 메타데이터 작업을 위해 사용된다.</li>
<li><code>메타데이터 작업</code>: ASM 디스크 그룹, ASM 파일 생성, 삭제, 수정과 같은 파일 관련 작업을 관리한다.</li>
<li>Connection Pooling : 여러 클라이언트(데이터베이스 인스턴스)와 ASM 인스턴스 간의 연결을 지속적으로 유지하여, 연결 성능을 최적화한다.</li>
</ul>
<h3 id="rbal-asm-rebalance-master">RBAL (ASM Rebalance Master)</h3>
<ul>
<li>Rebalance Activity 조정함<ul>
<li><code>리밸런싱 작업</code>은 ASM 디스크 그룹 내의 데이터 분포를 자동으로 조정하여 성능을 최적화하는 기능</li>
</ul>
</li>
<li>ASM Instance에서는 Disk Group의 Rebalance Activity를 조정함</li>
<li>Database Instance에서는 ASM DiskGroup을 관리함</li>
</ul>
<h3 id="onnn-asm-connection-pool">Onnn (ASM Connection Pool)</h3>
<ul>
<li>ASM 인스턴스와 데이터베이스 인스턴스 간의 연결을 유지하고 관리하는 백그라운드 프로세스</li>
<li>OCFn과 유사하게 메타데이터 작업 및 데이터 액세스를 위한 연결 풀링을 관리한다.</li>
<li>데이터베이스 인스턴스가 ASM 인스턴스와의 연결을 효율적으로 사용할 수 있도록 돕는다.</li>
</ul>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/9d6b7b36-ac6a-434f-a571-4012cbff3e31/image.png" /></p>
<h3 id="adr-automatic-diagnostic-repository">ADR (Automatic Diagnostic Repository)</h3>
<ul>
<li>Oracle Database의 오류 및 문제 진단을 위해 자동으로 수집되고 관리되는 통합 저장소</li>
<li>오류 발생 원인을 분석하고, 문제 해결을 지원하는 중요한 기능으로, 모든 진단 정보는 ADR로 수집된다.</li>
<li><code>BG Trace File</code>: 백그라운드 프로세스가 생성한 트레이스 파일</li>
<li><code>FG Trace File</code>: 사용자 프로세스가 생성한 트레이스 파일(예: SQL 실행 오류, 세션 관련 오류)</li>
<li><code>Dump File</code>: 데이터베이스 덤프 파일로, 심각한 오류 발생 시 생성됨</li>
<li><code>HM Reports(Health Monitor Reports)</code>: 데이터베이스의 상태 점검 결과를 보여주는 보고서</li>
<li><code>Incident Packages</code>: 특정 오류와 관련된 진단 데이터를 하나로 묶어 패키지로 저장한다.</li>
<li><code>Incident Dumps</code>: 심각한 오류 발생 시 자동으로 생성되는 덤프 파일</li>
<li><code>AlertLog File</code>: 데이터베이스 인스턴스의 이벤트 및 오류를 기록하는 중요한 로그 파일</li>
</ul>
<h3 id="diag-diagnostic-capture-process">DIAG (Diagnostic Capture Process)</h3>
<ul>
<li>진단 Dump를 수행</li>
<li>다른 프로세스로부터 요청받은 진단 Dump 및 Process 혹은 Instance 종료에 의해 Trigger되는 Dump를 수행한다.</li>
<li>오라클 RAC에서는 DIAG는 Remote Instance로부터 요구된 Global Diagnostic Dump를 실행한다.</li>
</ul>
<h3 id="dia0-diagnostic-process">DIA0 (Diagnostic Process)</h3>
<ul>
<li>Hang 및 deadlock 검출하여 해결함</li>
<li>Hang Detection: 데이터베이스 내 세션 및 프로세스가 응답하지 않는 상태가 발생하면 이를 감지</li>
<li>Deadlock Detection : 두 개 이상의 세션이 서로를 기다리며 영원히 진행되지 못하는 상태를 감지한다.</li>
</ul>
<h3 id="prnn-parallel-recovery-process">PRnn (Parallel Recovery Process)</h3>
<ul>
<li>병렬 인스턴스 복구</li>
<li>병렬 미디어 복구: 손상된 데이터파일을 복구할 때 병렬로 복구 작업을 수행하여 빠른 복구 가능</li>
</ul>
<hr />
<img src="https://velog.velcdn.com/images/greendev/post/d7c7367d-5680-457f-a8b1-8d2af734a59b/image.png" width="400" />



<h3 id="pnnn-parallel-query-slaves">Pnnn (Parallel Query Slaves)</h3>
<ul>
<li>SQL문(Query, DML 혹은 DDL)을 Parallel하여 수행함</li>
<li>Parallel Query에는, Query Coordinator 로서 동작하는 Foreground Process인 일련의 Parallel Slave(Pnnn)의 2개의 Component가 있다.</li>
<li>Background Proces는, Prallel 문의 시작 시에 기동 혹은 재이용된다.</li>
<li>이러한 프로세스는 Query Coordinator로부터 송신된 작업 단위를 받아 실행한다.</li>
<li>Pnnn 프로세스의 최대 수는 초기화 파라미터 PARALLEL_MAX_SERVERS에 의해 제어된다. Slave Process에는 0부터 PARALLEL_MAX_SERVERS에 설정된 값까지의 번호가 부여된다.</li>
<li>Query가 GV$인 경우에, 이러한 백그라운드 프로세스에는 PPA7부터 시작하는 번호가 순서대로 부여된다.</li>
</ul>
<h3 id="snnn-shared-servers">Snnn (Shared Servers)</h3>
<ul>
<li>Shared Server Architecture로 Client request를 처리함</li>
<li>Shared Server Architecture에서는 Client는 Dispatcher Process에 접속한다. 이것에 의해 각 접속에 대해 Virtual Curcuit(가상회선)가 형성된다. </li>
<li>Client가 서버에 데이터를 전송하면, Dispatcher는 Virtual Curcuit에 데이터를 받아 Idle상태의 Shared Server에 의해 조회되는 공통 Queue에 Active Curcit을 배치한다.</li>
<li>Shared Server는 Virtual Curcuit으로부터 데이터를 읽어들여, Request의 완료에 필요한 데이터베이스 작업을 실행한다.</li>
<li>공유 서버가 Client에 데이터를 송신할 필요할 경우, Shared Server는 Data를 가상 회로에 다시 쓰고, Dispatcher가 그 데이터를 클라이언트에 전송한다.</li>
<li>Client Request완료 후, Shared Server는 virtual Curcuit을 해산하여 Dispatcher로 다시 돌아오고 다른 Client 대응할 수 있는 상태가 된다.</li>
</ul>
<h3 id="dnnn-dispatchers">Dnnn (Dispatchers)</h3>
<ul>
<li><p>Shared Server Architecture에서 네트워크 통신을 실행함</p>
</li>
<li><p>Shared Server Architecture에서는 Client는 Dispatcher Process에 접속한다. 이것에 의해 각 접속에 대해 Virtual Curcuit(가상회선)가 형성된다. </p>
</li>
<li><p>Client가 서버에 데이터를 전송하면, Dispatcher는 Virtual Curcuit에 데이터를 받아 Idle상태의 Shared Server에 의해 조회되는 공통 Queue에 Active Curcit을 배치한다.</p>
</li>
<li><p>Shared Server는 Virtual Curcuit으로부터 데이터를 읽어들여, Request의 완료에 필요한 데이터베이스 작업을 실행한다.</p>
</li>
<li><p>공유 서버가 Client에 데이터를 송신할 필요할 경우, Shared Server는 Data를 가상 회로에 다시 쓰고, Dispatcher가 그 데이터를 클라이언트에 전송한다.</p>
</li>
<li><p>Client Request완료 후, Shared Server는 virtual Curcuit을 해산하여 Dispatcher로 다시 돌아오고 다른 Client 대응할 수 있는 상태가 된다.</p>
</li>
<li><p>몇 개의 초기화 파라미터는 Shared Server에 관련되어 있다. 주요 파라미터는 </p>
<ul>
<li><code>DISPATCHERS</code></li>
<li><code>SHARED_SERVERS</code></li>
<li><code>MAX_SHARED_SERVERS</code></li>
<li><code>LOCAL_LISTENER</code></li>
<li><code>REMOTE_LISTENER</code></li>
</ul>
</li>
</ul>
<h3 id="user-process">User Process</h3>
<ul>
<li>사용자 또는 애플리케이션이 데이터베이스와 연결하려 할 때 만들어지는 프로세스이다.</li>
<li>예를 들어 SQL Plus, SQL Developer, 또는 애플리케이션 서버에서의 연결 등</li>
<li><em>역할*</em></li>
<li>SQL문 작성하여 데이터베이스에 요청을 보냄</li>
<li>데이터베이스로부터 결과를 받아 사용자가 볼 수 있게 처리</li>
</ul>
<h4 id="cursor">Cursor</h4>
<ul>
<li>SQL문을 실행하고, 그 결과 집합을 저장하기 위한 메모리 영역</li>
<li>SQL문이 실행될 때 현재 상태를 추적하고 데이터를 순차적으로 접근하는 데 사용된다.</li>
</ul>
<p><strong>커서의 종류</strong></p>
<ol>
<li>Implict Cursor(암시적 커서)</li>
</ol>
<ul>
<li>일반적인 SQL문(SELECT, INSERT, UPDATE, DELETE)실행 시 자동으로 생성됨</li>
<li>사용자가 직접 정의할 필요 없음</li>
</ul>
<ol start="2">
<li>Explicit Cursor(명시적 커서)</li>
</ol>
<ul>
<li>PL/SQL에서 프로그래머가 명시적으로 정의하고 제어하는 커서</li>
<li>ex) 데이터베이스에서 여러 행을 검색하고 처리할 때 사용</li>
</ul>
<h3 id="listener">Listener</h3>
<ul>
<li>클라이언트(사용자 프로세스)로부터 들어오는 연결 요청을 수신하는 네트워크 프로세스</li>
<li>사용자 프로세스가 데이터베이스와의 연결을 요청하면, listener가 그 요청을 받아 적절한 서버 프로세스를 할당한다.</li>
<li>Oracle Net Services 구성 요소 중 하나로, TCP/IP 프로토콜을 이용하여 통신한다.</li>
</ul>
<p><strong>역할</strong></p>
<ol>
<li>연결 요청 수신: 사용자 프로세스가 요청하면, listener가 이를 감지하여 연결을 수립한다.</li>
<li>프로세스 할당: 연결 방식에 따라 Dedicated Server Process 또는 Shared Server Process를 할당한다.</li>
</ol>
<ul>
<li>Dedicated Server: 사용자가 전용으로 사용하는 프로세스 </li>
<li>Shared Server: 여러 사용자가 하나의 서버 프로세스를 공유 </li>
</ul>
<h3 id="lreg-listener-registration-process">LREG (Listener Registration Process)</h3>
<ul>
<li>Instance를 리스너에 등록한다.</li>
<li>사용자 프로세스를 확인하고, 연결을 할당한다.<ul>
<li>Instance, Service, Handler 및 Endpoint를 Listener에 알린다.</li>
</ul>
</li>
<li><em>역할*</em></li>
<li>인스턴스가 시작될 때 Listener에게 자동으로 등록</li>
<li>클라이언트가 데이터베이스와 연결하려 할 때 올바른 서비스로 연결되도록 도와준다.</li>
</ul>
<h3 id="server-process">Server Process</h3>
<ul>
<li>데이터베이스 요청을 실제로 처리하는 프로세스</li>
<li>사용자 프로세스와 직접적으로 상호작용하여 SQL문을 처리한다.</li>
</ul>
<h3 id="lnnn-pooled-server-process">Lnnn (Pooled Server Process)</h3>
<ul>
<li>데이터베이스 상주 접속 Pooling으로 Client Request를 처리한다</li>
<li>데이터베이스 상주 접속 pooling에서는 Client는 접속 Broker Process에 접속한다.</li>
<li>접속이 Actrive상태가 되면, 접속 브로커는 상호성이 있는 Pool Server Process에 접속을 전달한다.</li>
<li>Pool Server Process는 Client접속에서 직접 네트워크 통신을 수행하고, Client가 서버를 해제하기까지 요구를 처리한다.</li>
<li>해제 후,  접속은 감시를 위해 Broker에 돌려주고 서버는 다른 Client에 자유롭게 대응하는 상태가 된다. </li>
</ul>
<h3 id="nnnn-connection-broker-process">Nnnn (Connection Broker Process)</h3>
<ul>
<li>데이터베이스에 상주 접속 Pooling으로 Idle 상태의 접속을 감시하고 Active한 접속을 전달한다.</li>
<li>데이터베이스 상주 접속 pooling에서는 Client는 접속 Broker Process에 접속한다.</li>
<li>접속이 Actrive상태가 되면, 접속 브로커는 상호성이 있는 Pool Server Process에 접속을 전달한다.</li>
<li>Pool Server Process는 Client접속에서 직접 네트워크 통신을 수행하고, Client가 서버를 해제하기까지 요구를 처리한다.</li>
<li>해제 후,  접속은 감시를 위해 Broker에 돌려주고 서버는 다른 Client에 자유롭게 대응하는 상태가 된다. </li>
</ul>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/2024b091-aaf0-4cb5-bc4b-a34920160afa/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/fefd557b-f038-47cc-b52a-2da9a822b312/image.png" /></p>
<h2 id="pga-program-global-area">PGA (Program Global Area)</h2>
<ul>
<li>Oracle Process전용의 데이터 및 제어 정보를 포함하여 비공유 메모리 영역이다. </li>
<li>Oracle Database에서는 Oracle Process의 기동 시에 PGA가 생성된다.</li>
<li>PGA는 Server Process마다 백그라운드 프로세스마다 존재한다. <ul>
<li>Server Process: User request를 만족하기 위해, Client Process 및 Oracle Database와 통신하는 오라클 프로세스. 서버 프로세스는 데이터베이스 인스턴스와 관련되어 있지만, Instance 일부는 아니다.</li>
</ul>
</li>
<li>각각의 PGA집합은 합계 Instance PGA 혹은 Instance PGA라고 불린다.</li>
<li>각각의 PGA가 아니라, 데이터베이스 초기화 파라미터를 사용해서 인스턴스 PGA 사이즈를 설정한다.</li>
</ul>
<h3 id="sql-work-areas">SQL Work Areas</h3>
<ul>
<li>PGA에 포함되는 메모리 영역으로, 특정 SQL 연산을 수행하기 위해 필요한 메모리 공간이다.</li>
<li>특히, 정렬(Sort), 해시 연산(Hash), 비트맵 병합(Bitmap Merge)등과 같은 작업을 수행할 때 사용된다.</li>
</ul>
<h4 id="sort-area">Sort Area</h4>
<ul>
<li><code>ORDER BY</code>, <code>GROUP BY</code>, <code>DISITNCT</code>, <code>INDEX CREATION</code> 등 정렬이 필요한 SQL문을 처리하기 위한 메모리 영역</li>
<li>주로 PGA 메모리를 사용하며, 메모리가 부족할 경우 디스크의 임시 테이블스페이스를 사용한다.<ul>
<li>즉, 메모리 사용량을 줄이고 디스크 I/O를 발생시킬 수 있다.</li>
</ul>
</li>
</ul>
<h4 id="hash-area">Hash Area</h4>
<ul>
<li>해시 조인과 같은 해시 연산을 수행하기 위해 사용되는 메모리 영역</li>
<li>특히 큰 데이터 집합을 결합할 때 효과적이다. </li>
</ul>
<p><strong>동작 방식</strong></p>
<ol>
<li>Build Phase (구축 단계)</li>
</ol>
<ul>
<li>작은 테이블이나 인덱스의 데이터를 읽어 해시 테이블을 생성한다.</li>
<li>이 테이블은 hash area라는 메모리 영역에 저장된다.</li>
</ul>
<ol start="2">
<li>Probe Phase (탐색 단계)</li>
</ol>
<ul>
<li>큰 테이블에서 데이터를 읽어 해시 테이블을 검색하여 매칭되는 데이터를 찾는다.</li>
</ul>
<ol start="3">
<li>디스크 사용 (필요 시)</li>
</ol>
<ul>
<li>메모리가 부족하면 임시 테이블스페이스를 사용하여 데이터를 저장하고 처리</li>
</ul>
<h4 id="bitmap-merge-area">Bitmap Merge Area</h4>
<ul>
<li>비트맵 인덱스를 사용하여 병합 연산을 수행할 때 사용되는 메모리 영역이다.<ul>
<li>비트 값으로 표현되어 있어, 검색 조건을 빠르게 결합할 수 있다.</li>
</ul>
</li>
</ul>
<h3 id="user-global-area-uga">User Global Area (UGA)</h3>
<ul>
<li>User session에 관련된 메모리</li>
<li>로그온 정보 등 세션 변수가 저장된 세션 메모리이며, OLAP Pool을 포함하기도 한다.<ul>
<li>OLAP Pool: Online 분산처리. OLAP는 이력 데이터의 동적인 디멘션(다양한 관점) 분석을 특징으로 한다.<ul>
<li>대량의 데이터를 빠르게 조회하고, 분석하는 데 사용되며 보통 데이터웨어하우스에 저장된 데이터를 대상으로 한다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h4 id="session-variables-세션-변수">Session Variables (세션 변수)</h4>
<ul>
<li>사용자 세션에서 저장되는 데이터로, 특정 사용자 또는 세션의 고유한 정보를 임시로 저장하는 메모리 영역</li>
<li><em>특징*</em></li>
<li>세션별로 독립적: 다른 사용자가 접근하거나 수정할 수 없음</li>
<li>일시적 데이터 저장: 세션이 종료되면, 메모리에서 사라진다.</li>
<li>세션 상태 관리: 예를 들어, 사용자가 특정 트랜잭션을 수행할 때의 상태를 유지하는 데 사용됨</li>
</ul>
<h4 id="olap-pool">OLAP Pool</h4>
<ul>
<li>Oracle의 OLAP(Online Analytical Processing)작업을 수행하기 위해 사용되는 메모리 공간</li>
<li>특히, 다차원 분석, 큐브 연산, 데이터 집계와 같은 복잡한 분석 작업을 수행할 때 사용됨</li>
</ul>
<h3 id="private-sql-area">Private SQL Area</h3>
<ul>
<li>특정 SQL문을 실행하기 위해 개별적으로 할당되는 메모리 영역</li>
<li>사용자가 SQL문을 실행하면 그 문에 대한 정보가 이 공간에 저장되고 관리된다. </li>
<li><h4 id="persistent-area-영구-영역">Persistent Area (영구 영역)</h4>
</li>
<li>SQL문 실행에 대한 정보를 지속적으로 저장하는 공간<ul>
<li>Shared Server 환경에서는 SGA의 UGA에서 관리된다. </li>
<li>Dedicated Server환경에서는 PGA에서 관리된다. </li>
</ul>
</li>
<li>ex) 바인드 변수 정보와 같은 데이터를 저장한다. </li>
<li>세션이 종료되기 전까지는 유지된다.</li>
<li><em>바인드 변수*</em></li>
<li>SQL문 내 Placeholder로, SQL문을 정상으로 수행하기 위해 유효한 값 혹은 값의 address와 치환되어야 할 필요가 있다.</li>
<li>바인드 변수를 사용하면 수행 시 입력 데이터 혹은 parameter를 받는 sql문을 생성할 수 있다.</li>
<li><code>SELECT * FROM employees WHERE employee_id = :v_empid;</code></li>
</ul>
<h4 id="runtime-area-실행-영역">Runtime Area (실행 영역)</h4>
<ul>
<li>SQL문이 실제로 실행되는 동안 사용되는 메모리 공간</li>
<li>SQL 실행 중에 필요한 정보들을 저장하고 관리한다.</li>
<li><em>특징*</em></li>
<li>실행 상태 정보 저장</li>
<li>정렬 작업, 조인 작업, 데이터 검색 결과 등을 포함</li>
<li>SQL문이 실행되는 동안만 유지되며, 실행이 완료되면 메모리에서 해제된다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/c5e5db94-eea4-4a47-ba56-0b1ba5001af3/image.png" /></p>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/d137fee5-b8b6-4a57-a43f-8419a16faf35/image.png" /></p>
<h3 id="rvwr-recovery-writer">RVWR (Recovery Writer)</h3>
<ul>
<li>Flashback Data를 Fast Recovery Area의 Flashback log에 주기적으로 씀<ul>
<li>주로 DML 작업이 발생할 때, 변경된 데이터 블록의 이전 이미지를 기록한다.</li>
</ul>
</li>
<li>RVWR는, SGA내 Flashback Buffer로부터 Flashback Data를 Flashback Log에 쓴다. 또한 Flashback Log를 생성하여 Flashback Log 자동관리용의 일부 task를 수행한다.</li>
</ul>
<h2 id="flashback-logs">Flashback Logs</h2>
<ul>
<li>Oracle Database의 Flashback기술을 사용하여 과거 시점으로 데이터베이스를 되돌릴 수 있도록 데이터를 저장하는 파일이다.</li>
<li>디스크의 Fast Recovery Area(FRA)에 저장된다.<ul>
<li><code>ALTER SYSTEM SET DB_FLASHBACK_RETENTION_TARGET = 1440;</code>: 24시간 (1440분)</li>
</ul>
</li>
<li>Flashback Thread : RAC 환경에서 사용되는 구조이다.<ul>
<li>다중 인스턴스 환경에서 각 인스턴스의 Flashback로그를 관리하는 단위</li>
<li>각 인스턴스마다 별도의 Flashback Thread가 존재한다.</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/eda1bbef-77ab-4983-9b97-9e1ccd05808e/image.png" /></p>
<h3 id="tmon-transport-monitor">TMON (Transport Monitor)</h3>
<ul>
<li>Oracle Database에서 데이터 전송과 관련된 작업을 모니터링하고 관리하는 백그라운드 프로세스</li>
<li>데이터 전송 모니터링, 오류 감지, 오류 복구, 전송 상태 관리</li>
<li>20c document에서 확인했을 때 사라진 프로세스인 것 같음...!</li>
</ul>
<h3 id="fbda-flashback-data-archiver">FBDA (Flashback Data Archiver)</h3>
<ul>
<li>Flashback Data Archive에 추적대상 테이블의 이력 row를 archive하여, archive 영역, 편성, 저장을 관리한다.</li>
<li>추적대상의 테이블을 변경할 트랜잭션이 commit되면, FBDA는 그 행의 사전 이미지를 archive에 insert한다.</li>
<li>FBDA는 현재 row에 메타데이터를 가지고 있으며, archive된 데이터의 size를 추적한다.</li>
<li>FBDA는 flashback Data Archive의 영역, 편성(tablespace의 파티션화), 저장에 대해서도 자동적으로 관리한다.</li>
<li>또한, FBDA 추적대상의 transaction의 archive 진척상황도 기록한다.</li>
</ul>
<h3 id="dbw0j-dbwr-database-writer">DBW0,j (DBWR; Database Writer)</h3>
<ul>
<li>변경된 블록을 데이터베이스, Buffer Cache로부터 데이터파일에 기록한다.</li>
<li>DBWR 프로세스에서는 주로 블록 데이터를 디스크에 기록한다.</li>
<li>또한, 체크포인트, 파일 open 동기화, block 쓰기 기록 logging도 처리한다.</li>
<li>많은 경우, dbwr 프로세스에서 기록되는 블록은 disk전체에 분산된다.
그렇기 때문에 이 쓰기는 LGWR가 수행되는 순차적 기록보다도 늦어질 가능성이 있다.</li>
<li>효율이 향상되는 경우에는 dbwr 프로세스에서 멀티블록 쓰기가 실행되는 경우이다.</li>
<li>Multi block 쓰기에서 기록되는 블록 수는 OS에 따라 다르다.</li>
<li>dbwr 프로세스 수는 <code>DB_WRITER_PROCESSES</code> 초기화 파라미터에서 지정한다.</li>
<li>1부터 100 데이터베이스 Writer process를 지정할 수 있다.</li>
<li><em>BW36..99*</em></li>
<li>최초 36의 dbwr 프로세스명은 <code>DBW0-DBW9 및 DBWa-DBWz</code>가 된다. 37<del>100까지 dbwr 프로세스명은 `BW36</del>BW99`가 된다.</li>
<li>데이터베이스는 <code>DB_WRITER_PROCESSES</code>파라미터에 대해 적절한 디폴트 설정을 선택하거나, 또는 유저 지정 설정을 CPU와 프로세서 Group 수에 기반하여 조정한다.</li>
<li><a href="https://docs.oracle.com/cd/F32587_01/refrn/DB_WRITER_PROCESSES.html#GUID-75774634-3B5E-49F8-A5C5-65923F596845">DB_WRITER_PROCESS</a></li>
<li>1개의 인스턴스에 대해 DBWR 프로세스 수의 초기값을 지정한다. </li>
</ul>
<h2 id="flash-cache">Flash Cache</h2>
<ul>
<li>Oracle Database가 데이터블록을 메모리 대신 플래시메모리(SSD)에 저장하여 I/O 성능을 개선하기 위한 기술</li>
<li>Oracle Exadata 또는 Oracle Database Smart Flash Cache 환경에서 사용된다.</li>
<li><em>특징*</em></li>
<li>디스크 I/O 부하 감소<ul>
<li>주로 읽기 작업의 성능을 개선한다.</li>
<li>읽기 캐시로 사용되며, 데이터를 디스크로부터 읽기 전에 먼저 Flash Cache를 검색한다.</li>
</ul>
</li>
<li>Automatic Storage Management(ASM)과 연동<ul>
<li>Oracle ASM 환경에서 디스크 그룹으로 구성된다.</li>
</ul>
</li>
<li>SGA 확장 기능 (SGA Extension)<ul>
<li>기존의 메모리 캐시(Buffer Cache)를 보완하여 더 많은 데이터를 캐싱할 수 있다. </li>
</ul>
</li>
<li>Transparent 사용<ul>
<li>애플리케이션 레벨에서 수정 없이 자동으로 사용된다. </li>
</ul>
</li>
</ul>
<h3 id="ckpt-checkpoint-process">CKPT (Checkpoint Process)</h3>
<ul>
<li>Checkpoint에서 DBWn에 시그널을 보내, Database의 모든 Datafile과 controlfile을 update하여 최신의 Checkpoint를 나타낸다.</li>
<li>특정 시점에, CKPT는 사용 완료된 Buffer를 디스크로 기록하도록 DBWn에 메시지를 전송하고 체크포인트 request를 시작한다.</li>
<li>각각의 checkpoint request 완료 시에 CKPT는 데이터 파일 header 및 controlfile 을 update하여 최신의 checkpoint를 기록한다.</li>
<li>CKPT는 메모리 size가 <code>PGA_AGGREGATE_LIMIT</code>초기화 파라미터의 값을 초과하는지 여부를 3초마다 체크하여, 초과한 경우 <code>PGA_AGGREGATE_LIMIT</code> 값에 기술된 Action을 수행한다.</li>
</ul>
<h4 id="checkpoint가-발생하는-시점">Checkpoint가 발생하는 시점</h4>
<ul>
<li>Log Switch 발생 시 </li>
<li>dba가 수동으로 체크포인트를 발생시킬 때</li>
<li>FAST_START_MTTR_TARGET 사용 시 : 빠른 복구를 위해 지정된 시간 내 체크포인트 발생 </li>
<li>데이터베이스를 정상종료할 때 (SHUTDOWN IMMEDIATE/NORMAL)</li>
<li>ARCHIVELOG 모드일 때 : 아카이브로그가 생성될 때 체크포인트가 발생 </li>
</ul>
<h3 id="acms-atomic-control-file-to-memory-service">ACMS (Atomic Control File to Memory Service)</h3>
<ul>
<li>Oracle RAC 환경에서 인스턴스 간 컨트롤 파일 업데이트의 일관성을 유지하는 백그라운드 프로세스. </li>
<li>Oracle RAC 환경 내 모든 instance 상에 대응하는 SGA와, controlfile resource로의 update 일관성이 유지되도록 조정한다.</li>
<li>ACMS 프로세스는 조정된 호출 소스와 연계하여 장애상황에서도 Oracle RAC 내 모든 인스턴스에서 확실하게 작업이 수행되도록 한다. </li>
<li>ACMS 프로세스는 분산 작업이 call된다. (Distributed Call:분산 호출)<ul>
<li>RAC 환경에서 여러 인스턴스 간의 분산 작업을 호출한다.</li>
</ul>
</li>
<li>그 결과, 이 프로세스는 다양한 작업을 할 가능성이 있다. 보통, ACMS 동작은 인스턴스간 일부 작업에 대응되는, 소규모의 비 block화 상태 변경에 한정되어 있다. </li>
</ul>
<h3 id="lgwr-redo-log-writer">LGWR (Redo Log Writer)</h3>
<ul>
<li>Online Redo Log에 Redo Entry를 기록함<ul>
<li>변경된 데이터(DML 및 일부 DDL)에 대한 로그 기록을 Redo Log Buffer에 생성한다.</li>
<li>이후 이 데이터를 Online Redo Log 파일로 기록한다.</li>
<li>기록된 정보는 트랜잭션이 커밋이 되었는지 여부와 상관없이 저장한다.</li>
</ul>
</li>
<li>Multi Processor System 상에서 Worker Process를 생성하고, Redo Log로의 쓰기 성능을 개선한다.</li>
<li>LGWR Worker는 SYNC 스탠바이 접속 주소가 있는 경우 사용되지 않는다.</li>
<li>가능한 프로세스는 LG00-LG99. </li>
<li>트랜잭션 커밋 처리<ul>
<li>사용자가 commit 명령어를 실행하면, LGWR는 Redo Log Buffer에 저장된 트랜잭션 정보를 Online Redo Log 파일로 기록한다.</li>
<li>기록이 완료된 후 사용자에게 커밋 성공 메시지가 반환된다.</li>
</ul>
</li>
</ul>
<h3 id="tt00-zz-ttnn-redo-transport-slave">TT00-zz (TTnn; Redo Transport Slave)</h3>
<ul>
<li>Oracle Data Guard 환경에서, Primary Database의 Redo Log 데이터를 Standby Database로 전송하는 백그라운드 프로세스 그룹이다.</li>
<li>병렬 프로세스로 운영하며, 전송 성능을 개선한다.</li>
<li>ASYNC 전송용으로 구성된 Remote Standby 접속 주소로 현재 온라인 및 스탠바이 Redolog로부터 REDO를 전송함</li>
<li>복수 프로세스로서 실행 가능하다. (nn은, 00-ZZ)</li>
<li>Database Instance, Data Guard</li>
</ul>
<blockquote>
<p><strong>동작 방식</strong></p>
</blockquote>
<ol>
<li>Primary Database에서 Redo Data 수집</li>
</ol>
<ul>
<li>Redo Log Buffer 또는 Online Redo Log Files에서 데이터를 읽는다.</li>
</ul>
<ol start="2">
<li>Redo Data 전송: 여러 <code>TTnn</code> 프로세스가 병렬로 데이터를 Standby Database로 전송한다.</li>
<li>Standby Database로 데이터 적용<ul>
<li>Standby Database의 RFS(Remote File Server) 프로세스가 데이터를 받아 디스크에 기록한다.</li>
</ul>
</li>
</ol>
<blockquote>
<ul>
<li>관련 설정: ASYNC/SYNC 설정</li>
</ul>
</blockquote>
<ul>
<li><code>ASYNC</code> 모드: Redo 전송의 성능을 극대화(일부 손실 가능)</li>
<li><code>SYNC</code> 모드: 데이터 손실 없이 전송하나, 성능 저하 가능<pre><code class="language-SQL">ALTER SYSTEM SET LOG_ARCHIVE_DEST_1='LOCATION=/u01/app/oracle/archivelog/';
ALTER SYSTEM SET LOG_ARCHIVE_DEST_2='SERVICE=standby SYNC';</code></pre>
</li>
</ul>
<h3 id="archn-archiver-process-n09-or-nat">ARCHn (Archiver Process) n=0..9 or n=a..t</h3>
<ul>
<li>Online Redo Log파일을 Archive Redo Log 파일로 디스크에 백업하는 백그라운드 프로세스</li>
<li>Oracle Database가 ARHICVELOG Mode로 설정되어 있어야 한다. </li>
<li>31 possible destinations: 최대 31개 프로세스. 여러 목적지로 동시에 데이터를 아카이브한다.</li>
<li><a href="https://imbang.net/2019/05/18/%EC%98%A4%EB%9D%BC%ED%81%B4-%EC%95%84%EC%B9%B4%EC%9D%B4%EB%B8%8C-%EB%AA%A8%EB%93%9Carchive-log-mode-%EB%B3%80%EA%B2%BD-%EB%B0%A9%EB%B2%95/">오라클 아카이브모드 적용</a></li>
</ul>
<h2 id="archived-redo-log-files">Archived Redo Log Files</h2>
<ul>
<li>Online Redo Log Files의 백업 파일로, 데이터베이스를 복구하거나 Flashback 기능을 위해 사용되는 로그 파일이다.</li>
<li>주 저장 위치: <code>LOG_ARCHIVE_DEST_n</code> 으로 설정된 경로<ul>
<li>사용 목적: RMAN 백업, Flashback 기능, Point-In-Time Recovery (PITR)</li>
</ul>
</li>
</ul>
<h2 id="redo-log-files">Redo Log Files</h2>
<ul>
<li>데이터 변경 사항을 기록하여 장애 발생 시 복구하는 데 사용되는 파일.<ul>
<li>LGWR(Redo Log Writer)에 의해 기록된다.</li>
<li>로그 스위치: 하나의 파일이 가득 차면, 다음 파일로 전환한다.</li>
<li><code>DB_CREATE_ONLINE_LOG_DEST_n</code> 파라미터를 통해 지정된다. </li>
</ul>
</li>
<li>Redo Thread: RAC 환경에서 각 인스턴스별로 할당되는 독립적인 Redo Log 스트림</li>
</ul>
<h3 id="ctwr-change-tracking-writer">CTWR (Change Tracking Writer)</h3>
<ul>
<li>RMAN 백업 성능을 향상시키기 위해, 블록 변경 사항을 추적하는 백그라운드 프로세스</li>
</ul>
<ol>
<li>블록 변경 추적(Block Change Tracking)</li>
</ol>
<ul>
<li>데이터 파일의 변경 사항을 추적하여 전체 데이터 파일을 읽지 않고도 빠르게 백업할 수 있도록 한다.</li>
</ul>
<ol start="2">
<li>백업 최적화</li>
</ol>
<ul>
<li>변경된 블록만 백업하므로 백업 시간이 크게 단축된다. </li>
</ul>
<ol start="3">
<li>동작 방식</li>
</ol>
<ul>
<li><code>CTWR</code> 프로세스는 변경 사항을 별도의 파일(change Tracking File)에 기록한다.</li>
</ul>
<h2 id="rman-process">RMAN Process</h2>
<h3 id="mml-meida-management-layer-routines">MML (Meida Management Layer routines)</h3>
<ul>
<li>RMAN과 테이프 백업 장치 또는 스토리지 시스템 간 통신을 위한 인터페이스</li>
<li>외부 백업 장치와의 연결을 관리하는 역할</li>
<li>Oracle Secure Backup (OSB), NetBackup, Tivoli 등</li>
</ul>
<h3 id="osb-oracle-secure-backup">OSB (Oracle Secure Backup)</h3>
<ul>
<li>오라클에서 제공하는 전용 백업 솔루션으로, RMAN관의 완벽한 통합을 제공</li>
<li>테이프 드라이브 또는 클라우드 스토리지로 데이터를 백업하낟.</li>
</ul>
<h4 id="tape-backup">Tape backup</h4>
<ul>
<li>백업 데이터를 물리적 테이프 장치에 저장</li>
<li>대용량 데이터 백업 및 장기 보관용으로 사용</li>
<li>비용 효율적이지만, 복구 속도는 느리다.</li>
<li>오프라인으로 보관하기 좋다.</li>
</ul>
<h4 id="storage-cloud">Storage Cloud</h4>
<ul>
<li>클라우드 스토리지 (예: Oracle Cloud, AWS S3) 에 백업을 저장.</li>
<li>확장성이 뛰어나며, 물리적 장치 없이 원격으로 데이터 보호 가능.</li>
</ul>
<h3 id="image-copies">Image Copies</h3>
<ul>
<li>데이터 파일의 완전한 물리적 복사본 을 만드는 백업 방식</li>
<li>원본 파일과 동일한 형태로 저장되며, 데이터 파일을 복구 시 직접 사용할 수 있음</li>
<li>백업 과정이 느리지만, 복구 속도는 빠름.</li>
<li>BACKUP AS COPY 명령어로 생성.</li>
</ul>
<h3 id="backup-sets">Backup Sets</h3>
<ul>
<li>데이터베이스 파일을 RMAN에서 압축하고 저장하는 논리적 백업 방식.</li>
<li>이미지 복사본과 달리 압축, 병렬 처리 등이 가능하여 저장 공간을 줄일 수 있음.</li>
<li>BACKUP AS BACKUPSET 명령어로 생성.</li>
</ul>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/64f01588-9233-4624-851f-8c55c15dde28/image.png" /></p>
<ul>
<li><a href="https://docs.oracle.com/cd/F39414_01/cncpt/memory-architecture.html#GUID-4FF66585-E469-4631-9225-29D75594CD14">메모리 아키텍처</a></li>
</ul>
<blockquote>
<p><strong>SGA 내 구성 요소</strong></p>
<ol>
<li>Database Buffer Cache (데이터베이스 버퍼 캐시)</li>
<li>Shared Pool (공유 풀)</li>
<li>Large Pool(대형 풀)</li>
<li>Java Pool(자바 풀)</li>
<li>Streams Pool(스트림 풀)</li>
<li>Flash Buffer Area(플래시 버퍼 영역-&gt; Exadata 환경에서 사용)</li>
</ol>
</blockquote>
<h2 id="flashback-buffer">Flashback Buffer</h2>
<ul>
<li>Flashback Database 기능을 지원하기 위해 SGA 내에서 변경사항을 일시적으로 저장하는 메모리 공간. Flashback Log를 생성하여 특정 시점으로 데이터베이스를 복구할 수 있도록 한다.</li>
<li>사용자가 데이터를 변경할 때, 변경 사항이 Redo Log Buffer 와 함께 Flash Back Buffer 에도 기록됩니다.</li>
<li>RVWR (Recovery Writer) 프로세스가 이 내용을 Flashback Log 로 기록하여 디스크에 저장합니다.</li>
<li>Flashback 기능이 활성화되면 항상 작동하며, db_flashback_retention_target 값에 따라 보관 기간이 결정됩니다.</li>
</ul>
<p><strong>관련 파라미터</strong></p>
<ul>
<li><code>db_flashback_retention_target</code>: Flashback Log를 보관할 시간 (분 단위).</li>
<li><code>db_recovery_file_dest</code>: Flashback Log가 저장되는 위치 (Fast Recovery Area).</li>
<li><code>db_recovery_file_dest_size</code>: Flashback Log 저장 공간의 최대 크기.</li>
</ul>
<h2 id="redo-log-buffer">Redo Log Buffer</h2>
<ul>
<li>사용자가 데이터를 변경할 떄 발생하는 모든 변경 사항을 기록하는 임시 저장 공간</li>
<li>LGWR (Log Writer) 는 Redo Log Buffer의 내용을 Online Redo Log Files로 기록하는 백그라운드 프로세스</li>
</ul>
<p><strong>특징</strong> </p>
<ul>
<li>메타데이터 기록: 변경된 데이터 자체가 아닌 변경 내용에 대한 정보(INSERT, UPDATE, DELETE)</li>
<li>LGWR 프로세스 사용: commit명령어가 발생할 때 즉시 디스크로 기록</li>
<li><em>주 목적*</em>: 트랜잭션이 성공적으로 완료되었다는 것을 보장하기 위해 사용하며 복구 시, 트랜잭션 단위로 데이터를 되돌릴 수 있게 한다. </li>
</ul>
<blockquote>
<p><strong>동작 방식</strong></p>
</blockquote>
<ol>
<li>트랜잭션 발생: 사용자가 데이터를 변경하면, 그 변경 사항이 Redo Log Buffer 에 기록됩니다.</li>
<li>커밋 요청 (COMMIT): 사용자가 COMMIT 을 실행하면, LGWR (Log Writer) 가 Redo Log Buffer 의 내용을 Online Redo Log Files (디스크) 로 기록합니다.</li>
<li>저장 완료: 저장이 완료되면 사용자에게 트랜잭션이 성공적으로 완료되었다는 응답이 돌아옵니다.</li>
</ol>
<h1 id="database-buffer-cache">Database Buffer Cache</h1>
<ul>
<li>디스크의 데이터 파일에서 읽어온 데이터 블록의 복사본을 일시적으로 저장하여 성능을 개선하는 캐시</li>
<li>데이터 파일로부터 읽힌 Data Block Copy 를 저장하는 memory 영역</li>
<li>디스크 I/O를 줄이기 위해 데이터 파일에서 읽은 데이터 블록의 복사본을 캐시하는 것이다.</li>
<li>Buffer: 현재 사용되고 있는 데이터 블록 혹은 최근 사용된 데이터 블록이 Buffer Manager에 의해 일시적으로 캐시되는 메인 메모리 주소를 말한다.<ul>
<li>현재 사용중이거나 최근에 사용된 데이터 블록이 임시로 캐시되는 메모리 주소를 의미한다.</li>
<li>이 메모리 주소는 버퍼관리자(Buffer Manager)에 의해 관리된다.</li>
</ul>
</li>
<li>데이터베이스 인스턴스에 동시접속된 사용자는 모두 버퍼 캐시로의 access를 공유한다.</li>
</ul>
<p><strong>특징</strong></p>
<ul>
<li>실제 데이터 블록 보관: 테이블 데이터, 인덱스 정보 등 실제 데이터를 메모리에 보관한다.</li>
<li>지연 기록(Deffered Write): 데이터 변경 사항이 발생하면, 즉시 디스크로 기록되지 않고, 메모리에만 반영된다.</li>
<li>DBWR 프로세스 사용(Database Writer): 주기적으로 또는 특정 이벤트 발생 시 변경된 데이터 블록을 디스크로 기록한다.</li>
<li>캐싱 목적: 디스크I/O를 줄이고, 데이터 접근 속도 높임</li>
</ul>
<p><strong>동작 방식</strong></p>
<ol>
<li>데이터 조회: 사용자가 데이터를 요청할 때, Database Buffer Cache 에서 먼저 찾습니다.</li>
</ol>
<ul>
<li>캐시에 없으면 디스크에서 읽어와 캐시에 저장합니다.</li>
</ul>
<ol start="2">
<li>데이터 변경: 변경된 데이터는 Database Buffer Cache 에만 반영되고, 디스크에는 기록되지 않습니다. (지연 기록)</li>
<li>DBWR 프로세스 작동: 주기적으로 또는 특정 이벤트가 발생하면 변경 사항을 디스크의 Data Files 에 기록합니다.</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/8216c0e5-a7b8-4877-ad45-69e8f0b228a7/image.png" /></p>
<h2 id="database-buffer-cache-작동-방식">Database Buffer Cache 작동 방식</h2>
<ol>
<li>사용자가 데이터 블록을 읽을 때:</li>
</ol>
<ul>
<li>Database Buffer Cache 를 먼저 검색</li>
<li>캐시에 없으면 디스크에서 읽어와서 캐시에 저장.</li>
</ul>
<ol start="2">
<li>사용자가 데이터를 수정할 때:</li>
</ol>
<ul>
<li>Database Buffer Cache 에서 변경 사항을 반영.</li>
<li>변경 내용은 즉시 디스크에 기록되지 않음.</li>
</ul>
<ol start="3">
<li>변경 사항이 많아지면:</li>
</ol>
<ul>
<li>DBW (Database Writer) 프로세스 가 백그라운드에서 변경된 데이터 블록을 디스크로 기록</li>
</ul>
<h2 id="flash-buffer-area">Flash Buffer Area</h2>
<ul>
<li>Flash Buffer Area 는 Exadata 환경에서 사용되는 고속 캐시</li>
<li>플래시 메모리(SSD) 기반의 고속 캐시 영역으로, Oracle Exadata 또는 Oracle Database Smart Flash Cache 환경에서 사용되는 메모리 구조</li>
<li>디스크 I/O를 줄이기 위해 자주 사용되는 데이터 블록을 메모리 대신 플래시 메모리에 저장하여 빠르게 접근할 수 있도록 한다. </li>
<li><em>Flash LRU Chain*</em></li>
<li>LRU(Least Recently Used)알고리즘을 사용하여 데이터를 관리한다.</li>
</ul>
<h3 id="default-flash-lru-chain">DEFAULT flash LRU Chain</h3>
<ul>
<li>플래시 버퍼 영역에서 기본적으로 데이터를 관리하는 방식이다.</li>
<li>모든 데이터가 기본적으로 이 영역에 저장되며, 자주 사용되지 않으면 자동으로 제거된다.</li>
<li>일반적인 테이블, 인덱스 데이터가 캐싱된다.</li>
<li>블록이 통상 cache되는 장소이다. 수동으로 개별로 pool을 구성하지 않는 경우에는 DEFAULT Pool이 유일한 버퍼 풀이 된다.</li>
<li>그 외 pool 옵션 구성에 의해 defualt 풀은 영향을 받지 않는다. </li>
</ul>
<h3 id="keep-flash-lru-chain">KEEP flash LRU Chain</h3>
<ul>
<li>중요하거나 자주 사용되는 데이터를 장기간 보존하기 위해 사용하는 영역</li>
<li>DEFUALT LRU chain과는 달리, 오래 사용되지 않아도 제거되지 않도록 설정된다.</li>
<li>주로 hot data를 유지하기 위해 사용된다.</li>
</ul>
<h2 id="buffer-pools">Buffer Pools</h2>
<ul>
<li>Buffer Pools 는 데이터베이스의 디스크 I/O를 줄이기 위해 사용되는 메모리 캐시입니다.</li>
<li>SGA의 Data Buffer Cache에서 데이터를 캐싱하기 위해 사용하는 메모리 영역</li>
<li>디스크에서 데이터를 읽을 떄, 데이터를 Buffer Pool에 저장하여 메모리에서 빠르게 접근할 수 있도록 한다.
1) Defualt Buffer Pool</li>
<li>대부분의 데이터가 저장되는 기본 버퍼 풀</li>
<li>특별한 설정 없이 모든 데이터 블록이 저장되는 영역
2) Keep Buffer Pool</li>
<li><strong>중요하거나, 자주 사용되는 데이터 블록을 오래 유지하기 위해 사용하는 버퍼 풀</strong></li>
<li>테이블이나 인덱스에서 자주 읽히는 데이터를 유지하여 성능을 극대화</li>
<li><code>ALTER TABLE my_table STORAGE(BUFFER_POOL KEEP);</code>
3) Recycle Buffer Pool</li>
<li><strong>임시로 사용되는 데이터를 빠르게 제거하기 위한 버퍼 풀</strong></li>
<li>디스크 I/O 성능을 향상시키기 위해 사용되지 않거나, 잘못된 데이터를 빨리 버린다.</li>
<li><code>ALTER TABLE temp_table STORAGE (BUFFER_POOL RECYCLE);</code></li>
</ul>
<h2 id="non-defualt-buffer-pools">Non Defualt Buffer Pools</h2>
<ul>
<li>표준 블록 크기(보통 8kb)가 아닌, 다른 블록 크기를 사용하는 데이터 파일을 캐싱하기 위한 버퍼 풀</li>
<li>특정 테이블스페이스가 다른 블록 크기를 사용한다면, 그에 맞게 적절한 buffer Pool을 만들어야 한다.</li>
<li><em>Non-Default Buffer Pool의 종류*</em></li>
<li>2k: 더 작은 블록 크기를 사용하는 테이블스페이스용. </li>
<li>4k: 더 작은 블록 크기를 사용하는 경우</li>
<li>16k: 데이터웨어하우스, 인덱스 등에서 사용</li>
<li>32k: 대규모 블록 크기를 사용하는 테이블스페이스용</li>
</ul>
<hr />
<h1 id="others">Others</h1>
<h3 id="oracle-resource-manager">Oracle Resource Manager</h3>
<ul>
<li>데이터베이스 내에서 리소스(CPU, 메모리, I/O 등)를 효율적으로 관리하기 위한 기능</li>
<li>Resource Manager의 역할</li>
</ul>
<blockquote>
</blockquote>
<p><strong>1. 자원 할당 제어 (CPU, 메모리, I/O)</strong></p>
<ul>
<li>데이터베이스에서 여러 사용자가 동시에 작업할 때, 특정 작업이 과도하게 자원을 사용하지 않도록 제어합니다. <p></p></li>
<li><em>2. Resource Plan (리소스 계획) 설정*</em></li>
<li>리소스 사용 우선순위 및 할당량을 정의</li>
<li>예를 들어, 중요한 백업 작업(RMAN)이나 중요한 보고서 쿼리에 더 많은 리소스를 할당하도록 설정할 수 있습니다.<p></p></li>
<li><em>3. Consumer Group (소비자 그룹)*</em></li>
<li>사용자가 작업을 실행할 때 할당된 리소스 그룹으로, 동일 그룹 내에서 리소스를 공유합니다.<p></p></li>
<li><em>4. Scheduler와의 협력 (VKRM)*</em></li>
<li>Resource Manager는 VKRM을 사용하여 설정된 Resource Plan을 기반으로 CPU 리소스를 조정합니다.</li>
</ul>
<h3 id="oracle-goldengate">Oracle Goldengate</h3>
<ul>
<li>Oracle 데이터베이스 및 비Oracle 데이터베이스 간의 데이터를 실시간으로 복제하고 동기화하는 고성능 데이터 복제 솔루션이다.</li>
<li>기업에서 중요한 데이터를 실시간으로 전송하거나, 데이터 웨어하우스 환경으로 복제할 때 주로 사용된다.</li>
<li>Oracle Streams는 오래된 방식이며, Oracle 12c 이후에 지원되지 않음</li>
</ul>
<p><strong>구성요소(component)</strong></p>
<ul>
<li>Extract (추출) : 원본 데이터베이스에서 데이터를 캡쳐하여 로그 파일로 저장</li>
<li>Trail Files(트레일 파일): 추출된 데이터를 임시로 저장하는 파일</li>
<li>Data Pump (데이터 펌프) : 트레일 파일을 다른 위치로 전송</li>
<li>Replicat(적용): 트레일 파일의 데이터를 목적지 데이터베이스에 적용</li>
</ul>
<h3 id="pmem-file-store-영구-메모리-파일-저장소">PMEM File Store; 영구 메모리 파일 저장소</h3>
<ul>
<li>Oracle Database에서 사용할 수 있는 비휘발성 메모리 저장소</li>
<li>디스크가 아닌 메모리에 직접 데이터를 저장하고 관리할 수 있도록 한다.</li>
</ul>
<p><strong>특징</strong></p>
<ol>
<li>빠른 데이터 접근 (Fast Data Access)</li>
</ol>
<ul>
<li>디스크를 거치지 않고 메모리에서 직접 데이터를 읽고 쓰기 때문에 성능이 뛰어납니다.</li>
</ul>
<ol start="2">
<li>Buffer Cache 우회 (Bypassing Buffer Cache)</li>
</ol>
<ul>
<li>데이터 파일이 PMEM 블록 에 매핑되면 Buffer Cache 메커니즘을 우회 할 수 있습니다.</li>
<li>이렇게 하면 불필요한 I/O 작업을 피하고 성능을 개선합니다.</li>
</ul>
<ol start="3">
<li>버퍼 헤더 (Buffer Header)</li>
</ol>
<ul>
<li>PMEM 블록에 대응하는 메타데이터를 저장하여, Oracle Database에서 쉽게 접근하고 관리할 수 있게 합니다.</li>
</ul>
<h3 id="deferred-writes-지연-기록">Deferred Writes 지연 기록</h3>
<ul>
<li>DBWR 프로세스가 백그라운드에서 변경 사항을 디스크로 기록 </li>
</ul>
<h3 id="buffer-관련된거-구분">Buffer 관련된거 구분</h3>
<ul>
<li><code>Flashback Buffer</code> Flashback 기능을 위해 데이터 변경 사항을 기록하는 메모리 공간 (SGA 내부).</li>
<li><code>Flash Buffer Area</code> SSD를 활용하여 읽기 성능을 최적화하는 캐시 메모리 (외부 플래시 메모리).</li>
<li><code>Database Buffer Cache</code> (버퍼 캐시) 는 데이터 파일에서 읽은 데이터를 메모리에 저장하여 성능을 개선하는 구조.</li>
</ul>