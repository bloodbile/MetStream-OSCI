# 🎀 MetStream OSCI 🎀
## Overview
A critical vulnerability has been found in all versions of Gill Instruments' MetStream. The application is vulnerable to OS command injection attacks via the zone parameter. This vulnerability allows an attacker to inject arbitrary OS commands that can be executed by the application's back-end service. A payload including the pipe character (|) was submitted through the zone parameter, which included a command designed to echo a specific string. The application's response confirmed the command's execution by returning the output.
## Impact
Operating system command injection vulnerabilities allow attackers to manipulate server commands, potentially leading to unauthorized access to sensitive data or server-level control. If exploited, this could result in a complete compromise of the server hosting the application, enabling attackers to launch further attacks on other systems or networks within its reach.
