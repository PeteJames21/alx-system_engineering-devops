#!/usr/bin/env ruby
pattern = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
str = ARGV[0]
matches = str.scan(pattern)  # Find matches
puts matches.join(",")  # Concatenate the matching strings and print them
