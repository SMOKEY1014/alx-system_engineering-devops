#!/usr/bin/env ruby
# puts ARGV[0].scan(/hbt{2,5}n/).join("\n")
# puts ARGV[0].scan(/\b(\w*(\w)\2\w*)\b/).join("\n")
puts ARGV[0].scan(/\b(\w*(\w)\2\w*)\b/).map { |match| match[0] }.join("\n")
# puts ARGV[0].scan(/\b(\w*(\w)\2{1,4}\w*)\b/).map { |match| match[0] }.join("\n")

Find the regular expression that will match the following cases 
Your Test string :
htn
hbtn
hbbtn
hbbbtn

Match results :
htn
hbtn

Using the project format given, create a Ruby script that accepts one argument and pass it to a regular expression matching method