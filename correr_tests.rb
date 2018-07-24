#!/usr/bin/env ruby
files = Dir["./tests/*"]

`reset`
files.sort().each do |f|
  puts "-"*40
  puts "Archivo: #{f}"
  puts "Input: " + `cat #{f}`
  puts "Output:"
  `./main.py #{f}`.split("\n").each do |line|
    puts "\t #{line}"
  end
  puts "-"*40
end
