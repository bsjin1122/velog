<blockquote>
<p>출처</p>
</blockquote>
<ul>
<li><a href="https://www.oracle.com/technetwork/jp/ondemand/database/db-new/120517-consultant-shinzui-part2-1641035-ja.pdf">오라클 컨설턴트가 말하는 성능분석의 실상 part2</a></li>
<li><a href="https://www.oracle.com/assets/20140716-performance-2252985-ja.pdf">오라클 컨설턴트가 말하는 성능분석의 실상 part1</a></li>
</ul>
<h1 id="성능분석이란">성능분석이란?</h1>
<ul>
<li>시스템의 성능 문제(응답 지연, 처리량 저하 등) 을 분석하는 과정</li>
<li>성능 분석의 목적은 시스템의 병목 현상을 파악하고, 적절한 대응을 통해 성능을 개선하는 것</li>
<li>성능 분석에는 Reactive(사후 대응형)과 Proactive(사전 예방형) 두 가지 방식이 있다.</li>
</ul>
<h2 id="reactive한-성능-분석사후대응형">Reactive한 성능 분석(사후대응형)</h2>
<ul>
<li><p><strong><code>문제가 발생한 후 원인을 분석하고 대응하는 방식</code></strong></p>
</li>
<li><p>ex) 데이터베이스 트랜잭션이 지연됨 / cpu 사용률이 갑자기 증가 </p>
</li>
<li><p>목적: 문제가 발생한 후에 그 원인(병목현상, 리소스 부족 등)을 분석하여 해결</p>
</li>
<li><p>특징: 이미 발생한 성능 문제를 분석하여 대응하는 방식, 문제를 해결할 수 있지만, 사전에 예방하지 못함</p>
</li>
<li><p>단점: 문제가 발생한 후 대응하기 때문에 장애 발생 가능성이 있음</p>
</li>
</ul>
<h2 id="proactive한-성능분석사전예방형">Proactive한 성능분석(사전예방형)</h2>
<ul>
<li><p><strong><code>문제가 발생하기 전에 미리 성능을 분석하고, 최적화하는 방식</code></strong></p>
</li>
<li><p>예제 상황: 현재는 문제가 없지만, 미래에 CPU, 메모리, 스토리지 부족 가능성이 있음</p>
</li>
<li><p>주기적으로 성능 모니터링 및 튜닝을 수행</p>
</li>
<li><p>성능 저하가 발생하기 전에 미리 문제를 감지하고 예방</p>
</li>
<li><p><strong>특징</strong></p>
<ul>
<li>시스템의 상태를 정기적으로 분석하고 튜닝을 수행</li>
<li>성능 문제를 사전에 방지</li>
</ul>
</li>
<li><p>** 단점**</p>
<ul>
<li>성능 분석 및 모니터링에 추가적인 비용과 시간이 필요하다.</li>
</ul>
</li>
<li><p>시스템을 이용하고 있는 서비스에서 reponse 지연/처리량 저하 등의 성능 문제나 리소스 부족 등에 따른 예기치못한 장애를 미연에 방지하기 위해, 정기적으로 실시한다.</p>
</li>
<li><p>문제가 발생하기 전에 대응하는, 사전적인 성능분석</p>
</li>
</ul>
<h2 id="성능분석이란-1">성능분석이란?</h2>
<ul>
<li>2개의 성능 분석이 중요한 이유
<img alt="" src="https://velog.velcdn.com/images/greendev/post/55130384-3a26-4df9-b284-beb4edbdbc70/image.png" /></li>
</ul>
<blockquote>
<ul>
<li>Reactive: 몸이 안 좋네.. 독감이므로 약을 드리죠!</li>
</ul>
</blockquote>
<ul>
<li><p>Proactive: 달에 한 번 정기검진이다. -- 나빠질 곳이 있는지를 체크합시다!</p>
</li>
<li><p><code>사람</code>을 <code>시스템</code>, <code>병원</code>을 <code>성능분석</code>으로 치환하면 성능분석에서는 2개의 패턴으로 중요하다는 것을 알 수 있다.</p>
</li>
</ul>
<h2 id="reactive한-성능분석">Reactive한 성능분석</h2>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/fa49e29e-9b40-49bb-ae07-a3868c3e9d7b/image.png" /></p>
<blockquote>
<p><strong>안 좋은 접근</strong></p>
</blockquote>
<ul>
<li><ol>
<li>성능이 안좋은 문제 때문에, 침착하게 대응할 수 없다</li>
</ol>
</li>
<li><ol start="2">
<li>성능이 개선될 가능성이 있는 대책을 잡히는대로 실시</li>
</ol>
</li>
<li><ol start="3">
<li>미해결</li>
</ol>
</li>
</ul>
<blockquote>
<p><strong>올바른 접근</strong></p>
</blockquote>
<ul>
<li><ol>
<li>상황파악 -- 조회할 정보를 결정함</li>
</ol>
</li>
<li><ol start="2">
<li>고찰/분석</li>
</ol>
<ul>
<li>분석결과를 근거로 원인 추궁</li>
<li>문제해결 방법의 고찰</li>
</ul>
</li>
<li><ol start="3">
<li>해결 :)</li>
</ol>
</li>
</ul>
<h2 id="proactive한-성능분석">Proactive한 성능분석</h2>
<p><strong>체크포인트</strong></p>
<ul>
<li>baseline 활용<ul>
<li>performance를 비교하기 위해서, 정상으로 동작하고 있는 정보를 조회, 베이스라인에 의해 장애 시에 정상적일 때와의 차이를 비교해서 문제점을 파악하는 것이 가능하다.</li>
</ul>
</li>
<li>Capacity Planning<ul>
<li>평소부터 정기적으로 성능분석을 행하는 것으로, 향후 리소스의 고갈을 예방하고 미래의 resource 부족에 대비하여 사전에 준비하는 것이 가능하다.</li>
</ul>
</li>
</ul>
<h2 id="성능-분석에서의-필요-정보">성능 분석에서의 필요 정보</h2>
<ul>
<li>성능분석을 실시하기 위한 필요한 정보</li>
<li>특정 시스템 뿐만 아니라, 시스템 전체의 성능 정보를 조회
<img alt="" src="https://velog.velcdn.com/images/greendev/post/fd1e60d2-17eb-43bc-9fad-18461b797f48/image.png" /></li>
<li>*<span style="color: blue;">각 레이어별 리소스(CPU, Memory, Disk, Network, DB) 정보를 조회</span></li>
<li>*</li>
</ul>
<h2 id="awr-레포트를-사용한-성능분석">AWR 레포트를 사용한 성능분석</h2>
<ul>
<li>proactive에 정기검진을 받은 후, 중요한 것은 검진 결과를 이해하고 현재의 건강상태를 아는 것이다. AWR 레포트를 사용한 성능분석에서는 무엇을 이해하면 시스템의 상태를 이해할 수 있는걸까? </li>
</ul>
<h3 id="awr-레포트를-사용한-성능-분석">AWR 레포트를 사용한 성능 분석</h3>
<h4 id="awrautomatic-workload-repository-개요">AWR(Automatic Workload Repository) 개요</h4>
<ul>
<li>DB 내부의 통계정보(snapshot)을 조회하는 기능</li>
<li>어느 두 구간에서 조회한 DB 내부의 통계 정보(snapshot)의 차등(차이)를 근거로 그 사이의 performance 통계 데이터를 report로 출력 가능하다.
<img alt="" src="https://velog.velcdn.com/images/greendev/post/baef4607-bcca-40f5-a7db-7e5c1c4b8c9f/image.png" /></li>
<li>DiagnosticPack 라이선스가 필요하다</li>
</ul>
<h2 id="oracle-database에-특화된-성능분석-정보">Oracle Database에 특화된 성능분석 정보</h2>
<h3 id="snapshot-관리">Snapshot 관리</h3>
<ul>
<li>EM</li>
<li>PL/SQL (DBMS_WORKLOAD_REPOSITORY)</li>
</ul>
<p><strong>CASE1</strong>:  수동으로 스냅샷을 조회하고, 성능 분석을 수행하고 싶을 때 </p>
<pre><code class="language-sql">begin
 DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT();
