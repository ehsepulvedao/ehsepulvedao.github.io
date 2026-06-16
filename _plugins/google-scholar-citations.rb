require "active_support/all"
require "nokogiri"
require "open-uri"

module Helpers
extend ActiveSupport::NumberHelper
end

module Jekyll
class GoogleScholarCitationsTag < Liquid::Tag
Citations = {}
CitationNumbers = {}

```
def initialize(tag_name, params, tokens)
  super
  splitted = params.split(" ").map(&:strip)
  @scholar_id = splitted[0]
  @article_id = splitted[1]
end

def render(context)
  article_id = context[@article_id.strip].to_s
  scholar_id = context[@scholar_id.strip].to_s

  article_url = "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=#{scholar_id}&citation_for_view=#{scholar_id}:#{article_id}"

  begin
    if GoogleScholarCitationsTag::Citations.key?(article_id)
      return GoogleScholarCitationsTag::Citations[article_id]
    end

    sleep(rand(1.5..3.5))

    doc = Nokogiri::HTML(
      URI.open(article_url, "User-Agent" => "Ruby/#{RUBY_VERSION}")
    )

    citation_count_number = 0

    description_meta = doc.css('meta[name="description"]')
    og_description_meta = doc.css('meta[property="og:description"]')

    if !description_meta.empty?
      cited_by_text = description_meta[0]["content"].to_s
      matches = cited_by_text.match(/Cited by (\d+[,\d]*)/)

      if matches
        citation_count_number = matches[1].delete(",").to_i
      end

    elsif !og_description_meta.empty?
      cited_by_text = og_description_meta[0]["content"].to_s
      matches = cited_by_text.match(/Cited by (\d+[,\d]*)/)

      if matches
        citation_count_number = matches[1].delete(",").to_i
      end
    end

    citation_count_display = Helpers.number_to_human(
      citation_count_number,
      format: "%n%u",
      precision: 2,
      units: {
        thousand: "K",
        million: "M",
        billion: "B"
      }
    )

  rescue Exception => e
    citation_count_number = 0
    citation_count_display = "N/A"

    puts "Error fetching citation count for #{article_id}: #{e.class} - #{e.message}"
  end

  GoogleScholarCitationsTag::Citations[article_id] = citation_count_display
  GoogleScholarCitationsTag::CitationNumbers[article_id] = citation_count_number

  citation_count_display
end
```

end

class GoogleScholarTotalCitationsTag < Liquid::Tag
def render(context)
total = GoogleScholarCitationsTag::CitationNumbers.values.map(&:to_i).sum

```
  return "0" if total == 0

  Helpers.number_to_human(
    total,
    format: "%n%u",
    precision: 2,
    units: {
      thousand: "K",
      million: "M",
      billion: "B"
    }
  )
end
```

end
end

Liquid::Template.register_tag("google_scholar_citations", Jekyll::GoogleScholarCitationsTag)
Liquid::Template.register_tag("google_scholar_total_citations", Jekyll::GoogleScholarTotalCitationsTag)
