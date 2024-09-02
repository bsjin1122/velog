<h2 id="상황">상황</h2>
<ul>
<li>DB에는 공공 API 사용하고 있는데, 값이 국내에서 사용되는 좌표계로 사용되고 있었다.</li>
<li>그렇다보니 파라미터와 값이 맞지 않아 변환하는 쪽으로 테스트 하게 되었다.</li>
<li><a href="https://blog.acronym.co.kr/283">좌표계 종류</a></li>
</ul>
<h2 id="해결">해결</h2>
<ul>
<li>DB 전처리 쪽에서 WGS84 좌표계로 바꿔달라고 요청해서 수정이 되었지만 <pre><code class="language-java">Coordinate coordinate = coordinateService.getCoordinate(rawRestaurant.getRdnwhladdr());</code></pre>
</li>
<li>코드를 만들어 놨기에 올려본다. <h3 id="buildgradle">build.gradle</h3>
</li>
</ul>
<blockquote>
</blockquote>
<pre><code>// 좌표계 변환
    implementation 'org.locationtech.proj4j:proj4j:1.1.1'</code></pre><h3 id="java">java</h3>
<pre><code class="language-java">// 메서드 사용 시
double[] tmCoordinates = transformWGS84ToTM(lon, lat);
    double tmLon = tmCoordinates[0];
    double tmLat = tmCoordinates[1];

// WGS84 좌표를 중부원점(TM) 좌표계로 변환하는 메서드
    public double[] transformWGS84ToTM(double lon, double lat) {
        CRSFactory crsFactory = new CRSFactory();

        // WGS84 좌표계 (EPSG:4326)
        CoordinateReferenceSystem crsWGS84 = crsFactory.createFromName(&quot;EPSG:4326&quot;);

        // TM 중부원점 좌표계 (EPSG:2097)
        CoordinateReferenceSystem crsTM = crsFactory.createFromParameters(&quot;EPSG:2097&quot;, &quot;+proj=tmerc +lat_0=38 +lon_0=127.5 +k=1 +x_0=200000 +y_0=500000 +ellps=GRS80 +units=m +no_defs&quot;);

        // CoordinateTransformFactory 생성
        CoordinateTransformFactory ctFactory = new CoordinateTransformFactory();

        // 좌표 변환 객체 생성
        CoordinateTransform transform = ctFactory.createTransform(crsWGS84, crsTM);

        // 변환할 좌표 설정
        ProjCoordinate sourceCoordinate = new ProjCoordinate(lon, lat);
        ProjCoordinate targetCoordinate = new ProjCoordinate();

        // 좌표 변환 수행
        transform.transform(sourceCoordinate, targetCoordinate);

        return new double[]{targetCoordinate.x, targetCoordinate.y};
    }</code></pre>