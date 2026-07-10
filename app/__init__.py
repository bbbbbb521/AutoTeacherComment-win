import customtkinter as ctk
from app.home_tab import HomeTab
from app.schedule_tab import ScheduleTab

class AutoTeacherApp:
    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("教师评价助手 - AutoTeacherComment")
        self.root.geometry("900x650")
        self.root.minsize(800, 580)
        self._center_window()

        self.config = {
            "score": 100,
            "score_confirmed": False,
            "evaluation_url": "https://zhjw.nuc.edu.cn/jwglxt/xspjgl/xspj_cxXspjIndex.html?doType=details&gnmkdm=N401605&layout=default",
        }

        self._build_ui()
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _center_window(self):
        self.root.update_idletasks()
        w, h = 900, 650
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    def _build_ui(self):
        self.main_container = ctk.CTkFrame(self.root, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=0, pady=0)

        title_frame = ctk.CTkFrame(self.main_container, fg_color="#1565C0", height=56, corner_radius=0)
        title_frame.pack(fill="x", padx=0, pady=0)
        title_frame.pack_propagate(False)

        ctk.CTkLabel(
            title_frame, text="\U0001f4dd 教师评价助手",
            font=ctk.CTkFont(size=20, weight="bold"), text_color="white",
        ).pack(side="left", padx=24, pady=12)

        ctk.CTkLabel(
            title_frame, text="v1.0 Windows 版",
            font=ctk.CTkFont(size=12), text_color="white",
        ).pack(side="right", padx=24, pady=12)

        self.tab_view = ctk.CTkTabview(
            self.main_container, fg_color="transparent",
            segmented_button_fg_color="#E3F2FD",
            segmented_button_selected_color="#1565C0",
            segmented_button_selected_hover_color="#1976D2",
            segmented_button_unselected_color="#E3F2FD",
            text_color="white",
        )
        self.tab_view.pack(fill="both", expand=True, padx=16, pady=(12, 16))

        self.home_tab_frame = self.tab_view.add("\U0001f3e0 首页")
        self.home_tab = HomeTab(self.home_tab_frame, self.config)

        self.schedule_tab_frame = self.tab_view.add("\U0001f4cb 课表")
        self.schedule_tab = ScheduleTab(self.schedule_tab_frame)
        self.tab_view.set("\U0001f3e0 首页")

    def _on_close(self):
        try:
            self.root.quit()
            self.root.destroy()
        except Exception:
            pass

    def run(self):
        self.root.mainloop()
