<p>Block corruption 발생시</p>
<ol>
<li>DBVERIFY 를 이용한 Block 관리</li>
</ol>
<p>DBVerify는 Data file block, index file block, undo block 등을 점검해주는 유틸리티입니다. 복구 유틸리티는 아닙니다. Database가 open 상태에서 사용할 수 있는 유틸리티로 database의 중단 없이 점검이 가능합니다. 대신 점검 중인 datafile은 read-only가 되기 때문에 만약 점검 중일 때 DML 작업이 발생하면 잠시 작업이 중단되었다가 다시 실행됩니다. Datafile에 대해서만 점검이 가능합니다.</p>
<p>기본 사용 법</p>
<p>dbv file= [options]</p>
<p>options</p>
<p>file : 점검해야 할 파일명
start : 점검을 시작할 블록 번호 (기본값은 해당 파일의 첫 번째 블록)
end : 점검을 종료할 블록 번호 (기본값은 해당 파일의 마지막 블록)
blocksize : 점검하기를 원하는 파일의 block 크기 (기본값은 2048 byte)
logfile : 점검 결과를 저장할 파일명을 지정 (기본값은 none이며 결과를 화면으로 출력함)
feedback : 0 이상의 숫자로 설정할 수 있으며 검사가 진행되는 동안에 화면에 … 을 찍어서 진행 과정을 보여줌 (기본값은 0)
parfile : dbv를 실행할 때 적용하는 각종 설정들을 파일에 저장해두고 불러와서 사용
userid : ASM 기반의 파일을 점검할 경우 ASM 인스턴스에 접속해야 하기 때문에 반드시 userid를 사용해야 함
segment_id : 특정 세그먼트(table, index, undo) 만 골라서 검사할 수 있음 (9i 이상)
Case 1 – 특정 Datafile 검사</p>
<p>oracle@server111 ~]$ which dbv
~/product/10g/bin/dbv
[oracle@server111 ~]$ dbv file=/home/oracle/oradata/testdb/test01.dbf
DBVERIFY: Release 10.2.0.5.0 - Production on Mon Mar 12 22:51:20 2012
Copyright (c) 1982, 2007, Oracle.  All rights reserved.
DBVERIFY - Verification starting : FILE = /home/oracle/oradata/testdb/test01.dbf
DBVERIFY - Verification complete
Total Pages Examined         : 1280  -&gt; 테스트 한 총 블록의 개수
Total Pages Processed (Data) : 0  -&gt; 테스트 한 총 테이블 블록 개수
Total Pages Failing   (Data) : 0  -&gt; 문제가 있는 블록 개수
Total Pages Processed (Index): 0  -&gt; 테스트 한 총 인덱스 블록 개수
Total Pages Failing   (Index): 0  -&gt; 문제가 있는 블록 개수
Total Pages Processed (Other): 8  -&gt; 테이블이나 인덱스 외 다른 블록 개수
Total Pages Processed (Seg)  : 0
Total Pages Failing   (Seg)  : 0
Total Pages Empty            : 1272  -&gt; 비어있는 블록 개수
Total Pages Marked Corrupt   : 0  -&gt; 문제가 있어서 corrupt marked 된 블록 개수
Total Pages Influx           : 0  -&gt; 다른 사용자가 먼저 데이터를 변경하고 있어서 dbv를 하기 위해 다시 읽은 블록 개수
Highest block SCN            : 504316 (0.504316)
[oracle@server111 ~]$
Case 2 – 특정 세그먼트만 점검</p>
<p>점검해야 하는 data file의 용량이 커서 검사에 많은 시간이 소요되고, 점검이 필요한 테이블에 대한 점검만 진행 할 경우, 특정 세그먼트만 점검을 수행할 수 있습니다.</p>
<p>SQL&gt; create table scott.tt100 (no number) tablespace test;
Table created.
SQL&gt; begin 
  2   for i in 1..100000 loop
  3    insert into scott.tt100 values (i);
  4   end loop;
  5   commit;
  6  end; 
  7  /
