//countDays.js
//CHANGELOG
//V1.0:
//-Original Program structure and logic by Sharky Cuddle- program unchanged except for stylistic choices
//V1.1:
//-Corrected obvious mistakes so that program will actually run. Changes documented below.
//-V1.2: 
//-Optimised program logic in an attempt to improve runtime.
//V1.3:
//-Corrected minor changelog format error for V1.2
//-Replaced uneeded function with a direct if-statement
//-Removed reduce function by pre-processing the result set it created
//-retyped output string for clarity

//Replaced daysInMonth with daysInMonths
let daysInMonths = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
let totalDays   = 0;
let dayOfMonth  = prompt("Enter day of month");
let monthOfYear = prompt("Enter month number");
let year        = prompt("Enter Year");

//Further replaced Reduce function(Formerly for-loop) by replacing the daysInMonth list with a
// preprocessed "daysInMonths" list to ensure accurate final output
//We now assign this pre-processed value directly to the totalDays var,
totalDays = daysInMonths[monthOfYear -1];


//Removed unneeded isLeapYear function- moved internal if statement directly into relevant conditional
if (year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0)) {
    totalDays = totalDays + 1;
};

totalDays = totalDays + parseInt(dayOfMonth);
//Updated Alert to use a, slightly clearer, `format string`
alert(`${totalDays} days have passed since your date in ${year}`);