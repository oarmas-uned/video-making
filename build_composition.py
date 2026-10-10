import json
import os

cards_data = [
    {
        "id": "card-01",
        "intent": "Three days ago, ChatGPT stopped just answering questions.",
        "startSec": 0.0,
        "endSec": 7.6,
        "accentIndex": 0,
        "zone": "lower-third",
        "kicker": "THE SHIFT",
        "title": "BUILDING<br/>THINGS.",
        "detail": "Three days ago, ChatGPT stopped just answering questions. It started building things."
    },
    {
        "id": "card-02",
        "intent": "Ask for an app, and it appears.",
        "startSec": 7.6,
        "endSec": 14.7,
        "accentIndex": 1,
        "zone": "lower-third",
        "kicker": "ON DEMAND",
        "title": "LIVE<br/>TOOLING.",
        "detail": "Ask for a budget tracker. It builds the tool <span class='pink'>live</span>, right in front of you."
    },
    {
        "id": "card-03",
        "intent": "Intelligent UI",
        "startSec": 14.7,
        "endSec": 21.8,
        "accentIndex": 2,
        "zone": "lower-third",
        "kicker": "INTELLIGENT UI",
        "title": "1 BILLION<br/>USERS.",
        "detail": "Arrived with GPT-4v on Oct 7th. Over 1 billion people use it every week."
    },
    {
        "id": "card-04",
        "intent": "No more app stores.",
        "startSec": 21.8,
        "endSec": 27.6,
        "accentIndex": 3,
        "zone": "lower-third",
        "kicker": "APP STORES",
        "title": "NO MORE<br/>APPS?",
        "detail": "That's a billion people who may <span class='pink'>never open an app store</span> again."
    },
    {
        "id": "card-05",
        "intent": "The prompt is the product.",
        "startSec": 27.6,
        "endSec": 34.3,
        "accentIndex": 4,
        "zone": "lower-third",
        "kicker": "FUTURE",
        "title": "THE<br/>PROMPT.",
        "detail": "When software can be built on demand, the real product becomes the prompt."
    }
]

storyboard = {
    "schemaVersion": 3,
    "composition": {
        "fps": 30,
        "width": 1080,
        "height": 1920,
        "durationSeconds": 34.379,
        "layout": "portrait",
        "themeId": "noir",
        "seed": 42
    },
    "videoTrack": {
        "sourcePath": "input-video.mp4",
        "startSec": 0,
        "endSec": 34.379,
        "bounds": { "x": 0, "y": 0, "width": 1080, "height": 1920 }
    },
    "subtitles": { "enabled": False },
    "cards": [
        {
            "id": c["id"],
            "intent": c["intent"],
            "startSec": c["startSec"],
            "endSec": c["endSec"],
            "accentIndex": c["accentIndex"],
            "zone": c["zone"],
            "contentHints": {
                "kicker": c["kicker"],
                "title": c["title"],
                "detail": c["detail"]
            }
        } for c in cards_data
    ]
}

