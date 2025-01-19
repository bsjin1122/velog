<blockquote>
<p>도서: 오라클 데이터베이스 11g RAC 리눅스</p>
</blockquote>
<h2 id="taftransparent-application-failover">TAF(Transparent Application Failover)</h2>
<ul>
<li><p>클라이언트 측 기능</p>
</li>
<li><p>인스턴스나 노드의 장애 시 세션의 페일오버/재접속을 의미</p>
</li>
<li><p>active/passive 클러스터에서도 동일하게 활용 가능</p>
</li>
<li><p>클라이언트의 tnsnames.ora 파일에서 로컬 명명을 사용하거나, RAC 데이터베이스의 서비스 속성으로 정의할 수 있다. </p>
<ul>
<li>선호되는 방법: 후자</li>
<li>OCI(Oracle Call Interface) 라이브러리가 필요하다. <ul>
<li>Oracle Instance Client 도입, 설치</li>
</ul>
</li>
</ul>
</li>
<li><p>오라클 NETCA는 클라이언트 측 TAF 설정 지원하지 않음</p>
</li>
</ul>
<p>1) 노드 장애 시 세션 복원
2) SELECT 구문을 다시 실행</p>
<pre><code class="language-sql">MYDB =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = primary_host)(PORT = 1521))
      (ADDRESS = (PROTOCOL = TCP)(HOST = secondary_host)(PORT = 1521))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = myservice)
      (FAILOVER_MODE =
        (TYPE = SELECT)  -- SELECT 문을 다시 실행할 수 있음
        (METHOD = BASIC) -- 장애 발생 시 즉시 failover
        (RETRIES = 10)   -- 10번까지 재시도
        (DELAY = 5)      -- 5초 간격으로 재시도
      )
    )
  )
</code></pre>
<h3 id="taf-한계">TAF 한계</h3>
<ul>
<li>DML 수행 중 장애 발생 시 복구되지 않음 (트랜잭션 보장 안 됨).</li>
<li>커서가 닫힐 수도 있어서 응용 프로그램에서 새로 OPEN 필요.</li>
</ul>
<h2 id="fcffast-connection-failover">FCF(Fast Connection Failover)</h2>
<ul>
<li><p>노드 장애를 처리할 수 있는 또 다른 방법을 제공</p>
</li>
<li><p>RAC 고가용성 프레임워크에서 발생한 이벤트를 다룰 수 있다.</p>
<ul>
<li>WAS나 사용자 pc에게 장애가 났음을 고지</li>
</ul>
</li>
<li><p>TAF보다 빠르게 장애 감지 및 전환 수행.</p>
</li>
<li><p>Oracle RAC, Data Guard 환경에서 세션이 있는지 확인하고 새로운 연결을 제공.</p>
<ul>
<li>ONS(Oracle Notification Service)를 활용하여 장애 발생을 감지.</li>
</ul>
</li>
<li><p>DML과 SELECT 모두 가능 (커넥션 풀 사용 시).</p>
</li>
<li><p>JDBC, ODP.NET, OCI Driver에서 지원.</p>
</li>
</ul>
<h3 id="설정-방법-java-연결-예시">설정 방법 (Java 연결 예시)</h3>
<pre><code class="language-java">Properties props = new Properties();
props.setProperty(&quot;oracle.jdbc.FastConnectionFailover&quot;, &quot;true&quot;);
props.setProperty(&quot;oracle.net.ns.SQLnet.ONS_CONFIGURATION&quot;, &quot;(ADDRESS=(PROTOCOL=TCP)(HOST=primary_host)(PORT=6200))&quot;);
OracleDataSource ds = new OracleDataSource();
ds.setConnectionProperties(props);</code></pre>
<h3 id="fcf-동작-방식">FCF 동작 방식</h3>
<ul>
<li>ONS를 통해 장애 발생 감지.</li>
<li>Connection Pool에서 장애가 난 노드의 연결을 제거.</li>
<li>새로운 Connection을 자동으로 정상 노드로 연결</li>
</ul>
<h3 id="한계">한계</h3>
<ul>
<li>ONS가 설정되어 있어야 함.</li>
<li>Connection Pool을 사용해야 효과적</li>
<li>연결이 끊어진 후 새로운 Connection을 생성하는 방식이므로 기존 세션은 유지되지 않음</li>
</ul>
<hr />
<h2 id="ctf-client-transparent-failover">CTF (Client Transparent Failover)</h2>
<ul>
<li>CTF는 Oracle 19c에서 새롭게 추가된 기능으로, 기존 세션을 유지하면서 자동으로 연결을 재설정해 주는 기능</li>
</ul>
<h3 id="주요-특징">주요 특징</h3>
<ul>
<li>클라이언트의 개입 없이 투명하게 연결을 복구.</li>
<li>JDBC, ODP.NET, Oracle Call Interface (OCI)에서 지원.
RAC 및 Data Guard 환경에서 유용</li>
<li>기존의 TAF와 FCF의 단점을 보완</li>
<li>DML 및 SELECT 모두 복구 가능</li>
<li>기존의 세션과 상태를 유지하여 사용자 개입을 최소화</li>
</ul>
<h3 id="설정-방법-jdbc-예시">설정 방법 (JDBC 예시)</h3>
<pre><code class="language-java">Properties props = new Properties();
props.setProperty(&quot;oracle.jdbc.CTF&quot;, &quot;true&quot;);
OracleDataSource ds = new OracleDataSource();
ds.setConnectionProperties(props);</code></pre>
<h3 id="ctf-동작-방식">CTF 동작 방식</h3>
<ul>
<li>장애 발생 시 기존 Connection을 자동으로 재설정.</li>
<li>연결이 새로운 노드로 이동하면서 현재 상태를 유지.</li>
<li>SELECT 및 DML 모두 지속적으로 실행 가능.</li>
</ul>
<h3 id="한계-1">한계</h3>
<ul>
<li>Oracle 19c 이상에서만 지원</li>
<li>일부 오래된 드라이버에서는 사용 불가</li>
</ul>