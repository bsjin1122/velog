<blockquote>
<p><strong>참고</strong></p>
</blockquote>
<ul>
<li><a href="https://docs.oracle.com/cd/F19136_01/refrn.pdf">19c 레퍼런스 pdf</a></li>
<li><a href="https://osh88itopia.tistory.com/173">https://osh88itopia.tistory.com/173</a></li>
<li><a href="https://docs.oracle.com/en/database/oracle/oracle-database/21/multi/create-cdb-adv.html#ADMIN11101">DBA 관리자 가이드</a></li>
<li><a href="https://docs.oracle.com/en/database/oracle/oracle-database/21/rilin/selecting-a-database-name.html">Linux 및 Unix용 RAC 설치 가이드</a></li>
<li><a href="https://dataforum.io/display/ORCL/Oracle+Database+11g+R2+Data+Guard">https://dataforum.io/display/ORCL/Oracle+Database+11g+R2+Data+Guard</a></li>
</ul>
<pre><code class="language-sql">SQL&gt; show parameter name

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
cdb_cluster_name                     string
cell_offloadgroup_name               string
db_file_name_convert                 string
👉db_name                              string      ORACOW
👉db_unique_name                       string      ORACOW
👉global_names                         boolean     FALSE
👉instance_name                        string      ORACOW1
lock_name_space                      string
log_file_name_convert                string
pdb_file_name_convert                string
processor_group_name                 string

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
👉service_names                        string      ORACOW,ORAJIN
</code></pre>
<h2 id="instance_name"><a href="https://docs.oracle.com/cd/F39414_01/refrn/INSTANCE_NAME.html">INSTANCE_NAME</a></h2>
<ul>
<li><p>RAC환경에서 여러 인스턴스를 단일의 데이터베이스 서비스와 연관짓는 것이 가능하다. </p>
</li>
<li><p>client는 데이터베이스에 접속하는 특정한 인스턴스를 지정하여 Oracle의 LoadBalancing을 override할 수 있다.</p>
</li>
<li><p>Single Instance Database system에서는 통상적으로 instance명은 db_name과 동일하다.</p>
</li>
<li><p>참고: SID는 HOST에서의 INSTANCE의 공유 메모리를 식별
하지만, 다른 인스턴스로부터는 유일하게 식별되지 않는다.</p>
</li>
</ul>
<h2 id="db_name"><a href="https://docs.oracle.com/cd/F39414_01/refrn/DB_NAME.html">DB_NAME</a></h2>
<ul>
<li><p>db가 여러 개 있는 경우, 이 파라미터 값은 시스템에서 실행중인 각 데이터베이스와 혼동되지 않도록 각 instance Oracle SID와 일치할 필요가 있다. </p>
</li>
<li><p>Standby 및 Primary 초기화 파라미터 파일 둘다 DB_NAME과 일치할 필요가 있다.</p>
</li>
<li><p>Cluster Database의 각 instance에 대응하는 <code>startup</code> 명령어 혹은 <code>alter database... mount</code>으로 지정한 데이터베이스는 DB_NAME 초기화 파라미터 설정에 대응되는 값이어야 한다.</p>
</li>
<li><p>rac: 모든 인스턴스에 대해 설정해야 한다.</p>
</li>
<li><p>rac: 여러 인스턴스는 동일한 값을 사용할 수 있다.</p>
</li>
<li><p>단일 데이터베이스 이름으로, 데이터베이스를 식별</p>
<h2 id="db_unique_name"><a href="https://docs.oracle.com/cd/F39414_01/refrn/DB_UNIQUE_NAME.html">DB_UNIQUE_NAME</a></h2>
</li>
<li><p>클러스터 환경에서 각 데이터베이스 인스턴스를 고유하게 식별</p>
</li>
<li><p>db_name 파라미터 값은  Primary와 Standby가 모두 동일하지만, db_unique_name은 (DataGuard구성 시) Primary와 Standby가 달라야 한다.</p>
<table>
<tr>
<th>구분</th>
<th>db_name</th>
  <th>db_unique_name</th>
</tr>
<tr>
<td>Primary</td>
<td>orcl</td>
  <td>ORCL</td>
</tr>
<tr>
<td>Standby</td>
<td>orcl</td>
  <td>ORCL_STB</td>
