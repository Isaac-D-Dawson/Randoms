//countDays.js
//CHANGELOG
//V1.0:
//-Original Program structure and logic by Sharky Cuddle- program unchanged except for stylistic choices
//V1.1:
//-Corrected obvious mistakes so that program will actually run. Changes documented below.

let daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
let totalDays   = 0;
let dayOfMonth  = prompt("Enter day of month");
let monthOfYear = prompt("Enter month number");
let year        = prompt("Enter Year");

for (let i = 0; i < monthOfYear-1; i++) {
    totalDays = totalDays + daysInMonth[i];
}

totalDays = totalDays + parseInt(dayOfMonth);

alert(totalDays + " days have passed this year");

function isLeapYear(targetYear) {
    if (targetYear % 400 === 0) {return true};
    if (targetYear % 100 === 0) {return false};
    return targetYear % 4 === 0;
};

if (isLeapYear(year) === true){
    totalDays = totalDays + 1;
};