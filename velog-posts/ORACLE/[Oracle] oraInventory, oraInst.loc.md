<h3 id="상황">상황</h3>
<blockquote>
<ul>
<li>db설치 진행 중에 2번 노드에 /u02 디렉토리 경로도 잘 안잡혀져 있었고 ... 등등의 문제로 
runInstaller도 안되고, deinstall도 안되는 상황이 있었다.</li>
</ul>
</blockquote>
<ul>
<li>oraInst.loc 파일을 따라서 oraInventory 경로에 inventory.xml 파일에 노드1에는 설치가 되어있는 상태로 기술되어 있었고, 노드2에는 설치가 안되어있는 상태로 있었다. </li>
<li>그래서 해당 OraDB19Home1 이 있는 줄을 삭제하고, 다시 진행하게 되었다.</li>
</ul>
<h2 id="orainventory">oraInventory</h2>
<ul>
<li><p>Oracle Universal Installer (OUI) 및 관련 유틸리티가 사용하며, 설치된 모든 Oracle 제품에 대한 정보를 중앙 집중식으로 관리한다.</p>
</li>
<li><p>이 디렉토리는 시스템에 설치된 여러 Oracle Home의 위치, 설치 버전, 패치 적용 내역 등 기록하여, 제품 관리 및 업그레이드, 패치 적용 시 중요한 참조 자료 역할을 수행한다.</p>
</li>
</ul>
<h2 id="inventoryxml">inventory.xml</h2>
<ul>
<li>oraInventory/ContentsXML/inventory.xml<pre><code class="language-xml">&lt;?xml version=&quot;1.0&quot; standalone=&quot;yes&quot; ?&gt;
&lt;!-- Copyright (c) 1999, 2025, Oracle and/or its affiliates.
All rights reserved. --&gt;
&lt;!-- Do not modify the contents of this file by hand. --&gt;
&lt;INVENTORY&gt;
&lt;VERSION_INFO&gt;
 &lt;SAVED_WITH&gt;12.2.0.7.0&lt;/SAVED_WITH&gt;
 &lt;MINIMUM_VER&gt;2.1.0.6.0&lt;/MINIMUM_VER&gt;
&lt;/VERSION_INFO&gt;
&lt;HOME_LIST&gt;
&lt;HOME NAME=&quot;OraGI19Home1&quot; LOC=&quot;/u01/app/oracle/product/19c/gridhome_1&quot; TYPE=&quot;O&quot; IDX=&quot;1&quot; CRS=&quot;true&quot;/&gt; 
&lt;HOME NAME=&quot;OraDB19Home1&quot; LOC=&quot;/u02/app/oracle/product/19c/dbhome_1&quot; TYPE=&quot;O&quot; IDX=&quot;2&quot;/&gt;
&lt;/HOME_LIST&gt;
&lt;COMPOSITEHOME_LIST&gt;
&lt;/COMPOSITEHOME_LIST&gt;
&lt;/INVENTORY&gt;</code></pre>
</li>
<li>VERSION_INFO: Inventory 파일의 생성 시점 및 최소 버전 정보 </li>
<li>HOME_LIST: 시스템에 설치된 각 Oracle Home에 대한 정보를 기록</li>
</ul>
<h2 id="orainstloc">oraInst.loc</h2>
<ul>
<li>Oracle Universal Installer(OUI) 및 관련 도구들이 Oracle Inventory의 위치를 식별할 수 있도록 도와주는 구성 파일이다.<pre><code class="language-shell">inventory_loc=/u01/app/oraInventory -- 실제 Oracle Inventory 디렉토리의 경로
inst_group=dba -- Oracle Inventory를 관리하는 OS 그룹</code></pre>
</li>
</ul>
<blockquote>
<ul>
<li>inventory.xml</li>
</ul>
</blockquote>
<ul>
<li>Oracle Inventory에 등록된 Oracle Home 및 설치 제품의 상세 정보를 XML 형식으로 기록한 파일로, 제품 관리와 패치 내역 등을 추적하는 데 사용된다. <ul>
<li>oraInst.loc</li>
</ul>
</li>
<li>OUI와 기타 Oracle 도구가 위의 inventory.xml파일이 위치한 Oracle Inventory디렉토리를 올바르게 찾을 수 있도록 경로(inventory_loc)와 관리 그룹(inst_group)정보를 제공하는 구성 파일이다.</li>
</ul>
<pre><code class="language-shell">$ find / -name &quot;oraInst.loc&quot; 2&gt;/dev/null
/etc/oraInst.loc
/tmp/GridSetupActions2025-02-17_06-11-50PM/PatchActions/oraInventory/oraInst.loc
/u01/app/oracle/product/19c/gridhome_1/oraInst.loc
/u01/app/oraInventory/oraInst.loc
/u02/app/oracle/product/19c/dbhome_1/oraInst.loc</code></pre>