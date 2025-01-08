<pre><code class="language-shell">[oracle@cubjin4 20250107-23:08:46]:ORACUB:[/oramedia]
$ cat dbca.rsp | grep -v ^# | grep -v '^$' &gt; dbc.rsp
[oracle@cubjin4 20250107-23:14:02]:ORACUB:[/oramedia]
$ ls
19.20  19c_base  dbca.rsp  dbc.rsp  db_install.rsp  dbi.rsp
[oracle@cubjin4 20250107-23:14:05]:ORACUB:[/oramedia]
$ vi dbc.rsp
responseFileVersion=/oracle/assistants/rspfmt_dbca_response_schema_v19.0.0
gdbName=ORACUB
sid=ORACUB
databaseConfigType=SI
RACOneNodeServiceName=
policyManaged=
createServerPool=
serverPoolName=
cardinality=
force=
pqPoolName=
pqCardinality=
createAsContainerDatabase=FALSE
numberOfPDBs=
pdbName=
useLocalUndoForPDBs=
pdbAdminPassword=
nodelist=
templateName=/u01/app/oracle/product/19c/dbhome_1/assistants/dbca/templates/New_Database.dbt
sysPassword=패스워드
systemPassword=패스워드
oracleHomeUserPassword=
emConfiguration=NONE
emExpressPort=5500
runCVUChecks=
dbsnmpPassword=
omsHost=
omsPort=
emUser=
emPassword=
dvConfiguration=
dvUserName=
dvUserPassword=
dvAccountManagerName=
dvAccountManagerPassword=
olsConfiguration=
datafileJarLocation=
datafileDestination=/u02/oradata
recoveryAreaDestination=
storageType=FS
diskGroupName=
asmsnmpPassword=
recoveryGroupName=
characterSet=AL32UTF8
nationalCharacterSet=AL16UTF16
registerWithDirService=
dirServiceUserName=
dirServicePassword=
walletPassword=
listeners=
variablesFile=
variables=
initParams=
sampleSchema=
memoryPercentage=40
databaseType=MULTIPURPOSE
automaticMemoryManagement=FALSE</code></pre>
<ul>
<li><code>nohup dbca -silent -createDatabase -responseFile /oramedia/dbc.rsp -totalMemory 4096 &amp;</code></li>
</ul>