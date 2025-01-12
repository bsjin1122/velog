<ul>
<li><a href="https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_2014.htm">https://docs.oracle.com/cd/E16338_01/server.112/b56299/statements_2014.htm</a><h2 id="sid">SID</h2>
</li>
<li>값을 유효하게 할 instance의 sid를 지정할 수 있다.</li>
<li>이 파라미터가 아직 명시적으로 설정되지 않은 모든 인스턴스에 대해 파라미터 값을 Oracle Database에서 변경하는 경우에는, <code>SID='*'</code>를 지정한다.</li>
<li>sid의 인스턴스만 파라미터 값을 변경할 경우, <code>SID='sid'</code>로 지정한다.</li>
<li>이 설정은 SID='*'를 지정하는 전후 ALTER SYSTEM SET 구문으로부터 우선시된다.</li>
</ul>
<h3 id="sid를-지정하지-않은-경우">SID를 지정하지 않은 경우</h3>
<ul>
<li>pfile을 사용하여 instnace를 기동할 경우, 현행의 instance의 sid를 지정했다고 간주된다.</li>
<li>spfile을 사용해 instance를 기동하는 경우, SID='*'를 지정했다고 간주한다.</li>
</ul>
<h2 id="scope">SCOPE</h2>
<ul>
<li><p>변경이 유효하게 될 타이밍을 지정할 수 있다.</p>
</li>
<li><p>유효범위는 데이터베이스의 기동 시 사용하는 파일이 향후 pfile일지, spfile이 될지에 따라 달라진다.</p>
</li>
<li><p><code>MEMORY</code>: 변경이 MEMORY에서 행해져, 곧바로 유효하게 되어, database가 정지할 때까지 지속한다.</p>
<ul>
<li>pfile을 사용해서 데이터베이스를 기동할 경우, 이 유효범위만을 지정할 수 있다.</li>
</ul>
</li>
<li><p><code>SPFILE</code>: 변경이 spfile에서 행해진다. 새로운 설정은 database가 그 다음으로 정지하고, 
재기동될 때 유효하게 된다. 변경불가능이라고 명시되있는 정적 파라미터를 변경할 경우, SPFILE이라고 지정할 필요가 있다.</p>
</li>
<li><p><code>BOTH</code>: 변경이 메모리와 spfile 동시에 행해진다. 새로운 설정은 곧바로 유효해지며, 재기동 뒤에도 지속된다.</p>
</li>
</ul>
<hr />
<ul>
<li>MEMORY: 테스트나 임시 변경을 위해 사용, 데이터베이스를 재시작하면 설정이 리셋된다.</li>
<li>SPFILE: 영구적인 변경을 위해 사용</li>
</ul>