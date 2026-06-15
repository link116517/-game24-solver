#!/bin/bash
# 24点游戏APK打包脚本
# 此脚本需要在Linux或WSL环境下运行

echo "======================================"
echo "  24点游戏 - Android APK打包工具"
echo "======================================"
echo ""

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到Python3，请先安装Python 3.7+"
    exit 1
fi

echo "✅ Python版本: $(python3 --version)"

# 检查pip是否安装
if ! command -v pip3 &> /dev/null; then
    echo "❌ 错误: 未找到pip3"
    exit 1
fi

# 检查Buildozer是否安装
if ! command -v buildozer &> /dev/null; then
    echo "📦 正在安装Buildozer..."
    pip3 install buildozer
    if [ $? -ne 0 ]; then
        echo "❌ Buildozer安装失败"
        exit 1
    fi
fi

echo "✅ Buildozer已安装"
echo ""

# 检查配置文件
if [ ! -f "buildozer.spec" ]; then
    echo "❌ 错误: 找不到buildozer.spec配置文件"
    exit 1
fi

echo "🔧 开始打包APK..."
echo ""

# 清理之前的构建
if [ -d "bin" ]; then
    echo "🗑️  清理旧的APK文件..."
    rm -rf bin
fi

# 执行打包
buildozer -v android debug

# 检查打包结果
if [ $? -eq 0 ]; then
    echo ""
    echo "======================================"
    echo "  ✅ APK打包成功！"
    echo "======================================"
    echo ""
    echo "📁 APK文件位置:"
    ls -lh bin/*.apk 2>/dev/null || echo "未找到APK文件"
    echo ""
    echo "📱 安装到手机:"
    echo "   adb install bin/game24solver-1.0.0-*-debug.apk"
    echo ""
else
    echo ""
    echo "======================================"
    echo "  ❌ APK打包失败"
    echo "======================================"
    echo ""
    echo "请检查错误信息并修复后重试"
    exit 1
fi