end;</code></pre>
<p><strong>CASE2</strong>: 성능 테스트를 실시하기 위해, 자동 스냅샷 조회 간격을 default 60분에서 10분으로 변경하고, 성능분석을 수행하고 싶음</p>
<pre><code class="language-sql">begin
 DBMS_WORKLOAD_REPOSITORY.MODIFY_SNAPSHOT_SETTINGS(11520,10);
end;</code></pre>
<p><strong>CASE3.</strong>: SYSAUX 테이블스페이스가 용량을 차지해와서, Snapshot id 1000-2000의 snapshot 삭제를 실행하고 싶음</p>
<pre><code class="language-sql">begin
 DBMS_WORKLOAD_REPOSITORY.DROP_SNAPSHOT_RANGE(1000,2000);
end;</code></pre>
<h2 id="awr-report-생성">AWR report 생성</h2>
<ul>
<li>생성 방법 2가지: EM, SQL</li>
<li>기간 비교: 다른 기간 사이에서의 AWR 레포트를 비교함에 따라, 상세적인 performance를 분석하는 것이 가능하다.</li>
<li>baseline과 비교하는 것도 가능
<img alt="" src="https://velog.velcdn.com/images/greendev/post/cf11d581-87a2-403b-8c84-958098fa4cc7/image.png" /></li>
</ul>
<h3 id="awr에-저장되는-정보">AWR에 저장되는 정보</h3>
<ul>
<li><p>Database Segment Access 정보</p>
<ul>
<li><p>데이터베이스 내에서 특정 세그먼트가 얼마나 자주 접근되고, 얼마나 많은 I/O 작업이 이루어지는지 등을 보여준다.</p>
<ul>
<li><p>segment 사용률: 테이블이나 인덱스가 얼마나 자주 읽히고 쓰이는 지에 대한 정보이다. 예를 들어, 특정 테이블이 자주 조회되거나 수정되는 경우, 이 정보를 통해 해당 테이블의 성능 최적화가 필요할 수 있음을 알 수 있다.</p>
</li>
<li><p>I/O 정보: 세그먼트에 대한 읽기 및 쓰기 작업이 얼마나 자주 발생하는지, 그리고 그로 인한 디스크 I/O가 얼마나 발생하는지를 추적할 수 있다.</p>
</li>
</ul>
</li>
</ul>
</li>
<li><p>시간 모델의 정보(10g부터의 새로운 통계 정보)</p>
<ul>
<li>어느 처리에서 어느 정도 시간을 소비했는지의 정보</li>
<li><code>V$SYS_TIME_MODEL, V$SESS_TIME_MODEL</code> 동적 성능 뷰로부터 수집<ul>
<li>V$SYS_TIME_MODEL : 시스템 전체에서 발생하는 시간 소비를 보여주는 뷰</li>
<li>V$SESS_TIME_MODEL : 각 세션별로 소모된 시간을 추적하는 뷰, 각 세션이 어떤 자원에 대해 얼마나 많은 시간을 소비했는지 세부적으로 알 수 있다.</li>
</ul>
</li>
</ul>
</li>
<li><p>SYSTEM, session 통계</p>
<ul>
<li><code>V$SYSSTAT, V$SESSTAT</code> 동적 성능 뷰로부터 수집<ul>
<li>V$SYSSTAT: 시스템 수준에서 발생하는 통계 정보를 제공, 전체 데이터베이스의 CPU 사용량, 메모리 소비, 디스크 I/O와 같은 통계 데이터를 추적한다.</li>
<li>V$SESSTAT: 각 세션별 통계정보를 제공하며, 특정 사용자가 실행하는 SQL문이나 트랜잭션에 대한 세부 성능 데이터를 추적한다. 예를 들어 특정 사용자가 많은 쿼리를 실행하면서 CPU 자원을 많이 사용하는지, 아니면 disk i/o가 많은지 등의 정보를 알 수 있다.</li>
</ul>
</li>
</ul>
</li>
<li><p>부하가 높은 sql 정보</p>
<ul>
<li>실행 시간이나 CPU를 소비한 시간 등에 기반함</li>
</ul>
</li>
<li><p>최신 Session activity의 이력을 나타내는 ASH 통계</p>
<ul>
<li>1초마다 sampling하고 있는, active한 session 정보</li>
</ul>
</li>
<li><p><strong>ASH(Active Session History)</strong> 는 1초마다 활성 세션에 대한 정보를 샘플링하여 저장하는 시스템. 이를 통해 실시간으로 활성 세션의 상태를 추적할 수 있다.</p>
<ul>
<li>샘플링 주기: 매초 1번씩 활성 세션을 샘플링, 각 세션이 어떤 작업을 하고 있는지 기록한다. 
이를 통해 사용자가 데이터를 조회하거나 트랜잭션을 실행하는 동안의 상태 변화를 추적할 수 있다.</li>
<li>활성 세션 정보: 각 세션이 어떤 리소스를 대기 중인지, SQL 실행 중인지, 또는 기타 작업을 수행 중인지와 같은 정보를 알 수 있다.</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/7fccc4cb-24a4-4506-82e3-8336f9acbc09/image.png" /></p>
<h2 id="main-report">Main Report</h2>
<ol>
<li>Report Summary</li>
<li>대기 이벤트 통계</li>
<li>SQL</li>
<li>Instance 통계</li>
<li>I/O 통계 </li>
<li>Buffer Pool 통계</li>
<li>Advisor 통계</li>
<li>Wait Statistics</li>
<li>Undo 통계</li>
<li>Latch 통계</li>
<li>Segment 통계 </li>
<li>Dictionary Cache 통계</li>
<li>Library Cache 통계</li>
<li>Memory 통계</li>
<li>Stream 통계 </li>
<li>Resource 제한 통계 </li>
<li>init.ora 파라미터 (초기화파라미터)</li>
</ol>
<h3 id="more-rac-statistics">More RAC Statistics</h3>
<ol start="18">
<li>RAC에 관한 추가정보 레포트</li>
<li>Global Enqueue 통계</li>
<li>Global CR 통계</li>
<li>실행 후의 Global Current 통계</li>
<li>Global Cache의 송신 통계 </li>
</ol>
<hr />
<h1 id="awr-레포트에-대한-분석-접근">AWR 레포트에 대한 분석 접근</h1>
<h2 id="awr-확인-포인트">AWR 확인 포인트</h2>
<p><strong>1. Load Profile</strong>: DB의 처리양을 표시한다.
<strong>2. Instance Efficiency</strong> : Oracle Instance의 사용효율을 표시
<strong>3. Top5 Timed Events:</strong> 처리시간의 긴 순위 5번째까지의 이벤트를 나타낸다.
<strong>4. SQL Section :</strong> 각 처리에서의 SQL문 순위를 표시한다.</p>
<h2 id="1-load-profile">1. Load Profile</h2>
<ul>
<li>AWR 조회 시의 시간대 DB의 처리 경향을 파악하는 것이 가능하다.</li>
<li>데이터베이스의 실행 부하를 측정하는 지표로, 정상 시점과 장애 발생 시점을 분석하여 성능을 분석하는 데 사용된다.</li>
</ul>
<blockquote>
<ul>
<li>*<em>DB Time(s)        *</em> :     DB에서 처리된 총 시간 (초)</li>
</ul>
</blockquote>
<ul>
<li>*<em>DB CPU(s)        *</em> :     DB가 CPU에서 처리한 시간 (초)</li>
<li>*<em>Redo size        *</em> :     생성된 REDO 로그의 크기 (Byte)</li>
<li>*<em>Logical reads    *</em> :     논리적 블록 읽기 수 (버퍼 캐시에서 읽은 블록)</li>
<li>*<em>Block changes    *</em> :     데이터 블록 변경 횟수</li>
<li>*<em>Physical reads    *</em> :     디스크에서 직접 읽은 블록 수</li>
<li>*<em>Physical writes    *</em> :     디스크에 직접 기록한 블록 수</li>
<li>*<em>User calls        *</em> :     사용자 요청 (SQL 실행 등) 수</li>
<li>*<em>Parses    SQL     *</em> :     문을 파싱한 횟수</li>
<li>*<em>Hard parses        *</em> :     성능이 낮은 Hard Parse 횟수 (SQL 재사용 불가)</li>
<li><strong>W/A MB processed</strong> :     작업 영역에서 처리된 데이터 크기 (MB)</li>
<li>*<em>Logons            *</em> :     로그인 수</li>
<li>*<em>Executes        *</em> :     SQL 문을 실행한 횟수</li>
<li>*<em>Rollbacks        *</em> :     롤백된 트랜잭션 수</li>
<li>*<em>Transactions    *</em> :     초당 트랜잭션 수</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/fbb9710c-1893-4034-a5b5-c97fa1cb0ebc/image.png" /></p>
<h2 id="2-instance-efficiency">2. Instance Efficiency</h2>
<ul>
<li>OLTP 시스템에서는 Buffer Hit%, Library Hit%는 90% 정도가 되어야 한다.</li>
<li>Library Hit%와 Soft Parse%는 의존 관계에 있어, Library Hit가 낮은 경우엔 Hard Parse가 차지하는 비율이 높아진다.</li>
<li>데이터베이스 내부에서 자원을 얼마나 효율적으로 사용하는지를 파악한다.</li>
<li>일반적으로 Buffer Hit, Soft Parse 비율을 확인<ul>
<li>장애 시 평상시와 hit율의 비교
<img alt="" src="https://velog.velcdn.com/images/greendev/post/90403763-e772-4d02-b915-93e17f5be532/image.png" /></li>
</ul>
</li>
</ul>
<blockquote>
<ul>
<li>Buffer No wait: DB Buffer에 요청했을 때 즉시 사용가능했던 비율</li>
</ul>
</blockquote>
<ul>
<li>Redo No Wait: redo log에 요청했을 때 즉시 사용가능했던 비율</li>
<li>Inmemory Sort: 정렬(Sort) 작업이 메모리에서 수행된 비율을 나타내는 AWR 리포트 지표<ul>
<li>디스크를 사용하지 않고, 메모리에서 정렬이 이루어진 비율을 의미한다.</li>
</ul>
</li>
</ul>
<table>
<thead>
<tr>
<th>항목</th>
<th>의미</th>
<th>해석</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Buffer Nowait %</strong></td>
<td>DB 버퍼에서 데이터를 요청했을 때, 즉시 사용 가능했던 비율</td>
<td><strong>100 (좋음)</strong> → 대기 없이 즉시 버퍼 접근 가능</td>
</tr>
<tr>
<td><strong>Redo NoWait %</strong></td>
<td>Redo 로그를 기록할 때, 즉시 사용할 수 있었던 비율</td>
<td><strong>100 (좋음)</strong> → Redo 로그 버퍼가 부족하지 않음</td>
</tr>
<tr>
<td><strong>Buffer Hit %</strong></td>
<td>데이터 조회 시, 버퍼 캐시에서 읽어온 비율</td>
<td><strong>24.84 (문제 가능)</strong> → 디스크에서 직접 읽는 비율이 높음</td>
</tr>
<tr>
<td><strong>Library Hit %</strong></td>
<td>SQL 실행 시, 라이브러리 캐시에서 재사용된 비율</td>
<td><strong>99.08 (좋음)</strong> → SQL이 잘 재사용됨</td>
</tr>
<tr>
<td><strong>Execute to Parse %</strong></td>
<td>실행된 SQL 중, 새로운 파싱 없이 실행된 비율</td>
<td><strong>69.02 (낮음)</strong> → SQL 파싱 비용이 높음</td>
</tr>
<tr>
<td><strong>Parse CPU to Parse Elapsed %</strong></td>
<td>SQL 파싱 중, CPU 사용만으로 완료된 비율</td>
<td><strong>0 (문제 가능)</strong> → 파싱 시 CPU 이외의 대기 시간이 많음</td>
</tr>
<tr>
<td><strong>In-memory Sort %</strong></td>
<td>정렬이 메모리에서 수행된 비율</td>
<td><strong>97.62 (좋음)</strong> → 대부분의 정렬이 메모리에서 수행됨</td>
</tr>
<tr>
<td><strong>Latch Hit %</strong></td>
<td>Latch(동기화 메커니즘) 충돌 없이 성공한 비율</td>
<td><strong>99.98 (좋음)</strong> → Latch 경합 문제 없음</td>
</tr>
<tr>
<td><strong>Non-Parse CPU %</strong></td>
<td>전체 CPU 사용량 중 SQL 파싱 외의 작업에 사용된 비율</td>
<td><strong>100 (좋음)</strong> → CPU가 파싱 외의 작업에 효과적으로 사용됨</td>
</tr>
</tbody></table>
<h2 id="3-top5-timed-event">3. Top5 Timed Event</h2>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/c39e068b-0bce-4bad-a44d-4316c6921361/image.png" /></p>
<blockquote>
<ul>
<li>Event: 이벤트명</li>
</ul>
</blockquote>
<ul>
<li>Waits: 이벤트 때문에 대기한 합계횟수</li>
<li>Time(s): 이벤트 합계 대기시간 및 합계 CPU시간(초)</li>
<li>% Total Ela TIme: 전체에 대해 이 이벤트 및 CPU 시간의 비율(각 이벤트 대기시간/합계처리시간)</li>
</ul>
<h2 id="4-sql-section--sql-order-by-gets">4. SQL Section ~ SQL Order by Gets</h2>
<ul>
<li><p>SQL Order by Gets: 버퍼읽기(Buffer Gets)가 많은 SQL을 순위별로 정렬한 리스트로, 즉, 많은 데이터를 논리적으로 읽어들이는 SQL을 파악하는 데 유용한 지표이다.</p>
<ul>
<li><p>Buffer Gets: SQL이 실행될 때 버퍼 캐시에서 데이터를 읽은 횟수를 의미한다.</p>
<ul>
<li>이 값이 크다는 것은 해당 SQL이 메모리에서 많은 데이터를 가져오고 있다는 뜻이다.</li>
<li>논리적인 데이터 조회(버퍼 읽기)가 많은 SQL을 확인하고, 비효율적인 SQL을 튜닝하는 데 사용된다.
<img alt="" src="https://velog.velcdn.com/images/greendev/post/01e0406d-297e-442c-930b-837c9cbca6df/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<blockquote>
<ul>
<li>Gets Per Exec: Access된 Buffer 수/실행횟수</li>
</ul>
</blockquote>
<ul>
<li>%Total: Access된 Buffer 비율</li>
<li>CPU Time(s): 이 SQL문 실행에 대한 누적 CPU시간(초) </li>
<li>Elapsed Time(s): 이 SQL문의 누적실행시간(초)</li>
<li>Hash Value: Shared Pool 내 SQL 텍스트 Hash값</li>
</ul>
<h1 id="case-study">Case Study</h1>
<ul>
<li>AWR 레포트에서의 분석 접근<ul>
<li>A사에서 Proactive한 성능분석을 수행하기 위해 평소부터 AWR를 조회하고 있다. 어느날, Application측으로부터 &quot;고객으로부터 화면 Response가 늦어졌어요 라고 들었지만, DB측에 문제가 있나요?&quot; </li>
<li>Application측에서는 문제를 발견할 수 없었기에, DB측을 조사해주실 수 있나요? 라는 요구사항을 들었다.<blockquote>
<p>AWR을 사용해서, 어떻게 성능 분석을 진행할 수 있을까?</p>
</blockquote>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/02e70263-b803-4103-ab34-e5736ea46383/image.png" /></p>
<blockquote>
<p>Top 5 wait event로부터 대기 이벤트 db file sequential read가 발생, 물리적 읽기가 많은 segment는 IO_NECK_TAB_IX로 불리는 INDEX이며, IO대기가 발생하고 있다.</p>
</blockquote>
<ul>
<li>특정 Segment에서의 IO대기가 발생하고 있다는 것은...</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/e441f8b7-6f6a-4ec0-886f-582474bc72c5/image.png" /></p>
<ul>
<li>Summary-&gt; 물리적인 Read가 많은 segment라고 분석을 진행한 것은 Oracle Architecture을 이해하고 있기 때문<ul>
<li>db file sequential read가 발생하고 있다는 것은? </li>
</ul>
</li>
</ul>