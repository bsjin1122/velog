<h2 id="lsnrctl-listener-control">lsnrctl (Listener Control)</h2>
<ul>
<li><p>오라클 리스너(Oracle Listener)를 관리하기 위한 명령어 기반의 도구 </p>
</li>
<li><p>오라클 데이터베이스에서 리스너(Listener)는 <strong>클라이언트와 데이터베이스 서버 간의 네트워크 연결</strong>을 관리하는 역할 </p>
</li>
<li><p><strong>리스너</strong>는 <strong>클라이언트가 서버에 접속할 수 있도록</strong> 클라이언트의 요청을 수신하고, 해당 요청을 데이터베이스에 전달하여 클라이언트와 데이터베이스 간의 연결을 성립하게 한다.</p>
</li>
</ul>
<h2 id="주요-역할">주요 역할</h2>
<ul>
<li><p>리스너를 <strong>시작, 중지, 재시작</strong> 하거나, <strong>리스너 상태 확인</strong> 및 <strong>트러블 슈팅</strong> 작업을 수행하는 데 사용된다.</p>
</li>
<li><p>이 도구를 통해 오라클 리스너의 동작을 제어하고, 리스너의 상태 및 구성 정보를 확인할 수 있다.</p>
</li>
</ul>
<h3 id="lsnrctl을-통해-할-수-있는-작업">lsnrctl을 통해 할 수 있는 작업</h3>
<p>** 1. 리스너 시작 (lsnrctl start) **</p>
<ul>
<li>리스너를 시작하여, 클라이언트의 연결 요청을 수신할 수 있게 합니다.</li>
</ul>
<p>** 2. 리스너 중지 (lsnrctl stop)** </p>
<ul>
<li>리스너를 중지하여, 더 이상 클라이언트의 연결 요청을 받지 않게 한다.</li>
</ul>
<p>** 3. 리스너 상태 확인 (lsnrctl status) **</p>
<ul>
<li>리스너의 현재 상태(대기 중인 포트, 서비스 등) 확인할 수 있다.</li>
<li>예를 들어, 리스너가 어떤 포트에서 대기 중인지, 어느 데이터베이스 서비스에 연결할 수 있는지 등을 확인할 수 있다.</li>
</ul>
<p>** 4. 리스너 리로드 (lsnrctl reload)**</p>
<ul>
<li>리스너의 설정 파일(listener.ora)을 다시 로드한다.</li>
<li>리스너를 재시작하지 않고, 설정 변경 사항을 반영할 수 있다.</li>
</ul>
<p>** 5. 리스너 재시작 (lsnrctl stop 후 lsnrctl start)**</p>
<ul>
<li>리스너를 중지한 후, 다시 시작하여, 완전히 재시작한다.</li>
</ul>
<p>** 6. 리스너 로그 파일 확인 (lsnrctl show log)**</p>
<ul>
<li>리스너의 로그 파일을 확인하여, 문제 발생 시 트러블슈팅을 위한 정보를 얻을 수 있다.</li>
</ul>