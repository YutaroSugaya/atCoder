# AtCoder 競技プログラミング環境設定

## 初期設定・ログイン

- 初回または期間が空いた時は `acc login` を実行
- CLIのログインは今できないので以下の手順でsessionを編集する（session.jsonだけでOK）
- 参考: [AtCoderのログイン問題解決方法](https://kaiyou9.com/acc_and_oj_login_failed/)

## 問題取得

問題を取得するコマンド（数字を変えると取ってこれる）

```bash
acc new abc100
```

## ファイル実行
python3 abc413/a/main.py
abcXXX/Xを都度変え、input項目を入力する


## テスト実行

- **Ctrl + T** でテストケースを確認

## 生成AIの使用ルール

1. 問題文の翻訳をAIに任せる
2. 自分の知らない知識やアルゴリズムに関する情報をAIから得る
3. 方針やアルゴリズムのアイデアをAIに提案してもらう
4. コードの補完やバグ修正など、実装作業の補助にAIを利用する
5. 実装したい内容を自然言語で伝え、コードの生成をAIに委任する（ただし上記の禁止事項に該当しない範囲に限る）

## 参考サイト

- [AtCoder環境構築の参考記事](https://qiita.com/prln/items/974f1280baa70bd1fd0d)

