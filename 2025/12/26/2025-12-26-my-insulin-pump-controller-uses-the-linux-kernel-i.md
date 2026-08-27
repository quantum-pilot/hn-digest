# My insulin pump controller uses the Linux kernel. It also violates the GPL

- Score: 495 | [HN](https://news.ycombinator.com/item?id=46395184) | Link: https://old.reddit.com/r/linux/comments/1puojsr/the_device_that_controls_my_insulin_pump_uses_the/

### TL;DR

A type 1 diabetic reports that Insulet's OmniPod Dash controller runs Android Marshmallow on Linux 3.18.19, lacks verified boot, and can be reflashed with physical access. After nearly two years, neither Insulet nor hardware supplier Nuu provided the requested corresponding kernel source, despite apparent device-specific modifications and GPLv2 obligations. Discussion separates source disclosure from permission to alter medical software, debates who can enforce compliance, and notes that regulated-device lifecycles may explain old code without excusing licensing failures.

### Comment pulse

- Enforcement is legally unsettled → kernel copyright holders clearly have standing, while an end user's direct contractual rights remain disputed.
- Operational neglect is plausible → outsourced teams, staff churn, and unequipped support channels commonly strand source requests.
- Disclosure is not device control → signed firmware can block modifications while manufacturers still publish GPL-covered source.

### LLM perspective

- View: Safety regulation and copyleft compliance are separate obligations; neither inherently prevents the other.
- Impact: Patients cannot independently audit maintained patches, while kernel contributors lose the reciprocity GPLv2 requires.
- Watch next: A formal legal request should establish the distribution offer, exact modifications, and responsible distributor.
