require 'json'
require 'net/http'

$app_id = "245300832548900"
$app_secret = "a9d3f550918392cb207faaf14b7cc054"

def get (uri)
  return Net::HTTP.get_response(URI(uri)).body
end

#uri = URI('http://example.com/index.html?count=10')
$acces_token = get("https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id=#{$app_id}&client_secret=#{$app_secret}")

data = get("https://graph.facebook.com/blekitna14/posts?#{$acces_token}&limit=3")

#puts data

array = []

items = JSON.parse(data)['data']
items.each do |item|
  puts item['id']
  attachments= get("https://graph.facebook.com/#{item['id']}/attachments?#{$acces_token}")
  puts attachments
end
  #attachments_parsed = JSON.parse(attachments)['data']
  #if attachments_parsed[0].media = nil
  #  img_src = 
