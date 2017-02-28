require 'sinatra'

set :bind, '92.222.86.146'
set :port, '8080'

get '*' do
  send_file 'index.html'
end
