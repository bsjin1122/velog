<h2 id="1-tnsnamesora">1. tnsnames.ora</h2>
<ul>
<li>클라이언트가 오라클 데이터베이스에 연결할 때 필요한 정보를 제공</li>
<li>$ORACLE_HOME/network/admin 디렉토리에 위치</li>
<li>호스트이름, 포트 번호, 서비스 이름(service_name), sid 등 포함</li>
</ul>
<blockquote>
<pre><code class="language-shell">ORCL =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = 192.168.1.10)(PORT = 1521))
    (CONNECT_DATA =
      (SERVICE_NAME = orcl)
    )
  )</code></pre>
</blockquote>
<pre><code>
## 2. listener.ora
- 클라이언트의 접속 요청을 수신하고, 이를 데이터베이스로 연결해주는 리스너(Listener)에 대한 정보를 정의
- 주로 서버 측의 $ORACLE_HOME/network/admin 디렉토리 위치
- 리스너의 호스트 이름, 포트 번호, 프로토콜 등의 정보를 포함한다.
### 작동 방식
- 리스너는 클라이언트의 연결 요청을 수신, 연결 요청이 들어오면 클라이언트를 해당 데이터베이스 인스턴스로 연결

- 데이터베이스 인스턴스가 여러 개 있거나, 다양한 포트에서 클라이언트를 수용해야 할 때 리스너를 통해 연결을 관리

&gt;
```shell
LISTENER =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = TCP)(HOST = myserver)(PORT = 1521))
    )
  )
SID_LIST_LISTENER =
  (SID_LIST =
    (SID_DESC =
      (GLOBAL_DBNAME = orcl)
      (ORACLE_HOME = /u01/app/oracle/product/19.0.0/dbhome_1)
      (SID_NAME = orcl)
    )
  )</code></pre><blockquote>
<p>tnsnames.ora 는 클라이언트가 연결할 데이터베이스 정보를 정의하고, listener.ora는 서버에서 클라이언트 요청을 수신, 연결을 제공하는 역할을 한다.</p>
</blockquote>