PL/SQL procedure successfully completed.
SQL&gt; select t.ts#, s.header_file, s.header_block
  2  from v$tablespace t, dba_segments s
  3  where s.segment_name = 'TT100'
  4  and owner='SCOTT'
  5  and t.name = s.tablespace_name;
       TS# HEADER_FILE HEADER_BLOCK</p>
<hr />
<pre><code>     7           6           11  -&gt; segment id</code></pre><p>SQL&gt;
SQL&gt; host
[oracle@server111 ~]$ dbv userid=scott/tiger segment_id=7.6.11
DBVERIFY: Release 10.2.0.5.0 - Production on Mon Mar 12 22:59:19 2012
Copyright (c) 1982, 2007, Oracle.  All rights reserved.
DBVERIFY - Verification starting : SEGMENT_ID = 7.6.11
DBVERIFY - Verification complete
Total Pages Examined         : 256
Total Pages Processed (Data) : 0
Total Pages Failing   (Data) : 0
Total Pages Processed (Index): 0
Total Pages Failing   (Index): 0
Total Pages Processed (Other): 0
Total Pages Processed (Seg)  : 0
Total Pages Failing   (Seg)  : 0
Total Pages Empty            : 256
Total Pages Marked Corrupt   : 0
Total Pages Influx           : 0
Highest block SCN            : 0 (0.0)
[oracle@server111 ~]$
Case 3 – DML 도중 강제 offline 된 datafile 점검</p>
<p>2개의 터미널을 열고 하나는 update를 수행하고, 다른 터미널에서는 update 되고 있는 table이 속한 tablespace를 강제로 offline 시킨 후 block corruption을 점검하는 실습입니다.</p>
<p>Step 1 – 1번 터미널</p>
<p>QL&gt; select count(<em>)
  2  from scott.tt100;
  COUNT(</em>)</p>
<hr />
<pre><code>400000</code></pre><p>SQL&gt; 
SQL&gt; update scott.tt100
  2  set no=2222;
업데이트 실행중에 2번 터미널에서 TBS 오프라인
Step 2 – 2번 터미널</p>
<p>SQL&gt; @df
t/s name             NAME                                          STATUS         MB         scn</p>
<hr />
<p>SYSTEM               /home/oracle/oradata/testdb/system01.dbf      SYSTEM               470  504806
UNDOTBS1             /home/oracle/oradata/testdb/undotbs01.dbf     ONLINE                55  504806
SYSAUX               /home/oracle/oradata/testdb/sysaux01.dbf      ONLINE               250  504806
USERS                /home/oracle/oradata/testdb/users01.dbf       ONLINE             11.25  504806
EXAMPLE              /home/oracle/oradata/testdb/example01.dbf     ONLINE               100  504806
TEST                 /home/oracle/oradata/testdb/test01.dbf        ONLINE                10  506788
6 rows selected.
1번 터미널에서 update되고 있는 table의 tablespace를 강제로 offline
SQL&gt; alter tablespace test offline immediate;
Tablespace altered.
Step 3 – 1번 터미널에서 에러 발생</p>
<p>SQL&gt; update scott.tt100
2 set no=2222;
update scott.tt100
*
ERROR at line 1:
ORA-00372: file 6 cannot be modified at this time
ORA-01110: data file 6: '/home/oracle/oradata/testdb/test01.dbf'
-&gt; update 도중 에러 발생
Step 4 – DBVerify로 점검</p>
<p>oracle@server111 ~]$ dbv file=/home/oracle/oradata/testdb/test01.dbf
DBVERIFY: Release 10.2.0.5.0 - Production on Mon Mar 12 23:33:37 2012
Copyright (c) 1982, 2007, Oracle.  All rights reserved.
DBVERIFY - Verification starting : FILE = /home/oracle/oradata/testdb/test01.dbf
DBVERIFY - Verification complete
Total Pages Examined         : 1280
Total Pages Processed (Data) : 182
Total Pages Failing   (Data) : 0
Total Pages Processed (Index): 0
Total Pages Failing   (Index): 0
Total Pages Processed (Other): 20
Total Pages Processed (Seg)  : 0
Total Pages Failing   (Seg)  : 0
Total Pages Empty            : 1078
Total Pages Marked Corrupt   : 0
Total Pages Influx           : 0
Highest block SCN            : 506733 (0.506733)
[oracle@server111 ~]$
Step 5 – segment id로 점검</p>
<p>SQL&gt; select t.ts#, s.header_file, s.header_block
  2  from v$tablespace t, dba_segments s
  3  where s.segment_name = 'TT100'
  4  and owner='SCOTT' 
  5  and t.name = s.tablespace_name;
       TS# HEADER_FILE HEADER_BLOCK</p>
