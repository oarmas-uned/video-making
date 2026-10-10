import json
import os

cards_data = [
    {
        "id": "card-01",
        "intent": "Three days ago",
        "startSec": 0.0,
        "endSec": 1.0,
        "accentIndex": 0,
        "kicker": "11 PM",
        "title": "THREE DAYS AGO.",
        "detail": ""
    },
    {
        "id": "card-02",
        "intent": "ChatGPT stopped answering",
        "startSec": 1.0,
        "endSec": 3.7,
        "accentIndex": 1,
        "kicker": "THE SHIFT",
        "title": "NO MORE<br/>ANSWERS.",
        "detail": "ChatGPT stopped just answering questions."
    },
    {
        "id": "card-03",
        "intent": "started building",
        "startSec": 3.7,
        "endSec": 5.4,
        "accentIndex": 2,
        "kicker": "NEW ERA",
        "title": "BUILDING<br/>THINGS.",
        "detail": "It started building things."
    },
    {
        "id": "card-04",
        "intent": "Ask for an app",
        "startSec": 5.4,
        "endSec": 7.6,
        "accentIndex": 0,
        "kicker": "MAGIC",
        "title": "APP<br/>APPEARS.",
        "detail": "Ask for an app, and it appears."
    },
    {
        "id": "card-05",
        "intent": "budget tracker",
        "startSec": 7.6,
        "endSec": 9.2,
        "accentIndex": 1,
        "kicker": "EXAMPLE",
        "title": "BUDGET<br/>TRACKER.",
        "detail": "Ask for a budget tracker."
    },
    {
        "id": "card-06",
        "intent": "live tool",
        "startSec": 9.2,
        "endSec": 13.0,
        "accentIndex": 2,
        "kicker": "ON DEMAND",
        "title": "LIVE<br/>TOOLING.",
        "detail": "It won't explain how to build one. It builds the tool <span class='pink'>live</span>."
    },
    {
        "id": "card-07",
        "intent": "in front of you",
        "startSec": 13.0,
        "endSec": 14.7,
        "accentIndex": 0,
        "kicker": "REAL TIME",
        "title": "RIGHT IN<br/>FRONT OF YOU.",
        "detail": ""
    },
    {
        "id": "card-08",
        "intent": "Intelligent UI",
        "startSec": 14.7,
        "endSec": 16.8,
        "accentIndex": 1,
        "kicker": "OPENAI",
        "title": "INTELLIGENT<br/>UI.",
        "detail": "OpenAI calls it Intelligent UI."
    },
    {
        "id": "card-09",
        "intent": "GPT-4v",
        "startSec": 16.8,
        "endSec": 19.0,
        "accentIndex": 2,
        "kicker": "RELEASE",
        "title": "OCTOBER<br/>7TH.",
        "detail": "It arrived with GPT-4v on October 7th."
    },
    {
        "id": "card-10",
        "intent": "1 billion",
        "startSec": 19.0,
        "endSec": 21.8,
        "accentIndex": 0,
        "kicker": "SCALE",
        "title": "1 BILLION<br/>USERS.",
        "detail": "Over 1 billion people use chat GPT every week."
    },
    {
        "id": "card-11",
        "intent": "never open app store",
        "startSec": 21.8,
        "endSec": 24.9,
        "accentIndex": 1,
        "kicker": "APP STORES",
        "title": "NO MORE<br/>APP STORE.",
        "detail": "That's a billion people who may never open an app store again."
    },
    {
        "id": "card-12",
        "intent": "what happens",
        "startSec": 24.9,
        "endSec": 27.5,
        "accentIndex": 2,
        "kicker": "QUESTION",
        "title": "APPS YOU<br/>PAY FOR?",
        "detail": "So what happens to every app you pay for?"
    },
    {
        "id": "card-13",
        "intent": "on demand",
        "startSec": 27.5,
        "endSec": 29.8,
        "accentIndex": 0,
        "kicker": "FUTURE",
        "title": "SOFTWARE ON<br/>DEMAND.",
        "detail": "Because when software can be built on demand,"
    },
    {
        "id": "card-14",
        "intent": "prompt product",
        "startSec": 29.8,
        "endSec": 31.8,
        "accentIndex": 1,
        "kicker": "REALITY",
        "title": "THE PROMPT IS<br/>THE PRODUCT.",
        "detail": "the real product becomes the prompt."
    },
    {
        "id": "card-15",
        "intent": "outro",
        "startSec": 31.8,
        "endSec": 34.379,
        "accentIndex": 2,
        "kicker": "SUBSCRIBE",
        "title": "FOLLOW FOR<br/>MORE.",
        "detail": "Follow for the text stories, nobody explains."
    }
]

