<ul>
<li>데이터베이스가 데이터를 읽고 쓸 때 일반적인 버퍼 캐시를 거치지 않고, 데이터 파일에서 직접 I/O 작업을 수행하는 방식이다. 이를 통해 성능을 크게 향상시킬 수 있다.</li>
</ul>
<h2 id="비유---도서관">비유 - 도서관</h2>
<ul>
<li>도서관에서 책을 빌릴 때, 책을 책장에서 바로 꺼내기보다 사서에게 요청해서 사서가 책을 찾아서 가져오는 것</li>
<li>사서가 사용하는 카운터: 버퍼 캐시<ul>
<li>중간 단계를 거치면, 책을 찾는 속도가 늦어질 수 있다.</li>
</ul>
</li>
</ul>
<h3 id="direct-path-io는">Direct Path I/O는</h3>
<ul>
<li><p>도서관에 들어가서 내가 직접 필요한 책을 책장에서 바로 꺼내는 것. </p>
</li>
<li><p>일반적으로 대용량 데이터 작업, ex) 대용량 테이블의 Full Table Scan이나, 대량의 데이터 로드(예: Oracle의 SQL*Loader) 시에 사용된다.</p>
</li>
<li><p>이런 경우, 데이터를 빠르게 처리하는 것이 중요한데, 버퍼 캐시를 통해 데이터를 처리하면 효율이 떨어지기 때문에 Direct Path I/O가 더 적합하다.</p>
<br />
</li>
<li><p><strong>Buffer Cache를 우회</strong></p>
<ul>
<li>Direct Path I/O는 버퍼 캐시를 거치지 않기 때문에 메모리를 사용하지 않고, 디스크에서 데이터를 직접 읽거나 쓰게 된다.</li>
</ul>
</li>
<li><p><strong>대량 데이터 처리</strong></p>
<ul>
<li>큰 블록 단위로 데이터를 읽거나, 쓰기 때문에 대량의 데이터를 빠르게 처리</li>
</ul>
</li>
<li><p><strong>I/O 대기 시간 감소</strong></p>
<ul>
<li>일반 I/O 방식보다 대기 시간이 줄어 더 빠른 데이터 처리가 가능</li>
</ul>
</li>
</ul>
<h2 id="언제-사용하나요">언제 사용하나요?</h2>
<ul>
<li>대용량 데이터를 처리할 때 성능을 높이기 위해 Direct Path I/O 사용</li>
<li>ex) CREATE TABLE AS SELECT (CTAS) , 병렬 처리가 필요한 작업</li>
</ul>
<pre><code class="language-sql">CREATE TABLE 새로운테이블명 AS
SELECT 열1, 열2, ...
FROM 기존_테이블명 
WHERE 조건;</code></pre>
<h3 id="왜-ctas를-사용하지-않을-때-디스크와-메모리를-더-많이-사용하게-될까요">왜 CTAS를 사용하지 않을 때 디스크와 메모리를 더 많이 사용하게 될까요?</h3>
<ol>
<li><strong>버퍼 캐시 사용</strong> </li>
</ol>
<ul>
<li>일반적인 <code>INSERT INTO</code>는 데이터를 읽고 쓰는 과정에서 Oracle의 버퍼 캐시를 이용한다. 
버퍼 캐시에 데이터가 로드되고, 그 데이터를 수정한 후 다시 디스크로 쓰기 때문에 메모리와 I/O 리소스를 더 많이 사용하게 된다.</li>
</ul>
<ol start="2">
<li><strong>Direct Path I/O 미사용</strong></li>
</ol>
<ul>
<li><code>INSERT INTO</code> 방식은 최적화가 적용되지 않는다.</li>
<li>CTAS는 Direct Path I/O를 통해, 버퍼 캐시를 우회하고 디스크에서 직접 데이터를 읽고 쓰기 때문에 디스크 I/O도 최소화가 가능하다. </li>
</ul>