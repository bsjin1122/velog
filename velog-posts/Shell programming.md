<ul>
<li>임시저장글에 적어뒀던 것...</li>
<li><a href="https://oslab.kaist.ac.kr/wp-content/uploads/2019/06/shell_programming-1.pdf">구글링하다가 얻은 한양대 pdf 자료..</a></li>
</ul>
<h2 id="standard-file-descriptor">Standard File Descriptor</h2>
<ul>
<li>유닉스 계열 운영체제 및 리눅스에서 <strong>프로세스와 입출력(I/O)</strong> 를 다루기 위해 사용되는 파일 서술자 중 표준으로 정의된 세 가지를 의미</li>
</ul>
<p><strong>1. stdin (Standard Input)</strong></p>
<ul>
<li>파일 서술자 번호: 0 </li>
<li>프로세스가 입력 받을 때 기본으로 사용하는 기본 입력 채널</li>
<li>예) 키보드(사용자 입력 받기)</li>
</ul>
<p><strong>2. stdout (standard output)</strong></p>
<ul>
<li>파일 서술자 번호: 1</li>
<li>프로세스가 출력 데이터를 보낼 때 사용하는 기본 출력 채널</li>
<li>예: 모니터(터미널), 화면에 메시지 및 데이터 처리 결과 출력</li>
</ul>
<p><strong>3. stderr (standard Error Output)</strong></p>
<ul>
<li>파일 서술자 번호: 2</li>
<li>프로세스가 에러 메시지를 출력할 때 사용하는 채널. 표준 출력과는 별도로 관리된다.</li>
</ul>
<h2 id="redirection">Redirection</h2>
<ul>
<li><code>&gt;</code>: 덮어쓰기. 기존 파일 내용을 지우고 새로 작성</li>
<li><code>&gt;&gt;</code>: 추가하기. 기존 파일의 내용을 유지하며 새 데이터 추가</li>
<li><code>2&gt;</code>: stderr를 파일로 지정</li>
<li><code>&amp;&gt;</code>: stdout과 stderr 모두 재지정<ul>
<li>command &amp;&gt; output.log : 출력과 에러 모두 저장</li>
</ul>
</li>
<li><code>&lt;&lt;</code>: Here Document, 입력 데이터를 직접 스크립트에 작성하여 명령어에 전달할 때 사용<pre><code class="language-shell">cat &lt;&lt; EOF
Line 1
Line 2
EOF</code></pre>
</li>
</ul>
<h3 id="shell-programming-2가지-방법">Shell Programming 2가지 방법</h3>
<ul>
<li>Line Command</li>
<li>Script를 이용<ul>
<li>script 작성</li>
<li>실행 파일로 만들기</li>
<li>실행</li>
</ul>
</li>
</ul>
<h3 id="shell-변수">Shell 변수</h3>
<ul>
<li>모든 변수는 <code>문자열</code>로 간주한다.<ul>
<li>숫자값을 가지는 경우에도 문자열로 간주된다.</li>
</ul>
</li>
<li>shell에서 변수는 사용할 때 선언</li>
<li>변수는 <code>대소문자</code>를 구분한다. </li>
<li>변수에 값이 부여될 때를 제외하고, 변수를 사용할 경우 변수 앞에 <code>$</code> 표시를 붙인다.</li>
<li>변수에 부여된 값은 echo 명령을 통해 확인 가능</li>
</ul>
<h3 id="shell-조건문">Shell 조건문</h3>
<ul>
<li>파일의 존재 유무를 확인하는 test 명령<ul>
<li><code>test -f &lt;filename&gt;</code>
<img alt="" src="https://velog.velcdn.com/images/greendev/post/c7a080ad-8253-4d0c-bc33-9d97fffb7d28/image.png" /></li>
</ul>
</li>
</ul>
<h2 id="shell-파라미터-변수">Shell 파라미터 변수</h2>
<ul>
<li><code>$1, $2 ...</code> : Script에 주어진 파라미터</li>
<li><code>$*</code> : 환경변수 IFS의 첫 문자로 구분되고, 하나의 변수에 저장되는 모든 파라미터의 목록</li>
<li><code>$@</code>: IFS 환경 변수를 사용하지 않는 $*에 대한 변형</li>
</ul>
<h3 id="shell-제어-구조">Shell 제어 구조</h3>
<blockquote>
<pre><code class="language-shell">if condition
  then 
     statements
  else
     statements
