![img](assets/banner.png)

<img src='assets/htb.png' style='zoom: 80%;' align=left /> <font size='10'><Challenge_Name></font>

1<sup>st</sup> February 2026

Prepared By: `Doston Abdullayev`

Challenge Author(s): `Doston Abdullayev`

Difficulty: <font color='orange'>Very Easy</font>

<br><br>

***NOTE : The headings with `(!)` should be necessarily included in your writeup while the ones with `(*)` are optional and should be included only if there is a need to. Of course, you can modify the content of each section accordingly. We just provide some boilerplate text.***

# Synopsis (!)

- Users should try to find secret message which is hidden in conversation using ASCII basic skills.

## Description (!)

- Scenario: Leader of hackers group sends message to his team members and hid secret message inside it

## Skills Required (!)

- ASCII
- Basic computer input understanding

## Skills Learned (!)

- How ASCII works

# Enumeration (!)

We have only message file and our objective is to find secret message from it which is flag.
Here is the message:
<img width="1722" height="526" alt="image" src="https://github.com/user-attachments/assets/5edfb87f-8e45-4a34-9293-ddaf605de1e8" />

Using tools like file says it is just unicode text, but when we used `strings` tool to message we can see something suspicious:</br>
<img width="802" height="178" alt="image" src="https://github.com/user-attachments/assets/f69eb16d-2277-4124-ac15-3ea2a0d39f10" /></br>

Strings does not show all letters!

## Exploitation (!)

After testing multpile tools we can use single `xxd` command to see what is happening:</br>
<img width="639" height="425" alt="image" src="https://github.com/user-attachments/assets/1c033749-803a-4c05-aefb-fd1a5afeb4ba" />
</br>
We can see writers of letter used cyrillic letters identical to latin to hide secret message</br>
For example above picture syrillic H is `d09d` meanwhile latin H is `480a`:</br>
<img width="502" height="95" alt="image" src="https://github.com/user-attachments/assets/e9037cdb-5ae0-4839-8a9e-b6bd1afe4ecd" /></br>
Point is computer treats cyrilic to latin differently even though it is same for the eyes



### Getting the flag (!)

To find secret message which is flag we need to retrieve each hidden cyrillic letters picking them from left to right. I noticed writer used team member to hide `{` and `}`
</br>
<img width="634" height="603" alt="image" src="https://github.com/user-attachments/assets/362ebc6d-3cac-4521-a67b-d57e9ea00010" />
</br>
Final form of our flag is: HTB{aOycexc}
