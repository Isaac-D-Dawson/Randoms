#CHANGELOG:
#V1.1:
#-removed a redundant if clause that was preventing the code form running at all
#-fixed a trailing whitespace issue that was causing asserts on the output to fail even when output was valid.
#V1.2:
#-Redesigned entire working function to use a smaller comparison set, reducing the memory needed.

def nth(number: int) -> str:
	suffixes = {"1":"st", "2":"nd", "3":"rd"}
	num = str(number)

	if len(num) >= 2:
		if num[-2] == "1":
			return f"{number}th"
		else:
			if num[-1] in "123":
				return f"{number}{suffixes[num[-1]]}"
			else:
				return f"{number}th"
	else:
		if num[-1] in "123":
				return f"{number}{suffixes[num[-1]]}"
		else:
			return f"{number}th"
    		


		
    		

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