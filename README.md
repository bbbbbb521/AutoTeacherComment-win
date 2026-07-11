# AutoTeacherComment-win

Windows 桌面版教师评价助手 — 基于 Edge WebView2 内嵌浏览器，自动填写中北大学教务系统教师评价表单。

> 基于 [yang-jingyu0722/nuc-teacher-comments](https://gitee.com/yang-jingyu0722/nuc-teacher-comments) 改进

---

## 原项目

| 项目 | 信息 |
|------|------|
| 项目名称 | nuc-teacher-comments |
| 原作作者 | [yang-jingyu0722](https://gitee.com/yang-jingyu0722) |
| 原仓库地址 | https://gitee.com/yang-jingyu0722/nuc-teacher-comments |
| 原项目说明 | 安卓应用，自动填写中北大学教务系统教师评价表单 |

## 功能特点

- 🎯 **自定义评分** — 设置 1-100 分
- 🤖 **自动填写** — 内嵌浏览器自动识别并填写评价表单
- 🔄 **自动提交** — 填写完成后自动点击提交
- 🎨 **简约界面** — customtkinter 现代化 UI

## 环境要求

- Windows 10/11
- Python 3.10+
- Edge WebView2 Runtime（Win10+ 已内置）

## 安装运行

```bash
pip install -r requirements.txt
python main.py
```

或直接双击 `run.bat`。

## 项目结构

```
AutoTeacherComment-win/
├── main.py              # 程序入口
├── run.bat              # 一键启动
├── requirements.txt     # Python 依赖
├── .gitignore
└── app/
    ├── __init__.py       # 主窗口 UI
    ├── home_tab.py       # 首页（评分设置、开始/停止）
    ├── schedule_tab.py   # 课表页面
    ├── evaluation_runner.py # WebView 评价浏览器
    ├── evaluator_js.py   # JS 注入代码生成
    └── inject_js.txt     # JS 注入模板
```

## 仓库

- GitHub：https://github.com/bbbbbb521/AutoTeacherComment-win
- Gitee：https://gitee.com/little-banyan/auto-teacher-comment-win

## 许可

仅供学习交流使用