# 📋 APK导出检查清单

## ✅ 准备工作

### 必需条件
- [ ] 已安装Git（检查命令：`git --version`）
- [ ] 拥有GitHub账号（注册：https://github.com/join）
- [ ] 网络连接稳定
- [ ] 项目文件完整

### 项目文件检查
- [x] `game_24_mobile.py` - 应用源代码
- [x] `buildozer.spec` - 打包配置
- [x] `build_apk.sh` - 打包脚本
- [x] `.github/workflows/build-apk.yml` - Actions配置

---

## 🚀 使用GitHub Actions打包（推荐）

### 第1步：创建GitHub仓库
- [ ] 访问 https://github.com/new
- [ ] 填写仓库名称：`game24-solver`
- [ ] 设置为 **Public**（公共仓库）
- [ ] 点击 **Create repository**

### 第2步：上传代码
**方法A：使用一键部署脚本**
- [ ] 双击运行 `deploy_to_github.bat`
- [ ] 输入GitHub仓库地址
- [ ] 等待上传完成

**方法B：手动上传**
```bash
cd f:\workspace\file
git init
git add .
git commit -m "Initial commit"
git remote add origin <你的仓库地址>
git push -u origin main
```

### 第3步：启用Actions
- [ ] 打开GitHub仓库页面
- [ ] 点击 **Settings** → **Actions** → **General**
- [ ] 选择 **"Allow all actions and reusable workflows"**
- [ ] 点击 **Save**

### 第4步：触发打包
**方法A：创建Tag（推荐）**
```bash
git tag v1.0.0
git push origin v1.0.0
```

**方法B：手动触发**
- [ ] 点击仓库的 **Actions** 标签
- [ ] 找到 **"Build Android APK"**
- [ ] 点击右侧的 **Run workflow**
- [ ] 选择分支 → 点击 **Run workflow**

### 第5步：等待构建
- [ ] 观察Actions运行状态
- [ ] 首次构建约需20-30分钟
- [ ] 所有步骤显示绿色✅表示成功

### 第6步：下载APK
- [ ] 点击最近的Actions运行记录
- [ ] 滚动到页面底部
- [ ] 找到 **Artifacts** 区域
- [ ] 点击 **Game24Solver-APK** 下载
- [ ] 解压zip文件得到 `.apk` 文件

---

## 📱 安装测试

### 传输到手机
- [ ] 通过USB复制到手机
- [ ] 或上传到网盘生成二维码
- [ ] 或通过ADB安装：`adb install xxx.apk`

### 安装验证
- [ ] 在手机上点击APK文件
- [ ] 允许"安装未知来源应用"
- [ ] 等待安装完成
- [ ] 打开应用

### 功能测试
- [ ] 输入：1 4 6 8 → 点击Solve → 应显示解法
- [ ] 输入：1 1 1 1 → 点击Solve → 应提示无法得出
- [ ] 点击Clear按钮 → 输入框应清空

---

## 🔧 故障排查

### 如果Actions失败

检查以下项：
- [ ] 查看Actions日志，找到错误信息
- [ ] 确认所有文件都已上传到GitHub
- [ ] 检查`.github/workflows/build-apk.yml`是否存在
- [ ] 确认`buildozer.spec`配置正确

常见错误及解决：
1. **依赖安装失败** → 检查工作流中的apt-get命令
2. **SDK下载超时** → 重试或使用缓存
3. **权限错误** → 确保build_apk.sh有执行权限

### 如果APK无法安装

- [ ] 检查Android版本是否≥5.0
- [ ] 确认APK文件完整（未损坏）
- [ ] 关闭手机的"验证应用"功能
- [ ] 尝试重新签名APK

### 如果应用崩溃

- [ ] 连接电脑，执行：`adb logcat | grep python`
- [ ] 查看错误日志
- [ ] 检查是否是字体问题（应为英文界面）

---

## 📊 时间估算

| 步骤 | 预计时间 |
|------|----------|
| 创建GitHub仓库 | 2分钟 |
| 上传代码 | 2-5分钟 |
| 启用Actions | 1分钟 |
| 触发打包 | 1分钟 |
| **等待构建完成** | **20-30分钟** |
| 下载APK | 1-2分钟 |
| 传输到手机 | 2-5分钟 |
| **总计** | **约30-45分钟** |

---

## 💡 优化建议

### 后续改进方向
- [ ] 添加应用图标（icon.png）
- [ ] 添加启动画面（splash.png）
- [ ] 构建Release版本（非Debug）
- [ ] 对APK进行签名
- [ ] 添加中文支持（需嵌入字体）
- [ ] 发布到应用商店

### 减小APK体积
- [ ] 移除不需要的Python模块
- [ ] 使用ProGuard压缩
- [ ] 优化图片资源

---

## 🎯 成功标准

完成后您应该拥有：
- [x] 一个可正常安装的APK文件（40-60MB）
- [x] 应用可以正常启动和运行
- [x] 能够正确求解24点游戏
- [x] 界面无乱码（英文显示）
- [x] 触控操作流畅

---

## 📞 获取帮助

遇到问题时：
1. 查看详细教程：`APK导出指南.md`
2. 检查错误日志
3. 复制错误信息
4. 联系技术支持

---

**准备好了吗？让我们开始导出APK吧！** 🚀

按照以上清单逐步操作，您将成功获得可用的Android APK！