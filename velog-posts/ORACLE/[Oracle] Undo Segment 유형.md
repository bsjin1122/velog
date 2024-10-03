<h2 id="undo-segment란">Undo Segment란?</h2>
<ul>
<li>Undo Segment는 데이터베이스에서 트랜잭션이 변경한 데이터의 이전 값을 저장하는 공간입니다. 이를 통해 두 가지 주요 기능을 지원합니다.</li>
</ul>
<h2 id="undo-2가지-주요-기능">Undo 2가지 주요 기능</h2>
<ul>
<li><p><code>트랜잭션 롤백</code>: 트랜잭션이 완료되기 전에 오류가 발생하거나 사용자가 트랜잭션을 취소했을 때, 변경 사항을 되돌릴 수 있는 기능을 제공합니다. </p>
<ul>
<li>이때 Undo Segment에 저장된 이전 값을 사용하여 데이터를 복구합니다.</li>
</ul>
</li>
<li><p><code>읽기 일관성(Read Consistency)</code></p>
<ul>
<li>여러 사용자가 동시에 데이터를 읽거나 쓸 때, 다른 사용자가 데이터를 변경 중이더라도 변경 전의 데이터를 읽을 수 있도록 보장합니다. </li>
<li>Undo Segment에 저장된 이전 값을 통해 사용자는 안전하게 데이터를 읽을 수 있습니다.</li>
</ul>
</li>
</ul>
<h2 id="undo-segment의-주요-유형">Undo Segment의 주요 유형</h2>
<ul>
<li>Undo Segment는 데이터베이스에서 자동으로 관리되며, 몇 가지 유형으로 나눌 수 있습니다. 
이 유형은 데이터베이스의 트랜잭션 처리 방식과 성능 최적화에 중요한 영향을 줍니다.</li>
</ul>
<table>
<thead>
<tr>
<th>유형</th>
<th>정의</th>
<th>특징</th>
<th>용도</th>
</tr>
</thead>
<tbody><tr>
<td><strong>System Undo Segment</strong></td>
<td>시스템 트랜잭션을 처리하는 특별한 Undo Segment</td>
<td>시스템에서 발생하는 필수 트랜잭션을 별도로 관리</td>
<td>데이터베이스 운영 및 복구에 사용</td>
</tr>
<tr>
<td><strong>Non-System Undo Segment</strong></td>
<td>사용자 트랜잭션을 처리하는 Undo Segment</td>
<td>일반 트랜잭션에서 발생한 데이터 변경 사항을 저장</td>
<td>대부분의 사용자 트랜잭션 처리</td>
</tr>
<tr>
<td><strong>Manual Mode</strong></td>
<td>DBA가 수동으로 Undo Segment를 관리</td>
<td>DBA가 직접 Undo Segment를 생성하고 관리</td>
<td>성능 관리가 필요한 환경에서 사용 (최근에는 잘 사용되지 않음)</td>
</tr>
<tr>
<td><strong>Automatic Mode</strong></td>
<td>데이터베이스가 자동으로 Undo Segment를 관리</td>
<td>시스템이 자동으로 Undo 크기 및 수명을 조절, DBA의 개입이 적음</td>
<td>현대 오라클 시스템에서 주로 사용</td>
</tr>
<tr>
<td><strong>Private Undo Segment</strong></td>
<td>특정 트랜잭션 또는 인스턴스에만 할당된 Undo Segment</td>
<td>RAC 환경에서 각 인스턴스에 고유하게 할당, 성능 최적화</td>
<td>RAC 환경에서 노드 간 성능 분리 및 최적화</td>
</tr>
<tr>
<td><strong>Public Undo Segment</strong></td>
<td>여러 트랜잭션에서 공유하는 Undo Segment</td>
<td>여러 트랜잭션이 동일한 Undo Segment를 공유</td>
<td>일반적인 싱글 인스턴스 환경에서 사용</td>
</tr>
<tr>
<td><strong>Deferred Undo Segment</strong></td>
<td>Undo 처리를 지연시켜 성능을 최적화하는 방법</td>
<td>트랜잭션 완료 시까지 Undo 처리를 지연, 대규모 트랜잭션 성능 최적화</td>
<td>대규모 트랜잭션 처리 시 성능 저하 방지</td>
</tr>
</tbody></table>
<br />

