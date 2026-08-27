# Hacking Washing Machines [video]

- Score: 204 | [HN](https://news.ycombinator.com/item?id=46428496) | Link: https://media.ccc.de/v/39c3-hacking-washing-machines

### TL;DR

A 56-minute CCC talk examines reverse-engineering household appliances from B/S/H and Miele. The researchers analyze control boards, proprietary internal buses, hidden diagnostic interfaces, firmware protections, and ways to bypass access restrictions, then use the findings for cloud-free integration of legacy machines with home automation. HN discussion added practical color: appliance test engineering can expose rich telemetry and control, Miele’s optical interface provides electrical isolation, and both manufacturers reportedly engaged constructively with the researchers about undisclosed issues.

### Comment pulse

- Appliance engineering is unusually tangible → telemetry, automated controls, destructive tests, and daily cooking connect software directly to physical outcomes.
- Optical diagnostics are pragmatic → infrared serial links avoid conductive ports and isolate service equipment from mains voltage.
- Vendor engagement helped → B/S/H and Miele reportedly checked whether the research exposed previously unknown problems.

### LLM perspective

- View: Local diagnostic buses offer a durable integration layer when cloud services disappear or reject older appliances.
- Impact: Owners and home-automation developers gain control, while manufacturers face pressure to document safe interfaces.
- Watch next: Seek released tooling, protocol documentation, model coverage, disclosure outcomes, and safeguards against remote actuation.
