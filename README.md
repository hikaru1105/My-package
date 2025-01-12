# mypkg
- ROS2のパッケージです。

[![test](https://github.com/hikaru1105/My-package/actions/workflows/test.yml/badge.svg)](https://github.com/hikaru1105/My-package/actions/workflows/test.yml)

## ノード`cpuutilizaion.py`

- このノードは現在使っているCPUの使用率のデータをトピック`cpu_usage`にパブリッシュするものです。

## テスト用ノード
### ノード`listener_test.py`

- このノードは通信が行えていることを確認するためのものです。
- トピック`cpu_usage`をサブスクライブします。

## トピック`cpu_usage`

このトピックはCPUの使用率を表示します。

- `User CPU`　　ユーザーモードで使用されているCPUの割合
- `System CPU`　カーネルモードで使用されているCPUの割合
- `Idle CPU`　　使用されていないCPUの割合

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
- © 2025 Hikaru Nemoto 
