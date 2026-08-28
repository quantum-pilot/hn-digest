# The time picker on the iPhone's alarm app isn't circular, it's just a long list

- Score: 270 | [HN](https://news.ycombinator.com/item?id=45093765) | Link: https://old.reddit.com/r/interestingasfuck/comments/1n5lztw/the_time_picker_on_the_iphones_alarm_app_isnt/

### TL;DR

A Reddit video and commenters demonstrate that the iPhone alarm time picker only appears circular: repeated flicks eventually reach an endpoint, implying a very long sequence of repeated values rather than a truly endless loop. One discussion points to UIPickerView tutorials that fake looping with many rows, though the supplied material does not prove Apple's exact implementation. The practical effect is negligible during normal use, but the discovery prompted broader criticism of the wheel's bounce, AM/PM selection behavior, overshooting, and weaker confirmation compared with alternative clock interfaces.

### Comment pulse

- Multiple users described a consequential bug where AM/PM changes may not stick if Save is tapped before scrolling settles.
- Suggested alternatives included numeric keypads, short minute lists, tap-to-increment digits, and circular clock-face selectors.

### LLM perspective

- View: The finite list is harmless theater; unreliable state commitment is the consequential usability concern.
- Impact: A familiar visual metaphor can conceal edge behavior and make critical alarm mistakes difficult to notice.
- Watch next: AlarmKit alternatives and tests of save-before-settle behavior could separate preference from reproducible defect.
