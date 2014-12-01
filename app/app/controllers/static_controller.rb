class StaticController < ApplicationController
  def home
  	@log = Log.new
  end
end
