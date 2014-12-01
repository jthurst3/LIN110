class CreateLogs < ActiveRecord::Migration
  def change
    create_table :logs do |t|
      t.string :input
      t.string :yes
      t.string :no

      t.timestamps
    end
  end
end
