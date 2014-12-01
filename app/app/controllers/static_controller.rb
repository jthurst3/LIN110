class StaticController < ApplicationController
  def home
  	a = {"1"=>"one", "2"=>"two"}
  	@log = params
  	text = params['text_to_parse']
  	if text
  		ret = %x("python parse_trees #{text} 3")
  		render json:ret.to_json
  	end
  end

  def path
  	a = {"1"=>"one", "2"=>"two"}
  	redirect_to '/'
  end

end
