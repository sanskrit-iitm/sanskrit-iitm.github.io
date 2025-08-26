---
layout: authors
icon: fas fa-feather-alt   # pick any FontAwesome icon
order: 4
---

<h1>All Authors</h1>
<div class="author-list">
  {% for author_id in site.data.authors %}
    {% assign data = site.data.authors[author_id[0]] %}
    <div class="author-card">
      <a href="/authors/{{ author_id[0] }}.html">
        <strong>{{ data.name }}</strong> ({{ data.name_eng }})
      </a>
    </div>
  {% endfor %}
</div>
