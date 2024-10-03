<h2 id="개념">개념</h2>
<blockquote>
<p><strong>MGA(Managed Global Area)</strong>는 _<code>Oracle 12c</code>_부터 도입된 개념으로, 
Multitenant Architecture에서 <strong>PDB(Pluggable Database)</strong>와 관련된 메모리 영역을 관리하는 부분</p>
</blockquote>
<ul>
<li>Oracle의 기존 메모리 구조는 <strong>SGA(System Global Area)</strong>와 <strong>PGA(Program Global Area)</strong>로 나뉘었지만, </li>
<li>MGA는 이와는 다른 새로운 메모리 영역으로, Multitenant 환경에서의 PDB 관리를 위한 목적으로 등장했다.</li>
</ul>
<h2 id="mga의-특징-및-역할">MGA의 특징 및 역할</h2>
<ul>
<li><p>Multitenant 아키텍처 지원</p>
<ul>
<li>Oracle의 Multitenant 아키텍처는 CDB(Container Database) 내에 <strong>여러 PDB(Pluggable Database)</strong>를 포함하는 구조입니다. </li>
<li>MGA는 이러한 PDB 메모리 관리를 위해 설계되었습니다.</li>
</ul>
</li>
<li><p>PDB 별 메모리 관리</p>
<ul>
<li>MGA는 PDB에 필요한 메모리 리소스를 관리하며, 각각의 PDB가 별도의 메모리 할당을 통해 독립적으로 운영되도록 지원합니다.</li>
</ul>
</li>
<li><p>독립적인 메모리 할당</p>
<ul>
<li>MGA는 각각의 PDB에 독립적으로 메모리를 할당하며, 해당 PDB의 작업에 필요한 메모리 사용을 최적화할 수 있습니다.</li>
</ul>
</li>
<li><p>SGA와의 차이점</p>
<ul>
<li>기존의 SGA는 모든 인스턴스가 공유하는 메모리 영역이었지만, MGA는 PDB와 관련된 메모리 작업을 별도로 처리합니다. 즉, Multitenant 환경에서 여러 PDB 간의 메모리 격리가 필요할 때 유용합니다.</li>
</ul>
</li>
</ul>
<h2 id="mga의-주요-목적">MGA의 주요 목적</h2>
<ul>
<li><p>Multitenant 아키텍처에서의 성능 향상: 여러 PDB가 CDB 내에서 운영될 때, 각각의 PDB가 독립적인 메모리 공간을 사용할 수 있도록 보장해줌으로써 성능을 최적화합니다.</p>
</li>
<li><p>메모리 충돌 방지: 각 PDB에 독립적인 메모리 영역을 할당함으로써, 여러 PDB가 메모리를 충돌하지 않고 효율적으로 사용할 수 있도록 돕습니다.</p>
</li>
<li><p>유연한 리소스 관리: MGA는 각 PDB의 작업량과 요구에 따라 메모리 리소스를 동적으로 관리합니다.</p>
</li>
</ul>
<blockquote>
<p><strong>MGA(Managed Global Area)</strong>는 Oracle 12c의 Multitenant 환경에서 PDB와 관련된 메모리 관리를 위한 메모리 영역입니다. 기존의 SGA 및 PGA와는 별도로 작동하며, 각 PDB가 독립적으로 메모리를 사용할 수 있게 해주는 중요한 역할을 합니다.</p>
</blockquote>