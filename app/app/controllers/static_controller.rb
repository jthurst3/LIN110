class StaticController < ApplicationController
  def home
    cookies[:user_count] = 0 if cookies.key? :user_count
  end

  def log(result)
    if cookies.key? :user_count
      cookies[:user_count] = cookies[:user_count].to_i + 1 unless result.nil? #only if successfully parsed
    else
      cookies[:user_count] = 1
    end
    cookies[:user_count].to_i
  end

  def clear
    cookies.delete :user_count
  end

  def path
  	text = params['k'].to_s
    clear if text == "clear"
  	ret = %x(cd ..; python parse_trees.py "#{text}" 1)
  	ret = ret.strip
  	link = ret[6..ret.length]
  	r = %x(mv ../#{ret} app/assets/images/#{link} )
    success = log link
    #logger.debug "THIS IS A LOG TEXT #{success}"
  	render json:{tree: link, counter: success} .to_json
  end

end
