# SchedulePortal  
Version: 0.1.0

*(c) 2021 Garret Burkhardt, All rights reserved*

---

## Purpose

### Problem Being Solved
When I developed Schedule Portal, I was working for Publix. Their schedule would come out every wednesday and each schedule would be vastly different from the week prior. This meant that I had to check my work schedule at minimum once a week, but every day if I wanted to feel confident about my daily plans.

My schedule is burried deep under a lot of clicks as well as a login that I need to get right otherwise I'd have to make a call to corporate using a store phone sat next to HR. Long story short, if I messed up, it'd be an absolute headache.

Now, I _REALLY_ value my time, and this whole process took me 4 minutes to navigate. Thats enough time for a chaotic mind to lose focus on a login and find something else -- and often I did.

So how did SchedulePortal Solve this?

### Solution
- Schedule Portal pre-defines a direct link to where my schedule is hidden, the HTML form element IDs, and credentials for when the website asks for them.
- Using the Chrome Driver API by selenium Schedule Portal is able to navigate the website using the information it's provided!
- _Minor Problem_: The publix schedule site doesnt plainly offer schedule info in html elements, it references other links, so skimming is out of play.
    - A Screenshot will solve this! _Plus it looks better than a spreadsheet._
- Once again, using the ChromeDriver API, Schedule Portal waits a bit of time to allow for the unfortunately slow page load time, and then snags a screenshot.
- The screenshot is saved in a local resources folder within the program directory. It could've been saved anywhere, but I don't like the idea of programs leaving stray files all around the user's computer. Plus it makes clean up easier when you remove the program completely!
- _Minor Problem_: If Schedule Portal simply saved the photo in the directory, I would need to remember to check it and I also wouldnt know when the file would be there, so I'd forget.
    - Notifications!!! Schedule portal pulls from the Plyer API to trigger system notifications that let me know when and where the photo is.

Schedule Portal takes a 4 minute process and reduces it to 9s! I timed it.  

__THAT'S A 2567% RETURN ON MY TIME!__ 

---

## How This Demo Works

I cannot legally give you access to my work credentials, plus its for my own privacy.  
However, to demonstrate the process of Schedule Protal, I have entered false credentials that wont log in, but it will allow Schedule Portal to continue through it's entire process!

Your result will be a screenshot of the Publix Login it a Login Error - That's is to be expected!

---

## Usage
***USE AT YOUR OWN RISK***  
**SchedulePortal is for demonstrational purposes by the author only.** SchedulePortal is not to be shared or sold by any means by anyone other than the author. Any Commercial use of SchedulePortal is strictly prohibited.  

If you are given access to this project and/or its' sourcecode,  
**YOU ASSUME ALL POSSIBLE LIABILITIES IF YOU USE IT**.\*

> *\* This code is experimental and may pose a threat to the sensitive information that you feed to it. SchedulePortal, itself, is not maliciously designed. However, consider yourself sufficiently warned should anything happen.*

---

## Sourcecode Info
**File:** "SchedulePortal.py" *(Main Source File)*

**Dependencies:**
|Library | Version | Purpose|
| :--- | :---: | :--- |
|Selenium | 3.141.0 | Controls the Webdriver |
|Plyer | 2.0.0 | Triggers Notifications |

---

Document History:  
06-JAN-2021 - <burkhardtgarret710@gmail.com> - Created README
