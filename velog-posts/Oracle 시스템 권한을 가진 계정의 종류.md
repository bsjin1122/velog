<h2 id="sys">SYS</h2>
<ul>
<li>오라클 Super 사용자 계정</li>
<li>데이터베이스에서 발생하는 모든 문제들을 처리할 수 있는 권한<h3 id="권한">권한</h3>
</li>
<li>SYS 계정은 SYSDBA 권한을 자동으로 부여받으며, 데이터베이스의 관리와 복구, 핵심 시스템 파일 관리 등의 작업을 할 수 있는 최상위 권한을 갖는다.<h3 id="특징">특징</h3>
</li>
<li>오라클 데이터베이스의 <strong>시스템 데이터 사전</strong>을 소유한다.<h3 id="사용-목적">사용 목적</h3>
</li>
<li>데이터베이스의 <strong>복구 작업, 백업 관리, 패치 적용, 업그레이드</strong> 등 데이터베이스 구조와 시스템에 직접적인 영향을 미치는 작업을 수행한다.</li>
</ul>
<hr />
<h2 id="system">SYSTEM</h2>
<ul>
<li>오라클 데이터베이스를 유지보수, 관리할 때 사용하는 사용자 계정</li>
<li>SYS와의 차이점: 데이터베이스를 생성할 수 있는 권한이 없으면, 복구를 할 수 없다.</li>
</ul>
<hr />
<h2 id="hr">HR</h2>
<ul>
<li>처음 오라클을 사용하는 사용자의 실습을 위해 만들어 놓은 교육용 계정</li>
</ul>
<hr />
<h2 id="sysdba">SYSDBA</h2>
<ul>
<li>오라클 데이터베이스에서 최상위 관리자 권한</li>
<li>데이터베이스의 시작 및 종료, 복구, 백업, 구조 수정과 같은 핵심 시스템 작업을 수행할 수 있는 권한<h3 id="권한-1">권한</h3>
</li>
<li>데이터베이스의 모든 작업을 무제한으로 수행할 수 있는 권한으로, <strong>SYS 계정</strong>을 통해 주로 사용되지만, 특정 사용자에게 SYSDBA 권한을 부여할 수도 있다.<h3 id="특징-1">특징</h3>
</li>
<li>SYSDBA 권한으로 연결하면, SYS 계정의 모든 권한을 갖는다. <ul>
<li>루트 관리자(root) 역할을 수행한다.</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>출처: <a href="https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&amp;blogId=imf4&amp;logNo=220597495770">거셩님 블로그</a></li>
</ul>