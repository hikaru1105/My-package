# My-package
このリポジトリはロボットシステム学の授業で使用するROS2のパッケージです。

# CPU使用率を出力するノード
[![test](https://github.com/hikaru1105/My-package/actions/workflows/test.yml/badge.svg)](https://github.com/hikaru1105/My-package/actions/workflows/test.yml)

## 概要

- このノードは現在使っているCPUの使用率のデータをROS2を用いて通信するものです。

## 実行方法

### 実行方法の例

```
$ ros2 run mypkg cpuutilization
```

### 通信できているかの確認方法

- 実行しているUbuntuと別のUbuntuを開き、そこで以下に示されているコマンドを入力します。
```
$ ros2 topic echo cpu_usage
data: 'User CPU: 0%, System CPU: 0%, Idle CPU: 100%'
---
data: 'User CPU: 0%, System CPU: 0%, Idle CPU: 100%'
---  
```
## テスト環境   
- Ubuntu 22.04 LTS
## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
## Copyright
- © 2024 Hikaru Nemoto 
