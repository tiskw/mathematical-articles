# Mathematical Articles

本レポジトリは，石川およびその共著者が作成した技術文書のソースコード群をまとめたものです．
文書の内容だけでなく，TeXのサンプルとしてもご活用頂ければ幸いです．


## 再コンパイル（タイプセット）の方法

### 環境の準備

再現性を担保するため，タイプセット環境は docker イメージとして提供しています．
まずは docker の動作する環境と make コマンドをインストールして下さい．
Ubuntu の場合，管理者権限にて以下コマンドを実行することでインストールすることができます．

```console
# make のインストール
$ apt install make

# docker のインストール
$ apt install apt-transport-https ca-certificates curl software-properties-common 
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
$ apt update
$ apt install docker-ce
```

### 再タイプセットのコマンド

どの文書も `Makefile` を提供しており，`make` コマンドでタイプセットできるようになっています．
各ディレクトリで以下を実行して下さい．

```console
$ make
```

事前に docker コンテナに入っておく必要はありません．`Makefile` が内部で docker コマンドを呼び出しています．


## ライセンス

本レポジトリの技術文書およびソースコードは，表示-非営利-改変禁止のクリエイティブコモンズライセンスの元で公開しています．
詳細は [LICENSE](LICENSE)，あるいは[リーガルコード](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.ja)をご参照下さい．


## 著者

石川 徹也 ([EMail](mailto:tiskw111@gmail.com), [Website](https://tiskw.gitlab.io/home/))