<hr />
<pre><code>     7           6           11</code></pre><p>SQL&gt;
[oracle@server111 ~]$ dbv userid=scott/tiger segment_id=7.6.11
DBVERIFY: Release 10.2.0.5.0 - Production on Mon Mar 12 23:36:05 2012
Copyright (c) 1982, 2007, Oracle.  All rights reserved.
DBVERIFY - Verification starting : SEGMENT_ID = 7.6.11
DBV-00111: OCI failure (3427) (ORA-01002: fetch out of sequence)
현재 해당 segment가 속한 data file이 offline이기 때문에 조회가 되지 않습니다. tablespace 복구 후 online하고 다시 시도해 보겠습니다.</p>
<p>SQL&gt; recover tablespace test;
Media recovery complete.
SQL&gt; alter tablespace test online;
Tablespace altered.
[oracle@server111 ~]$ dbv userid=scott/tiger segment_id=7.6.11
DBVERIFY: Release 10.2.0.5.0 - Production on Mon Mar 12 23:47:10 2012
Copyright (c) 1982, 2007, Oracle.  All rights reserved.
DBVERIFY - Verification starting : SEGMENT_ID = 7.6.11
DBVERIFY - Verification complete
Total Pages Examined         : 1152
Total Pages Processed (Data) : 1126
Total Pages Failing   (Data) : 0
Total Pages Processed (Index): 0
Total Pages Failing   (Index): 0
Total Pages Processed (Other): 25
Total Pages Processed (Seg)  : 1
Total Pages Failing   (Seg)  : 0
Total Pages Empty            : 0
Total Pages Marked Corrupt   : 0
Total Pages Influx           : 0
Highest block SCN            : 508673 (0.508673)
[oracle@server111 ~]$
현재 해당 segment에 속한 block에는 corruption이 발생하지 않은 상태이기 때문에 에러가 검출되지 않습니다.</p>
<p>Case 4 – 백업 datafile corruption 발생 시킨 후 점검</p>
<p>[oracle@server111 backup]$ dd if=/dev/zero of=/home/oracle/backup/test01.dbf
-&gt; block corruption 발생
189641+0 records in
189641+0 records out
[oracle@server111 backup]$ 
[oracle@server111 backup]$ 
[oracle@server111 backup]$ dbv file=/home/oracle/backup/test01.dbf
DBVERIFY: Release 10.2.0.5.0 - Production on Mon Mar 12 23:49:20 2012
Copyright (c) 1982, 2007, Oracle.  All rights reserved.
DBVERIFY - Verification starting : FILE = /home/oracle/backup/test01.dbf
Page 1 is marked corrupt
Corrupt block relative dba: 0x00000001 (file 0, block 1)
Completely zero block found during dbv: 
Page 2 is marked corrupt
Corrupt block relative dba: 0x00000002 (file 0, block 2)
Completely zero block found during dbv: 
Page 3 is marked corrupt
Corrupt block relative dba: 0x00000003 (file 0, block 3)
.........(생략)
Page 11776 is marked corrupt
Corrupt block relative dba: 0x00002e00 (file 0, block 11776)
Completely zero block found during dbv: 
DBV-00600: Fatal Error - [25] [134999752] [134999752] [134816776]
[oracle@server111 backup]$
block corruption이 발생한 block에 대해서 위와 같이 corruption 발생한 내역이 출력됩니다.</p>
<ol start="2">
<li>DBMS_REPAIR 패키지 사용</li>
</ol>
<p>DBMS_REPAIR 패키지는 Oracle 8i 부터 포함되어 block corruption을 detection하고 repair하는 패키지입니다. Table block과 index block을 조사하여 문제가 있는 block을 수정해주는 data corruption repair 패키지를 가지고 있으며, sys 계정으로 작업해야 합니다. 엄연히 말하면 dbms_repair 패키지는 block corruption을 복구하는 것이 아니라 block corruption이 발생한 해당 block을 사용하지 않도록 하고 나머지 block들을 사용가능 하게 하는 것입니다. (block corruption이 발생하면 그 이후의 block 들 모두 사용할 수 없기 때문)</p>
<p>1) dbms_repair 프로시저</p>
<p>제약 사항 및 한계점</p>
<p>lob 이나 cluster index는 지원하지 않는다.
dump_orphan_keys 프로시저는 bitmap index, function-based index는 지원하지 않으며 3950 bytes 이상은 지원하지 못한다.
다음은 dbms_repair 패키지에 포함된 프로시저를 설명합니다.</p>
<p>dmin_table</p>
<p>block repair를 하기 위해 필요한 관리 작업(create, drop, purge)을 제공한다. 이런 작업을 하기 위한 테이블 들은 항상 sys schema 소유로 생성되며, 이 테이블에 손상이 발생한 블록들의 리스트를 저장하게 된다.</p>
<p>check_object</p>
<p>table 이나 index의 block corruption을 체크하고 문제가 있는 block은 admin_table 프로시저로 만든 repair table에 기록한다.</p>
<p>corrupt된 블록을 찾아서 corrupt 되었다고 marking까지 한다.</p>
<p>dump_orphan_keys</p>
<p>corrupted 된 블록들이 테이블과 관련된 것이라면 admin_table에서 생성한 곳에 기록이 되지만 index와 관련 있는 블록들이라면 이 테이블에 기록한다.</p>
<p>rebuild_freelists</p>
<p>object의 freelist를 재생성 한다.</p>
<p>segment_fix_status</p>
<p>ASSM 기능을 사용하고 있는 bitmap index가 corrupt 되었다면 이 프로시져가 fix해 준다.</p>
<p>skip_corrupt_blocks</p>
<p>table이나 index scan 할 때 기존에 mark 된 corrupt block 들은 확인하지 않고 건너 뛴다.</p>
<p>2) dbms_repair 사용 준비</p>
<p>① repair_table 생성</p>
<p>SQL&gt; begin
  2   dbms_repair.admin_tables(
  3    table_name=&gt;'REPAIR_TABLE',  -&gt; 이름변경하면 안된다.
  4    table_type=&gt;dbms_repair.repair_table,
  5    action=&gt;dbms_repair.create_action,
  6    tablespace=&gt;'TEST');  -&gt; admin_table이 저장될 tablespace로 변경 가능하다.
  7  end;
  8  /
