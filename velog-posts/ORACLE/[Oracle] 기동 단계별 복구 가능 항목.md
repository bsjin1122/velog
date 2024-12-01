<blockquote>
<ol>
<li>NOMOUNT 단계</li>
<li>MOUNT 단계</li>
<li>OPEN 단계</li>
</ol>
</blockquote>
<h1 id="nomount-단계">NOMOUNT 단계</h1>
<ul>
<li>데이터베이스 인스턴스와 백그라운드 프로세스 시작</li>
<li>데이터베이스 파일에 직접 접근하지 않음</li>
<li>SPFILE 또는 PFILE을 읽어 초기화 파라미터를 읽음<h2 id="복구-가능-항목">복구 가능 항목</h2>
</li>
<li>pfile 또는 spfile 문제<ul>
<li>데이터베이스 파일에 직접 접근하지 않음 </li>
<li><code>CREATE PFILE FROM SPFILE</code> 명령으로 파일을 복원 가능.</li>
</ul>
</li>
<li>메모리 설정 관련 문제 <ul>
<li>SGA, PGA 메모리 설정 오류를 수정</li>
</ul>
</li>
<li>ASM 관련 문제<ul>
<li>ASM 디스크 그룹에 접근 불가 시, ASM 인스턴스를 확인하고 기동</li>
</ul>
</li>
<li>복구 작업<ul>
<li>PFILE, SPFILE 수정 또는 생성</li>
<li>Oracle Home, 환경 변수 설정 확인</li>
</ul>
</li>
</ul>
<h1 id="mount">MOUNT</h1>
<ul>
<li>데이터베이스가 컨트롤 파일을 로드하여 데이터베이스 구조를 확인</li>
<li>데이터파일 및 로그 파일의 위치 정보가 control file에서 읽힌다.<h2 id="복구-가능-항목-1">복구 가능 항목</h2>
</li>
<li>control file 손상<ul>
<li><code>RECOVER DATABASE USING BACKUP CONTROLFILE</code> 명령 사용</li>
</ul>
</li>
<li>파일 경로 정보 오류<ul>
<li><code>ALTER DATABASE RENAME FILE</code>로 수정</li>
</ul>
</li>
<li>ASM 디스크 관련 문제<h3 id="복구-작업">복구 작업</h3>
</li>
<li>control file 복구 또는 재생성</li>
<li>데이터 파일 및 로그 파일 경로 수정<h1 id="open-단계">OPEN 단계</h1>
</li>
<li>데이터베이스 파일(데이터파일, 로그 파일)에 접근, 데이터베이스가 사용자 연결을 받을 준비가 됨</li>
<li>UNDO 테이블스페이스와 TEMP 테이블스페이스가 활성화됨<h2 id="복구-가능-항목-2">복구 가능 항목</h2>
</li>
<li>데이터 파일 손상<ul>
<li>데이터파일이 손상된 경우, 백업 파일로 복구하거나 <code>RECOVER DATABASE</code>를 수행</li>
</ul>
</li>
<li>미사용 상태 파일 </li>
<li>테이블스페이스 관련 문제 <ul>
<li>특정 테이블스페이스를 OFFLINE으로 전환하여 데이터베이스를 부분적으로 OPEN 가능 </li>
</ul>
</li>
<li>아카이브 로그 또는 백업을 사용한 데이터 파일 복구<ul>
<li>ALTER DATABASE 명령으로 문제 파일 제거 또는 경로 변경</li>
<li></li>
</ul>
</li>
</ul>