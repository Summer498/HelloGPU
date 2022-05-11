# HelloGPU

## これは何?
- Nvidia 製 GPU 持ちのマシンで TensorFlow がきちんと GPU を使っているのか確認するためのプログラム
- .py 版と .ipynb 版がある

## 使い方
### Windows
```
git clone https://github.com/Summer498/HelloGPU/
python HelloGPU\HelloGPU.py
```

### Linux & Mac
```
git clone https://github.com/Summer498/HelloGPU/
python HelloGPU/HelloGPU.py
```

## 結果の見方
1.お使いのGPUの名前 (GeForce とか) がログとして出てくれば少なくともGPUを認識している
  - 出てこなければ認識すらしていない.
  - CUDA, CuDNN, TensorFlow のバージョン合わせをやり直す
    - [TensorFlow テスト済みのビルド構成 for Linux & Mac](https://www.tensorflow.org/install/source#tested_build_configurations)
    - [TensorFlow テスト済みのビルド構成 for Windows](https://www.tensorflow.org/install/source_windows#tested_build_configurations)

2.タスクマネージャーでGPUの使用量が上がっていることを確認
  - HelloGPU[.py|.ipynb] 内のバッチサイズを大きめにとると GPU の使用率が上がるので確認しやすい

## 参照
[@nemutas](https://qiita.com/nemutas), ["Anaconda + Keras でGPUを使用する環境を構築する"](https://qiita.com/nemutas/items/c7d9cca91a7e1bd404b6), Qiita
