# my_tf2_robot

## テーマ

**tf2で「ちゃんとしたロボ座標系」を作る**

このパッケージは、ROS2のtf2ライブラリを使って現実的なロボット座標系ツリーを構築する学習用サンプルです。
ロボットが半径1mの円を描きながら走り、LiDARセンサーのフレームまでTFを正しく配信します。

---

## TFツリー

```
odom
 └── base_link        (動的TF: ロボットが円を移動)
      └── laser_frame (静的TF: base_linkの前方x=0.2m、上方z=0.1m)
```

| フレーム | 親フレーム | 種別 | 説明 |
|---|---|---|---|
| `base_link` | `odom` | 動的 (TransformBroadcaster) | ロボット本体。半径1m・角速度0.1 rad/sで円運動 |
| `laser_frame` | `base_link` | 静的 (StaticTransformBroadcaster) | LiDARセンサー取付位置 (x=0.2m, z=0.1m) |

---

## 学んだこと

- **`tf2_ros.TransformBroadcaster`** — タイマーコールバックで `TransformStamped` を都度ブロードキャストし、動的なTFを配信する方法
- **`tf2_ros.StaticTransformBroadcaster`** — 起動時に一度だけ送信すれば良い固定オフセットの配信方法
- **`geometry_msgs/msg/TransformStamped`** — TFメッセージの構造（header.frame_id, child_frame_id, translation, rotation）
- **TFツリーの構成** — `odom → base_link → laser_frame` という階層で座標変換を連鎖させる考え方
- **Foxgloveでの3D可視化** — foxglove_bridgeを使ってWebブラウザからTFツリーや点群をリアルタイムで確認する方法

---

## 起動方法

```bash
ros2 launch my_tf2_robot tf2_foxglove.launch.py
```

Foxgloveブラウザを開いて `ws://localhost:8765` に接続すると、ロボットが円を描く様子を3Dで確認できます。

---

## 動作確認コマンド

### TF変換を確認する

```bash
# odom -> base_link の変換を確認
ros2 run tf2_ros tf2_echo odom base_link

# base_link -> laser_frame の変換を確認
ros2 run tf2_ros tf2_echo base_link laser_frame
```

### TFツリー全体を表示する

```bash
ros2 run tf2_tools view_frames
```

### LaserScanトピックを確認する

```bash
ros2 topic echo /scan
ros2 topic hz /scan
```

---

## パッケージ構成

```
my_tf2_robot/
├── launch/
│   └── tf2_foxglove.launch.py   # ノード + foxglove_bridge を起動
├── my_tf2_robot/
│   ├── __init__.py
│   └── tf2_robot_publisher.py   # メインノード
├── resource/
│   └── my_tf2_robot
├── package.xml
├── setup.py
└── README.md
```