os.makedirs("videos/my-reel/public/cards", exist_ok=True)
with open("videos/my-reel/storyboard.json", "w") as f:
    json.dump(storyboard, f, indent=2)

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
      top: 600px;
      height: 4px;
      width: 600px;
      background: var(--accent3);
      transform: rotate(-6deg);
    }}
    .card[data-card-id="{c['id']}"] .content {{
      position: absolute;
      left: 36px;
      top: 80px;
      right: 36px;
      bottom: 80px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 36px;
    }}
    .card[data-card-id="{c['id']}"] .kicker {{
      align-self: flex-start;
      padding: 10px 18px;
      background: var(--ink);
      color: var(--bg);
      font: 800 24px/1 var(--font-mono);
      letter-spacing: 0.24em;
    }}
    .card[data-card-id="{c['id']}"] .title {{
      margin: 0;
      font: 900 132px/0.92 var(--font-sans);
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
      font: 600 36px/1.4 var(--font-sans);
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
      data-anim="slide-in"
      data-anim-at="0.1"
      data-anim-duration="0.45"
      data-anim-from="left"
      data-anim-distance="540"
    ></span>
    <span
      class="slab-2"
      id="{c['id']}-slab2"
      data-anim="slide-in"
      data-anim-at="0.25"
      data-anim-duration="0.45"
      data-anim-from="right"
      data-anim-distance="360"
    ></span>
    <span
      class="stripe"
      id="{c['id']}-stripe"
      data-anim="grow-x"
      data-anim-at="0.5"
      data-anim-duration="0.5"
      data-anim-target-w="600"
    ></span>

    <div class="content">
      <span class="kicker" id="{c['id']}-kicker" data-anim="fade-in" data-anim-at="0.05" data-anim-duration="0.4">{c['kicker']}</span>

      <h1 class="title" id="{c['id']}-title" data-anim="fade-in" data-anim-at="0.55" data-anim-duration="0.5">
        {c['title']}
      </h1>

      <p class="detail" id="{c['id']}-detail" data-anim="fade-in" data-anim-at="0.95" data-anim-duration="0.4">
        {c['detail']}
      </p>
    </div>
  </div>
</div>
"""

for c in cards_data:
    with open(f"videos/my-reel/public/cards/{c['id']}.html", "w") as f:
        f.write(gen_card_html(c))

# Generate index.html
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
        left: 0; top: 0; width: 1080px; height: 1920px;
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
    
    # top 44% = 844. Bottom = 1920-844 = 1076. Stack layout. card bottom 56% (approx height 1076)
    # the stack.html says "top 844" for video, so card should be below it. 
    # Let's say top: 844, height: 1076.
    index_html += f"""
      <div
        class="card-host clip"
        data-card-id="{c['id']}"
        data-start="{c['startSec']:.4f}"
        data-duration="{(c['endSec'] - c['startSec']):.4f}"
        data-track-index="2"
        style="left:0;top:844px;width:1080px;height:1076px;visibility:hidden;opacity:0;"
      >
{card_content}
      </div>
"""

index_html += """
      <script src="vendor/gsap.min.js"></script>
      <script>
        (function () {
          const tl = window.gsap.timeline({ paused: true });

          // initial video bounds for stack layout
          tl.set("#video-wrap", { left: 0, top: 0, width: 1080, height: 844 }, 0);

"""

for c in cards_data:
    dur = c['endSec'] - c['startSec']
    s = c['startSec']
    e = c['endSec']
    
    # fade in
    index_html += f"""
          tl.set('.card-host[data-card-id="{c['id']}"]', {{ visibility: "visible" }}, {s:.4f});
          tl.fromTo('.card-host[data-card-id="{c['id']}"]',
            {{ opacity: 0 }},
            {{ opacity: 1, duration: 0.4, ease: "power2.out" }},
            {s:.4f}
          );
          
          tl.fromTo('.card[data-card-id="{c['id']}"] #{c['id']}-slab1', {{ opacity: 0, x: -540 }}, {{ opacity: 1, x: 0, duration: 0.45, ease: 'power2.out' }}, {(s+0.1):.4f});
          tl.fromTo('.card[data-card-id="{c['id']}"] #{c['id']}-slab2', {{ opacity: 0, x: 360 }}, {{ opacity: 1, x: 0, duration: 0.45, ease: 'power2.out' }}, {(s+0.25):.4f});
          tl.fromTo('.card[data-card-id="{c['id']}"] #{c['id']}-stripe', {{ width: 0 }}, {{ width: 600, duration: 0.5, ease: 'power2.out' }}, {(s+0.5):.4f});
          
          tl.fromTo('.card[data-card-id="{c['id']}"] #{c['id']}-kicker', {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4, ease: 'power2.out' }}, {(s+0.05):.4f});
          tl.fromTo('.card[data-card-id="{c['id']}"] #{c['id']}-title', {{ opacity: 0 }}, {{ opacity: 1, duration: 0.5, ease: 'power2.out' }}, {(s+0.55):.4f});
          tl.fromTo('.card[data-card-id="{c['id']}"] #{c['id']}-detail', {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4, ease: 'power2.out' }}, {(s+0.95):.4f});

          tl.to('.card-host[data-card-id="{c['id']}"]',
            {{ opacity: 0, duration: 0.35, ease: "power2.in" }},
            {(e-0.35):.4f}
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

print("Done generating files!")
