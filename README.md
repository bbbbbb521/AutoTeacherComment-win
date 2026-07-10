# AutoTeacherComment-win

基于 [yang-jingyu0722/nuc-teacher-comments](https://gitee.com/yang-jingyu0722/nuc-teacher-comments) 改进的 Windows 桌面版。

---

## 原项目

**项目名称**：nuc-teacher-comments
**原作作者**：[yang-jingyu0722](https://gitee.com/yang-jingyu0722)
**原仓库地址**：https://gitee.com/yang-jingyu0722/nuc-teacher-comments
**原项目说明**：一款安卓应用，用于自动填写中北大学教务系统中的教师评价表单。

## 本版本改进

- 将 Android App（Kotlin）转换为 **Windows 桌面应用**（Python）
- 使用 **customtkinter** 构建现代化桌面 UI，替代 Android Material Design
- 使用 **Edge WebView2** 内嵌浏览器替代 Android WebView，支持 JavaScript 注入自动填表
- 独立的子进程评价浏览器，不阻塞主界面
- 移除 Android 特有的 AccessibilityService、悬浮窗权限等依赖
- 保留核心的 JavaScript 自动填写逻辑（单选按钮 + 输入框双模式）

## 功能特点

- 🎯 **自定义评分** - 设置 1-100 分的自定义分数
- 🤖 **自动填写** - 在应用内浏览器打开教务系统，自动识别并填写评价表单
- 🔄 **自动提交** - 填写完成后自动点击提交
- ➡️ **自动切换** - 自动切换到下一位老师继续评价
- 📋 **课表管理** - 课程表查看（框架已搭建，待完善）
- 🎨 **简约界面** - customtkinter 现代化 UI

## 使用说明

### 环境要求
- Windows 10/11
- Python 3.10+
- Edge WebView2 Runtime（Windows 10+ 已内置）

### 安装和运行

\\bash
pip install -r requirements.txt
python main.py
\
或者双击 run.bat\。

## 项目结构

\AutoTeacherComment-win/
├── main.py                 # 程序入口
├── run.bat                 # 一键启动脚本
├── requirements.txt        # Python 依赖
├── README.md               # 本文档
└── app/
    ├── __init__.py          # 主窗口 UI（标题栏 + 标签页）
    ├── home_tab.py          # 首页（评分设置、开始/停止评价）
    ├── schedule_tab.py      # 课表页面
    ├── evaluation_runner.py # 独立进程：WebView 评价浏览器
    ├── evaluator_js.py      # JavaScript 注入代码生成器
    └── inject_js.txt        # JS 注入模板
\
## 许可证

本项目仅供学习交流使用。
