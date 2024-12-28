<table>
<thead>
<tr>
<th>작업명</th>
<th>명령어</th>
<th>출력 결과</th>
</tr>
</thead>
<tbody><tr>
<td>sqlplus 기동 중지</td>
<td><code>$ sqlplus / as sysdba</code></td>
<td><code>Connected to: Oracle Database 19c Enterprise Edition Release 19.0.0.0.0</code><br /><code>SQL&gt; shutdown immediate;</code><br /><code>Database dismounted.</code><br /><code>ORACLE instance shut down.</code></td>
</tr>
<tr>
<td>listener 확인, 중지</td>
<td>N/A</td>
<td>Listener 상태 확인 및 중지 작업 필요. (명령어 미제공)</td>
</tr>
<tr>
<td>해당 interim scp로 전송</td>
<td><code>$ scp /bsj/interim/* oracle@n1:/oramedia/interim</code></td>
<td>파일들이 성공적으로 전송됨. (각 파일 전송 결과 포함)</td>
</tr>
<tr>
<td>interim 경로 확인</td>
<td><code>$ ls -al</code></td>
<td>경로 내 파일 리스트 출력.<br /><code>p30787757_1924000DBRU_Linux-x86-64.zip</code> 등 다수의 파일 포함</td>
</tr>
<tr>
<td>압축 풀기</td>
<td><code>$ unzip p30787757_1924000DBRU_Linux-x86-64.zip</code></td>
<td>압축 해제 완료.<br /><code>30787757/files/lib/libserver19.a/qosp.o</code> 등의 파일 생성.<br /><code>README.txt</code> 포함</td>
</tr>
<tr>
<td>충돌나는 패치가 있는지 확인</td>
<td><code>$ opatch prereq CheckConflictAgainstOHWithDetail -ph ./</code></td>
<td><code>Prereq &quot;checkConflictAgainstOHWithDetail&quot; passed.</code><br /><code>OPatch succeeded.</code></td>
</tr>
<tr>
<td>opatch apply</td>
<td><code>$ opatch apply</code></td>
<td>패치 적용 성공.<br /><code>Patch 30787757 successfully applied.</code><br />로그 파일 위치 제공: <code>/u01/app/oracle/...</code></td>
</tr>
<tr>
<td>opatch lspatches</td>
<td><code>$ opatch lspatches</code></td>
<td>적용된 패치 리스트 출력:<br /><code>30787757;GLOBAL INDEX DISTINCT_KEYS SET TO ZERO AFTER PARTITION MOVE</code> 등 다수.</td>
</tr>
</tbody></table>