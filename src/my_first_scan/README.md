# テーマ1: 疑似LaserScanの配信とRViz2可視化

**目的:** ROS2の基本通信・標準メッセージ・TF・可視化の流れを理解する

**内容:**
- Pythonノードで疑似 `LaserScan` を10Hzでpublish
- `base_link` → `laser_frame` の静的TFを設定
- RViz2で扇形スキャンを表示確認

## 起動方法

**ターミナル1: スキャンpublisher**
```bash
ros2 run my_first_scan scan_publisher
```

**ターミナル2: 静的TF**
```bash
ros2 run tf2_ros static_transform_publisher \
  --x 0.2 --y 0 --z 0.1 \
  --frame-id base_link --child-frame-id laser_frame
```

**ターミナル3: 確認**
```bash
ros2 topic list
ros2 topic echo /scan
```

**RViz2:**
1. `rviz2` 起動
2. Fixed Frame → `base_link`
3. Add → LaserScan → Topic: `/scan`

## Foxglove Studio での可視化（スマホ・ブラウザ対応）

RViz2 の代わりに Foxglove Studio を使うと、スマホブラウザから VPS 上の ROS2 を可視化できる。

### インストール（VPS）

```bash
sudo apt install ros-jazzy-foxglove-bridge
```

### 一括起動（scan_publisher + TF + foxglove_bridge）

```bash
ros2 launch my_first_scan scan_foxglove.launch.py
```

### 接続（スマホ / PC ブラウザ）

1. ブラウザで https://studio.foxglove.dev を開く
2. 「Open connection」→「WebSocket」を選択
3. `ws://<VPS_IP>:8765` を入力して接続
4. 「Add panel」→「3D」→ トピック `/scan` を選択

### ポート開放（必要な場合）

```bash
sudo ufw allow 8765
```

### Tailscale 利用時（推奨）

インターネット公開せず安全に接続できる。

```bash
ws://<tailscale_ip>:8765
```

---

## 学んだこと
- [x] rclpy の Node / Timer / Publisher の使い方
- [x] `sensor_msgs/msg/LaserScan` のフィールド構成
- [x] `header.frame_id` と TF の関係
- [x] `static_transform_publisher` でフレームを繋ぐ方法
- [x] RViz2 での LaserScan 表示設定
- [x] Foxglove Studio + foxglove_bridge でスマホ・ブラウザから可視化する方法
- [x] launch ファイルで複数ノードを一括起動する方法
