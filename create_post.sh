#!/bin/bash
if [ -z "$1" ]; then
  echo "Error: No post name provided"
  echo "Usage: source create_post.sh \"<post-name>\""
else
    title=$1
    date=$(date "+%Y-%m-%d %H:%M:%S %z")

    # Convert to lowercase, replace spaces with dashes
    slug=$(echo "$title" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g')
    filename=./_posts/$(date "+%Y-%m-%d")-$slug.md

    touch $filename
    
# Prepare front matter content
    cat > "$filename" <<EOF
---
title: $title
permalink: /posts/$slug # Change to Harvard-Kyoto
date: $date
categories: []
tags: []  # TAG names should always be lowercase
authors: []
description: 
# toc: false
# comments: false
---

## समस्या X

{%t सन्ध्यादियुक्तवाक्यांशोऽयम्|सन्धि-आदि-युक्त-वाक्य-अंशः_अयम्}

<details>
  <summary>आङ्ग्ला-ऽनुवादः</summary>
<div markdown="1">



</div>
</details>

## समाधानानि

<!-- Verse format -->

{% include verse.html
   author="...,..."
   meter="..."
   verse="
    ...
    ...
   "
   anvaya="..."
%}

EOF
    echo "Successfully created $filename"
fi