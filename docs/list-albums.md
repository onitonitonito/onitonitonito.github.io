---
layout: default
permalink: /albums/
---
{% for album in site.albums %}

<!-- 아트스트 정보 -->

  <h1> {{ album.title }} </h1>
  <!-- 앨범 이미지 화일 / 앨범소스 링크 / 앨범타이틀 -->
  <a href="{{album.music}}" target="new">
    <img src="{{album.img}}" width="200" align="left" style="padding: 5px 30px 0px 0px;"></a>

  <p>[Arist] Performed by ... {{ album.artist }}<br>
    {% if album.director %}
    [Direct] Directed by ... {{ album.director }}
    {% endif %}

    <ul>
      <li>Released : {{album.released}}</li>
      <li>Genres : <br>
      {% for genre in album.genres %}
        {{album.genres}},
      {% endfor %}

      </li>
    </ul>

  <br>
    {% for work in album.works %}
      <h1> {{ work.title }} </h1>
      <p> [Compose] Composed by ... {{ work.composer }}</p>
      <ol>
        {% for track in work.tracks %}
          <li>{{ track.title }} ({{ track.duration }})</li>
        {% endfor %}
      </ol>
    {% endfor %}
  </p>

<!-- Hr 스타일 참조: https://css-tricks.com/examples/hrs/ -->
<!-- Simple Styles for <hr>'s -->

  <hr style="
    border: 0;
    height: 1px;
    background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0));">
  <br><br>
{% endfor %}
