<h1 id="rat-real-application-testing">RAT (Real Application Testing)</h1>
<h2 id="개념">개념</h2>
<ul>
<li><code>SQL Performance Analyzer(SPA)</code>와 <code>Database Replay</code> 기능을 <strong>통합한 Oracle의 솔루션</strong></li>
<li>이러한 통합을 통해, SQL 단위의 성능 분석 + 전체 데이터베이스 부하 분석을 동시에 수행할 수 있다.</li>
</ul>
<h3 id="왜-사용하는가">왜 사용하는가?</h3>
<ul>
<li>데이터베이스에 변경 사항을 적용할 때 SQL 단위의 세밀한 분석과 전체 시스템의 영향도를 모두 평가해야 안전한 운영이 가능하다. RAT는 이러한 두 가지 관점을 모두 커버할 수 있도록 해준다.<blockquote>
<ul>
<li><code>SQL Performance Analyzer</code>: 세밀하게 SQL 실행 계획 변화를 분석합니다.</li>
</ul>
</blockquote>
<ul>
<li><code>DB Replay</code>: 프로덕션 환경의 실제 부하를 테스트하여, 시스템 전체에 미치는 영향을 평가. </li>
<li><code>RAT</code>: 데이터베이스의 큰 변화(업그레이드, 하드웨어 변경, 설정 변경 등)에 대한 포괄적인 테스트 도구로, SQL 성능과 시스템 부하를 모두 테스트하여 안정성을 확보. </li>
</ul>
</li>
</ul>
<hr />
<h1 id="spasql-performance-analyzer">SPA(SQL Performance Analyzer)</h1>
<ul>
<li>SQL 문장의 성능을 분석하고, <code>특정 변화</code>(예: 데이터베이스 업그레이드, 인덱스 추가/삭제, 통계 갱신 등) 가 SQL 실행에 미치는 영향을 측정하는 도구이다.</li>
</ul>
<h3 id="왜-사용하는가-1">왜 사용하는가?</h3>
<ul>
<li>데이터베이스 환경에서 설정을 변경하거나, 업그레이드를 수행할 때, SQL 성능에 미칠 영향을 미리 파악하는 것이 매우 중요하다. 변화 후에 발생할 수 있는 성능 저하나, 문제를 사전에 방지할 수 있다.</li>
</ul>
<h2 id="사용-방법">사용 방법</h2>
<ol>
<li><strong>변화 전</strong> 상태에서 특정 SQL 작업을 SPA에 캡쳐하여, 기준 성능(성능 기준)을 측정한다.</li>
<li>데이터베이스 환경을 변경합니다. 예를 들어, 데이터베이스를 업그레이드하거나, 인덱스를 추가/삭제합니다.</li>
<li><strong>변화 후</strong> 다시 같은 SQL 작업을 수행하고 성능을 측정합니다.</li>
<li>SPA는 변화 전후의 성능을 비교하여, 어떤 SQL 문장이 성능에 변화가 있었는지를 알려줍니다.</li>
</ol>
<h2 id="주요-사용-사례">주요 사용 사례</h2>
<ul>
<li>데이터베이스 업그레이드 전후의 성능 비교</li>
<li>인덱스 추가, 파티션 변경, 통계 업그레이드 등에서의 SQL 성능 비교</li>
<li>계획 변화를 통한 최적의 SQL 실행 계획 선택</li>
</ul>
<hr />
<h1 id="database-replay">Database Replay</h1>
<h2 id="개념-1">개념</h2>
<ul>
<li><p>Production Database에서 발생한 실제 트랜잭션 부하를 캡쳐하고, 이를 테스트 환경에서 다시 실행하여 변경사항이 시스템에 비치는 영향을 평가할 수 있는 도구이다.</p>
<h3 id="왜-사용하는가-2">왜 사용하는가?</h3>
</li>
<li><p>DB Replay를 사용하면 실제 환경에서 발생할 수 있는 문제를 테스트 환경에서 미리 파악할 수 있다.</p>
</li>
<li><p>이 도구를 통해 <strong>대규모의 데이터베이스 변경 작업(예: 하드웨어 변경, 설정 변경, 패치 적용 등)이 실제 트랜잭션 부하에 미치는 영향을 사전에 분석</strong>할 수 있다.</p>
</li>
</ul>
<h3 id="사용-방법-1">사용 방법</h3>
<ol>
<li><p><strong>캡쳐</strong>: 프로덕션 데이터베이스에서 실제 사용자 트랜잭션 부하를 캡쳐합니다.</p>
</li>
<li><p><strong>리플레이 환경 설정</strong>: 테스트 환경을 프로덕션 환경과 동일하게 구성합니다.</p>
</li>
<li><p><strong>리플레이</strong>: 캡쳐한 부하를 테스트환경에서다시 실행합니다.</p>
</li>
<li><p><strong>분석</strong>: 리플레이 중에 발생한 성능 변화나 오류를 분석합니다.</p>
</li>
</ol>
<h2 id="주요-사용-사례-1">주요 사용 사례</h2>
<ul>
<li><p>데이터베이스 업그레이드 전후의 실제 부하 테스트</p>
</li>
<li><p>새로운 하드웨어 또는 Stroage 장치의 성능 영향 분석</p>
</li>
<li><p>데이터베이스 설정 변경(ex: 파라미터 변경)의 영향 분석.</p>
</li>
</ul>