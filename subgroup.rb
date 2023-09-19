# given a group and an element, determine the order of that element
# the groups are the integers modulo n

puts "Calculate the order of an element in the integers modulo n"
puts "n = "
n = gets.chomp.to_i

puts "Take element in modulo n"
m = gets.chomp.to_i

k = 1

until (k * m) % n == 0
    k += 1
end

puts "The order of element is #{k}"
