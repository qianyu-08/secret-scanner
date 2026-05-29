
# Secret Scanner

ローカルファイル内のAPIキーやトークンらしき文字列を検出する簡易スキャナー。

## Features

- GitHub token検出
- AWS key形式検出
- OpenAI key形式検出
- regexベース
- ローカル実行のみ

## Usage

```bash
python scan.py sample.txt
````

## Example

```txt
[FOUND] GitHub Token
Line 3:
ghp_xxxxxxxxxxxxxxxxxxxx
```

## Warning

* 本物のキーは公開repoへ置かない
* 誤検知あり
* 学習/監査用途

```
```

