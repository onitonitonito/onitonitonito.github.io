---
layout: default
---
<!-- blog post contents : described as { { content } } -->
<div class="posts">
<article class="post">
  {% for post in site.posts %}
      <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>
      <div class="post-list">{{ post.excerpt }}</div>
      <div class="read-more">[<a href="{{ site.baseurl }}{{ post.url }}">Read More</a>]</div>
  {% endfor %}
  </article>
</div>
