<h2 id="상황">상황</h2>
<pre><code class="language-sql">
INSERT INTO tableName (id, call_taxi_name, call_taxi_contact, home_page, can_truenline_reserve, road_id) VALUES
    ('1', '강릉시교통약자이동지원센터', '1577-2014', 'https://call.gwd.go.kr/guide/web', 'TRUE', '187'),
    ('2', '강릉시교통약자이동지원센터', '1577-2014', 'https://call.gwd.go.kr/guide/web', 'TRUE', '188'),
    ('3', '고성군교통약자이동지원센터', '1577-2014', 'https://call.gwd.go.kr/guide/web', 'TRUE', '189'),
    ('4', '강원도지체장애인협회 고성군지회', '1577-2014', 'https://call.gwd.go.kr/guide/web', 'TRUE', '190'),
    ('5', '동해시교통약자이동지원센터', '1577-2014', 'https://call.gwd.go.kr/guide/web', 'TRUE', '191'),
    ('6', '속초시 교통약자이동지원센터', '1577-2014', 'https://call.gwd.go.kr/guide/web', 'TRUE', '192'),
    ('7', '양구군 장애인생활이동지원센터', '1577-2014', 'https://call.gwd.go.kr/guide/web', 'TRUE', '193'),</code></pre>
<ul>
<li>초기 더미데이터를 sql문으로 만들기 위해, <a href="https://tableconvert.com/ko/csv-to-sql">tableconvert 사이트</a>에서 csv 파일을 넣고, sql을 추출했는데.. id, road_id가 '1' 이렇게 되어있어서 수작업... 을 해야하나 답이 없던 상황이었다.</li>
<li>gpt는 글자수의 한계인건지... 파일을 올려도 돌아오는 파일이 내용이 10개밖에 안돌려줘서 ㅋㅋ </li>
<li>id는 자동으로 생성되는데, 하필 fk 때문에,,,, id를 넣어줘야 했다.. </li>
</ul>
<h2 id="방법">방법</h2>
<ul>
<li>notepad에서 정규표현식을 사용해서 제거하기로 생각했다. 
<img alt="" src="https://velog.velcdn.com/images/greendev/post/823a9b5d-5094-4c41-91b0-ef4dffde17f2/image.png" /></li>
</ul>
<h3 id="숫자---숫자로-바꾸기">'숫자' -&gt; 숫자로 바꾸기</h3>
<blockquote>
<p>찾을 문자: <code>'(\d+)'</code></p>
</blockquote>
<ul>
<li><code>'</code> : 작은 따옴표를 의미</li>
<li><code>(\d+)</code>: 하나 이상의 숫자를 그룹으로 캡쳐한다.<ul>
<li><code>\d</code>: 숫자를 의미</li>
<li><code>+</code>: 1개 이상의 숫자를 의미</li>
<li><code>(\d+)</code>: 작은 따옴표로 둘러싸인 숫자 패턴을 찾는다.</li>
</ul>
</li>
</ul>
<blockquote>
<p>바꿀 문자: <code>\1</code></p>
</blockquote>
<ul>
<li>php, javascript 인 경우엔 $1</li>
</ul>
<h3 id="python으로도-방법이-resub">python으로도 방법이 (re.sub())</h3>
<pre><code class="language-python">import re

text = &quot;'123', '456', '789'&quot;
result = re.sub(r&quot;'(\d+)'&quot;, r&quot;\1&quot;, text)
print(result)  # 123, 456, 789</code></pre>
<p>뭐.. 이렇게로도 해결이 가능하다고 한다.</p>
<h2 id="해결">해결!</h2>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/ef50363f-5f52-4cce-b146-948dbb8205cb/image.png" />
아주 잘 빠졌다. 흐뭇.. </p>
<h2 id="추가">추가</h2>
<ul>
<li><a href="https://www.google.com/search?q=dml+%EC%83%9D%EC%84%B1+%EC%82%AC%EC%9D%B4%ED%8A%B8&amp;oq=dml+%EC%83%9D%EC%84%B1+%EC%82%AC%EC%9D%B4%ED%8A%B8+&amp;gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABixAxiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDc5NjFqMGo3qAIAsAIA&amp;sourceid=chrome&amp;ie=UTF-8">더미데이터 만들 때 참고해야징</a></li>
</ul>