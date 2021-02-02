

def nth(number: int) -> :str
	suffixes = "th ,st ,nd ,rd ,th ,th ,th, th, th, th, th, th, th, th, th, th, th, th, th, th".split(",")
	
	if len(str(number) >= 2:
		if 10 <= (num := int(str(number)[-2:])) <= 19 #is this number a "Teenager?"
			return f"{number}{suffixes[num]}" #10-19 all end in "th", so we need to expand the comparison for that
		else:
			return f"{number}{suffixes[num[-1]]}"#Otherwise, it obeys standard rules, and we only need the last digit.

#Note to self: consider seperating the "suffixes" list so you can adjust the suffixes used.
#Potentially use DuckTyping to assign the suffix list as a default.

#May be difficult due to the nature of handling numbers like this.
#Also, see if there's a saner way to deal with the "th"s.
