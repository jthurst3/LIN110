class StaticController < ApplicationController
  def home
    cookies[:user_count] = 0 if cookies.key? :user_count
  end

  def parsing
  	cookies[:user_count] = 0 if cookies.key? :user_count
  end

  def phonology
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
  	puts params
    puts "hello"
  	text = params['k'].to_s
  	grammar = params['gram']
    clear if text == "clear"
  	ret = %x(cd ..; python parse_trees.py "#{text}" #{grammar})
  	ret = ret.strip
  	link = ret[6..ret.length]
  	r = %x(mv ../#{ret} app/assets/images/#{link} )
    success = log link
    #logger.debug "THIS IS A LOG TEXT #{success}"
  	render json:{tree: link, counter: success} .to_json
  end

  def phoneme_allophone_program
  	puts params
  	phones = params['phones']
  	words = params['words']
    word_strings = ""
    words.each { |w| word_strings << (w + " ") }
  	ret = %x(cd ..; python driver.py "#{phones}" #{word_strings})
  	results = ret.split(/\n/)
    environment1 = results[0]
    environment2 = results[1]
    compContrastive = results[2]
    phonemeResult = results[3]
    puts environment1
    puts environment2
  	# link = ret[6..ret.length]
  	# r = %x(mv ../#{ret} app/assets/images/#{link} )
    # success = log link
    #logger.debug "THIS IS A LOG TEXT #{success}"
    # counter is a placeholder. TODO: consider deleting?
  	render json:{env1: environment1, env2: environment2, result1: compContrastive, result2: phonemeResult, counter: 1} .to_json
  end

end