</tr>

</table>
## [GLOBAL_NAMES](https://docs.oracle.com/cd/E16338_01/server.112/b56311/initparams098.htm)</li>
<li><p>database link가 접속하는 데이터베이스와 동일한 이름을 갖는 필요인지 아닌지를 지정한다.</p>
</li>
<li><p>(default값: ) false의 경우, check를 수행하지 않는다. 분산처리를 사용하는 경우에는, 이 파라미터를 true로 설정하여, 네트워크 환경에서 데이터베이스 및 링크에 대해 일관된 naming 규칙을 확실하게 사용할 것을 권장한다.</p>
<blockquote>
<ul>
<li>데이터베이스 링크의 이름과, 연결하려는 데이터베이스의 이름이 일치하지 않아도 연결을 허용한다.</li>
</ul>
</blockquote>
</li>
</ul>
<h2 id="service_names"><a href="https://docs.oracle.com/cd/F39414_01/refrn/SERVICE_NAMES.html">SERVICE_NAMES</a></h2>
<ul>
<li><p>SERVICE_NAMES 초기화 파라미터는 19c에서는 비권장되어 향후 release에서 support되지 않을 가능성이 있다.</p>
</li>
<li><p>service를 관리하기 위해서는 srvctl commandline utility, gdsctl commandline utility, 혹은 dbms_service의 pl/sql 패키지를 대신해서 사용하는 것을 권장한다.</p>
</li>
<li><p>클라이언트가 데이터베이스에 연결할 때 사용하는 서비스이름</p>
</li>
<li><p>데이터베이스의 네트워크 서비스 이름으로, 여러 서비스와 연결될 수 있으며, 주로 리스너에서 사용된다. </p>
</li>
<li><p>init.ora/spfile: SERVICE_NAMES: 파라미터 파일에서 Oracle Instance가 서비스 이름을 인식하고, 클라이언트 요청 처리할 수 있도록 한다.</p>
</li>
<li><p>이 파라미터에 DOMAIN을 붙여 이름을 지정하지 않는 경우, DB_DOMAIN 파라미터 값으로 수식된다.</p>
<ul>
<li>DB_DOMAIN이 지정되지 않는 경우에는, 미수식된 SERVICE_NAMES의 값에 도메인은 적용되지 않는다.</li>
</ul>
</li>
</ul>
<blockquote>
</blockquote>
<pre><code class="language-sql">SID_LIST_LISTENER =
  (SID_LIST =
    (SID_DESC =
      (GLOBAL_DBNAME = orcl_service)
      (ORACLE_HOME = /u01/app/oracle)
      (SID_NAME = orcl)
    )
  )</code></pre>
<h2 id="sid"><a href="https://docs.oracle.com/cd/F19136_01/riwin/selecting-a-database-name.html">SID</a></h2>
<ul>
<li>Instance를 실행할 때 사용하는 이름으로, init.ora 혹은 spfile에서 설정한다.</li>
<li>RAC에서 policy 관리형 데이터베이스를 선택한 경우, Oracle은 <code>name_#</code>(name은 DB_UNIQUE_NAME 최초 8문자 영숫자, #는 인스턴스 번호) 형식의 sid를 생성한다.</li>
<li>그러나 RAC One Node 데이터베이스의 경우, instance명은 <code>ORACLE_SID_1</code>로, 이것은 SID 접두사에 <code>_1</code>을 더해 구성된다.</li>
</ul>
<h2 id="db_domain"><a href="https://docs.oracle.com/cd/F19136_01/riwin/selecting-a-database-name.html">DB_DOMAIN</a></h2>
<ul>
<li>분산 데이터베이스 시스템에서 DB_DOMAIN 초기화 매개변수는 네트워크 구조 내에서 데이터베이스의 논리적인 위치를 지정한다.</li>
<li>데이터베이스가 생성되는 네트워크 도메인을 지정하는 텍스트 문자열이다.<ul>
<li>이는 선택사항으로, 생성하려는 데이터베이스가 분산 데이터베이스 시스템의 일부가 될 경우 데이터베이스를 생성하기 전에 초기화 파라미터 값에 주의해야한다.</li>
</ul>
</li>
</ul>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/390f82df-bded-4b69-919b-8544d57b4a3d/image.png" /></p>