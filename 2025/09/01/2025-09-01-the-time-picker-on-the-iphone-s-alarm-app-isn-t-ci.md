# The time picker on the iPhone's alarm app isn't circular, it's just a long list

- Score: 270 | [HN](https://news.ycombinator.com/item?id=45093765) | Link: https://old.reddit.com/r/interestingasfuck/comments/1n5lztw/the_time_picker_on_the_iphones_alarm_app_isnt/

- TL;DR
An HN post notes the iPhone Clock app’s “spinning” time picker isn’t circular; it’s a very long, repeating UIPickerView list. Users report real-world bugs: AM/PM not registering until momentum stops, overshooting minutes, and accidental changes during animations. Many prefer direct entry via keypad or 24‑hour time, and praise Android’s confirmation (“goes off in X hours”) and older Nokia/Palm designs. Developers explain the looping trick and suggest snap‑back fixes. With iOS 26’s AlarmKit, third‑party alarm apps may finally address these gaps; Sleep schedule already covers “skip next” cases.
  
  Content unavailable; summarizing from title/comments.

- Comment pulse
  - Momentum wheel causes mis-selections → AM/PM doesn't “stick” until scrolling stops; overshoot common; keypad or 24‑hour time reduces errors.
  - Better patterns exist → Android shows “goes off in X hours,” offers circular picker; Nokia N9/PalmOS used sliders/tap-to-increment for predictable input.
  - Implementation is a long repeating list → UIPickerView fakes infinity; snapping midlist suggested—counterpoint: Sleep schedule already supports skip-next, mitigating missed alarms.

- LLM perspective
  - View: Focus on deterministic input; momentum-based wheels are error-prone under time pressure.
  - Impact: AlarmKit could shift innovation to third-party apps; Apple may deprecate the wheel or default to keypad.
  - Watch next: iOS 26 APIs, human interface updates, and usability studies measuring setup speed/errors across keypad, sliders, and looping pickers.
