#!/usr/bin/env ruby
pattern = /^[0-9]{10,10}$/
str = ARGV[0]
matches = str.scan(pattern)  # Find matches
puts matches.join()  # Concatenate the matching strings and print them
