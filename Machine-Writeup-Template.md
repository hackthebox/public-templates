# [Machine Name]

## Introduction

[Include why you made this box, what skills and vulnerabilities you wanted to highlight, etc]

## Info for HTB

### Access

Passwords:

| User  | Password                            |
| ----- | ----------------------------------- |
| user1 | [pass phrase, not too hard to type] |
| user2 | [pass phrase, not too hard to type] |
| root  | [pass phrase, not too hard to type] |

### Key Processes

[Describe processes that are running to provide basic services on the box, such as web server, FTP, etc. **For any custom binaries, include the source code (in a separate file unless very short)**. Also, include if any of the services or programs are running intentionally vulnerable versions.]

### Automation / Crons

[Describe any automation on the box:

- What does it do?
- Why? (necessary for exploit step, clean up, etc)
- How does it do it? Provide source code (anything longer than a few lines in a separate attachment)
- How does it run?

]

### Firewall Rules

[Describe any non-default firewall rules here]

### Docker

[Describe how docker is used if at all. Attach Dockerfiles]

### Other

[Include any other design decisions you made that the HTB staff should know about]



# Writeup

[

Provide an in-depth explanation of the steps it takes to complete the box from start to finish. Divide your walkthrough into the below sections and sub-sections and include images to guide the user through the exploitation. 

Please also include screenshots of any visual elements (like websites) that are part of the submission. Our review team is not only evaluating the technical path, but the realism and story of the box.

Show **all** specific commands using markdown's triple-backticks (```` ```bash ````) such that the reader can copy/paste them, and also show the commands' output through images or markdown code blocks (```` ``` ````). 

**A reader should be able to solve the box entirely by copying and pasting the commands you provide.**

]

# Enumeration

[Describe the steps that describe the box's enumeration. Typically, this includes a sub-heading for the Nmap scan, HTTP/web enumeration, etc.]

# Foothold

[Describe the steps for obtaining an initial foothold (shell/command execution) on the target.]

# Lateral Movement (optional)

[Describe the steps for lateral movement. This can include Docker breakouts / escape-to-host, etc.]

# Privilege Escalation

[Describe the steps to obtaining root/administrator privileges on the box.]
