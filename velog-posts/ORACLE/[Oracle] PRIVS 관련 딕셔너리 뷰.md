<h2 id="role_role_privs">ROLE_ROLE_PRIVS</h2>
<ul>
<li><p>역할이 다른 역할을 부여받은 상태를 나타냄</p>
</li>
<li><p><code>ROLE</code>: 역할 이름</p>
</li>
<li><p><code>GRANTED_ROLE</code>: 이 역할이 부여받은 다른 역할</p>
</li>
<li><p><a href="https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ROLE_ROLE_PRIVS.html">ROLE_ROLE_PRIVS</a></p>
<pre><code class="language-SQL">ROLE_ROLE_PRIVS              Roles which are granted to roles
ROLE_SYS_PRIVS               System privileges granted to roles
ROLE_TAB_PRIVS               Table privileges granted to roles
SESSION_PRIVS                Privileges which the user currently has set
</code></pre>
</li>
</ul>
<hr />
<p>SQL&gt; SELECT * FROM ROLE_ROLE_PRIVS WHERE ROWNUM &lt;= 10;</p>
<pre><code>               ROLE             GRANTED_ROLE    ADMIN_OPTION    COMMON    INHERITED</code></pre><hr />
<p>EXP_FULL_DATABASE       SELECT_CATALOG_ROLE      NO              NO        NO
GSMADMIN_ROLE           AQ_ADMINISTRATOR_ROLE    NO              NO        NO
GSMROOTUSER_ROLE        CONNECT                  NO              NO        NO
DBA                     EXECUTE_CATALOG_ROLE     NO              NO        NO
SELECT_CATALOG_ROLE     HS_ADMIN_SELECT_ROLE     NO              NO        NO
SYSUMF_ROLE             SELECT_CATALOG_ROLE      NO              NO        NO
GSMUSER_ROLE            GDS_CATALOG_SELECT       NO              NO        NO
EXP_FULL_DATABASE       EXECUTE_CATALOG_ROLE     NO              NO        NO
HS_ADMIN_ROLE           HS_ADMIN_EXECUTE_ROLE    NO              NO        NO
EXECUTE_CATALOG_ROLE    HS_ADMIN_EXECUTE_ROLE    NO              NO        NO</p>
<pre><code>

### ROLE_SYS_PRIVS
- 역할(ROLE)에 시스템 권한(System Privileges)이 부여된 정보를 나타냄
- `ROLE`: 역할이름
- `PRIVILEGE`: 부여된 시스템 권한 이름

