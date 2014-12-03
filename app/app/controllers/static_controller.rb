class StaticController < ApplicationController
  def home
  end

  def path
  	text = params['k']
  	ret = %x(cd ..; python parse_trees.py "#{text}" 1)
  	ret = ret.strip
  	link = ret[6..ret.length]
  	#r = %x(ls app/assets/images/trees ; mv ../#{ret} app/assets/images/#{ret} )
  	r = %x(mv ../#{ret} app/assets/images/#{link} )
  	render json:link.to_json
  end

end
