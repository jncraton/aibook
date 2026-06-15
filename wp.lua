function Strong(elem)
  -- 1. Ensure the bold element actually has text content
  if elem.content and #elem.content > 0 then
    -- 2. Convert the bold content into a plain string for the URL
    local link_text = pandoc.utils.stringify(elem.content)
    
    -- 3. Replace spaces with underscores for the Wikipedia URL
    local search_term = link_text:gsub(" ", "_")
    local url = "https://en.wikipedia.org/wiki/" .. search_term
    
    -- 4. Return a Link where the clickable text is the original Strong element
    return pandoc.Link({elem}, url)
  end
end