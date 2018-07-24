#!/usr/bin/env ruby
files = Dir["./tests/*"]

system "tput reset" or system "clear" or system "cls"

puts "Inicio tests"
2.times { || puts "*"*80 }

files.sort().each do |f|
  puts "-"*50
  puts "Archivo: #{f}"
  puts "Input: " + `cat #{f}`
  puts "Output:"
  `./main.py #{f}`.split("\n").each do |line|
    puts "\t #{line}"
  end
  puts "-"*50
end