os.makedirs("videos/my-reel/public/cards", exist_ok=True)

def gen_card_html(c):
    return f"""<div class="card" data-card-id="{c['id']}">
  <style>
    .card[data-card-id="{c['id']}"] .root {{
      --bg: #0a0c12;
      --ink: #ffffff;
      --muted: #aaaaaa;
      --accent: #d4ff00;
      --accent2: #ff2e88;
      --accent3: #ffffff;
      --font-sans: "Inter", ui-sans-serif, system-ui, sans-serif;
      --font-mono: ui-monospace, "SF Mono", Menlo, monospace;

      width: 100%;
      height: 100%;
      position: relative;
      overflow: hidden;
      background: var(--bg);
      color: var(--ink);
      font-family: var(--font-sans);
    }}
    .card[data-card-id="{c['id']}"] .slab-1 {{
      position: absolute;
      left: 0;
      top: 0;
      width: 540px;
      height: 200px;
      background: var(--accent);
    }}
    .card[data-card-id="{c['id']}"] .slab-2 {{
      position: absolute;
      right: 0;
      bottom: 0;
      width: 360px;
      height: 360px;
      background: var(--accent2);
    }}
    .card[data-card-id="{c['id']}"] .stripe {{
      position: absolute;
      left: -40px;
      top: 500px;
      height: 4px;
      width: 800px;
      background: var(--accent3);
      transform: rotate(-6deg);
    }}
    .card[data-card-id="{c['id']}"] .content {{
      position: absolute;
      left: 36px;
      top: 60px;
      right: 36px;
      bottom: 60px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 20px;
    }}
    .card[data-card-id="{c['id']}"] .kicker {{
      align-self: flex-start;
      padding: 10px 18px;
      background: var(--ink);
      color: var(--bg);
      font: 800 28px/1 var(--font-mono);
      letter-spacing: 0.24em;
    }}
    .card[data-card-id="{c['id']}"] .title {{
      margin: 0;
      font: 900 110px/0.95 var(--font-sans);
      color: var(--ink);
      letter-spacing: -0.04em;
      text-transform: uppercase;
    }}
    .card[data-card-id="{c['id']}"] .stroke {{
      -webkit-text-stroke: 4px var(--accent);
      color: transparent;
    }}
    .card[data-card-id="{c['id']}"] .detail {{
      margin: 0;
      font: 600 42px/1.4 var(--font-sans);
      color: var(--muted);
      max-width: 90%;
    }}
    .card[data-card-id="{c['id']}"] .detail .pink {{
      color: var(--accent2);
    }}
  </style>

  <div class="root">
    <span
      class="slab-1"
      id="{c['id']}-slab1"
    ></span>
    <span
      class="slab-2"
      id="{c['id']}-slab2"
    ></span>
    <span
      class="stripe"
      id="{c['id']}-stripe"
    ></span>

    <div class="content">
      <span class="kicker" id="{c['id']}-kicker">{c['kicker']}</span>
      <h1 class="title" id="{c['id']}-title">{c['title']}</h1>
      <p class="detail" id="{c['id']}-detail">{c['detail']}</p>
    </div>
  </div>
</div>
"""

for c in cards_data:
    with open(f"videos/my-reel/public/cards/{c['id']}.html", "w") as f:
        f.write(gen_card_html(c))

