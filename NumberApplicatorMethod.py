#CHANGELOG:
#V1.1:
#-removed a redundant if clause that was preventing the code form running at all
#-fixed a trailing whitespace issue that was causing asserts on the output to fail even when output was valid.
#V1.2:
#-Redesigned entire working function to use a smaller comparison set, reducing the memory needed.
#V1.3:
#-Further resdesign, removed unneded "Else" statements.
#-Improved function ducktyping
#--function can now parse an alternate dictionary for numberic suffixes
#---Frankly, this is completely useless, the rest of the code is too rigid.
#---But, it was a fun exercise, and gives this some extra "functionality"

def nth(number: int, suffixes = dict({"1":"st", "2":"nd", "3":"rd", "other":"th"})) -> str:
	num = str(number)

	if len(num) >= 2 and num[-2] == "1":
			return f"{number}{suffixes['other']}"
	if num[-1] in "123":
		return f"{number}{suffixes[num[-1]]}"
	return f"{number}{suffixes['other']}"

#Note to self: consider seperating the "suffixes" list so you can adjust the suffixes used.
#Potentially use DuckTyping to assign the suffix list as a default.

#May be difficult due to the nature of handling numbers like this.
#Also, see if there's a saner way to deal with the "th"s.
#Future note- not necessarily "Saner", but definitely more interactible than previously"


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

#Check Nendrteens too
assert nth(111) == "111th"
assert nth(112) == "112th"
assert nth(113) == "113th"

#test for alternate suffixes-
# Kinda pointless, as the whole construct is rigid to english numbering rules
# but what the heck, it keeps my skills sharp and provides optional extra use cases.
# More points of failure, but also groundwork for the future.

testDict = {"1":"nd", "2":"rd", "3":"iv", "other":"id"}

assert nth(23, testDict) == "23iv"
assert nth(34, testDict) == "34id"
assert nth(11, testDict) == "11id"