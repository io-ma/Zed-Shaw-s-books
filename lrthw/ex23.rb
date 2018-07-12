# Chose github > atech/postal/app/models/credential.rb because it had 7000+ stars and was open source

# == Schema Information
#
# Table name: credentials
#
#  id           :integer          not null, primary key
#  server_id    :integer
#  key          :string(255)
#  type         :string(255)
#  name         :string(255)
#  options      :text(65535)
#  last_used_at :datetime
#  created_at   :datetime
#  updated_at   :datetime
#  hold         :boolean          default(FALSE)
#

# extends class ApplicationRecord from class Credential
class Credential < ApplicationRecord
      # belongs to server
      belongs_to :server
      # types smtp and api
      TYPES = ['SMTP', 'API']
      # checks if ley is present and if it is unique then validates it
      validates :key, :presence => true, :uniqueness => true
      # checks if the type corresponds to the accepted types, smtp and api
      validates :type, :inclusion => {:in => TYPES}
      # checks if the name is present
      validates :name, :presence => true
      # generates a random string as a unique  key of 24 characters length
      random_string :key, :type => :chars, :length => 24, :unique => true
      # serialize options
      serialize :options, Hash
      # function to_param calls key
      def to_param
        key
      end
      # function use updates_column with the time it was last used
      def use
        update_column(:last_used_at, Time.now)
      end
      # function usage_type checks if it was unused, used less than 1 year, 6 months or one month ago or sooner
      def usage_type
        if last_used_at.nil?
          'Unused'
        elsif last_used_at < 1.year.ago
          'Inactive'
        elsif last_used_at < 6.months.ago
          'Dormant'
        elsif last_used_at < 1.month.ago
          'Quiet'
        else
          'Active'
        end
      end
      # function to_smtp_plain encodes the key in base 64 
      def to_smtp_plain
        Base64.encode64("\0XX\0#{self.key}").strip
      end
    
    end
