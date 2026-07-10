import customtkinter as ctk
import subprocess
import sys
import os

class HomeTab:
    def __init__(self, parent, config):
        self.parent = parent
        self.config = config
        self.eval_process = None
        self._build_ui()

    def _build_ui(self):
        main = ctk.CTkScrollableFrame(self.parent, fg_color="transparent")
        main.pack(fill="both", expand=True, padx=20, pady=16)

        score_card = ctk.CTkFrame(main, fg_color="white", corner_radius=12)
        score_card.pack(fill="x", pady=(0, 16))
        self._build_score_card(score_card)

        status_card = ctk.CTkFrame(main, fg_color="white", corner_radius=12)
        status_card.pack(fill="x", pady=(0, 16))
        self._build_status_card(status_card)

        action_card = ctk.CTkFrame(main, fg_color="white", corner_radius=12)
        action_card.pack(fill="x", pady=(0, 16))
        self._build_action_card(action_card)

    def _build_score_card(self, parent):
        header = ctk.CTkFrame(parent, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(16, 8))
        ctk.CTkLabel(header, text="评分设置", font=ctk.CTkFont(size=16, weight="bold"), text_color="#333").pack(side="left")

        input_frame = ctk.CTkFrame(parent, fg_color="transparent")
        input_frame.pack(fill="x", padx=20, pady=8)
        ctk.CTkLabel(input_frame, text="评价分数:", font=ctk.CTkFont(size=14), text_color="#555").pack(side="left", padx=(0, 12))
        self.score_var = ctk.StringVar(value="100")
        self.score_entry = ctk.CTkEntry(input_frame, textvariable=self.score_var, width=100, height=35, font=ctk.CTkFont(size=16))
        self.score_entry.pack(side="left", padx=(0, 12))
        ctk.CTkLabel(input_frame, text="(1-100)", font=ctk.CTkFont(size=12), text_color="#999").pack(side="left")

        btn_frame = ctk.CTkFrame(parent, fg_color="transparent")
        btn_frame.pack(fill="x", padx=20, pady=(8, 16))
        for label, val in [("90 分", 90), ("95 分", 95), ("100 分", 100)]:
            ctk.CTkButton(btn_frame, text=label, width=80, height=32,
                          fg_color="#E3F2FD", text_color="#1565C0", hover_color="#BBDEFB",
                          font=ctk.CTkFont(size=13, weight="bold"),
                          command=lambda v=val: self._set_preset_score(v)).pack(side="left", padx=(0, 8))

        self.confirm_btn = ctk.CTkButton(btn_frame, text="确认分数", width=100, height=32,
                                         fg_color="#1565C0", text_color="white",
                                         hover_color="#1976D2", font=ctk.CTkFont(size=13, weight="bold"),
                                         command=self._confirm_score)
        self.confirm_btn.pack(side="left", padx=(8, 0))
        self.score_status = ctk.CTkLabel(btn_frame, text="", font=ctk.CTkFont(size=13), text_color="#4CAF50")
        self.score_status.pack(side="left", padx=12)

    def _build_status_card(self, parent):
        header = ctk.CTkFrame(parent, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(16, 8))
        ctk.CTkLabel(header, text="状态", font=ctk.CTkFont(size=16, weight="bold"), text_color="#333").pack(side="left")
        status_frame = ctk.CTkFrame(parent, fg_color="transparent")
        status_frame.pack(fill="x", padx=20, pady=(8, 16))
        self.status_indicator = ctk.CTkLabel(status_frame, text="> 等待开始", font=ctk.CTkFont(size=14), text_color="#999")
        self.status_indicator.pack(side="left")

    def _build_action_card(self, parent):
        header = ctk.CTkFrame(parent, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(16, 8))
        ctk.CTkLabel(header, text="操作", font=ctk.CTkFont(size=16, weight="bold"), text_color="#333").pack(side="left")
        btn_frame = ctk.CTkFrame(parent, fg_color="transparent")
        btn_frame.pack(fill="x", padx=20, pady=(8, 16))
        self.start_btn = ctk.CTkButton(btn_frame, text="开始评价", width=140, height=40,
                                       fg_color="#4CAF50", text_color="white",
                                       hover_color="#388E3C", font=ctk.CTkFont(size=15, weight="bold"),
                                       command=self._start_evaluation)
        self.start_btn.pack(side="left", padx=(0, 12))
        self.stop_btn = ctk.CTkButton(btn_frame, text="结束评价", width=100, height=40,
                                      fg_color="#F44336", text_color="white", hover_color="#D32F2F",
                                      font=ctk.CTkFont(size=15, weight="bold"),
                                      command=self._stop_evaluation, state="disabled")
        self.stop_btn.pack(side="left")

    def _set_preset_score(self, val):
        self.score_var.set(str(val))

    def _confirm_score(self):
        try:
            val = int(self.score_var.get())
            if 1 <= val <= 100:
                self.config["score"] = val
                self.config["score_confirmed"] = True
                self.score_status.configure(text=f"OK: {val}")
                self.status_indicator.configure(text=f"> 分数已确认 ({val})", text_color="#4CAF50")
            else:
                self.score_status.configure(text="请输入 1-100", text_color="#F44336")
        except ValueError:
            self.score_status.configure(text="请输入有效数字", text_color="#F44336")

    def _start_evaluation(self):
        if not self.config.get("score_confirmed", False):
            self.score_status.configure(text="请先确认分数！", text_color="#F44336")
            return

        self.score_status.configure(text="启动中...", text_color="#1565C0")
        self.status_indicator.configure(text="> 评价进行中...", text_color="#4CAF50")
        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")

        score = self.config["score"]
        url = self.config.get("evaluation_url", "")
        runner_script = os.path.join(os.path.dirname(__file__), "evaluation_runner.py")

        # 启动独立进程（不隐藏控制台，让 webview 窗口正常弹出）
        self.eval_process = subprocess.Popen(
            [sys.executable, runner_script, str(score), url],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

    def _stop_evaluation(self):
        if self.eval_process and self.eval_process.poll() is None:
            try:
                self.eval_process.terminate()
            except Exception:
                pass
        self.eval_process = None
        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.status_indicator.configure(text="> 已停止", text_color="#999")
        self.score_status.configure(text="")
