<h3 id="가">[가]</h3>
<ul>
<li>ASM은 RAID 기능과 비슷하게 구성되어 있다.</li>
<li>ASM으로 구성되지 않았을 때, RAID처럼 구성되어 Voting disk를 각각 1, 3, 5개를 구성하여 이중화, 삼중화하는 것을 failgroup이라고 한다.</li>
</ul>
<h3 id="나">[나]</h3>
<p>그러면 Voting disk에서 1,3,5개는 왜 존재하는것일까? 
voting이 1개만 있는 경우엔, 바로 축출대상을 찾아 evict해버린다.
voting이 3개 중 2개가 과반수인 경우엔, 하나를 먼저 voting하고 난 다음 하나 더 확인하고 evict한다.
마지막으로 voting이 5개면 과반수가 3개이므로, 좀 더 정확하게 확인하고 evict하기 때문에, 더욱 민감하게 반응하고 기간계같은 중요한 서버에서 High로 할 것을 권고하기도 한다... </p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">ocr</th>
<th align="left">voting</th>
</tr>
</thead>
<tbody><tr>
<td align="left">External</td>
<td align="left">1</td>
<td align="left">1</td>
</tr>
<tr>
<td align="left">Normal</td>
<td align="left">2</td>
<td align="left">3</td>
</tr>
<tr>
<td align="left">High</td>
<td align="left">3</td>
<td align="left">5</td>
</tr>
</tbody></table>