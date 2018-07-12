print """
1. puts - writes a line + /n ( new line)
2. # - comments out whatever I write after - I like to call it HASH, sounds badass.
3. + ADDS
4. / DIVIDES 
5. 25.0 . -> float
6. - SUBSTRACTS
7. * MULTIPLIES asterisk
8. % MODULUS - divides left operand by right operand , returns remainder.
9. 3² = exponent - multiplies the number by itself exponent times
10. t_a imaginary space
11. "" enclose strings - quotes
12. > - greater than
13. < - less than
14. less than or equal to
15. >= greater than or equal to
16. #{} inserts code into strings
17. = assigns values
18. print - writes a line without /n
19. variable - a box with a name on it
20. irb - interactive ruby shell
21. .rb - ruby file
22. '' - enclose strings
23. true - a boolean with the value of true
24. false - a boolean with the value of false
25. %{} - formatter for strings
26. \""" - triple quote - multi-line strings
27. ''' - triple single-quote - multi-line strings , can contain code #{}
28. \\n - new line
29. \\tab
30. \\ backward slash
31. %q{} - escapes quotes
32. \\uxxxx - character with 16-bit hex value
33. gets - e method used to get input 
34. () brackets - used to enter parameters
35. chomp - removes the new line character at the end of the string
36. .to_i changes a string to an integer
37. ARGV - argument value, the arguments entered on the command line after calling the script
38. $stdin standard input - $stdin.gets different from kernel#gets
39. open(filename) - takes the filename as parameter and returns the file object
40. read - a file method , returns the content of the file as string 
41. .truncate() - a file method, changes the file size to integer bytes
42. .write - a file method , writes the given string to file
43. .close - a file method, closes the file
44. .length - a string method - returns the length of a string
45. open(filename, 'w') - opens the file in write only mode
46. open(filename, 'w+') - opens the file in read/write mode
47. open(filename, 'a') - opens the file in write only mode, appendsdata at the end
48. open(filename, 'a+') - opens the file in read write mode, appends at the end
49. exist? - File.exist? - tell if a file exists or not
50. *args -unpacks all arguments
51. def - defines a function
52. end - ends a function definition
53. run, call, use a function
54. seek - file method - a given position as integer in a stream 
55. += - x = x+ y x+= y
56. return - returns the value 
57. ARGV.first - first argument
"""