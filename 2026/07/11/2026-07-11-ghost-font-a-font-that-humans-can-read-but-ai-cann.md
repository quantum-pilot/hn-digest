# Ghost Font: A font that humans can read but AI cannot

- Score: 190 | [HN](https://news.ycombinator.com/item?id=48870381) | Link: https://www.mixfont.com/ghost-font

TL;DR  
Ghost Font encodes text in the subtle motion of random-dot noise over video frames: humans can often read it by tracking motion, while current frame-by-frame AI vision models fail. HN commenters quickly show it’s not fundamentally AI-proof: standard tricks (frame differencing, optical flow, compression-like processing) or GPT-5.6/Fable already decode it. People’s ability to see the text varies widely, with some only seeing the decoy overlay and others only the hidden message, raising usability questions for CAPTCHA-style use.  
*Content unavailable; summarizing from title/comments.*

Comment pulse  
- Novel CAPTCHA angle → Motion-based text defeats naive frame-wise OCR, but temporal aggregation and compression-style analysis can reconstruct characters. — counterpoint: still raises attack cost.  
- Easily breakable algorithmically → Simple frame-shift search, subtraction, then OCR works in ~20 lines when motion is linear.  
- Humans vary a lot → Some find the hidden text unreadable or headache-inducing; others barely see the decoy, complicating universal human-readability claims.

LLM perspective  
- View: This is an obfuscation against current video-processing defaults, not a durable “AI-proof” channel.  
- Impact: Forces model and product designers to handle temporal patterns, not just per-frame classification.  
- Watch next: Benchmarks where video models must decode such motion-encoded text; open-source implementations of both font and breaking algorithms.