PL/SQL procedure successfully completed.
SQL&gt; set line 50
SQL&gt; desc repair_table;  (또는 dba_repair_table)
 Name                    Null?    Type</p>
<hr />
<p> OBJECT_ID               NOT NULL NUMBER
 TABLESPACE_ID           NOT NULL NUMBER
 RELATIVE_FILE_ID        NOT NULL NUMBER
 BLOCK_ID                NOT NULL NUMBER
 CORRUPT_TYPE            NOT NULL NUMBER
 SCHEMA_NAME             NOT NULL VARCHAR2(30)
 OBJECT_NAME             NOT NULL VARCHAR2(30)
 BASEOBJECT_NAME                  VARCHAR2(30)
 PARTITION_NAME                   VARCHAR2(30)
 CORRUPT_DESCRIPTION              VARCHAR2(2000)
 REPAIR_DESCRIPTION               VARCHAR2(200)
 MARKED_CORRUPT          NOT NULL VARCHAR2(10)
 CHECK_TIMESTAMP         NOT NULL DATE
 FIX_TIMESTAMP                    DATE
 REFORMAT_TIMESTAMP               DATE
SQL&gt;
② orphan_key_table 생성</p>
<p>장애가 발생한 table과 관련있는 object( 관련 index, FK 등)를 저장하는 테이블. 테이블 검사를 진행하다가 관련있는 인덱스 등이 문제가 있을 수 있기 때문에 미리 생성해둡니다.</p>
<p>SQL&gt; begin
  2   dbms_repair.admin_tables(
  3    table_name=&gt;'ORPHAN_KEY_TABLE',
  4    table_type=&gt;dbms_repair.orphan_table,
  5    action=&gt;dbms_repair.create_action,
  6    tablespace=&gt;'TEST');
  7  end;
  8  /
