import sys
import os
import webview
import time

def main():
    score = int(sys.argv[1])
    url = sys.argv[2]

    runner_dir = os.path.dirname(os.path.abspath(__file__))
    js_path = os.path.join(runner_dir, 'inject_js.txt')
    with open(js_path, 'r', encoding='utf-8') as f:
        js_template = f.read()

    opt = "\u5b8c\u5168\u540c\u610f"
    if score > 80: opt = "\u5b8c\u5168\u540c\u610f"
    elif score > 60: opt = "\u540c\u610f"
    elif score > 40: opt = "\u4e00\u822c"
    elif score > 20: opt = "\u4e0d\u592a\u540c\u610f"
    else: opt = "\u5b8c\u5168\u4e0d\u540c\u610f"

    js = js_template.replace('SCORE_VAL', str(score)).replace("OPTION_VAL", opt)

    window = webview.create_window(
        "\u6559\u5e08\u8bc4\u4ef7 - \u81ea\u52a8\u586b\u5199\u52a9\u624b",
        url,
        width=1200, height=800, resizable=True
    )

    def inject_loop():
        """Periodically try to inject JS after page loads"""
        time.sleep(3)  # Wait for initial page load
        attempt = 0
        while attempt < 60:  # Try for ~5 minutes
            try:
                result = window.evaluate_js(js)
                if result is not None or attempt > 3:
                    time.sleep(2)
                    # Keep re-injecting for new pages
                    continue
            except Exception:
                pass
            attempt += 1
            time.sleep(3)

    webview.start(gui="edgechromium", func=inject_loop, debug=False)

if __name__ == "__main__":
    main()
