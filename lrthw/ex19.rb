# define a function named cheese_and_crackers and give it arguments cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers)
    # write a string that contains the first argument, cheese_count
    puts "You have #{cheese_count} cheeses!"
    # write a string that contains the second argument, boxes_of_crackers
    puts "You have #{boxes_of_crackers} boxes of crackers!"
    # write a string
    puts "Man that's enough for a party!"
    # write a string that contains a \n
    puts "Get a blanket.\n"
# ending the function definition
end

# write a string explaining we can give the function numbers directly when we run it
puts "We can just give the function numbers directly:"
# call the function by its name, cheese_and_crackers with two numbers as arguments
cheese_and_crackers(20, 30)

# write a string explaining we can use variables from our script as arguments when we run it
puts "OR, we can use variables from our script:"
# assign number 10 to variable amount_of_cheese
amount_of_cheese = 10
# assign number 50 to variable amount_of_crackers
amount_of_crackers = 50

# call the function by its name, cheese_and_crackers with two variables as arguments 
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# write a string explaining we can do math inside the () too
puts "We can even do math inside too:"
# call the function by its name, cheese_and_crackers with 2 math operations as arguments 
cheese_and_crackers(10 + 20, 5 + 6)

# write a string explaining we can combine variables and math as arguments when we run it
puts "And we can combine the two, variables and math:"
# call the function by its name, cheese_and_crackers with a combo of variables and math as arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Study drills
# 3

def count_wolfs(first_pack, second_pack)
    puts "The first pack of wolfs has #{first_pack} wolfs."
    puts "The second pack of wolfs has #{second_pack} wolfs."
    puts "The total number of wolfs is #{first_pack + second_pack}."
end

# now calling it:
puts count_wolfs(12, 7) # 1
print count_wolfs(3, 5) # 2
first_pack = 32
second_pack = 21
puts count_wolfs(first_pack, second_pack) # 3
count_wolfs(2 * 7, 3 * 19) # 4
count_wolfs( 3 + 2 * 2, 4) # 5
count_wolfs(10 % 3, 8 % 2) # 6
count_wolfs(22.0 / 2, 30.0 / 3) # 7
count_wolfs(4 ** 54, 699 ** 74) # 8
count_wolfs(490, 908) # 9
puts "Enter the number of wolfs in the first pack, please:"
first_number = gets.chomp.to_i
puts "Enter the number of wolfs in the second pack,please:"
second_number = gets.chomp.to_i
count_wolfs(first_number, second_number) # 10


















