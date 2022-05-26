//countDays.js
//CHANGELOG
//V1.0:
//-Original Program structure and logic by Sharky Cuddle- program unchanged except for stylistic choices
//V1.1:
//-Corrected obvious mistakes so that program will actually run. Changes documented below.
//-V1.2: Optimised program logic in an attempt to improve runtime.

let daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
let totalDays   = 0;
let dayOfMonth  = prompt("Enter day of month");
let monthOfYear = prompt("Enter month number");
let year        = prompt("Enter Year");

//Replaced for-loop with a reduce call on a list slice.
totalDays = daysInMonth.slice(0, monthOfYear-1).reduce(function(current, total){
    total = total + current
    return total
}, 0)

//Moved update and alert to end of program to ensure accurate final output

//Streamlined isLeapYear function considerably
function isLeapYear(targetYear) {
    return ( targetYear % 400 === 0 || (targetYear % 4 === 0 && targetYear % 100 !== 0) );
};

//Trimmed excess "is true"
if (isLeapYear(year)){
    totalDays = totalDays + 1;
};

totalDays = totalDays + parseInt(dayOfMonth);
//Updated Alert to use a `format string`
alert(`${totalDays} days have passed this year`);