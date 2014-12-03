class StaticController < ApplicationController
  def home
  end

  def path
  	text = params['k']
  	ret = %x(cd ..; python parse_trees.py #{text} 2)
  	ret = ret.strip
  	r = %x(ls app/assets/images/#{ret} ; mv ../#{ret} app/assets/images/#{ret} 2>&1)
  	render json:r.to_json
  end

end
