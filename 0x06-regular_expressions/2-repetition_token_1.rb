#!/usr/bin/env ruby
pattern = /hb?tn/
str = ARGV[0]
matches = str.scan(pattern)  # Find matches
puts matches.join()  # Concatenate the matching strings and print them