fi</code></pre>
</blockquote>
<pre><code>
### For
```shell
  for variable in values
do
  statements
done</code></pre><ul>
<li><img alt="" src="https://velog.velcdn.com/images/greendev/post/1e0d6be2-57a2-4d32-a8f6-4411d604d51d/image.png" /></li>
</ul>
<h3 id="while">while</h3>
<pre><code class="language-shell">#!/bin/bash
foo=1

while [ &quot;$foo&quot; -le 5 ]
do
        echo &quot;Here we go again&quot;
        foo=$(($foo+1))
done
exit 0

=====================================
[root@bastion seojin]# sh c*.sh
Here we go again
Here we go again
Here we go again
Here we go again
Here we go again</code></pre>
<h3 id="until">until</h3>
<pre><code>until condition
do
    statements
done</code></pre><h3 id="case">case</h3>
<pre><code class="language-shell">case variable in
    pattern statements;;
    pattern statements;;
    ...
esac</code></pre>
<h2 id="shell에-내장된-명령">Shell에 내장된 명령</h2>
<ul>
<li>exit n: 쉘 스크립트 또는 명령이 종료될 때 반환하는 <strong>종료 상태 코드</strong>를 나타낸다.</li>
<li>이 값은 프로세스 성공 여부 또는 실패 이유를 나타내며, 다른 프로그램이나 쉘이 이를 참조하여 후속 동작을 결정한다.<h3 id="n-값의-의미">n 값의 의미</h3>
</li>
<li>exit <code>0</code>: 성공적으로 실행되었음을 나타냄</li>
<li>exit <code>1~125</code>: 사용자 정의 에러 코드로, 스크립트에서 특정 오류를 나타내는 데 사용된다.<ul>
<li>예: 파일 없음, 잘못된 입력, 실행 실패 등</li>
</ul>
</li>
<li>exit <code>126</code>: 명령 또는 파일이 실행 불가능한 경우 반환<ul>
<li>예: 실행 권한이 없는 스크립트를 실행하려 했을 때</li>
</ul>
</li>
<li>exit <code>127</code>: 명령을 찾을 수 없음, 존재하지 않는 명령을 실행하려 했을 때</li>
<li>exit <code>128 이상</code>: 시그널로 인해 프로세스가 종료된 경우<ul>
<li>128에 시그널 번호를 더한 값으로 나타낸다.</li>
<li><code>kill -9</code> 명령으로 프로세스를 종료하면, 종료 코드는 137 (128+ 9)가 된다.<h3 id="종료-코드-확인-방법">종료 코드 확인 방법</h3>
</li>
</ul>
</li>
<li>echo $?<pre><code class="language-shell">[root@bastion seojin]# sh c*.sh
Here we go again
Here we go again
Here we go again
Here we go again
Here we go again
[root@bastion seojin]# echo $?
0</code></pre>
<h3 id="시그널-관련-종료-코드-128-이상">시그널 관련 종료 코드 (128 이상)</h3>
<img alt="" src="https://velog.velcdn.com/images/greendev/post/a8377375-4c51-40c9-90dd-98afb3186b9d/image.png" /></li>
</ul>
<h2 id="printf">printf</h2>
<ul>
<li>형식 지정 문자열과 변수를 사용하여 출력을 생성하는 함수/명령어</li>
<li>printf [형식문자열] 매개변수1 매개변수2</li>
</ul>
<blockquote>
<pre><code class="language-shell">[root@bastion ~]# printf &quot;Hello\\World\n&quot;
Hello\World
[root@bastion ~]# printf &quot;Column1\tColumn2\vNew Line\n&quot;
Column1 Column2
               New Line</code></pre>
</blockquote>
<pre><code>
### printf의 Escape Sequence

| **Escape Sequence** | **설명**                                   |
|----------------------|-------------------------------------------|
| `\\`                | 역슬래시 문자 출력                        |
| `\a`                | 경고음(벨 소리) 출력                      |
| `\b`                | 백스페이스 문자 출력                      |
| `\f`                | 폼 피드(Form Feed) 출력                   |
| `\n`                | 새 줄(Line Feed) 문자 출력                |
| `\r`                | 캐리지 리턴(Carriage Return) 문자 출력     |
| `\t`                | 탭(Tab) 문자 출력                         |
| `\v`                | 수직 탭(Vertical Tab) 문자 출력            |
| `\ooo`              | 8진수 값(ooo)으로 표현된 문자를 출력       |

### printf의 변환 지정자

| **변환 지정자** | **설명**            |
|------------------|---------------------|
| `%d`            | 정수를 10진수로 출력 |
| `%c`            | 문자를 출력          |
| `%s`            | 문자열 출력          |
| `%%`            | % 자체를 출력        |

```shell
[root@bastion ~]# printf &quot;정수 출력: %d\n&quot; 42
정수 출력: 42
[root@bastion ~]# printf &quot;문자 출력: %c\n&quot; A
문자 출력: A
[root@bastion ~]# printf &quot;문자열 출력: %s\n&quot; &quot;Hello, World!&quot;
문자열 출력: Hello, World!
[root@bastion ~]# printf &quot;퍼센트 출력: %%\n&quot;
</code></pre><hr />
<ul>
<li><a href="http://wiki.kldp.org/wiki.php/DocbookSgml/Shell_Programming-TRANS">KLDP Shell Programming의 기본</a></li>
<li><a href="http://www.softintegration.com/docs/ch/shell/">초보자용 Shell Programming</a></li>
</ul>