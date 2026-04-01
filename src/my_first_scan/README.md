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

## 学んだこと
- [ ] rclpy の Node / Timer / Publisher の使い方
- [ ] `sensor_msgs/msg/LaserScan` のフィールド構成
- [ ] `header.frame_id` と TF の関係
- [ ] `static_transform_publisher` でフレームを繋ぐ方法
- [ ] RViz2 での LaserScan 表示設定
