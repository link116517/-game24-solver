# 24点游戏手机版 - 快速开始指南

## 🚀 三种获取APK的方式

### 方式一：使用GitHub Actions自动打包（最简单）✨

1. **Fork本项目**到你的GitHub账号
2. **启用Actions**：在你的仓库页面 → Settings → Actions → General → 选择"Allow all actions"
3. **触发打包**：
   - 提交任意代码更改会自动触发打包
   - 或者手动触发：Actions → Build Android APK → Run workflow
4. **下载APK**：
   - Actions完成后，在Artifacts中下载
   - 或者在Releases页面下载（如果创建了tag）

### 方式二：使用WSL2在Windows上打包

#### 第1步：安装WSL2
```powershell
# 在PowerShell管理员模式下运行
wsl --install
```

#### 第2步：在WSL2中设置环境
```bash
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装依赖
sudo apt install -y python3-pip build-essential git python3-dev \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    openjdk-13-jdk autoconf automake libtool

# 安装Buildozer
pip3 install buildozer
```

#### 第3步：打包APK
```bash
# 进入项目目录
cd /mnt/f/workspace/file

# 运行打包脚本
chmod +x build_apk.sh
./build_apk.sh
```

#### 第4步：安装到手机
```bash
# 开启手机USB调试模式后
adb install bin/game24solver-1.0.0-*-debug.apk
```

### 方式三：使用Linux/Mac直接打包

#### Ubuntu/Debian用户
```bash
# 一键安装依赖并打包
sudo apt update
sudo apt install -y python3-pip build-essential git python3-dev \
    ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev \
    libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev \
    libavcodec-dev zlib1g-dev libgstreamer1.0 gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good openjdk-13-jdk autoconf automake libtool

pip3 install buildozer
cd f:\workspace\file
buildozer android debug
```

#### macOS用户
```bash
# 安装Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装依赖
brew install python3 cmake sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer

# 安装Buildozer并打包
pip3 install buildozer
cd f:\workspace\file
buildozer android debug
```

## 📱 在电脑上测试（无需打包）

如果你想先看看程序效果，可以在电脑上直接运行：

```bash
# 安装Kivy
pip install kivy

# 运行程序
python game_24_mobile.py
```

## 🎮 使用说明

1. **输入数字**：在4个输入框中输入1-10的数字
2. **点击"求解"**：程序会尝试找出能得到24的运算方式
3. **查看结果**：
   - ✅ 如果能得出24，显示具体表达式
   - ❌ 如果不能，提示无法得出
4. **清空重填**：点击"清空"按钮清除所有输入

## 🔧 常见问题

### Q1: 打包时卡在下载SDK怎么办？
```bash
# 可以手动下载SDK并配置路径
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
```

### Q2: APK文件太大（50MB+）？
这是正常的，Kivy应用包含Python运行时。可以通过以下方式优化：
- 使用ProGuard压缩
- 移除不需要的模块
- 构建release版本

### Q3: 安装后无法打开？
- 检查Android版本（需要Android 5.0+）
- 查看logcat日志：`adb logcat | grep python`

### Q4: 如何签名发布版APK？
```bash
# 生成keystore
keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000

# 构建release版本
buildozer android release

# 签名APK
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore bin/app-release-unsigned.apk alias_name
```

## 📊 项目结构

```
f:\workspace\file\
├── game_24_mobile.py          # Kivy应用程序源代码
├── buildozer.spec             # Buildozer配置文件
├── build_apk.sh               # 自动打包脚本
├── ANDROID_README.md          # 详细说明文档
└── .github/
    └── workflows/
        └── build-apk.yml      # GitHub Actions配置
```

## 🌟 下一步

- [ ] 添加应用图标
- [ ] 添加启动画面
- [ ] 构建release版本
- [ ] 发布到应用商店
- [ ] 添加更多功能（历史记录、挑战模式等）

## 💡 提示

如果你只是想使用这个应用，推荐使用：
1. **方式一**：等待我打包好的APK文件
2. **方式二**：在电脑上用Python直接运行测试

如果你是开发者想自己打包，建议使用GitHub Actions自动化流程。

---

**祝您使用愉快！** 🎉📱