```sql
Name    Null?             Type
_______________ ________ ________________
ROLE                     VARCHAR2(128)
PRIVILEGE                VARCHAR2(40)
ADMIN_OPTION             VARCHAR2(3)
COMMON                   VARCHAR2(3)
INHERITED                VARCHAR2(3)



SQL&gt; select * from ROLE_SYS_PRIVS where rownum &lt;= 10;

                         ROLE                           PRIVILEGE    ADMIN_OPTION    COMMON    INHERITED
_____________________________ ___________________________________ _______________ _________ ____________
EXP_FULL_DATABASE             READ ANY FILE GROUP                 NO              NO        NO
DATAPUMP_EXP_FULL_DATABASE    CREATE SESSION                      NO              NO        NO
IMP_FULL_DATABASE             ADMINISTER SQL MANAGEMENT OBJECT    NO              NO        NO
IMP_FULL_DATABASE             CREATE ANY SQL PROFILE              NO              NO        NO
IMP_FULL_DATABASE             ALTER PROFILE                       NO              NO        NO
IMP_FULL_DATABASE             DROP ANY PROCEDURE                  NO              NO        NO
IMP_FULL_DATABASE             CREATE ANY SEQUENCE                 NO              NO        NO
IMP_FULL_DATABASE             INSERT ANY TABLE                    NO              NO        NO
IMP_FULL_DATABASE             CREATE ANY TABLE                    NO              NO        NO
IMP_FULL_DATABASE             ALTER USER                          NO              NO        NO

10 rows selected.
</code></pre><h3 id="role_tab_privs">ROLE_TAB_PRIVS</h3>
<ul>
<li>역할에 부여된 테이블 권한을 설명한다.</li>
<li><code>GRANTABLE</code>: 특정 테이블에 대해 부여된 권한이 다른 사용자에게 부여할 수 있는지 여부를 나타낸다.<ul>
<li><code>YES</code>: 해당 권한은 다른 사용자에게 부여할 수 있음</li>
<li><code>NO</code></li>
</ul>
</li>
<li><code>COMMON</code>: 공통 테이블 권한이 부여된 역할을 나타낸다.<ul>
<li><code>YES</code>: 해당 역할이 공통 테이블 권한을 부여받은 경우</li>
<li><code>NO</code></li>
</ul>
</li>
<li>공통 테이블 권한(Common Table Privileges)은 여러 데이터베이스 오브젝트에 적용될 수 있으며, ROLE_TAB_PRIVS 뷰에서 역할에 부여된 테이블 권한을 관리하는 데 사용된다.</li>
</ul>
<pre><code class="language-sql">Name    Null?             Type
______________ ________ ________________
ROLE                    VARCHAR2(128)
OWNER                   VARCHAR2(128)
TABLE_NAME              VARCHAR2(128)
COLUMN_NAME             VARCHAR2(128)
PRIVILEGE               VARCHAR2(40)
GRANTABLE               VARCHAR2(3)
COMMON                  VARCHAR2(3)
INHERITED               VARCHAR2(3)


SQL&gt; select * from ROLE_TAB_PRIVS where rownum &lt;= 10;

                        ROLE    OWNER                   TABLE_NAME    COLUMN_NAME    PRIVILEGE    GRANTABLE    COMMON    INHERITED
____________________________ ________ ____________________________ ______________ ____________ ____________ _________ ____________
GSMUSER_ROLE                 SYS      IND$                                        READ         NO           NO        NO      
SYSUMF_ROLE                  SYS      PARTOBJ$                                    READ         NO           NO        NO      
GATHER_SYSTEM_STATISTICS     SYS      AUX_STATS$                                  INSERT       NO           NO        NO      
OPTIMIZER_PROCESSING_RATE    SYS      OPT_CALIBRATION_STATS$                      DELETE       NO           NO        NO      
EXP_FULL_DATABASE            SYS      INCFIL                                      INSERT       NO           NO        NO      
IMP_FULL_DATABASE            SYS      EXPIMP_TTS_CT$                              DELETE       NO           NO        NO      
SELECT_CATALOG_ROLE          SYS      V_$MAP_SUBELEMENT                           SELECT       NO           NO        NO      
SELECT_CATALOG_ROLE          SYS      V_$DLM_CONVERT_LOCAL                        SELECT       NO           NO        NO      
SELECT_CATALOG_ROLE          SYS      V_$DLM_TRAFFIC_CONTROLLER                   SELECT       NO           NO        NO      
SELECT_CATALOG_ROLE          SYS      V_$GES_ENQUEUE                              SELECT       NO           NO        NO      

10 rows selected.
</code></pre>
<h3 id="session_privs">SESSION_PRIVS</h3>
<ul>
<li>현재 사용자가 사용할 수 있는 시스템 권한을 설명한다.<pre><code class="language-sql">Name       Null?            Type</code></pre>
</li>
</ul>
<hr />
<p>PRIVILEGE    NOT NULL    VARCHAR2(40)</p>
<p>SQL&gt; select * from SESSION_PRIVS where rownum &lt;= 10;</p>
<pre><code>                   PRIVILEGE</code></pre><hr />
<p>TEXT DATASTORE ACCESS
WRITE ANY ANALYTIC VIEW CACHE
READ ANY ANALYTIC VIEW CACHE
DROP ANY ANALYTIC VIEW
ALTER ANY ANALYTIC VIEW
CREATE ANY ANALYTIC VIEW
CREATE ANALYTIC VIEW
DROP ANY HIERARCHY
ALTER ANY HIERARCHY
CREATE ANY HIERARCHY</p>
<p>10 rows selected.</p>
<pre><code>- `ANALYTIC VIEW`는 Oracle에서 제공하는 기능 중 하나로, 분석적 뷰와 관련이 있다.

### Analytic View(분석적 뷰)
- Oracle Autonomouns Database에서 제공하는 데이터 분석을 위한 특수한 뷰.
- 이 뷰는 데이터를 분석하고 보고서를 생성할 수 있는 미리 정의된 분석적 데이터 모델을 제공한다.
#### 기능
- 데이터 집합을 요약, 분석할 수 있도록 설계됨
- 다양한 분석 함수(예: 집계 함수, 윈도우 함수)를 지원
- 비즈니스 인텔리전스 및 데이터 분석 작업을 쉽게 할 수 있게 해준다.</code></pre>