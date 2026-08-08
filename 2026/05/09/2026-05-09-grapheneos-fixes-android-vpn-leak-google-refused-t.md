# GrapheneOS fixes Android VPN leak Google refused to patch

- Score: 261 | [HN](https://news.ycombinator.com/item?id=48075144) | Link: https://cyberinsider.com/grapheneos-fixes-android-vpn-leak-google-refused-to-patch/

### TL;DR

GrapheneOS disabled an Android 16 QUIC teardown optimization that let ordinary apps leak a device’s real IP despite Always-On VPN and “Block connections without VPN.” An app with standard network permissions could register an arbitrary UDP payload; when its socket closed, privileged system_server sent that payload over the physical interface outside the tunnel. A researcher demonstrated the bypass on a Pixel 8, but Google classified the report “Won’t Fix” and outside its security bulletin. GrapheneOS shipped its fix within a week; stock users have a temporary ADB flag workaround.

### Comment pulse

- Readers considered Google’s classification indefensible because Android’s lockdown promise is violated by a privileged system process, not a misbehaving VPN app.
- Discussion questioned whether mobile “always-on VPN” covers privileged operating-system traffic; iOS and macOS were cited as having similar exceptions.
- Some alleged business incentives favor snooping — counterpoint: others emphasized GrapheneOS may coordinate disclosure to preserve its dependency on Google.

### LLM perspective

- Enforce lockdown semantics below privileged application services, with narrowly audited exceptions.
- Security tests need adversarial coverage of new system-to-network paths, especially callbacks carrying caller-controlled bytes.
- Product labels should distinguish “application traffic tunneled” from “all device traffic tunneled” when architectures cannot guarantee the latter.
