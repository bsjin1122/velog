<ul>
<li><p>통계 수집 프로시저</p>
<pre><code class="language-sql">CREATE OR REPLACE PROCEDURE gather_seo_stats 
AS
BEGIN
  DBMS_STATS.GATHER_TABLE_STATS(
      ownname =&gt; 'SJBABO',
      tabname =&gt; 'WAREHOUSES',
      estimate_percent =&gt; 10,
      method_opt =&gt; 'FOR ALL COLUMNS SIZE AUTO',
      cascade =&gt; TRUE
  );

  DBMS_OUTPUT.PUT_LINE('Statistics gathered for SJBABO.WAREHOUSES');
END gather_seo_stats;
/
</code></pre>
</li>
</ul>
<hr />
<p>SQL&gt; EXEC gather_seo_stats;</p>
<p>PL/SQL procedure successfully completed.</p>
<pre><code>```sql
SQL&gt; SELECT TABLE_NAME, NUM_ROWS, BLOCKS, EMPTY_BLOCKS, AVG_ROW_LEN, LAST_ANALYZED
FROM DBA_TABLES
WHERE OWNER = 'SJBABO'
  AND TABLE_NAME = 'WAREHOUSES';    2    3    4

TABLE_NAME
--------------------------------------------------------------------------------
  NUM_ROWS     BLOCKS EMPTY_BLOCKS AVG_ROW_LEN LAST_ANAL
---------- ---------- ------------ ----------- ---------
WAREHOUSES
      1000        124            0          27 13-JAN-25👈
</code></pre><p>뭔가 신기</p>