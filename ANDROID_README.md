# 24点游戏 - Android APK版本

## 简介
这是一个基于Kivy框架开发的Android移动应用，可以判断输入的4个数字是否能通过四则运算得到24。

## 功能特点
- ✅ 支持输入4个1-10的数字
- ✅ 自动尝试所有可能的运算组合
- ✅ 如果能得出24，给出一种具体的运算方式
- ✅ 如果不能得出24，会明确提示
- ✅ 专为手机优化的触控界面
- ✅ 简洁美观的用户体验

## 📱 安装方法

### 方法一：使用预编译的APK（推荐）
如果您已经有APK文件，直接传输到手机安装即可。

### 方法二：自己打包APK

#### 环境要求
- **操作系统**：Linux（Ubuntu推荐）或 macOS
- **Python版本**：Python 3.7+
- **依赖工具**：Buildozer

#### 步骤1：安装依赖

**在Ubuntu/Linux上：**
```bash
# 安装系统依赖
sudo apt-get update
sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    libgstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    openjdk-13-jdk \
    autoconf \
    automake \
    libtool

# 安装Buildozer
pip3 install buildozer
```

**在macOS上：**
```bash
# 安装Homebrew（如果没有）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装依赖
brew install python3
brew install cmake sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer

# 安装Buildozer
pip3 install buildozer
```

#### 步骤2：准备项目
```bash
cd f:\workspace\file
```

#### 步骤3：打包APK
```bash
# 首次运行会自动下载Android SDK/NDK等
buildozer android debug

# 或者使用详细输出模式
buildozer -v android debug
```

#### 步骤4：查找生成的APK
打包完成后，APK文件位于：
```
bin/game24solver-1.0.0-arm64-v8a_armeabi-v7a-debug.apk
```

### ⚠️ Windows用户注意事项

**Buildozer不支持Windows原生环境**，Windows用户有以下选择：

#### 选项A：使用WSL2（推荐）
1. 安装WSL2（Windows Subsystem for Linux）
2. 在WSL2中安装Ubuntu
3. 按照上述Linux步骤进行打包

#### 选项B：使用虚拟机
1. 安装VirtualBox或VMware
2. 创建Ubuntu虚拟机
3. 在虚拟机中进行打包

#### 选项C：使用在线服务
可以使用GitHub Actions等CI/CD服务自动打包APK

## 🧪 测试应用

### 在电脑上测试
在打包成APK之前，可以先在电脑上测试：

```bash
# 安装Kivy
pip install kivy

# 运行程序
python game_24_mobile.py
```

## 📋 项目文件说明

- `game_24_mobile.py` - Kivy应用程序源代码
- `buildozer.spec` - Buildozer配置文件
- `bin/` - 生成的APK文件目录（打包后自动创建）

## 🎨 自定义配置

### 修改应用图标
替换 `icon.png` 文件（512x512像素）

### 修改启动画面
替换 `splash.png` 文件

### 修改应用名称
编辑 `buildozer.spec` 中的 `title` 字段

### 修改包名
编辑 `buildozer.spec` 中的 `package.name` 和 `package.domain` 字段

## 🔧 常见问题

### Q: 打包时下载SDK/NDK很慢怎么办？
A: 可以使用国内镜像源，或在buildozer.spec中指定已下载的SDK路径。

### Q: APK文件太大怎么办？
A: 这是正常现象，Kivy应用通常包含Python运行时，APK大小约30-50MB。

### Q: 如何在真机上调试？
A: 开启手机的USB调试模式，使用adb安装和调试：
```bash
adb install bin/game24solver-1.0.0-arm64-v8a_armeabi-v7a-debug.apk
adb logcat | grep python
```

### Q: 应用崩溃怎么办？
A: 查看logcat日志：
```bash
adb logcat
```

## 📝 代码结构

### 核心类
- `EvaluateExpression`: 24点求解核心逻辑
- `Game24App`: Kivy应用程序主类

### UI组件
- 4个数字输入框
- "求解"和"清空"按钮
- 结果显示区域（支持滚动）

## 📄 许可证
本项目仅供学习和个人使用。

## 🌟 优化建议

如需发布到应用商店，建议：
1. 添加应用图标和启动画面
2. 构建release版本（去掉debug标志）
3. 对APK进行签名
4. 优化应用大小
5. 添加更多功能（历史记录、提示等）

## 📞 技术支持

如遇到问题，请检查：
1. Python版本是否正确（3.7+）
2. 依赖是否完整安装
3. Android SDK/NDK配置是否正确
4. 查看错误日志

---

**祝您使用愉快！** 🎉