PL/SQL procedure successfully completed.
SQL&gt; 
SQL&gt; desc orphan_key_table;
 Name                    Null?    Type</p>
<hr />
<p> SCHEMA_NAME             NOT NULL VARCHAR2(30)
 INDEX_NAME              NOT NULL VARCHAR2(30)
 IPART_NAME                       VARCHAR2(30)
 INDEX_ID                NOT NULL NUMBER
 TABLE_NAME              NOT NULL VARCHAR2(30)
 PART_NAME                        VARCHAR2(30)
 TABLE_ID                NOT NULL NUMBER
 KEYROWID                NOT NULL ROWID
 KEY                     NOT NULL ROWID
 DUMP_TIMESTAMP          NOT NULL DATE
SQL&gt;
③ db_block_checking 파라미터</p>
<p>block이 문제가 있는지 없는지를 확인하려면 오라클 파라미터 중에서 block checking 이라는 파라미터를 true 값으로 변경해주어야 합니다. db_block_checking=true 로 설정할 경우 오라클은 모든 블록을 체크하기 시작하기 때문에 어느정도의 overhead 발생합니다. 이 파라미터 값이 false 일 경우 system tablespace만 체크하고 나머지 tablespace는 체크하지 않습니다. db_block_checking 파라미터는 즉시 변경하여 적용가능한 파라미터 입니다. (issys_modifiable = IMMEDIATE)</p>
<p>SQL&gt; alter system set db_block_checking=true;
System altered.</p>
<ol start="3">
<li>dbms_repair 사용(table)</li>
</ol>
<p>실습을 하기 위해서는 먼저 datafile에 block corruption을 발생시켜야 합니다. 발생시키는 방법은 먼저 해당 tablespace를 offline 시키니 후 datafile을 윈도우로 옮겨서 ultra editor와 같이 hex값 수정 가능한 에디터로 열어서 (테이블에 입력된 데이터 중 아무 데이터나 골라서 복사한 후) 원하는 데이터를 찾고 수정합니다. 그 다음 저장 후 다시 Oracle에 넣고 tablespace online 시키면 block corruption이 발생합니다.</p>
<p>SQL&gt; create table scott.test01 (
  2  no number,
  3  name varchar2(10)) tablespace test;
Table created.
SQL&gt; begin<br />  2   for i in 1..10000 loop
  3    insert into scott.test01 values (i, dbms_random.string('A',10));
  4   end loop;
  5   commit;
  6  end;
  7  /
