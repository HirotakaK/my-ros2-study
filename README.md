# my-ros2-study

ROS2の基礎を手を動かして学ぶリポジトリ。

---

## セットアップ

### 1. uv のインストール

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 開発環境の構築

```bash
cd ~/my-ros2-study
uv sync          # .venv を作成して開発ツール(flake8, pytest)をインストール
```

### 3. ROS2 のセットアップ

```bash
source /opt/ros/jazzy/setup.bash
# colcon が未インストールの場合
pip install --user --break-system-packages colcon-common-extensions
```

> **補足:** ROS2パッケージ本体の依存 (`rclpy`, `sensor_msgs` など) は `package.xml` と colcon で管理します。
> uv はリンター・テストなど開発ツールの管理に使います。

### 4. ビルド

```bash
colcon build
source install/setup.bash
```

---

## テーマ1: 疑似LaserScanの配信とRViz2可視化

**目的:** ROS2の基本通信・標準メッセージ・TF・可視化の流れを理解する

**内容:**
- Pythonノードで疑似 `LaserScan` を10Hzでpublish
- `base_link` → `laser_frame` の静的TFを設定
- RViz2で扇形スキャンを表示確認

### ビルドと起動

```bash
cd ~/my-ros2-study
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash
```

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

### 学んだこと
- [ ] rclpy の Node / Timer / Publisher の使い方
- [ ] `sensor_msgs/msg/LaserScan` のフィールド構成
- [ ] `header.frame_id` と TF の関係
- [ ] `static_transform_publisher` でフレームを繋ぐ方法
- [ ] RViz2 での LaserScan 表示設定
