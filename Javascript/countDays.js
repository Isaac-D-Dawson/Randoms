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
//V1.4:
//-Corrected underlying logic issue with Leap Years.
//-Noted small discrepancy with parseInt- purely commentary, no actual change.

let daysInMonths = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
let totalDays   = 0;
let dayOfMonth  = prompt("Enter day of month");
let monthOfYear = prompt("Enter month number");
let year        = prompt("Enter Year");

totalDays = daysInMonths[monthOfYear -1];

//Added a month check to confirm we're only adding leap days AFTER Febuary, and not always.
if ( monthOfYear > 2 && (year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0))) {
    totalDays = totalDays + 1;
};

totalDays = totalDays + parseInt(dayOfMonth);   //Wait, shouldn't this be different?
//totalDays = totalDays + Number.parseInt(dayOfMonth, 10)
//You could probably also use this to handle the concept of months to years in some kind of duodecimal system

alert(`${totalDays} days have passed since your date in ${year}`);