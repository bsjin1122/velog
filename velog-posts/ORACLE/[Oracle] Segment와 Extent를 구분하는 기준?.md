<h1 id="segment">Segment</h1>
<ul>
<li>논리적인 데이터 저장 단위</li>
<li>특정 데이터 객체(테이블, 인덱스 등)에 속한 모든 데이터가 저장되는 영역</li>
<li>Segment는 하나 이상의 Extent로 구성<h3 id="특징">특징</h3>
</li>
<li>테이블, 인덱스, 파티션과 같은 고수준의 데이터 객체를 나타낸다.</li>
<li>데이터베이스 사용자는 일반적으로 Segment 단위로 데이터를 관리하고 접근</li>
<li>ex) 하나의 테이블이 하나의 Segment로 표현된다.</li>
</ul>
<h1 id="extent">Extent</h1>
<ul>
<li>물리적인 데이터 저장 단위로, 연속된 데이터 블록(Block)들의 집합이다.</li>
<li>Segment 내에서 데이터를 저장하기 위해 할당</li>
<li>Segment 데이터가 증가하면, 새로운 Extent가 추가로 할당</li>
<li>Extent는 <code>항상 연속된 블록</code>으로 구성, I/O 효율성을 높이기 위해 설계</li>
<li>Extent 크기 및 개수는 데이터 증가율과 Tablespace 설정에 따라 조정</li>
</ul>
<h3 id="데이터-관리의-논리적물리적-구분">데이터 관리의 논리적/물리적 구분</h3>
<ul>
<li>Segment는 사용자 관점에서 데이터 객체(테이블, 인덱스)를 논리적으로 표현.</li>
<li>Extent는 데이터가 저장되는 물리적 공간의 단위로, 데이터베이스 관리자가 효율적으로 공간을 할당하고 관리.
이를 통해 데이터베이스는 사용자에게 논리적인 단순성을 제공하면서도, 내부적으로는 물리적 효율성을 유지.</li>
</ul>