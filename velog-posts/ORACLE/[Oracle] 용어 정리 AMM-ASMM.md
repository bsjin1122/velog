<h1 id="ammasmm">AMM/ASMM</h1>
<blockquote>
<ul>
<li>AMM (Automatic Memory Management)</li>
</ul>
</blockquote>
<ul>
<li>ASMM (Automatic Shared Memory Management)</li>
<li>2가지 메모리 관리기법</li>
</ul>
<h1 id="amm-automatic-memory-management">AMM (Automatic Memory Management)</h1>
<ul>
<li><p>AMM은 Oracle에서 전체 데이터베이스 메모리(SGA와 PGA)를 자동으로 관리하는 방식</p>
<blockquote>
<ul>
<li>Oracle 11g부터 도입된 AMM은 <strong>SGA (System Global Area)</strong>와 <strong>PGA (Program Global Area)</strong>의 크기를 자동으로 조정하여, 사용 패턴에 따라 데이터베이스 성능을 최적화합니다.</li>
</ul>
</blockquote>
</li>
<li><p>SGA: 데이터베이스의 공유 메모리 영역으로, 캐시된 데이터나 SQL 문 등 여러 사용자가 공동으로 사용하는 메모리 영역입니다.</p>
</li>
<li><p>PGA: 각 세션별로 할당되는 메모리로, 소트 연산, 해시 연산 등에서 사용되는 메모리입니다.</p>
</li>
</ul>
<h3 id="amm의-특징">AMM의 특징</h3>
<ul>
<li><p>전체 메모리 관리: DBA가 직접 메모리 할당을 조정할 필요 없이, Oracle이 자동으로 SGA와 PGA 간의 메모리 사용량을 관리합니다.</p>
</li>
<li><p>동적 조정: 데이터베이스가 실행 중일 때 메모리 사용 패턴을 분석하고, 필요한 메모리 크기를 동적으로 조정합니다.</p>
</li>
</ul>
<h3 id="amm-사용-시-필요한-파라미터">AMM 사용 시 필요한 파라미터</h3>
<ul>
<li><p><code>MEMORY_TARGET</code>: 데이터베이스 전체 메모리 크기를 설정합니다. 이 값은 SGA와 PGA를 모두 포함한 전체 메모리의 크기를 의미합니다.</p>
</li>
<li><p><code>MEMORY_MAX_TARGET</code>: 데이터베이스가 사용할 수 있는 최대 메모리 크기를 설정합니다.</p>
</li>
</ul>
<hr />
<h1 id="asmm-automatic-shared-memory-management">ASMM (Automatic Shared Memory Management)</h1>
<blockquote>
<ul>
<li>ASMM은 Oracle에서 SGA만을 자동으로 관리하는 방식</li>
</ul>
</blockquote>
<ul>
<li>AMM과 다르게 PGA는 수동으로 관리되고, SGA의 구성 요소들인 shared pool, database buffer cache, large pool 등의 크기를 자동으로 관리</li>
</ul>
<h3 id="asmm의-특징">ASMM의 특징</h3>
<ul>
<li>SGA의 각 구성 요소는 시스템 사용 패턴에 따라 동적으로 메모리 크기가 조정됩니다.
동적 SGA 크기 조정: ASMM은 SGA_TARGET 파라미터를 사용해, SGA 내에서 필요한 메모리 양을 실시간으로 조정합니다.</li>
</ul>
<h3 id="asmm-사용-시-필요한-파라미터">ASMM 사용 시 필요한 파라미터:</h3>
<ul>
<li><p><code>SGA_TARGET</code>: SGA 영역의 전체 크기를 정의합니다. 이 값은 SGA 내에서 각 영역의 메모리 할당을 자동으로 조정합니다.</p>
</li>
<li><p><code>SGA_MAX_SIZE</code>: SGA가 사용할 수 있는 최대 메모리 크기를 설정합니다.</p>
</li>
</ul>
<h2 id="amm과-asmm의-차이점">AMM과 ASMM의 차이점</h2>
<ul>
<li>AMM: SGA와 PGA를 통합적으로 관리하여 메모리 관리를 단순화합니다.</li>
<li>ASMM: SGA만을 자동으로 관리하며, PGA는 수동으로 관리됩니다.</li>
</ul>
<blockquote>
<p>AMM은 SGA와 PGA 전체 메모리를 자동으로 관리하는 방식이고, ASMM은 SGA 메모리만 자동으로 관리하는 방식이다.</p>
</blockquote>
