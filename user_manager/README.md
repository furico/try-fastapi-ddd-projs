# User管理API

## 仕様
- ユーザー登録
- ユーザーBAN
- ユーザー取得

## ドメイン要件
- Guest は存在しない（DBには保存されない）
- ActiveUser → BannedUser にのみ遷移可能
- BannedUser は取得できるが操作不可

## 実行方法

```
fastapi dev app/api/main.py   
```

## 動作確認

```
curl -X POST "http://localhost:8000/users?user_id=1&email=a@example.com"
curl "http://localhost:8000/users/1"   
curl -X POST "http://localhost:8000/users/1/ban"  
```
