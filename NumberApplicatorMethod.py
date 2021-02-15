#CHANGELOG:
#-removed a redundant if clause that was preventing the code form running at all
#-fixed a trailing whitespace issue that was causing asserts on the output to fail even when output was valid.

def nth(number: int) -> str:
	suffixes = "th ,st ,nd ,rd ,th ,th ,th, th, th, th".split(" ,")
	
	if 10 <= (int(str(number)[-2:])) <= 19:
	#is this number a "Teenager?"
		return f"{number}th" #10-19 all end in "th", so we can cheat
	else:
		return f"{number}{suffixes[number%10]}"#Otherwise, it obeys standard rules, and we only need the last digit.

#Note to self: consider seperating the "suffixes" list so you can adjust the suffixes used.
#Potentially use DuckTyping to assign the suffix list as a default.

#May be difficult due to the nature of handling numbers like this.
#Also, see if there's a saner way to deal with the "th"s.

print(nth(0))

#Check for single digit numbers
assert nth(0) == "0th"
assert nth(1) == "1st"
assert nth(2) == "2nd"
assert nth(3) == "3rd"
assert nth(4) == "4th"

#Check teenagers
assert nth(11) == "11th"
assert nth(12) == "12th"
assert nth(13) == "13th"

#Check hundreds
assert nth(100) == "100th"
assert nth(101) == "101st"
assert nth(102) == "102nd"