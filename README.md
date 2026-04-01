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

## テーマ一覧

| # | パッケージ | 内容 |
|---|---|---|
| 1 | [my_first_scan](src/my_first_scan/) | 疑似LaserScanの配信とRViz2可視化 |
