<pre><code class="language-shell">[root@kidjin5 ~]# cd /u01/app/oracle/product/19c/gridhome_1/cv/rpm
[root@kidjin5 rpm]# rpm -ivh cvuqdisk-*.rpm
Verifying...                          ################################# [100%]
Preparing...                          ################################# [100%]
Using default group oinstall to install package
Group oinstall not found
oinstall : Group doesn't exist.
Please define environment variable CVUQDISK_GRP with the correct group to be used
error: %prein(cvuqdisk-1.0.10-1.x86_64) scriptlet failed, exit status 1
error: cvuqdisk-1.0.10-1.x86_64: install failed</code></pre>
<ul>
<li>CVUQDISK_GRP</li>
<li>Preinstaller -&gt; group이 oinstall로 생성이 됨 (oracle계정)</li>
<li><code>export CVUQDISK_GRP=dba</code></li>
<li>-ivh 보단 -Uvh (upgrade까지) 사용</li>
</ul>
<pre><code>[root@kidjin5 rpm]# export CVUQDISK_GRP=dba
[root@kidjin5 rpm]# rpm -ivh cvuqdisk-*.rpm
Verifying...                          ################################# [100%]
Preparing...                          ################################# [100%]
Updating / installing...
   1:cvuqdisk-1.0.10-1                ################################# [100%]
</code></pre>