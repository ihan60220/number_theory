def harmonic(n):
    # gives the value of nth harmonic number,
    # which is given as the sum of all the reciprocals of n natural numbers
    # its difference with natural log should give the value of euler mascheroni constant
    result = 0
    n.times do |number|
        result += 1.0 / number

end

n = gets.chomp.to_i

puts harmonic(n)