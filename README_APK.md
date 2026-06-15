# 🎮 24点游戏求解器 - Android版

## 📱 快速导出APK（3步完成）

### 最简单的方法：GitHub Actions自动打包 ⚡

**无需安装任何软件，全程自动化！**

#### 步骤1：上传到GitHub
```bash
cd f:\workspace\file
git init
git add .
git commit -m "Initial commit"

# 在GitHub创建仓库后，替换下面的URL
git remote add origin https://github.com/你的用户名/game24-solver.git
git push -u origin main
```

#### 步骤2：触发自动打包
访问你的GitHub仓库页面 → **Actions** → **Run workflow**

或者执行：
```bash
git tag v1.0.0
git push origin v1.0.0
```

#### 步骤3：下载APK
等待约20-30分钟后：
- 点击 **Actions** → 选择运行记录
- 在 **Artifacts** 区域下载 **Game24Solver-APK**
- 解压得到 `.apk` 文件

---

## 📋 项目说明

### 功能特点
- ✅ 输入4个数字（1-10），自动求解24点
- ✅ 智能算法尝试所有运算组合
- ✅ 专为手机优化的触控界面
- ✅ 简洁美观的英文界面
- ✅ 支持Android 5.0+系统

### 界面预览
```
┌──────────────────────┐
│  24 Point Game Solver│
├──────────────────────┤
│ Enter 4 numbers (1-10)│
├──────────────────────┤
│ [1] [4] [6] [8]     │
├──────────────────────┤
│  [Solve]   [Clear]   │
├──────────────────────┤
│ Result:              │
│ Success! Found:      │
│ ((1-4)+6)*8 = 24    │
└──────────────────────┘
```

---

## 📁 文件说明

| 文件 | 用途 |
|------|------|
| `game_24_mobile.py` | Kivy应用源代码（英文版） |
| `buildozer.spec` | APK打包配置 |
| `build_apk.sh` | 自动打包脚本 |
| `.github/workflows/build-apk.yml` | GitHub Actions配置 |
| `APK导出指南.md` | 详细打包教程 |

---

## 🔧 本地开发测试

### 在电脑上预览
```bash
pip install kivy
python game_24_mobile.py
```

### 本地打包（需要Linux环境）
```bash
# 在WSL2或Linux上执行
chmod +x build_apk.sh
./build_apk.sh
```

---

## ❓ 常见问题

**Q: 我没有GitHub账号怎么办？**  
A: 注册一个免费账号即可（https://github.com/join）

**Q: 打包要多久？**  
A: 首次约20-30分钟，后续更快

**Q: APK多大？**  
A: 约40-60MB

**Q: 可以在iPhone上用吗？**  
A: 当前仅支持Android，iOS需要额外配置

---

## 📞 需要帮助？

详细教程请查看：**[APK导出指南.md](APK导出指南.md)**

如有问题，请告诉我具体错误信息！

---

**准备好了吗？让我们开始吧！** 🚀