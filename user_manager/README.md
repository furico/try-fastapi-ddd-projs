# User管理API

## 仕様
- ユーザー登録
- ユーザーBAN
- ユーザー取得

## ドメイン要件
- Guest は存在しない（DBには保存されない）
- ActiveUser → BannedUser にのみ遷移可能
- BannedUser は取得できるが操作不可