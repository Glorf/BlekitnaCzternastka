require 'json'
require 'net/http'

$app_id = "245300832548900"
$app_secret = "a9d3f550918392cb207faaf14b7cc054"

def get (uri)
  return Net::HTTP.get_response(URI(uri)).body
end

$acces_token = get("https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id=#{$app_id}&client_secret=#{$app_secret}")

data = get("https://graph.facebook.com/blekitna14/posts?#{$acces_token}&limit=100")
array = []

items = JSON.parse(data)['data']
items.each_with_index do |item, index|
  array << {:text => item['message'], :date => item['created_time']}
  attachments= get("https://graph.facebook.com/#{item['id']}/attachments?#{$acces_token}")
  parsed_attachment = JSON.parse(attachments)['data']
  next if parsed_attachment[0] == nil
  if parsed_attachment[0]['media'] != nil
    array[index][:img] = parsed_attachment[0]['media']['image']['src']
  elsif parsed_attachment[0]['subatachments'] != nil
    array[index][:img] = parsed_attachment[0]['subatachments']['data'][0]['media']['image']['src']
  end
end

html_array = []

array.each do |item| 
  html_array << "<div class=\"entry\"><img src=\"#{item[:img]}\"/><p>#{item[:text]}</p><p>#{item[:date]}</p></div>"
end

File.open('generated_index.html', 'w+') do |file|
  file.puts "<!DOCTYPE html><html><head></head><body>#{html_array.join("")}</body></html"
end
