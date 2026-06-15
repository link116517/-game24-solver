@echo off
chcp 65001 >nul
title 24点游戏 - GitHub自动部署工具
color 0A

echo.
echo ========================================
echo   24点游戏 - GitHub自动部署工具
echo ========================================
echo.
echo 本工具将帮助您快速上传代码到GitHub
echo 然后使用Actions自动打包APK
echo.
pause

echo.
echo [步骤1] 检查Git是否安装...
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ❌ 错误：未找到Git命令！
    echo.
    echo 请先安装Git: https://git-scm.com/download/win
    echo.
    pause
    exit /b
)
echo ✅ Git已安装
echo.

echo [步骤2] 请输入您的GitHub仓库地址
echo 格式：https://github.com/用户名/仓库名.git
echo 例如：https://github.com/zhangsan/game24-solver.git
echo.
set /p REPO_URL="请输入仓库地址: "

if "%REPO_URL%"=="" (
    echo ❌ 错误：仓库地址不能为空！
    pause
    exit /b
)

echo.
echo [步骤3] 初始化Git仓库...
cd /d %~dp0
git init
git add .
git commit -m "Initial commit: 24点游戏手机版"

echo.
echo [步骤4] 关联远程仓库...
git remote add origin %REPO_URL%

echo.
echo [步骤5] 推送到GitHub...
git push -u origin main

if %errorlevel% neq 0 (
    echo.
    echo ⚠️ 推送失败！可能是分支名称问题
    echo 尝试使用master分支...
    git branch -M master
    git push -u origin master
)

echo.
echo ========================================
echo   ✅ 代码上传成功！
echo ========================================
echo.
echo 下一步操作：
echo.
echo 1. 打开浏览器访问您的GitHub仓库
echo 2. 点击 "Actions" 标签页
echo 3. 点击 "Run workflow" 按钮
echo 4. 等待约20-30分钟
echo 5. 在Artifacts中下载APK文件
echo.
echo 详细教程请查看：APK导出指南.md
echo.
pause