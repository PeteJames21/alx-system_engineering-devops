#!/usr/bin/env ruby
pattern = /hbt{2,5}n/
str = ARGV[0]
matches = str.scan(pattern)  # Find matches
puts matches.join()  # Concatenate the matching strings and print them
