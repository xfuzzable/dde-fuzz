# dde-fuzz

## 编译项目及目标程序
```
installl package-name
```

## 编译项目及目标程序
```
cd fuzz-package-name
./build.sh package-name-path
```

## 运行模糊测试
```
./fuzz.sh 
```

## 目前支持模糊测试的应用

|dde-app-name|原生是否可编译|xfuzz是否可编译|测试版本|驱动是否已编写|
|---|---|---|---|---|
|dde-calendar|是|是|5.8.27|是|
|dde-clipboard|是|是|5.15.0102.6|是|
|dde-control-center|是|是|5.5.11.5|是|
|dde-device-formatter|是|是|0.0.1.12|是|
|dde-dock|是|是|5.5.9|是|
|dde-file-manager|是|是|5.5.3|是|
|dde-introduction|是|是|5.6.0.45|是|
|dde-kwin|是|是|5.4.19|是|
|dde-launcher|是|是|5.5.6|是|
|dde-network-utils|是|是|5.4.13|是|
|dde-polkit-agent|是|是|5.5.3|是|
|dde-printer|是|是|0.9.2|是|
|dde-qt-dbus-factory|是|是|5.5.5|是|
|dde-session-shell|是|是|5.5.9|是|
|dde-session-ui|是|是|5.5.6|是|
|dde-wayland|未知|未知|1.0.0|否|
