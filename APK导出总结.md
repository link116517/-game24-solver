# 📱 24点游戏APK导出 - 快速开始

## 🎯 最简单的方法（推荐）

### 使用GitHub Actions自动打包 ⚡

**无需安装任何软件，30分钟获得APK！**

---

## 📋 三步完成

### 第1步：上传到GitHub（5分钟）

**方法A：一键脚本（最简单）**
```bash
# 双击运行
deploy_to_github.bat
```

**方法B：手动上传**
```bash
cd f:\workspace\file
git init
git add .
git commit -m "Initial commit"

# 替换成你的仓库地址
git remote add origin https://github.com/你的用户名/game24-solver.git
git push -u origin main
```

### 第2步：触发自动打包（1分钟）

访问GitHub仓库页面 → **Actions** → **Run workflow**

或执行：
```bash
git tag v1.0.0
git push origin v1.0.0
```

### 第3步：下载APK（1分钟）

等待20-30分钟后：
- 点击 **Actions** → 选择运行记录
- 在 **Artifacts** 下载 **Game24Solver-APK**
- 解压得到 `.apk` 文件

---

## 📁 项目文件说明

| 文件 | 用途 |
|------|------|
| `game_24_mobile.py` | Kivy应用源代码 |
| `buildozer.spec` | APK打包配置 |
| `build_apk.sh` | Linux打包脚本 |
| `.github/workflows/build-apk.yml` | GitHub Actions配置 |
| `deploy_to_github.bat` | Windows一键部署脚本 |
| `README_APK.md` | 简明教程 |
| `APK导出指南.md` | 详细教程 |
| `APK导出检查清单.md` | 操作清单 |

---

## 🎮 应用功能

- ✅ 输入4个数字（1-10），自动求解24点
- ✅ 智能算法尝试所有运算组合
- ✅ 专为手机优化的触控界面
- ✅ 简洁美观的英文界面
- ✅ 支持Android 5.0+系统

---

## 📖 详细文档

1. **[README_APK.md](README_APK.md)** - 快速入门
2. **[APK导出指南.md](APK导出指南.md)** - 完整教程
3. **[APK导出检查清单.md](APK导出检查清单.md)** - 操作清单

---

## ❓ 常见问题

**Q: 真的完全免费吗？**  
A: 是的！GitHub为公共仓库提供每月2000分钟免费Actions时间。

**Q: 需要Linux环境吗？**  
A: 不需要！GitHub Actions在云端完成打包，您只需上传代码。

**Q: APK多大？**  
A: 约40-60MB（包含Python运行时）。

**Q: 可以在iPhone上用吗？**  
A: 当前仅支持Android。

---

## 🚀 立即开始

1. **确保已安装Git**（检查：`git --version`）
2. **创建GitHub账号**（https://github.com/join）
3. **运行部署脚本**：`deploy_to_github.bat`
4. **等待APK生成**：约30分钟
5. **安装到手机**：享受应用！

---

**准备好了吗？双击 `deploy_to_github.bat` 开始吧！** 🎉

如有问题，请查看详细教程或告诉我具体错误信息。