<hr />
<h3 id="1-system-undo-segment">1. System Undo Segment</h3>
<ul>
<li>정의: 시스템 트랜잭션(예: 데이터베이스 복구, 백업 작업)에 사용되는 특별한 Undo Segment입니다.</li>
<li>특징: 시스템에서 필수적인 트랜잭션에 대해 별도로 관리됩니다. 일반적인 사용자 트랜잭션과는 구분됩니다.</li>
<li>용도: 데이터베이스의 운영 및 관리와 관련된 작업에서 주로 사용됩니다. 예를 들어, SYSTEM 테이블스페이스에서 발생하는 트랜잭션 처리.</li>
</ul>
<h3 id="2-non-system-undo-segment">2. Non-System Undo Segment</h3>
<ul>
<li>정의: 일반 사용자 트랜잭션에 사용되는 Undo Segment입니다.</li>
<li>특징: 시스템 트랜잭션이 아닌 일반 트랜잭션에서 사용되며, 대부분의 데이터 변경 작업을 처리합니다.</li>
<li>용도: 사용자가 데이터베이스에서 행을 삽입, 업데이트, 삭제할 때 이전 데이터를 저장하여 트랜잭션을 복구하거나 읽기 일관성을 유지하는 데 사용됩니다.</li>
</ul>
<h3 id="3-manual-mode-수동-모드">3. Manual Mode (수동 모드)</h3>
<ul>
<li>정의: DBA가 직접 Undo Segment를 수동으로 관리하는 모드입니다.</li>
<li>특징<ul>
<li>DBA가 필요한 만큼의 Undo Segment를 직접 생성하고 관리합니다. </li>
<li>Automatic Undo Management(자동 관리 모드)가 도입되기 전에 주로 사용되었습니다.</li>
</ul>
</li>
<li>용도: Undo Segment가 제한된 환경에서 트랜잭션 처리 효율성을 높이기 위해 사용되었으나, 최근 버전에서는 잘 사용되지 않습니다.</li>
</ul>
<h3 id="4-automatic-mode-자동-모드">4. Automatic Mode (자동 모드)</h3>
<ul>
<li>정의: 오라클이 스스로 Undo Segment를 관리하는 모드입니다.</li>
<li>특징: 데이터베이스가 필요한 만큼의 Undo Segment를 자동으로 생성하고, 그 크기나 수명을 조정합니다. DBA가 직접 관리하지 않아도 시스템이 알아서 처리합니다.</li>
<li>용도: 대부분의 현대 오라클 시스템에서는 이 모드를 사용하며, 성능을 최적화하고 자동으로 필요한 Undo 리소스를 할당합니다.</li>
</ul>
<h3 id="5-private-undo-segment">5. Private Undo Segment</h3>
<ul>
<li>정의: 특정 트랜잭션 또는 인스턴스에만 할당된 Undo Segment입니다.</li>
<li>특징: Oracle RAC(Real Application Clusters) 환경에서 각 인스턴스에 고유하게 할당됩니다. 개별 트랜잭션 또는 인스턴스의 성능을 최적화하는 데 도움이 됩니다.</li>
<li>용도: RAC 환경에서 각 노드가 고유한 Undo Segment를 사용하여 서로의 작업에 영향을 받지 않고 처리할 수 있도록 합니다.</li>
</ul>
<h3 id="6-public-undo-segment">6. Public Undo Segment</h3>
<ul>
<li>정의: 여러 트랜잭션 또는 인스턴스에서 공유하는 Undo Segment입니다.</li>
<li>특징: 특정 트랜잭션에 할당되지 않고, 모든 트랜잭션에서 공유되어 사용할 수 있습니다.</li>
<li>용도: 일반적인 싱글 인스턴스 환경에서 사용되며, Undo 리소스를 여러 트랜잭션이 동시에 사용할 수 있습니다.</li>
</ul>
<h3 id="7-deferred-undo-segment-지연된-undo-segment">7. Deferred Undo Segment (지연된 Undo Segment)</h3>
<ul>
<li>정의: 메모리 관리 및 트랜잭션 성능을 최적화하기 위해 Undo 작업을 지연시키는 방법입니다.</li>
<li>특징: 트랜잭션이 완료될 때까지 Undo 정보의 일부 처리를 지연시킵니다. 이는 성능을 높이기 위한 기법으로, 특히 대규모 트랜잭션에서 효과적입니다.</li>
<li>용도: 매우 많은 양의 데이터 변경 작업을 처리할 때, 지연된 Undo 처리가 성능 저하를 방지하는 데 도움이 됩니다.</li>
</ul>
<hr />
<h2 id="undo-tablespace">Undo Tablespace</h2>
<ul>
<li><p>Undo Segment는 Undo Tablespace라는 특별한 저장 공간에 위치합니다. 모든 트랜잭션이 이 공간을 사용하여 Undo 정보를 저장합니다.</p>
</li>
<li><p>DBA는 UNDO_TABLESPACE 파라미터를 설정하여 특정 Undo Tablespace를 지정할 수 있습니다.</p>
</li>
<li><p>자동 관리(Automatic Undo Management) 모드에서는, 데이터베이스가 스스로 적절한 Undo Segment와 Tablespace를 관리합니다.</p>
</li>
</ul>
<h2 id="undo-segment의-관리">Undo Segment의 관리</h2>
<ul>
<li>DBA로서 Undo Segment를 잘 관리하려면 UNDO_RETENTION 파라미터에 주의를 기울여야 합니다. 이는 트랜잭션을 롤백할 수 있는 최대 시간을 설정하며, 데이터베이스가 오래된 Undo 정보를 재사용하는 시점을 결정합니다.</li>
</ul>
<blockquote>
<p>Undo Segment는 오라클 데이터베이스의 트랜잭션 관리와 읽기 일관성을 보장하는 중요한 요소입니다. </p>
</blockquote>
<ul>
<li>Undo 정보를 관리하여 데이터베이스의 안정성과 성능을 높일 수 있으며, 이를 통해 DBA는 데이터 복구 및 동시성 문제를 효과적으로 처리할 수 있습니다.</li>
<li>Undo Segment 관리의 핵심은 Undo Tablespace와 Undo Retention 설정을 적절히 유지하고, 시스템이 트랜잭션 작업을 원활하게 처리할 수 있도록 하는 것입니다.</li>
</ul>