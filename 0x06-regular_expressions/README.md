# 0x06. Regular expression
This folder contains a collection of Ruby scripts for matching various regular expressions. The matches made by each regular expression are concatenated and printed to the console. Each script accepts only one positional argument representing the string to be matched. 

## 0-simply_match_school.rb
Match the string `School`.

## 1-repetition_token_0.rb, 2-repetition_token_1.rb. 3-repetition_token_2.rb, 4-repetition_token_3.rb
Match a string with repeating tokens.

## 5-beginning_and_end.rb
The regular expression matches a three-character string that starts with `h` ends with `n` and can have any single character in between.

## 6-phone_number.rb
Match a 10-digit phone number. The string should only have digits and should not have spaces.

## 7-OMG_WHY_ARE_YOU_SHOUTING.rb
Match uppercase characters regardless of their position in the string.

## 100-textme.rb
Extract the following information from a line of a log file:
- The sender phone number or name (including country code if present)
- The receiver phone number or name (including country code if present)
- The flags that were used
The script prints: `[SENDER],[RECEIVER],[FLAGS]`

Example:
- input string: `'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'`
- output: `Google,+16474951758,-1:0:-1:0:-1`
