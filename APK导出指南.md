# 📱 24点游戏 - APK导出完整指南

## 🎯 三种导出方案

### ✨ 方案一：GitHub Actions自动打包（最推荐）

**优点：**
- ✅ 无需安装任何软件
- ✅ 全自动云端打包
- ✅ 支持Windows/Mac/Linux
- ✅ 每次提交代码自动构建

**步骤：**

#### 1️⃣ 创建GitHub仓库
```bash
# 在GitHub网站创建新仓库
# 访问: https://github.com/new
# 仓库名: game24-solver
# 可见性: Public（免费使用Actions）
```

#### 2️⃣ 上传代码到GitHub
```bash
# 在项目目录下执行
cd f:\workspace\file

# 初始化git（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: 24点游戏手机版"

# 添加远程仓库（替换成你的仓库地址）
git remote add origin https://github.com/你的用户名/game24-solver.git

# 推送
git push -u origin main
```

#### 3️⃣ 启用GitHub Actions
1. 打开你的GitHub仓库页面
2. 点击 **Settings** → **Actions** → **General**
3. 选择 **"Allow all actions and reusable workflows"**
4. 点击 **Save**

#### 4️⃣ 触发自动打包
```bash
# 方法A：创建一个新的tag
git tag v1.0.0
git push origin v1.0.0

# 方法B：直接在网页点击Actions标签页
# 找到 "Build Android APK" workflow
# 点击 "Run workflow" → "Run workflow"
```

#### 5️⃣ 下载APK
**方式A（通过Artifacts）：**
1. 点击仓库的 **Actions** 标签
2. 点击最近的一次运行记录
3. 在底部找到 **Artifacts** 区域
4. 点击 **Game24Solver-APK** 下载
5. 解压下载的zip文件，得到 `.apk` 文件

**方式B（通过Releases）：**
1. 点击仓库右侧的 **Releases**
2. 找到最新版本（v1.0.0）
3. 点击APK文件直接下载

---

### 💻 方案二：使用WSL2在Windows上打包

**适合：** 有稳定网络、想本地打包的用户

#### 第1步：安装WSL2
```powershell
# 以管理员身份运行PowerShell
wsl --install
```
重启电脑后完成安装。

#### 第2步：设置WSL2环境
```bash
# 在WSL2终端中执行
sudo apt update
sudo apt upgrade -y

# 安装依赖
sudo apt install -y python3-pip build-essential git python3-dev \
    ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev \
    libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev \
    libavcodec-dev zlib1g-dev libgstreamer1.0 gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good openjdk-17-jdk autoconf automake libtool

# 安装Buildozer
pip3 install buildozer
```

#### 第3步：打包APK
```bash
# 进入项目目录（Windows路径在WSL中的挂载点）
cd /mnt/f/workspace/file

# 运行打包脚本
chmod +x build_apk.sh
./build_apk.sh
```

#### 第4步：查找APK
```bash
# 打包完成后，APK位于bin目录
ls -lh bin/*.apk

# 复制到Windows桌面
cp bin/*.apk /mnt/c/Users/你的用户名/Desktop/
```

---

### 🐧 方案三：使用Linux虚拟机或真机

**适合：** 熟悉Linux的用户

#### 系统要求
- Ubuntu 20.04 LTS 或更高版本
- 至少8GB内存
- 至少20GB磁盘空间

#### 一键打包命令
```bash
# 克隆项目
git clone <你的仓库地址>
cd game24-solver

# 安装依赖
sudo apt update
sudo apt install -y python3-pip build-essential git python3-dev \
    ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev \
    libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev \
    libavcodec-dev zlib1g-dev libgstreamer1.0 gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good openjdk-17-jdk autoconf automake libtool

pip3 install buildozer

# 打包APK
chmod +x build_apk.sh
./build_apk.sh
```

---

## 📊 各方案对比

| 方案 | 难度 | 时间 | 成本 | 适用场景 |
|------|------|------|------|----------|
| GitHub Actions | ⭐ 简单 | 15-30分钟 | 免费 | 所有人，特别是Windows用户 |
| WSL2 | ⭐⭐ 中等 | 1-2小时 | 免费 | 有一定技术基础的用户 |
| Linux虚拟机 | ⭐⭐⭐ 较难 | 2-3小时 | 免费 | 熟悉Linux的用户 |

---

## 🔍 常见问题FAQ

### Q1: GitHub Actions免费吗？
**A:** 是的！GitHub为公共仓库提供每月2000分钟的免费Actions使用时间，对于本项目绰绰有余。

### Q2: 打包需要多长时间？
**A:** 
- GitHub Actions: 首次约20-30分钟（需下载SDK/NDK），后续约10-15分钟
- WSL2本地打包: 取决于网速和电脑性能，通常1-2小时

### Q3: APK文件大小是多少？
**A:** 约40-60MB，因为包含了Python运行时和Kivy框架。

### Q4: 可以在iOS上安装吗？
**A:** 当前配置仅支持Android。如需iOS支持，需要修改buildozer.spec并重新打包。

### Q5: 安装APK时提示"禁止安装未知来源应用"怎么办？
**A:** 在手机设置中允许"安装未知来源应用"：
   - 设置 → 安全 → 未知来源 → 允许
   - 或在安装时点击"允许"

### Q6: 安装后无法打开？
**A:** 检查：
   - Android版本是否≥5.0
   - 查看日志：`adb logcat | grep python`

---

## 📥 获取APK后的操作

### 安装到手机
```bash
# 方法1：通过USB传输
# 将APK文件复制到手机，然后点击安装

# 方法2：通过ADB安装（需开启USB调试）
adb install bin/game24solver-1.0.0-arm64-v8a_armeabi-v7a-debug.apk

# 方法3：扫码安装
# 将APK上传到网盘，生成二维码，手机扫码下载
```

### 测试应用
1. 打开应用
2. 输入4个数字（如：1, 4, 6, 8）
3. 点击 **Solve** 按钮
4. 查看结果：`((1-4)+6)*8 = 24` ✅

---

## 🚀 快速开始（推荐流程）

**我建议您使用GitHub Actions方案，具体步骤：**

1. **创建GitHub仓库**（5分钟）
2. **上传代码**（2分钟）
3. **启用Actions**（1分钟）
4. **触发打包**（1分钟，等待20-30分钟）
5. **下载APK**（1分钟）

**总计：约30-40分钟即可获得APK！**

---

## 📞 需要帮助？

如果在打包过程中遇到任何问题，请：
1. 查看错误日志
2. 复制错误信息
3. 告诉我具体的错误内容

我会帮您解决问题！

---

**祝您打包成功！** 🎉📱