<h2 id="검색-키워드">검색 키워드</h2>
<blockquote>
<p>CHAINING 
MIGRATION 
ROW 
PCTFREE</p>
</blockquote>
<ul>
<li><p>테이블 행 데이터가 1개의 데이터에 insert되지 않아, 행 연쇄와 행이행(row chaining, row migration)이라고 불리는 현상이 발생할 가능성이 있다.</p>
</li>
<li><p>行連鎖と行移行 (Doc ID 2452900.1)</p>
</li>
</ul>
<h2 id="row-chaining">Row Chaining</h2>
<ul>
<li>행이 insert된 시점에 1블록에 들어가지 않는 사이즈일 경우에 발생한다.</li>
<li>이러한 경우, oracle은 segment 내 복수의 블록을 chain하는 형태로 행 데이터를 넣는다.</li>
<li>LONG, LONG RAW, LOB 등의 데이터 타입을 갖는 테이블에서는 행 사이즈가 커지면서 로우체이닝이 발생할 가능성이 커진다.</li>
<li>행 사이즈가 블록 사이즈보다 큰 경우엔, 로우체이닝의 발생은 피할 수 없게 된다.</li>
</ul>
<h2 id="row-migration">Row Migration</h2>
<ul>
<li><p>일단 블록에 insert 된 행이, update에 의해 행 사이즈가 커지면서, 그 블록의 남은 공간이 부족한 경우에 발생한다.</p>
</li>
<li><p>이러한 경우, Oracle은 행 전체를 남는 영역의 별도 블록으로 이동시켜, 원래의 행이 insert되어 있던 블록에는 이동할 곳의 블록을 가리키는 포인터를 남긴다.</p>
</li>
<li><p>따라서 로우 마이그레이션이 발생해도 rowid는 변경되지 않는다.</p>
</li>
</ul>
<h3 id="성능-저하">성능 저하</h3>
<ul>
<li><p>row chaining이나 row migration이 발생하면, 행 데이터를 참조하기 위해 여러 개의 블록에 access 하지 않으면 안되기 때문에, 성능이 저하된다.</p>
</li>
<li><p>둘을 발생시키게 하는 insert나 update는, 추가의 처리가 필요하게 되기 때문에 성능이 안좋아진다.</p>
</li>
<li><p>행연쇄, 행이행 되고 있는 행을 index를 사용해서 access할 경우 select는 추가 I/O를 필요로 하게 된다.</p>
</li>
</ul>
<h2 id="row-chaining-row-migration의-검출">row chaining, row migration의 검출</h2>
<ul>
<li>테이블이나 클러스터 내 행연쇄, 행이행되어있는 row는 <code>ANALYZE</code> command를 <code>LIST CHAINED ROWS</code> 옵션을 지정해서 실행하는 것으로 식별이 가능하다.</li>
<li>이 명령어는 행이행이나 행연쇄가 발생하고 있는 행의 정보를 수집해서 특정한 테이블에 출력한다.</li>
<li>결과를 출력하기 위해 테이블은 , UTLCHAIN.SQL이라는 스크립트를 실행해 작성한다.</li>
</ul>
<pre><code class="language-sql">SQL&gt; ANALYZE TABLE &lt;USER_NAME&gt;.&lt;TABLE_NAME&gt; LIST CHAINED ROWS;
SQL&gt; SELECT * FROM chained_rows;

-----------------------------------
SQL&gt; SELECT name, value FROM v$sysstat WHERE name = 'table fetch continued row';

NAME                                                                 VALUE
---------------------------------------------------------------- ---------
table fetch continued row                                   
---&gt; Oracle 내부에서는 하나의 현상으로 취급된다.
- row chaining, row migration 이 검출된 경우에는 어느쪽에서 발생되고 있는지를 신중하게 분석할 필요가 있다.
</code></pre>
<h3 id="row-migration을-해소하기-위한-그-외-방법">row migration을 해소하기 위한 그 외 방법</h3>
<ul>
<li>sql 스크립트</li>
</ul>
<pre><code class="language-sql">-- Get the name of the table with migrated rows:
ACCEPT table_name PROMPT 'Enter the name of the table with migrated rows: '

-- Clean up from last execution
set echo off
DROP TABLE migrated_rows;
DROP TABLE chained_rows;

-- Create the CHAINED_ROWS table
@$ORACLE_HOME/rdbms/admin/utlchain.sql
set echo on
spool fix_mig
-- List the chained and migrated rows
ANALYZE TABLE &amp;amp;table_name LIST CHAINED ROWS;

-- Copy the chained/migrated rows to another table
create table migrated_rows as
SELECT orig.*
FROM &amp;amp;table_name orig, chained_rows cr
WHERE orig.rowid = cr.head_rowid
AND cr.table_name = upper('&amp;amp;table_name');

-- Delete the chained/migrated rows from the original table
DELETE FROM &amp;amp;table_name WHERE rowid IN (SELECT head_rowid FROM chained_rows);

-- Copy the chained/migrated rows back into the original table
INSERT INTO &amp;amp;table_name SELECT * FROM migrated_rows;

spool off</code></pre>
<ul>
<li>alter table move 명령어</li>
<li>table 레벨의 export/import</li>
</ul>
<h2 id="row-migration-row-chaining의-해소">row migration, row chaining의 해소</h2>
<ul>
<li><p>LONG, LOB 타입의 사이즈가 큰 경우의 열이 포함된 테이블의 경우, Row chaining의 발생은 피할 수 없는 경우가 대부분이다. </p>
</li>
<li><p>여러 개의 테이블로 행연쇄가 발생하고 있어, 평균 레코드 길이가 그만큼 크지 않은 경우에는 보다 큰 block size를 선택하는 것을 검토할 것</p>
</li>
<li><p>예를 들어, block size가 2kb인 경우, varchar2 타입의 열을 갖는 테이블에서는 record 길의 평균치가 2kb를 초과하는 경우가 있어 block size가 너무 작아 행 연쇄가 발생할 가능성이 있다.</p>
</li>
<li><p>이러한 경우, 보다 큰 block size를 선택하는 것으로 performance가 향상될 것이다.</p>
</li>
<li><p>pctfree가 작은 값으로 설정되어 있으면, 행의 변경 시 블록에 충분한 영역이 남아있지 않아 행이행이 발생되기 쉽다.</p>
</li>
<li><p>update가 발생하는 테이블에서는 update 시에 충분한 영역을 블록으로 남길 수 있도록 pctfree의 값을 설정한다.</p>
</li>
<li><p>pctfree의 값을 크게 하는 것으로 block의 남은 영역을 크게 남길 수 있어 행사이즈가 확장된 update가 가능하게 된다.</p>
</li>
</ul>