# Security researcher says Microsoft built a Bitlocker backdoor, releases exploit

- Score: 544 | [HN](https://news.ycombinator.com/item?id=48168856) | Link: https://www.techspot.com/news/112410-security-researcher-microsoft-secretly-built-backdoor-bitlocker-releases.html

- TL;DR  
    - A security researcher, Nightmare‑Eclipse, released “YellowKey,” a technique that uses a crafted FsTx folder on a USB stick (or EFI partition) plus Windows Recovery Environment to obtain a command shell that fully bypasses BitLocker disk encryption on Windows 11 and Server 2022/2025 systems, without the password. Because the vulnerable component exists only in live WinRE images and behaves differently in installation media, the researcher argues it’s an intentional Microsoft backdoor. Others have reproduced the behavior, raising major trust and mitigation questions around BitLocker.

- LLM perspective  
    - View: This looks like an egregious design flaw with highly suspicious characteristics, but “backdoor” remains an allegation until Microsoft’s technical explanation.  
    - Impact: Enterprises, governments, and regulated sectors depending on BitLocker for data‑at‑rest security may need compensating controls or alternative FDE solutions.  
    - Watch next: Microsoft advisory, scope confirmation, WinRE patches, and whether independent cryptographers get to review BitLocker/WinRE components more transparently.
