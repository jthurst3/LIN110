# coding: utf-8
class StaticController < ApplicationController
  def home
    cookies[:user_count] = 0 if cookies.key? :user_count
  end

  def parsing
  	cookies[:user_count] = 0 if cookies.key? :user_count

  	s = File.read("vocabulary.txt").split(/\n/)
  	@words = {}
  	@words["determiners"] = Array.new
  	@words["nouns"] = Array.new
  	@words["verbs"] = Array.new
  	@words["auxverbs"] = Array.new
  	@words["adjectives"] = Array.new
  	@words["adverbs"] = Array.new
  	@words["conjunctions"] = Array.new
  	@words["prepositions"] = Array.new
  	s.each do |w|
  		sp = w.split(/\t/)
  		pos = sp[0]
  		word = sp[1]

  		@words[pos].append(word)
  	end
  end

  def phonology
  	cookies[:user_count] = 0 if cookies.key? :user_count
  	# get sounds and their pronunciations
  	# examples copied from https://en.wikipedia.org/wiki/Arpabet
  	s = File.read("sounds.txt").split(/\n/)
  	@sounds = Array.new
  	s.each do |sound|
  		sp = sound.split(/\t/)
  		ipa = sp[0]
  		pronunciation = sp[1]
  		retString = ""
  		pronunciation.each_char do |letter|
  			if letter == letter.upcase
				retString += "<u><em>" + letter.downcase + "</em></u>"  				
  			else
  				retString += letter
  			end
  		end
  		@sounds.append([ipa, pronunciation, retString])
  	end
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
    %x(cd ..; echo "#{text}" #{grammar} >> parsing_queries.txt)
  	ret = %x(cd ..; python parse_trees.py "#{text}" #{grammar})
  	ret = ret.strip
  	link = ret[6..ret.length]
  	r = %x(mv ../#{ret} app/assets/images/#{link} )
    success = log link
    #logger.debug "THIS IS A LOG TEXT #{success}"
  	render json:{tree: link, counter: 0} .to_json
  end

  def phoneme_allophone_program
  	puts params
  	phones = params['phones']
  	words = params['words']
    word_strings = ""
    words.each { |w| word_strings << (w + " ") }
    %x(cd ..; echo "#{phones}" #{word_strings} >> phonology_queries.txt)
    # puts "python driver.py \"#{phones}\" #{word_strings}"
    # pythonVersion = %x(which python)
    # puts pythonVersion
  	ret = %x(cd ..; python driver.py "#{phones}" #{word_strings})
  	puts ret
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
  	render json:{env1: environment1, env2: environment2, result1: compContrastive, result2: phonemeResult, counter: 0} .to_json
  end

end
