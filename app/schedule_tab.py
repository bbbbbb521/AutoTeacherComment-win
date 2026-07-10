
import customtkinter as ctk

class ScheduleTab:
    def __init__(self, parent):
        self.parent = parent
        self._build_ui()

    def _build_ui(self):
        main = ctk.CTkScrollableFrame(self.parent, fg_color="transparent")
        main.pack(fill="both", expand=True, padx=20, pady=16)

        # Header
        header = ctk.CTkFrame(main, fg_color="white", corner_radius=12)
        header.pack(fill="x", pady=(0, 16))

        ctk.CTkLabel(header, text="\u8bfe\u7a0b\u8868", font=ctk.CTkFont(size=18, weight="bold"), text_color="#333").pack(anchor="w", padx=20, pady=(16, 4))
        ctk.CTkLabel(header, text="\u8bfe\u7a0b\u8868\u529f\u80fd\u5c06\u5728\u540e\u7eed\u7248\u672c\u4e2d\u5b8c\u5584", font=ctk.CTkFont(size=13), text_color="#999").pack(anchor="w", padx=20, pady=(4, 16))

        # Placeholder info
        info_card = ctk.CTkFrame(main, fg_color="white", corner_radius=12)
        info_card.pack(fill="x", pady=(0, 16))

        ctk.CTkLabel(info_card, text="\u529f\u80fd\u8bf4\u660e", font=ctk.CTkFont(size=16, weight="bold"), text_color="#333").pack(anchor="w", padx=20, pady=(16, 8))

        features = [
            "\u2022 \u5728\u7ebf\u5bfc\u5165: \u767b\u5f55\u6559\u52a1\u7cfb\u7edf\u6293\u53d6\u8bfe\u8868",
            "\u2022 \u56fe\u7247\u5bfc\u5165: \u622a\u5c4f/OCR\u8bc6\u522b\u8bfe\u8868",
            "\u2022 \u6587\u4ef6\u5bfc\u5165: \u652f\u6301 Excel/CSV \u683c\u5f0f",
            "\u2022 \u7f8e\u5316\u8bbe\u7f6e: \u81ea\u5b9a\u4e49\u989c\u8272\u3001\u900f\u660e\u5ea6",
            "\u2022 \u5206\u4eab: \u5bfc\u51fa/\u5206\u4eab\u8bfe\u8868",
        ]
        for f in features:
            ctk.CTkLabel(info_card, text=f, font=ctk.CTkFont(size=13), text_color="#555", anchor="w").pack(anchor="w", padx=20, pady=2)

        ctk.CTkLabel(info_card, text="", font=ctk.CTkFont(size=8)).pack()
        ctk.CTkLabel(info_card, text="\u8bfe\u7a0b\u8868\u6570\u636e\u4f1a\u672c\u5730\u4fdd\u5b58\uff0c\u91cd\u542f\u5e94\u7528\u4e0d\u4f1a\u4e22\u5931", font=ctk.CTkFont(size=12), text_color="#999").pack(anchor="w", padx=20, pady=(4, 16))

        # Quick guide card
        guide_card = ctk.CTkFrame(main, fg_color="white", corner_radius=12)
        guide_card.pack(fill="x")

        ctk.CTkLabel(guide_card, text="\u5feb\u901f\u6307\u5357", font=ctk.CTkFont(size=16, weight="bold"), text_color="#333").pack(anchor="w", padx=20, pady=(16, 8))

        steps = [
            "1. \u6253\u5f00\u6559\u52a1\u7cfb\u7edf\u8bfe\u8868\u9875\u9762",
            "2. \u70b9\u51fb\u53f3\u4e0a\u89d2\u201c\u6293\u53d6\u201d\u6309\u94ae\u83b7\u53d6\u5f53\u524d\u9875\u9762\u6570\u636e",
            "3. \u7cfb\u7edf\u81ea\u52a8\u89e3\u6790\u5e76\u5c55\u793a\u5728\u7f51\u683c\u4e2d",
            "4. \u53ef\u4ee5\u968f\u65f6\u7f16\u8f91\u3001\u6dfb\u52a0\u6216\u5220\u9664\u8bfe\u7a0b",
            "\u2605 \u6216\u4f7f\u7528\u8bfe\u8868\u622a\u56fe\u8fdb\u884c OCR \u8bc6\u522b\u5bfc\u5165",
        ]
        for s in steps:
            ctk.CTkLabel(guide_card, text=s, font=ctk.CTkFont(size=13), text_color="#555", anchor="w").pack(anchor="w", padx=20, pady=2)
        ctk.CTkLabel(guide_card, text="", font=ctk.CTkFont(size=8)).pack()