# Generate index.html
# We invert the stack layout.
# Total height 1920.
# Card on top (e.g. height 1076, top 0)
# Video on bottom (e.g. height 844, top 1076)
index_html = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <style>
      @font-face {{
        font-family: "Inter";
        src: url("fonts/Inter-400-latin.woff2") format("woff2");
        font-weight: 400;
        font-display: block;
      }}
      @font-face {{
        font-family: "Inter";
        src: url("fonts/Inter-700-latin.woff2") format("woff2");
        font-weight: 700;
        font-display: block;
      }}
      :root {{
        --bg: #0a0c12;
        --text: #ffffff;
      }}
      * {{ box-sizing: border-box; }}
      html, body {{
        margin: 0; padding: 0; width: 100%; height: 100%;
        overflow: hidden; background: #0a0c12;
        font-family: "Inter", ui-sans-serif, system-ui, sans-serif;
      }}
      #stage {{
        position: relative; width: 100%; height: 100%; overflow: hidden;
      }}
      .video-wrapper {{
        position: absolute;
        left: 0; top: 1076px; width: 1080px; height: 844px;
        overflow: hidden; border-radius: 0; box-shadow: none;
      }}
      .video-wrapper video {{
        width: 100%; height: 100%; object-fit: cover;
      }}
      .card-host {{
        position: absolute; pointer-events: none; overflow: hidden;
      }}
      .card-host .card {{
        position: relative; width: 100%; height: 100%; overflow: hidden;
      }}
    </style>
  </head>
  <body>
    <div
      id="stage"
      data-composition-id="talking-head-recut"
      data-start="0"
      data-duration="34.379"
      data-fps="30"
      data-width="1080"
      data-height="1920"
    >
      <div class="video-wrapper" id="video-wrap">
        <video
          id="bg-video"
          src="input-video.mp4"
          playsinline
          data-has-audio="true"
          data-start="0"
          data-duration="34.379"
          data-track-index="1"
        ></video>
      </div>

"""

for c in cards_data:
    with open(f"videos/my-reel/public/cards/{c['id']}.html", "r") as f:
        card_content = f.read()
    
    # Card is on top: top 0, height 1076
    index_html += f"""
      <div
        class="card-host clip"
        data-card-id="{c['id']}"
        data-start="{c['startSec']:.4f}"
        data-duration="{(c['endSec'] - c['startSec']):.4f}"
        data-track-index="2"
        style="left:0;top:0;width:1080px;height:1076px;visibility:hidden;opacity:0;"
      >
{card_content}
      </div>
"""

index_html += """
      <script src="vendor/gsap.min.js"></script>
      <script>
        (function () {
          const tl = window.gsap.timeline({ paused: true });

          // initial video bounds for inverted stack layout (video on bottom)
          tl.set("#video-wrap", { left: 0, top: 1076, width: 1080, height: 844 }, 0);

"""

for c in cards_data:
    dur = c['endSec'] - c['startSec']
    s = c['startSec']
    e = c['endSec']
    
    # Fast punchy animations
    index_html += f"""
          tl.set('.card-host[data-card-id="{c['id']}"]', {{ visibility: "visible" }}, {s:.4f});
          // snap opacity instantly for faster cuts
          tl.set('.card-host[data-card-id="{c['id']}"]', {{ opacity: 1 }}, {s:.4f});
          
          tl.fromTo('.card[data-card-id="{c['id']}"] #{c['id']}-slab1', {{ opacity: 0, x: -540 }}, {{ opacity: 1, x: 0, duration: 0.25, ease: 'power2.out' }}, {s:.4f});
          tl.fromTo('.card[data-card-id="{c['id']}"] #{c['id']}-slab2', {{ opacity: 0, x: 360 }}, {{ opacity: 1, x: 0, duration: 0.25, ease: 'power2.out' }}, {s:.4f});
          tl.fromTo('.card[data-card-id="{c['id']}"] #{c['id']}-stripe', {{ width: 0 }}, {{ width: 800, duration: 0.3, ease: 'power2.out' }}, {(s+0.1):.4f});
          
          tl.fromTo('.card[data-card-id="{c['id']}"] #{c['id']}-kicker', {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.25, ease: 'back.out(1.5)' }}, {(s+0.1):.4f});
          // scale pop for title to make it aggressive
          tl.fromTo('.card[data-card-id="{c['id']}"] #{c['id']}-title', {{ opacity: 0, scale: 0.6 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: 'back.out(1.6)' }}, {(s+0.15):.4f});
          tl.fromTo('.card[data-card-id="{c['id']}"] #{c['id']}-detail', {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: 'power2.out' }}, {(s+0.25):.4f});

          // fast exit
          tl.to('.card-host[data-card-id="{c['id']}"]',
            {{ opacity: 0, duration: 0.15, ease: "power2.in" }},
            {(e-0.15):.4f}
          );
          tl.set('.card-host[data-card-id="{c['id']}"]', {{ visibility: "hidden" }}, {e:.4f});
"""

index_html += """
          window.__timelines = window.__timelines || {};
          window.__timelines["talking-head-recut"] = tl;
        })();
      </script>
    </div>
  </body>
</html>
"""

with open("videos/my-reel/public/index.html", "w") as f:
    f.write(index_html)

print("Done generating updated fast-paced inverted files!")
