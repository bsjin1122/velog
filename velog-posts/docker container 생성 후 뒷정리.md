<ul>
<li>컨테이너를 생성한 후, 뒷정리하는 습관을 들이도록 하자. </li>
<li>도커 데스크톱을 사용할 때에는 컴퓨터의 리소스를 차지하는 경우가 많다. </li>
<li>이미지를 반복적으로 사용한다면 괜찮겠짐나, 그렇지 않다면 이미지를 그때그때 지우도록 하자.<ul>
<li>어떤 이미지와 컨테이너를 사용했는지 잊어버렸다면? <blockquote>
<p>docker ps / docker image ls 커맨드를 사용하자.</p>
</blockquote>
</li>
</ul>
</li>
</ul>
<h3 id="컨테이너-뒷정리">컨테이너 뒷정리</h3>
<table>
<thead>
<tr>
<th>설명</th>
<th>명령어</th>
</tr>
</thead>
<tbody><tr>
<td>컨테이너 목록 확인</td>
<td>docker ps -a</td>
</tr>
<tr>
<td>컨테이너 종료</td>
<td>docker stop 컨테이너이름</td>
</tr>
<tr>
<td>컨테이너 삭제</td>
<td>docker rm 컨테이너이름</td>
</tr>
</tbody></table>
<h3 id="이미지-뒷정리">이미지 뒷정리</h3>
<table>
<thead>
<tr>
<th>설명</th>
<th>명령어</th>
</tr>
</thead>
<tbody><tr>
<td>이미지 목록 확인</td>
<td>docker image ls</td>
</tr>
<tr>
<td>이미지 삭제</td>
<td>docker image rm 이미지이름</td>
</tr>
</tbody></table>
<h3 id="네트워크-뒷정리">네트워크 뒷정리</h3>
<table>
<thead>
<tr>
<th>설명</th>
<th>명령어</th>
</tr>
</thead>
<tbody><tr>
<td>네트워크 목록 확인</td>
<td>docker network ls</td>
</tr>
<tr>
<td>네트워크 삭제</td>
<td>docker network rm 네트워크이름</td>
</tr>
</tbody></table>
<h3 id="볼륨-뒷정리">볼륨 뒷정리</h3>
<table>
<thead>
<tr>
<th>설명</th>
<th>명령어</th>
</tr>
</thead>
<tbody><tr>
<td>볼륨 목록 확인</td>
<td>docker volume ls</td>
</tr>
<tr>
<td>볼륨 삭제</td>
<td>docker volume rm 볼륨이름</td>
</tr>
</tbody></table>