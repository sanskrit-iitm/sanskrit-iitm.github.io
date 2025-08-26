# _plugins/extract-verses.rb
require 'yaml'

module Jekyll
  class VerseExtractor < Generator
    safe true
    priority :low

    def generate(site)
      puts ">>> Verse extractor running in GitHub Actions"
      verses = []

      # ONLY look inside _posts
      site.posts.docs.each do |doc|
        next unless doc.content

        puts "Scanning post: #{doc.path}"

        # Match {% include verse.html ... %} blocks across multiple lines
        doc.content.scan(/{%\s*include\s+verse\.html([\s\S]*?)%}/).each do |match|
          params_str = match[0]

          verse = {}
          # Capture key="value" pairs
          params_str.scan(/(\w+)\s*=\s*"([^"]*?)"/m).each do |key, value|
            verse[key] = value.strip
          end

          # Split authors into an array
          if verse['author']
            verse['author'] = verse['author'].split(",").map(&:strip)
          else
            verse['author'] = []
          end

          verse['page'] = doc.url
          verse['title'] = doc.data['title'] || "Untitled"
          verses << verse
        end
      end

      # inject into site.data
      site.data['verses'] = verses

      puts "Extracted #{verses.size} verses into site.data['verses']"
    end
  end
end
