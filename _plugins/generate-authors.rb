module Jekyll
  class AuthorPageGenerator < Generator
    safe true

    def generate(site)
      puts ">>> Author generator running in GitHub Actions"
      authors = site.data['authors']

      authors.each do |id, data|
        site.pages << AuthorPage.new(site, site.source, File.join('authors'), id, data)
      end
    end
  end

  class AuthorPage < Page
    def initialize(site, base, dir, author_id, data)
      @site = site
      @base = base
      @dir  = dir
      @name = "#{author_id}.html"

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'author.html')
      self.data['title'] = data['name']
      self.data['author_id'] = author_id
      self.data['author'] = data
    end
  end
end
