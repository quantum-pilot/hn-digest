# Ubuntu 26.04 Ends 46 Years of Silent sudo Passwords

- Score: 304 | [HN](https://news.ycombinator.com/item?id=47464134) | Link: https://pbxscience.com/ubuntu-26-04-ends-46-years-of-silent-sudo-passwords/

### TL;DR

Ubuntu 26.04 development builds enable sudo-rs password feedback by default, displaying one asterisk per keystroke after 46 years of silent terminal entry. The upstream project argues that exposing password length adds negligible risk compared with the usability benefit, especially because graphical login screens already show placeholders. Critics call the old behavior a shoulder-surfing defense; supporters say blank prompts confuse newcomers and make high-latency SSH input hard to diagnose. Administrators can restore silence immediately by adding `Defaults !pwfeedback` through `visudo`; legacy sudo remains unaffected.

### Comment pulse

- Users reported pasting passwords into visible editors when faulty keyboards made silent entry uncertain, creating greater exposure than feedback would.
- Alternative animations can confirm keystrokes without revealing length — counterpoint: exact length helps users notice wrong passwords or incomplete deletion.
- Similar fixed-width login fields on macOS fail badly when long passwords or slow systems outgrow displayed placeholders.

### LLM perspective

- **View:** This is a defaults dispute, not a removed capability; both threat models remain one configuration line apart.
- **Impact:** Visible feedback may prevent first-time Linux users from mistaking a working prompt for a frozen installer.
- **Watch next:** Final-release behavior, downstream distribution adoption, SSH usability reports, and documented shoulder-surfing incidents.
