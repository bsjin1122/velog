<blockquote>
<pre><code class="language-SQL">SQL&gt; show parameter name
NAME                   TYPE    VALUE</code></pre>
</blockquote>
<hr />
<p>cdb_cluster_name       string
cell_offloadgroup_name string
db_file_name_convert   string
db_name                string  ORACUB
db_unique_name         string  ORACUB
global_names           boolean FALSE
instance_name          string  ORACUB
lock_name_space        string
log_file_name_convert  string
pdb_file_name_convert  string
processor_group_name   string
service_names          string  ORACUB</p>
<pre><code>
**1. cdb_cluster_name         **
- Container Database 환경에서 여러 데이터베이스 인스턴스를 관리할 때 사용하는 클러스터명

**2. cell_offloadgroup_name   **
- 주로 Exadata와 관련이 있으며, 특정 작업이 셀(Storage Cell)에서 오프로드 되도록 하는 설정

**3. db_file_name_convert     **
- 데이터베이스 파일 이름을 변환할 때 사용하는 설정


**4. db_name                  **
- DB_NAME은 데이터베이스가 생성될 때 지정하며, 동일한 DB_NAME을 사용하는 데이터베이스는 동일한 그룹에 속하는 것으로 간주된다.

**5. db_unique_name           **
- Oracle RAC와 같은 고가용성 환경에서 유용하게 사용된다.
- 데이터베이스의 고유 이름을 정의

**6. global_names             **
- 데이터베이스 이름을 전역적으로 유니크하게 설정할지 여부를 결정
- TRUE: DB_LINK에서 데이터베이스 이름을 반드시 전역적으로 유니크하게 설정

**7. instance_name            **
- 데이터베이스의 인스턴스 이름을 설정하는 파라미터
- 하나의 데이터베이스는 여러 인스턴스를 가질 수 있으며, 각 인스턴스는 고유한 이름을 갖는다.

**8. lock_name_space          **
- 데이터베이스에서 LOCK NAMESPACE를 정의
- 잠금 네임스페이스: 데이터베이스에서 특정 자원의 잠금을 정의하는 데 사용된다.
- 설정되지 않은 경우, 기본적으로 설정된다.

**9. log_file_name_convert    **
- 로그 파일 이름 변환 규칙을 정의하는 파라미터. 
- 데이터베이스 로그 파일이 이동될 때 기존 경로와 새 경로를 지정하는 데 사용된다.

**10. pdb_file_name_convert    **
- PDB(Pluggable Database)의 파일 이름 변환 규칙을 설정
- CDB환경에서 PDB를 이동하거나 복사할 때 유용하다.

**11. processor_group_name     **
- Oracle에서 사용하는 프로세서 그룹의 이름을 정의하는 파라미터

**12. service_names            **
- Oracle Net을 통해 사용자가 여러 데이터베이스에 접속할 때 사용되는 서비스의 이름. 
- 여러 서비스 이름을 설정하여 클라이언트가 여러 접속 옵션을 사용할 수 있도록 한다.</code></pre>