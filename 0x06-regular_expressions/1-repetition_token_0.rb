#!/usr/bin/env ruby
# puts ARGV[0].scan(/hbt{2,5}n/).join("\n")
# puts ARGV[0].scan(/\b(\w*(\w)\2\w*)\b/).join("\n")
puts ARGV[0].scan(/\b(\w*(\w)\2\w*)\b/).map { |match| match[0] }.join("")
# puts ARGV[0].scan(/\b(\w*(\w)\2{1,4}\w*)\b/).map { |match| match[0] }.join("\n")
