# Here's some new strange stuff, remember type it exactly.
# set days to a string 
days = "Mon Tue Wed Thu Fri Sat Sun"
# set months to a string that contains \n
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Writes a string containing days
puts "Here are the days: #{days}"
# Writes a string containing months
puts "Here are the months: #{months}"
# Writes a longer string separated in lines
puts %q{
    There's something going on here.
    With this weird quote
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5, or 6.
}