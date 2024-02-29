#!/usr/bin/env ruby
# from = ARGV[0].scan(/from:(.*?)\]/)
# to = ARGV[0].scan(/to:(.*?)\]/)
# flags = ARGV[0].scan(/flags:(.*?)\]/)
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")