PL/SQL procedure successfully completed.
SQL&gt; alter tablespace test offline;<br />Tablespace altered.
test01.dbf 파일을 윈도우로 이동시켜서 block 장애를 발생한 후 다시 리눅스로 복사합니다.</p>
<p>SQL&gt; alter tablespace test online;
-&gt; online이 되지 않는다면 test tablespace를 복구한 후 online 한다.
Tablespace altered.
SQL&gt; @df
t/s name             NAME                                          STATUS         MB         scn</p>
<hr />
<p>SYSTEM               /home/oracle/oradata/testdb/system01.dbf      SYSTEM               470  511693
UNDOTBS1             /home/oracle/oradata/testdb/undotbs01.dbf     ONLINE                55  511693
SYSAUX               /home/oracle/oradata/testdb/sysaux01.dbf      ONLINE               250  511693
USERS                /home/oracle/oradata/testdb/users01.dbf       ONLINE             11.25  511693
EXAMPLE              /home/oracle/oradata/testdb/example01.dbf     ONLINE               100  511693
TEST                 /home/oracle/oradata/testdb/test01.dbf        ONLINE                10  511753
6 rows selected.
SQL&gt; select count(<em>) from scott.test01;
select count(</em>) from scott.test01
                           *
ERROR at line 1:
ORA-01578: ORACLE data block corrupted (file # 6, block # 32)
ORA-01110: data file 6: '/home/oracle/oradata/testdb/test01.dbf'
SQL&gt; select * from scott.test01;
NO         NAME</p>
<hr />
<pre><code>   369 bmJAWMCtTx
   370 ZIoUbsiQFq</code></pre><p>..........(생략)
      1444 nfhorhlzLX
      1445 lIUNVRvlpS
ERROR:
ORA-01578: ORACLE data block corrupted (file # 6, block # 32)
ORA-01110: data file 6: '/home/oracle/oradata/testdb/test01.dbf'
-&gt; 해당 table을 조회하는 도중 block corruption이 발생한 block을 만나고 그 이후의 블록은 읽지 못하고 에러가 발생한다.
1440 rows selected.
-&gt; test01 table에는 총 10000건의 데이터가 존재하였는데 지금은 block corruption으로 인하여 1440 건의 데이터만 조회되고 있다.
SQL&gt;
장애 Block 검색</p>
<p>corrupt 발생한 block을 찾고, 해당 block에 corrupt가 발생하였다고 marking합니다.</p>
<p>SQL&gt; set serveroutput on;
SQL&gt; declare n_corrupt int;
  2  begin
  3   n_corrupt := 0;
  4   dbms_repair.check_object(
  5    schema_name=&gt;'SCOTT',
  6    object_name=&gt;'TEST01',
  7    repair_table_name=&gt;'REPAIR_TABLE', 
  8    corrupt_count=&gt;n_corrupt);
  9   dbms_output.put_line('장애블록 수: '|| to_char(n_corrupt));
 10  end;
 11  /
장애블록 수: 1
PL/SQL procedure successfully completed.
SQL&gt;
SQL&gt; select object_name, block_id, corrupt_type, marked_corrupt, corrupt_description 
  2  , repair_description
  3  from repair_table;
OBJECT_NAM            BLOCK_ID         CORRUPT_TYPE            MARKED_CORRUPT                    CORRUPT_DESCRIPTION                    REPAIR_DESCRIPTION</p>
<hr />
<p>TEST01                              32                    6148 TRUE                              mark block software                    corrupt
장애 block skip 처리 : skip_corrupt_blocks</p>
<p>SQL&gt; begin
  2   dbms_repair.skip_corrupt_blocks(
  3    schema_name=&gt;'SCOTT',
  4    object_name=&gt;'TEST01',
  5    object_type=&gt;dbms_repair.table_object,
  6    flags=&gt;dbms_repair.skip_flag);
  7  end;
  8  /
PL/SQL procedure successfully completed.
SQL&gt; select count(<em>) from scott.test01;
  COUNT(</em>)</p>
<hr />
<pre><code>  9632</code></pre><p>SQL&gt; select owner, table_name, skip_corrupt
  2  from dba_tables
  3  where owner='SCOTT'
  4  and table_name='TEST01';
OWNER            TABLE_NAME         SKIP_CORRUPT</p>
<hr />
<p>SCOTT            TEST01             ENABLED
-&gt; test01 table에 corrupt 된 블록을 skip 하도록 설정되어 있는지 확인
SQL&gt;</p>
<ol start="4">
<li>dbms_repair 사용(index 포함)</li>
</ol>
<p>SQL&gt; begin
  2   for i in 1..10000 loop
  3    insert into scott.test01 values (i, dbms_random.string('A',10));
  4   end loop;
  5   commit;
  6  end;
  7  /
PL/SQL procedure successfully completed.
SQL&gt; select table_name, owner, num_rows, blocks
  2  from dba_tables
  3  where table_name='TEST01';
TABLE_NAME           OWNER           NUM_ROWS              BLOCKS</p>
<hr />
<p>TEST01               SCOTT           10000                 28
-&gt; test01 table에 10000 row가 존재하고 28 개의 block을 사용하고 있다는 것을 확인
SQL&gt;
SQL&gt; create tablespace indx
  2  datafile '/home/oracle/oradata/testdb/indx01.dbf' size 10M;
-&gt; index 저장을 위한 tablespace 생성
Tablespace created.
SQL&gt; 
SQL&gt; create index scott.idx_test01_name on scott.test01(name) tablespace indx;
-&gt; test01 table의 name 컬럼에 index 생성
Index created.
SQL&gt; 
SQL&gt; select owner, index_name, table_name, num_rows, leaf_blocks
  2  from dba_indexes
  3  where table_name='TEST01';
OWNER      INDEX_NAME                              TABLE_NAME           NUM_ROWS            LEAF_BLOCKS</p>
<hr />
<p>SCOTT      IDX_TEST01_NAME                         TEST01               10000               31</p>
<p>-&gt; 생성된 index도 10000건의 row를 가지는 것을 확인
SQL&gt; 
SQL&gt; alter tablespace test offline;
Tablespace altered.
test01 data file을 윈도우로 옮겨서 block 장애를 일으킨 다음 다시 리눅스로 복사한다.
SQL&gt; 
SQL&gt; alter tablespace test online;
alter tablespace test online
*
ERROR at line 1:
ORA-01113: file 6 needs media recovery if it was restored from backup, or END BACKUP if it was not
ORA-01110: data file 6: '/home/oracle/oradata/testdb/test01.dbf'
-&gt; test tablespace 복구 후 다시 online 해야 함
SQL&gt; recover tablespace test;
Media recovery complete.
SQL&gt; alter tablespace test online;
Tablespace altered.
SQL&gt; select * from scott.test01;
select * from scott.test01
*
ERROR at line 1:
ORA-01578: ORACLE data block corrupted (file # 6, block # 12)
ORA-01110: data file 6: '/home/oracle/oradata/testdb/test01.dbf'
SQL&gt; select count(<em>) from scott.test01;
select count(</em>) from scott.test01
                           *
ERROR at line 1:
ORA-01578: ORACLE data block corrupted (file # 6, block # 12)
ORA-01110: data file 6: '/home/oracle/oradata/testdb/test01.dbf'
SQL&gt;
장애 Block 검색 : check_object</p>
<p>SQL&gt; set serveroutput on;
SQL&gt; 
SQL&gt; declare num_corrupt int;
  2  begin
  3   num_corrupt := 0;
  4   dbms_repair.check_object(
  5    schema_name=&gt;'SCOTT',
  6    object_name=&gt;'TEST01',
  7    repair_table_name=&gt;'REPAIR_TABLE',
  8    corrupt_count=&gt;num_corrupt);
  9   dbms_output.put_line('=============================');
 10   dbms_output.put_line('corrupted blocks: '|| to_char(num_corrupt));
 11  end;
 12  /
=============================
corrupted blocks: 1
PL/SQL procedure successfully completed.
SQL&gt;
SQL&gt; select object_name, block_id, corrupt_type, marked_corrupt, corrupt_description, repair_description
  2  from repair_table;
OBJECT_NAM            BLOCK_ID         CORRUPT_TYPE             MARKED_CORRUPT                  CORRUPT_DESCRIPTION                       REPAIR_DESCRIPTION</p>
<hr />
<p>TEST01                             12  6148                     TRUE                            mark block software                       corrupt
SQL&gt;
index block 상태 조회</p>
<p>SQL&gt; declare num_index int;
  2  begin
  3   num_index := 0;
  4   dbms_repair.dump_orphan_keys(
  5    schema_name=&gt;'SCOTT',
  6    object_name=&gt;'IDX_TEST01_NAME',
  7    object_type=&gt;dbms_repair.index_object,
  8    repair_table_name=&gt;'REPAIR_TABLE',
  9    orphan_table_name=&gt;'ORPHAN_KEY_TABLE',
 10    key_count=&gt;num_index);
 11   dbms_output.put_line('================================');
 12   dbms_output.put_line('index key count : '|| to_char(num_index));
 13  end;
 14  /
================================
index key count : 368
-&gt; test01 table의 block corruption으로 인하여 index 문제가 발생했음을 확인
PL/SQL procedure successfully completed.
SQL&gt;
장애 block skip 처리: skip_corrupt_blocks</p>
<p>SQL&gt; begin
  2   dbms_repair.skip_corrupt_blocks(
  3    schema_name=&gt;'SCOTT',
  4    object_name=&gt;'TEST01',
  5    object_type=&gt;dbms_repair.table_object,
  6    flags=&gt;dbms_repair.skip_flag);
  7  end;
  8  /
PL/SQL procedure successfully completed.</p>
<p>SQL&gt; select count(<em>) from scott.test01;
  COUNT(</em>)</p>
<hr />
<pre><code>  9632</code></pre><p>-&gt; block corruption 발생한 block을 skip하고 난 후 row 조회
SQL&gt;
장애 index 처리</p>
<p>테이블에서 block corruption이 발생한 block은 index 에도 영향을 준다는 것을 위에서 확인하였습니다. 장애가 발생한 index block은 위에서 처럼 skip 하고 다음 블록으로 넘어가도록 할 수 없습니다. 때문에 해당 index를 rebuild하고, 안되면 index 재생성을 해야 합니다.</p>
<p>SQL&gt; select count(<em>) from orphan_key_table;
  COUNT(</em>)</p>
<hr />
<pre><code>   368</code></pre><p>-&gt; 368개의 index key에 문제가 있음을 확인
SQL&gt; 
SQL&gt; truncate table orphan_key_table;
-&gt; table 초기화
Table truncated.
SQL&gt; 
SQL&gt; alter index scott.idx_test01_name rebuild;
-&gt; 장애 발생한 index rebuild
Index altered.
SQL&gt;
SQL&gt; declare num_index int;
  2  begin
  3   num_index := 0;
  4   dbms_repair.dump_orphan_keys(
  5    schema_name=&gt;'SCOTT',
  6    object_name=&gt;'IDX_TEST01_NAME',
  7    object_type=&gt;dbms_repair.index_object,
  8    repair_table_name=&gt;'REPAIR_TABLE',
  9    orphan_table_name=&gt;'ORPHAN_KEY_TABLE',
 10    key_count=&gt;num_index);
 11   dbms_output.put_line('================================');
 12   dbms_output.put_line('index key count : '|| to_char(num_index));
 13  end;
 14  /
================================
index key count : 0
PL/SQL procedure successfully completed.
SQL&gt;
SQL&gt; select count(<em>) from orphan_key_table;
  COUNT(</em>)</p>
<hr />
<pre><code>     0</code></pre><p>SQL&gt;
SQL&gt; select owner, index_name, table_name, num_rows, leaf_blocks
  2  from dba_indexes
  3  where table_name='TEST01';
OWNER         INDEX_NAME                      TABLE_NAME            NUM_ROWS            LEAF_BLOCKS</p>
<hr />
<p>SCOTT         IDX_TEST01_NAME                 TEST01                9632                30
-&gt; rebuild된 index도 skip 처리된 후의 test01 table의 row 수와 동일한 값을 가진다.</p>