<blockquote>
<p>용량 내림차순으로 딕셔너리를 조회했을 때 14가지 정도가 나왔다. 간략하게만 정리해두려고 한다.</p>
</blockquote>
<ul>
<li>INDEX PARTITION</li>
<li>TABLE PARTITION</li>
<li>TABLE</li>
<li>CLUSTER</li>
<li>INDEX</li>
<li>ROLLBACK</li>
<li>DEFERRED ROLLBACK</li>
<li>LOBINDEX</li>
<li>TEMPORARY</li>
<li>CACHE</li>
<li>LOBSEGMENT</li>
</ul>
<h2 id="1-table">1. TABLE</h2>
<ul>
<li>설명: 기본 데이터 공간으로, 데이터베이스 테이블에 데이터를 저장하는 세그먼트</li>
<li>특징: 가장 일반적인 세그먼트 유형이며, 각 행은 데이터 블록에 저장된다.</li>
</ul>
<h2 id="2-index">2. INDEX</h2>
<ul>
<li>설명: 테이블의 데이터를 빠르게 검색하기 위해 사용되는 세그먼트이다. </li>
<li>특징: 인덱스를 사용하면 데이터의 검색 성능을 크게 향상시킬 수 있다. </li>
<li>B-tree 구조를 많이 사용하며, 데이터 변경 시 동기화된다.</li>
</ul>
<h2 id="3-lob-segment">3. LOB SEGMENT</h2>
<ul>
<li>설명: LOB(Large Object) 데이터 유형(BLOB, CLOB, NCLOB)을 저장하는 세그먼트</li>
<li>특징: 대용량의 이진 데이터나, 텍스트 데이터를 저장하기 위한 공간이며, 실제 LOB 데이</li>
</ul>
<h2 id="4-table-partition">4. TABLE PARTITION</h2>
<ul>
<li>설명: 파티셔닝된 테이블의 각 파티션을 저장하는 세그먼트</li>
<li>특징: 테이블을 논리적으로 여러 파티션으로 나누어 관리하고, 각 파티션은 별도의 세그먼트로 저장된다.</li>
</ul>
<h2 id="5-index-partition">5. INDEX PARTITION</h2>
<ul>
<li>설명: 파티셔닝된 인덱스의 각파티션을 저장하는 세그먼트</li>
<li>특징: 인덱스가 파티셔닝되면 각 파티션은 별도의 세그먼트로 관리된다.<ul>
<li>대규모 데이터의 인덱싱에 유용하다.</li>
</ul>
</li>
</ul>
<h2 id="6-lob-subpartition">6. LOB SUBPARTITION</h2>
<ul>
<li>설명: LOB 데이터 유형의 파티셔닝된 테이블에 대한 하위 파티션을 저장하는 세그먼트</li>
<li>특징: 파티셔닝된 테이블에 대해 LOB 데이터를 효율적으로 관리하고 저장합니다.</li>
</ul>
<h2 id="7-index-subpartition">7. INDEX SUBPARTITION</h2>
<ul>
<li>설명: 파티셔닝된 인덱스의 하위 파티션을 저장하는 세그먼트</li>
<li>특징: 복잡한 파티션 구조에서 효율적인 인덱싱을 지원</li>
</ul>
<h2 id="8-type2-undo">8. TYPE2 UNDO</h2>
<ul>
<li>설명: UNDO 데이터용 세그먼트, Oracle 9i부터 도입된 새로운 UNDO 관리 방식이다.</li>
<li>특징: Automatic Undo Management (AUM)을 사용해서 UNDO 정보를 관리하며, 데이터의 일관성을 유지하고 트랜잭션 롤백을 지원한다.</li>
</ul>
<h2 id="9-lobindex">9. LOBINDEX</h2>
<ul>
<li>설명: LOB 데이터 세그먼트에 대한 인덱스를 저장하는 세그먼트</li>
<li>특징: LOB 데이터에 빠르게 액세스하기 위해 사용되며, LOB 데이터와 연계되어 관리된다.</li>
</ul>
<h2 id="10-lob-partition">10. LOB PARTITION</h2>
<ul>
<li>설명: LOB 데이터 유형의 파티셔닝 된 테이블에 대한 파티셔닝을 저장하는 세그먼트</li>
<li>특징: LOB 데이터의 효율적인 관리와 접근 지원한다.</li>
</ul>
<h2 id="11-cluster">11. CLUSTER</h2>
<ul>
<li>설명: 같은 키 값을 공유하는 두 개 이상의 테이블의 데이터 함께 저장하는 세그먼트</li>
<li>특징: 데이터 클러스터링을 통해 관련 데이터에 대한 빠른 검색을 가능하게 한다.<ul>
<li>특히, 조인 작업에서 성능을 향상</li>
</ul>
</li>
</ul>
<h2 id="12-system-statistics">12. SYSTEM STATISTICS</h2>
<ul>
<li>설명: 데이터베이스 시스템의 통계를 저장하는 세그먼트</li>
<li>특징: 일반적으로 자동 수집되며, 데이터베이스의 효율적인 운영을 위해 다양한 통계 정보를 수집하고 저장한다.</li>
</ul>
<h2 id="13-nested-table">13. NESTED TABLE</h2>
<ul>
<li>설명: 테이블 내 포함된 중첩 테이블의 데이터를 저장하는 세그먼트</li>
<li>특징: 중첩 테이블은 부모 테이블의 열에 저장되며 별도의 세그먼트로 관리된다. 객체 지향 데이터 모델링에서 사용된다.</li>
</ul>
<h2 id="14-rollback">14. ROLLBACK</h2>
<ul>
<li>설명: 이전에 변경된 데이터의 상태를 저장하는 세그먼트로, 트랜잭션의 롤백을 지원한다.</li>
<li>특징: UNDO 세그먼트와 유사하지만, 이전 Oracle 버전에서는 Rollback 세그먼트가 트랜잭션 제어에 직접 사용되었다.</li>
</ul>