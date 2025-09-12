module Jekyll
  class ToggleTag < Liquid::Tag
    def initialize(tag_name, text, tokens)
      super
      # Split on "|" to get original and alt
      parts = text.strip.split("|", 2)
      @original = parts[0].strip
      @alt      = parts[1]&.strip || ""
    end

    def render(context)
      <<~HTML
        <span class="toggle-text"
              data-original="#{@original}"
              data-alt="#{@alt}">
          #{@original}
        </span>
      HTML
    end
  end
end

Liquid::Template.register_tag('t', Jekyll::ToggleTag)
